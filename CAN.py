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

while 1:

    packet = bus.recv(1.0)

    if packet is not None:

        packetList = str(packet).strip().split(" ")
        line = []

        for i in packetList:
            if len(i) != 0:
                line.append(i)

        currentTime = float(line[1])
        contents.append(line)

        if currentTime - previousTime > 0.2:
            previousTime = currentTime

            rContents = reversed(contents)
            data = []

            # print(contents)
            for i in rContents:
                if i[3] == "18f0090b": # steering wheel angle
                    data.append(str(i[8]))
                    break

            for i in rContents:
                if i[3] == "18f0010b": # brake switch
                    data.append(str(i[7]))
                    break

            for i in rContents:
                if i[3] == "18ff550b": # brake strength
                    data.append(str(i[7]))
                    break

            for i in rContents:
                if i[3] == "0cf00300": # accelerator switch
                    data.append(str(i[7]))
                    break

            for i in rContents:
                if i[3] == "0cf00300": # accelerator strength
                    data.append(str(i[8]))
                    break

            for i in rContents:
                if i[3] == "18f00503": # gear position
                    data.append(str(i[7]))
                    break

            data.append("0")

            file.write(str(datetime.now()) + " " + str("_".join(data)) + "\n")

            print(data)
            print("***********************")

            contents.clear()

    else:
        print("no packet")
        break

file.close()
bus.shutdown()

