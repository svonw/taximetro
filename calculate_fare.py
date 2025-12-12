class FareCalculator:
    START_RATE = None
    STOPPED_RATE = None
    MOVING_RATE = None
    def calculate_fare(self, sec_stopped, sec_moving):
        total=self.START_RATE + sec_stopped * self.STOPPED_RATE + sec_moving * self.MOVING_RATE
        return round(total, 2)