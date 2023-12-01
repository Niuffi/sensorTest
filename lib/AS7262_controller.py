from lib.Sensor import Sensor
from lib.AS7262 import AS7262


class AS7262_controller(Sensor):

    def read(self):
        AS7262.soft_reset()

        hw_type, hw_version, fw_version = AS7262.get_version()

        print('{}'.format(fw_version))

        AS7262.set_gain(64)

        AS7262.set_integration_time(17.857)

        AS7262.set_measurement_mode(2)

        # AS7262.set_illumination_led_current(12.5)
        AS7262.set_illumination_led(1)
        # AS7262.set_indicator_led_current(2)
        # AS7262.set_indicator_led(1)

        try:
            while True:
                results = AS7262.get_calibrated_values()
                print("""
        Red:    {}
        Orange: {}
        Yellow: {}
        Green:  {}
        Blue:   {}
        Violet: {}""".format(*results))
        except KeyboardInterrupt:
            AS7262.set_measurement_mode(3)
            AS7262.set_illumination_led(0)

        return results
