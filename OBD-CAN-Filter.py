import can
import os
import time
import datetime
# from time import time as time2


interface = "neovi"
channel = 1

bus = can.interface.Bus(channel=channel,
                        bustype=interface,
                        bitrate=500000)
                        # can_filters=[{"can_id": 0x0111, "can_mask": 0x7ff, "extended": False}])

previousTime = 0
currentTime = 0
contents = []
while(1):

    message = bus.recv(1.0)
    if message is not None:
        # print(message)
        messageList = str(message).strip().split(" ")
        # print(messageList)
        line = []
        for i in messageList:
            if len(i) != 0:
                line.append(i)
        currentTime = int(line[1].split(".")[0])
        contents.append(line)
        if currentTime - previousTime > 0:
            previousTime = currentTime
            # os.system("cls")
            memory = set()
            for i in reversed(contents):
                if not i[3] in memory:
                    print(i)
                memory.add(i[3])
            print("***********************")
            contents.clear()

    else:
        print("error")

    # time.sleep(1.0)
        # time.sleep(1.0)
# while(1):
#     message = bus.recv(0.1)
#     bus.flush_tx_buffer()
#     if message is not None:
#         time.sleep(1.0)
#         print(message)
#         print(datetime.datetime.now())
#         # print(time2())
