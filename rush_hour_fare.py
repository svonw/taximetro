from calculate_fare import FareCalculator


class RushHourCalculator(FareCalculator):
    START_RATE = 6.5
    STOPPED_RATE = 0.04
    MOVING_RATE = 0.10

