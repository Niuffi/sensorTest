from lib.sensor import Sensor
from lib.AS7262 import AS7262


class AS7262_controller(Sensor):
    def read(self):
        try:
            AS7262.enable_as7262_power()
            colors = AS7262.read_as7262_data()
            for i, color in enumerate(colors):
                print(f"Color {i + 1}: {color}")


        except KeyboardInterrupt:
            AS7262.disable_as7262_power()
            pass
