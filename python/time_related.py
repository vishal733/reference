
def serviceRecentActivityRequest(request):
    # Get list of last recent video fiels based upon time parameter. Return as a json.
    try:
        # Start by getting list of video files which fall in the correct duration.
        recentActivityList = list();

        params= request.params.split(';',1)[0];   # Remove trailing ';' if it exists
        paramlist= params.split(',',1);
        if (len(paramlist) == 2):
            str_end_time = paramlist[0].strip();
            str_duration_mins = paramlist[1].strip();
            end_time = datetime.datetime.strptime(str_end_time[:19], "%Y-%m-%d_%H-%M-%S")

            #Get startdate, and enddate
            dur_mins = datetime.timedelta(0,0,0,0,int(str_duration_mins),0)
            start_time = end_time - dur_mins;
            
            print "serviceRecentActivityRequest(): StartTime:", start_time
            print "serviceRecentActivityRequest(): EndTime:", end_time
            #divmod((c-a).total_seconds(),60)[0]

            dirRootCrane = cntxt.localDB.getVal('dirRootCrane');
            hostname = socket.gethostname();
            vidaSetupID = cntxt.localDB.getVal('vidaSetupID');
            rootFolder = os.path.join(dirRootCrane, 'dev/html/assets/vidaCam/', hostname, vidaSetupID, "activityclips");

            folders= list()
            tmp_time = start_time;
            while tmp_time.date() <= end_time.date():
                dateStr = tmp_time.strftime("%Y-%m-%d")
                folders.append(os.path.join(rootFolder, dateStr));
                tmp_time = tmp_time + datetime.timedelta(hours=24)


            tmpThumbnailDir = os.path.join(dirRootCrane, 'dev/html/assets/tmp');
            if not os.path.exists(tmpThumbnailDir):
                os.makedirs(tmpThumbnailDir);
                os.system("rm -rf " + tmpThumbnailDir + "/*");   # clear previous thumbnail files
            
            for folder in folders:
              if os.path.isdir(folder):
                for base, dirs, files in os.walk(folder):
                    files.sort();
                    for fileName in files:
                        currFileTimeStamp = datetime.datetime.strptime(fileName[6:24], "%Y-%m-%d_%H-%M-%S")
                        if (currFileTimeStamp >=start_time) and (currFileTimeStamp <=end_time) :
                            fullFileName = os.path.join(base, fileName)
                            recentActivityList.append(fullFileName);

            recentActivityList.sort(reverse=True);
            activityList = [];
            for fullFileName in recentActivityList:
                baseFileName = os.path.basename(fullFileName);
                thumbnailFile = os.path.join(tmpThumbnailDir, baseFileName[0:-4] +".jpg");

                # Get Centre frame
                createThumbnailFileForVid(fullFileName, thumbnailFile)
                entry = {}
                startTime = baseFileName[6:25];
                startTime = startTime.replace('_', '-');
                entry['eventID'] = baseFileName[:-4];
                entry['startTime'] = startTime;
                entry['thumbnailFile'] = thumbnailFile[findNthLastOccurance(thumbnailFile,"/", 3)+1:];
                entry['videoClipFile'] = fullFileName[findNthLastOccurance(fullFileName,"/", 7)+1:];
                activityList.append(entry);

            mainActivityList = {}
            mainActivityList['Activities'] = activityList;
            mainActivityList['Total'] = len(activityList);
            jsonString = json.dumps(mainActivityList);
            request.replyClient(jsonString);
        else:
            request.replyBadRequest();

    except ValueError as ex:
        print "serviceRecentActivityRequest(): Error - ", ex;
        request.replyBadRequest();
