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

