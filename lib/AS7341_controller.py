from lib.Sensor import Sensor
from lib.AS7341 import AS7341
import logging


class AS7341_controller(Sensor):
    # i2c address: 0x39
    def read(self):
        results = {}

        logging.basicConfig(level=logging.INFO)

        obj = AS7341()
        obj.measureMode = 0
        obj.AS7341_ATIME_config(100)
        obj.AS7341_ASTEP_config(999)
        obj.AS7341_AGAIN_config(6)
        obj.AS7341_EnableLED(False)  # LED Enable

        try:
            obj.AS7341_ControlLed(True, 10)
            obj.AS7341_startMeasure(0)
            obj.AS7341_ReadSpectralDataOne()

            # channel1(405-425nm)
            results['405-425nm'] = obj.channel1

            # channel2(435-455nm)
            results['435-455nm'] = obj.channel2

            # channel3(470-490nm)
            results['470-490nm'] = obj.channel3

            # channel4(505-525nm)
            results['505-525nm'] = obj.channel4

            obj.AS7341_startMeasure(1)
            obj.AS7341_ReadSpectralDataTwo()

            # channel5(545-565nm)
            results['545-565nm'] = obj.channel5

            # channel6(580-600nm)
            results['580-600nm'] = obj.channel6

            # channel7(620-640nm)
            results['620-640nm'] = obj.channel7

            # channel8(670-690nm)
            results['670-690nm'] = obj.channel8

            # Clear
            results['clear'] = obj.CLEAR

            # NIR
            results['nir'] = obj.NIR

            print('----AS7341--------------------\n', results)


        except KeyboardInterrupt:
            logging.info('ctrl + c:')
            exit()

        return results
