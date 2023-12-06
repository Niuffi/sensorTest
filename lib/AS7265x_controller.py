import lib.AS7265x as AS7265x
from lib.Sensor import Sensor


class AS7265x_controller(Sensor):
    def read(self):
        obj = AS7265x
        results = obj.readCAL()
        print('-----------------------\n',results)
        return results








