from lib.AS7341_controller import AS7341_controller
from lib.AS7262_controller import AS7262_controller

# sensor1 = AS7341_controller()
# sensor1.read()
# sensor1.read_n_times(10)
# print(sensor1.get_results())

sensor2 = AS7262_controller()
sensor2.read()
sensor2.read_n_times(10)
print(sensor2.get_results())