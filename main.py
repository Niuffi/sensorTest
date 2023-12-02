import sys

from lib.AS7341_controller import AS7341_controller
from lib.AS7262_controller import AS7262_controller
#from lib.AS7265x_controller import AS7265x_controller

from util.display_help import display_help

n = 1
sensors = ['AS7341',
           'AS7262',]
           #'AS7265x']

arguments = sys.argv[1:]

i = 0

while i < len(arguments):
    if arguments[i] in ['-n', '--samples'] and i + 1 < len(arguments):
        n = int(arguments[i + 1])
        i += 1
    elif arguments[i] in ['--sensor'] and i + 1 < len(arguments):
        sensors = arguments[i + 1].split(',')
        i += 1
    elif arguments[i] in ['-h', '--help']:
        display_help()
        sys.exit(0)
    i += 1


if 'AS7341' in sensors:
    AS7341 = AS7341_controller()
    AS7341.read_n_times(n)
    print(AS7341.get_results())


if 'AS7262' in sensors:
    AS7262 = AS7262_controller()
    AS7262.read_n_times(10)
    print(AS7262.get_results())

# if 'AS7265x' in sensors:
#     AS7265x = AS7265x_controller()
#     AS7265x.read_n_times(n)
#     print(AS7265x.get_results())
