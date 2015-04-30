/*
Implementing the following:
gst-launch-1.0 -e v4l2src ! video/x-raw,width=1280,height=720 ! videoflip ! x264enc tune=zerolatency ! queue min-threshold-time=2000000000 ! m.  pulsesrc ! level ! audioconvert ! lamemp3enc ! m.  mp4mux name=m ! filesink location=out.mp4
*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <signal.h>


extern "C" {
    #include <gst/gst.h>
}

/* Structure to contain all our information, so we can pass it to callbacks */
typedef struct _CustomData {
  GstElement *pipeline;
  GstElement *binVid;
  GstElement *binAud;
  GstElement *binMux;

  GstElement *vidsrc;
  GstElement *capsfiltervid;
  GstElement *vidalg;
  GstElement *x264enc;
  GstElement *queue;

  GstElement *audsrc;
  GstElement *audlevel;
  GstElement *audconv;
  GstElement *audenc;

  GstElement *mux;
  GstElement *sink;
} CustomData;

void send_eos(int sig);
int do_exit = FALSE;
CustomData data;

int main(int argc, char *argv[])
{
    GstBus *bus = NULL;
    GstMessage *msg;
    GstStateChangeReturn ret;
    gboolean terminate = FALSE;
    gboolean add_timestamp = FALSE, debug = FALSE;

    /* Initialize GStreamer */
    gst_init (&argc, &argv);
    /*
    if(( strncmp("-h",argv[1],3) == 0 || strncmp("--help",argv[1],7) == 0 ) ) {
        g_print("Usage: ./main\n");
        return(0);
    }*/

    /* Create the empty pipeline */
    data.pipeline = gst_pipeline_new ("pipeline");
    data.binVid = gst_bin_new("binVid");
    data.binAud = gst_bin_new("binAud");
    data.binMux = gst_bin_new("binMux");

    /* Create the elements */
    data.vidsrc = gst_element_factory_make ("v4l2src", "vidsrc");
    data.capsfiltervid = gst_element_factory_make("capsfilter", "capsfiltervid");
    data.vidalg = gst_element_factory_make("videoflip", "vidalg");
    data.x264enc = gst_element_factory_make("x264enc", "x264enc");
    data.queue = gst_element_factory_make("queue", "queue");

    data.audsrc = gst_element_factory_make("pulsesrc", "audsrc");
    data.audlevel = gst_element_factory_make("level", "auddlevel");
    data.audconv = gst_element_factory_make("audioconvert", "audconv");
    data.audenc = gst_element_factory_make("lamemp3enc", "audenc");

    data.mux = gst_element_factory_make("mp4mux", "mux");
    data.sink = gst_element_factory_make("filesink", "filesink");

    g_object_set(G_OBJECT(data.vidsrc), "device", "/dev/video1", NULL);
    g_object_set(G_OBJECT(data.x264enc),"tune", 4, NULL);
    g_object_set(G_OBJECT(data.queue), "min-threshold-time", "2000000000", NULL);
    g_object_set(G_OBJECT(data.sink), "location", "out.mp4", NULL);
    g_object_set(G_OBJECT(data.capsfiltervid), "caps",
                 gst_caps_new_simple("video/x-raw",
                                     "width", G_TYPE_INT, 1280,
                                     "height", G_TYPE_INT, 720,
                                     NULL), NULL);

    gst_bin_add_many(GST_BIN(data.binVid), data.vidsrc, data.capsfiltervid, data.vidalg, data.x264enc, data.queue, NULL);
    gst_bin_add_many(GST_BIN(data.binAud), data.audsrc, data.audlevel, data.audconv, data.audenc, NULL);
    gst_bin_add_many(GST_BIN(data.binMux), data.mux, data.sink, NULL);
    gst_bin_add_many(GST_BIN(data.pipeline), data.binVid, data.binAud, data.binMux, NULL);

    if (!gst_element_link_many (
                    data.vidsrc,
                    data.capsfiltervid,
                    data.vidalg,
                    data.x264enc,
                    data.queue,
                    NULL )) {
        g_printerr ("Elements could not be linked in binVid.\n");
        gst_object_unref (data.pipeline);
        return -1;
    }

    if (!gst_element_link_many (
                    data.audsrc,
                    data.audlevel,
                    data.audconv,
                    data.audenc,
                    NULL )) {
        g_printerr ("Elements could not be linked in binAud.\n");
        gst_object_unref (data.pipeline);
        return -1;
    }

    if (!gst_element_link_many (
                    data.mux,
                    data.sink,
                    NULL )) {
        g_printerr ("Elements could not be linked in binMux.\n");
        gst_object_unref (data.pipeline);
        return -1;
    }

    /* add ghostpad */
    GstPad *padVid = gst_element_get_static_pad (data.queue, "src");
    GstPad *padGhostVid = gst_ghost_pad_new("src", padVid);
    gst_object_unref (GST_OBJECT (padVid));
    gst_element_add_pad (GST_ELEMENT(data.binVid), padGhostVid);

    GstPad *padAud = gst_element_get_static_pad (data.audenc, "src");
    GstPad *padGhostAud = gst_ghost_pad_new("src", padAud);
    gst_object_unref (GST_OBJECT (padAud));
    gst_element_add_pad (GST_ELEMENT(data.binAud), padGhostAud);

    GstPad *padGhostVidMux = gst_ghost_pad_new("video_0", gst_element_get_request_pad (data.mux, "video_0"));
    gst_element_add_pad (GST_ELEMENT(data.binMux), padGhostVidMux);

    GstPad *padGhostAudMux = gst_ghost_pad_new("audio_0", gst_element_get_request_pad (data.mux, "audio_0"));
    gst_element_add_pad (GST_ELEMENT(data.binMux), padGhostAudMux);

    if (gst_pad_link (padGhostVid, padGhostVidMux) != GST_PAD_LINK_OK)
    {
        g_printerr ("Elements could not be linked in mux bin(1).\n");
        gst_object_unref (data.pipeline);
        return -1;
    }

    if (gst_pad_link (padGhostAud, padGhostAudMux) != GST_PAD_LINK_OK)
    {
        g_printerr ("Elements could not be linked in mux bin(2)\n");
        gst_object_unref (data.pipeline);
        return -1;
    }
    //
    //
    //gst_object_unref (GST_OBJECT (padVidMux));
    //gst_object_unref (GST_OBJECT (padAudMux));

#if 0
    /* Connect to the pad-added signal */
      g_signal_connect (data.source, "pad-added", G_CALLBACK (pad_added_handler), &data);
      g_signal_connect (data.decodebin, "pad-added", G_CALLBACK (pad_added_handler), &data);
      g_signal_connect (data.motiondetect, "motion-start", G_CALLBACK (motion_start_handler), &data);
      g_signal_connect (data.motiondetect, "motion-stop", G_CALLBACK (motion_stop_handler), &data);

      //Create the pid file
      //create_pid_file("fixed-id", "gst-playback", argc, argv);
#endif


    ret = gst_element_set_state(data.pipeline, GST_STATE_PLAYING);
    GST_DEBUG_BIN_TO_DOT_FILE_WITH_TS (GST_BIN (data.pipeline), GST_DEBUG_GRAPH_SHOW_ALL, "pipeline");

    if (ret == GST_STATE_CHANGE_FAILURE)
    {
        g_printerr("Unable to set the pipeline to the playing state");
        gst_object_unref(data.pipeline);
        return -1;
    }

    g_print("Return value of setting pipeline to playing state= %d\n", ret);

    signal(SIGINT, send_eos);

    if (!bus)
    {
        bus = gst_element_get_bus(data.pipeline);
    }

    int time = 0;
    do{
        msg = gst_bus_timed_pop_filtered(bus, /*GST_CLOCK_TIME_NONE*/5000000000,
                  static_cast<GstMessageType> (GST_MESSAGE_STATE_CHANGED | GST_MESSAGE_ERROR | GST_MESSAGE_APPLICATION | GST_MESSAGE_EOS));
        if (msg != NULL)
        {
            GError *err;
            gchar *debug_info;
            switch(GST_MESSAGE_TYPE(msg))
            {
            case GST_MESSAGE_ERROR:
                break;
            case GST_MESSAGE_EOS:
                g_print ("End-Of-Stream reached.\n");
                do_exit = true;
                break;
            case GST_MESSAGE_STATE_CHANGED:
                /* We are only interested in state-changed messages from the pipeline */
                if (GST_MESSAGE_SRC (msg) == GST_OBJECT (data.pipeline)) {
                    GstState old_state, new_state, pending_state;
                    gst_message_parse_state_changed (msg, &old_state, &new_state, &pending_state);
                    g_print ("Pipeline state changed from %s to %s:\n",
                        gst_element_state_get_name (old_state), gst_element_state_get_name (new_state));

                    g_print("\nSink Caps is %s\n",
                    gst_caps_to_string(gst_pad_get_current_caps(gst_element_get_static_pad(data.sink,"sink"))));
                }
                break;
            case GST_MESSAGE_APPLICATION:
                break;
            default:
                break;
            }
        }
        gst_message_unref (msg);
    } while (!do_exit);

    gst_element_set_state(data.pipeline, GST_STATE_NULL);

terminate_process:
    /* Free resources */
    gst_object_unref(bus);
    gst_object_unref(data.pipeline);

    return 0;
}

void send_eos(int sig) {

    g_print("Received EOS\n");
    do_exit = true;
    gst_element_send_event(data.pipeline,gst_event_new_eos());
    return;
}

