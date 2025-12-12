
from night_fare import NightFareCalculator
from rush_hour_fare import RushHourCalculator
from standard_fare import StandardFare



def create_calculator(hour):
    if 22 <= hour or hour <= 6:
        return NightFareCalculator()
    elif 7 >= hour <= 9 or 17 <= hour <= 19:
        return RushHourCalculator()
    else:
        return StandardFare()