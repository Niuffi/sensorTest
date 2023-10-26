from lib.Sensor import Sensor

import logging
from lib.AS7341 import AS7341


class AS7341_controller(Sensor):

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
            results['channel1'] = obj.channel1

            # channel2(435-455nm)
            results['channel2'] = obj.channel2

            # channel3(470-490nm)
            results['channel3'] = obj.channel3

            # channel4(505-525nm)
            results['channel4'] = obj.channel4

            obj.AS7341_startMeasure(1)
            obj.AS7341_ReadSpectralDataTwo()

            # channel5(545-565nm)
            results['channel5'] = obj.channel5

            # channel6(580-600nm)
            results['channel6'] = obj.channel6

            # channel7(620-640nm)
            results['channel7'] = obj.channel7

            # channel8(670-690nm)
            results['channel8'] = obj.channel8

            # Clear
            results['clear'] = obj.CLEAR

            # NIR
            results['nir'] = obj.NIR


        except KeyboardInterrupt:
            logging.info('ctrl + c:')
            exit()

        return results
