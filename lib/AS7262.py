import RPi.GPIO as GPIO
import smbus
import time

AS7262_ADDRESS = 0x49

AS7262_CONTROL = 0x4F
AS7262_SLAVE_STATUS_REG = 0x2F
AS7262_DATA_1 = 0x08

I2C_BUS_NUMBER = 1

bus = smbus.SMBus(I2C_BUS_NUMBER)

power_enable_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_enable_pin, GPIO.OUT)


class AS7262:
    def enable_as7262_power(self):
        GPIO.output(power_enable_pin, GPIO.HIGH)
        time.sleep(0.1)

    def disable_as7262_power(self):
        GPIO.output(power_enable_pin, GPIO.LOW)

    def read_as7262_data(self):
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
