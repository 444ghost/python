import can
from datetime import datetime

interface = "neovi"
channel = 1

bus = can.interface.Bus(channel=channel, # from the reference
                        bustype=interface,
                        bitrate=500000) # BR 500k
                        # can_filters=[{"can_id": 0x0111, "can_mask": 0x7ff, "extended": False}])

previousTime = 0
currentTime = 0
contents = []

file = open(str(datetime.now().replace(second=0, microsecond=0)).replace(":", "-") + ".txt", "a")

while(1):

    packet = bus.recv(1.0)

    if packet is not None:

        packetList = str(packet).strip().split(" ")
        line = []

        for i in packetList:
            if len(i) != 0:
                line.append(i)

        # currentTime = float(line[1].split(".")[0])
        currentTime = float(line[1])
        contents.append(line)


        if currentTime - previousTime > 0.5:
            previousTime = currentTime

            for i in reversed(contents):
                if i[3] == "00c9":
                    print(i)
                    file.write(str(datetime.now()) + " " + str(i[2:]) + "\n")
            print("***********************")
            contents.clear()

    else:
        print("no packet")
        break

file.close()
bus.shutdown()

