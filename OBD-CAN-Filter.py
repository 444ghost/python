import can

interface = "neovi"
channel = 1

bus = can.interface.Bus(channel=channel, bustype=interface, bitrate=500000, can_filters=[{"can_id": 0x0111, "can_mask": 0x7ff, "extended": False}])
# bus.set_filters(can_filter=)


for i in range(10):
    message = bus.recv(0.1)
    if message is not None:
        print(message)

# bus.send(can.Message(arbitration_id=0x01bd))
# message = bus.recv(1.0)
# if message is not None:
#     print(message)
