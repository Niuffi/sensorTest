from lib.Sensor import Sensor
from lib.AS7262 import AS7262


class AS7262_controller(Sensor):

    def read(self):
        results = {}
        try:
            AS7262.enable_as7262_power()
            results = AS7262.read_as7262_data()

        except KeyboardInterrupt:
            AS7262.disable_as7262_power()
            pass

        return results
