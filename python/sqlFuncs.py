#!/usr/bin/python
import MySQLdb as mysql
from enum import Enum
"""
Feature-wise from the app:

index
uniqueID
vidFile
csvFile
starred
isUploaded
- uniqueID generation

- update Firebase upon an update
- add ID to delete list when user deletes a video.
delete entry. Also delete associated files
add entry (verify file exists before creation)

SQL COMMANDS:
SHOW databases;
USE <dbname>
SHOW tables;
SHOW COLUMNS from <table-name>
ALTER TABLE table_name ADD column_name datatype
ALTER TABLE Persons DROP COLUMN DateOfBirth
"""

SqlDBTable = {"fileList": None}
fileListTableColumns = {}
fileListTableColumns["sessionID"] = "text";
fileListTableColumns["vidFiles"] = "text";
fileListTableColumns["csvFiles"] = "text";
fileListTableColumns["timeLapseFiles"] = "text";
fileListTableColumns["clipFiles"] = "text";
fileListTableColumns["snapFiles"] = "text";
SqlDBTable["fileList"] = fileListTableColumns;

class SqlDBClass:
    con = None
    dbName = None
    filesTable = "fileList"

    def _ensureTableColumnExists_(self, cur, columnName, columnType):
        try:
            sqlCmd = "ALTER TABLE " + self.filesTable + " ADD " + columnName + " " + columnType + ";"; a
            cur.execute(sqlCmd);
            self.con.commit();
        except Exception as e:
            if not "Duplicate column name" in e[1] :    # If column alraedy exists, no worries!!
                print e

    def __init__(self, dbName):
        self.dbName = dbName;
        self.con = mysql.connect('127.0.0.1', 'root', 'lensbricks123');
        cur = self.con.cursor();
        cur._defer_warnings = True
        cur.execute("CREATE DATABASE IF NOT EXISTS " + self.dbName + ";");
        cur.execute("USE " + self.dbName + ";");
        cur.execute("CREATE TABLE IF NOT EXISTS " + self.filesTable + " (`id` int(11) NOT NULL AUTO_INCREMENT, PRIMARY KEY (`id`))");
        self.con.commit();
        for key in fileListTableColumns:
            self._ensureTableColumnExists_(cur, key, fileListTableColumns[key]);

    def createNewRecordingSession(self, fileName):
        # 
        print "B"

    def addCsvFile(self, fileName):
        # adfadsf
        print "A"

    def addTimeLapseFile(self, fileName):
        # adfadsf
        print "A"

    def addClipFile(self, fileName):
        # adfadsf
        print "A"

    def markAsStarredAndUpload(self, fileName):
        # adfadsf
        print "A"

if __name__ == '__main__':
    dbName = "local"
    sqlDB = SqlDBClass(dbName);

