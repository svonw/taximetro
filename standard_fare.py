from calculate_fare import FareCalculator


class StandardFare(FareCalculator):
    START_RATE = 4.5
    STOPPED_RATE=0.02
    MOVING_RATE=0.05
