import socket
import os
# import os, os.path

print("Connecting...")
if os.path.exists("/tmp/mysocket"):
    client = socket.socket( socket.AF_UNIX, socket.SOCK_SOCK_STREAM )
    client.connect("/tmp/mysocket")
    print("Ready.")
    print("Ctrl-C to quit.")
    print("Sending 'DONE' shuts down the server and quits.")
    while True:
        try:
            x = input( "> " )
            if "" != x:
            	print("SEND:", x)
                client.send( x )
                if "DONE" == x:
                    print("Shutting down.")
                break
        except KeyboardInterrupt, k:
            print("Shutting down.")
    client.close()
else:
    print("Couldn't Connect!")
    print("Done")
