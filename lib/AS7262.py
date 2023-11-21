from gpiozero import LED
import smbus
import time


AS7262_ADDRESS = 0x49

AS7262_CONTROL = 0x4F
AS7262_SLAVE_STATUS_REG = 0x2F
AS7262_DATA_1 = 0x08


bus = smbus.SMBus(1)


power_enable_pin = LED(17)

def enable_as7262_power():
    power_enable_pin.on()
    time.sleep(0.1)

def disable_as7262_power():
    power_enable_pin.off()

def read_as7262_data():
    bus.write_byte_data(AS7262_ADDRESS, AS7262_CONTROL, 0x03)


    while True:
        data = bus.read_byte_data(AS7262_ADDRESS, AS7262_SLAVE_STATUS_REG)
        if (data & 0x02) == 0x02:
            break
        time.sleep(0.1)

    color_data = []
    for i in range(6):
        color_data.append(bus.read_byte_data(AS7262_ADDRESS, AS7262_DATA_1 + i))

    return color_data


