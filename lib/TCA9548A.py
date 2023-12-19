import smbus
import time


class TCA9548A:
    def __init__(self, address=0x70, bus_number=1):
        self.address = address
        self.bus_number = bus_number
        self.bus = smbus.SMBus(bus_number)

    def select_channel(self, channel):
        self.bus.write_byte(self.address, 1 << channel)
        time.sleep(0.1)
