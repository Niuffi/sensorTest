from lib.Sensor import Sensor
from lib.AS7262 import AS7262


class AS7262_controller(Sensor):

    def read(self):
        results = {}
        obj = AS7262()

        try:
            obj.setup()
            obj.enable_as7262_power()
            results = obj.read_as7262_data()

        except KeyboardInterrupt:
            pass

        return results
