import csv
import datetime


class Sensor:
    results = []

    def read(self):
        raise NotImplementedError("Method read() must be implemented")

    def read_n_times(self, n):
        for i in range(n):
            reading = self.read()
            self.results.append(reading)

    def get_results(self):
        return self.results

    def get_results_as_csv(self, n):
        self.results = []
        self.read_n_times(n)

        class_name = self.__class__.__name__.split("_")[0]
        data_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # data_time = data_time.replace(":", "-")
        file_name = f'{class_name}_{data_time}_{n}.csv'

        with open(f'home/kamil/sensorTest/data/{file_name}', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.results[0].keys())
            for result in self.results:
                writer.writerow(result.values())

        csvfile.close()

