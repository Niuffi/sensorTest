from lib.Sensor import Sensor
from lib.AS7262 import AS7262


class AS7262_controller(Sensor):
    # i2c address: 0x49
    def read(self):
        obj = AS7262()

        obj.soft_reset()

        hw_type, hw_version, fw_version = obj.get_version()

        obj.set_gain(64)

        obj.set_integration_time(17.857)

        obj.set_measurement_mode(2)

        # obj.set_illumination_led_current(12.5)
        obj.set_illumination_led(0)
        # obj.set_indicator_led_current(2)
        # obj.set_indicator_led(1)

        try:
            results = obj.get_calibrated_values()
            return results
        except KeyboardInterrupt:
            obj.set_measurement_mode(3)
            obj.set_illumination_led(0)
            obj.set_indicator_led(0)
