from calculate_fare import FareCalculator


class NightFareCalculator(FareCalculator):
    START_RATE = 5.5
    STOPPED_RATE = 0.03
    MOVING_RATE = 0.08
