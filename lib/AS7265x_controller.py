import lib.AS7265x as AS7265x
from lib.Sensor import Sensor


class AS7265x_controller(Sensor):
    # i2c address: 0x49
    def read(self):
        obj = AS7265x
        output = obj.readCAL()
        results = {
            '410nm': output[0],
            '435nm': output[1],
            '460nm': output[2],
            '485nm': output[3],
            '510nm': output[4],
            '535nm': output[5],
            '560nm': output[6],
            '585nm': output[7],
            '610nm': output[8],
            '645nm': output[9],
            '680nm': output[10],
            '705nm': output[11],
            '730nm': output[12],
            '760nm': output[13],
            '810nm': output[14],
            '860nm': output[15],
            '900nm': output[16],
            '940nm': output[17],
        }
        print('-----------------------\n', results)
        return results
