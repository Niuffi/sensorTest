from lib import AS7341_controller

sensor1 = AS7341_controller.AS7341_controller()

sensor1.read()
sensor1.read_n_times(10)
print(sensor1.get_results())
