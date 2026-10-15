class Observation:
    def __init__(self, target, observer, filter_name, exposure):
        self.target = target
        self.observer = observer
        self.filter = filter_name
        self.exposure = float(exposure)

    def summary_info(self):
        return f"""Target: {self.target}
Filter name: {self.filter}
Exposure: {self.exposure}
Observer name: {self.observer}"""

    def exposure_min(self):
        return self.exposure / 60


class Photometric_observation(Observation):
    def __init__(self, target, observer, filter_name, exposure, wavelength):
        super().__init__(target, observer, filter_name, exposure)
        self.wavelength = wavelength

    def summary_info(self):
        return f"""Target: {self.target}
Filter name: {self.filter}
Exposure: {self.exposure}
Observer name: {self.observer}
Wavelength: {self.wavelength}"""