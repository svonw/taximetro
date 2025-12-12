import datetime

from trip import Trip
from trip_recorder import save_trips
from hours_calculator import create_calculator


def taximeter():
    '''
    funcion para las opciones del taximetro
    '''
    print("welcome to F5 taximeter")
    print("Available commands: 'start','stop','move', 'finish', 'exit'\n")

    trip=Trip()
    current_hour = datetime.datetime.now().hour
    calculator = create_calculator(current_hour)

    while True:
        command = input(">").strip().lower()
        if command == "start":
            trip.start(command)

        elif command in ("stop", "move"):
            trip.stop_move(command)

        elif command == "finish":

            if trip.finish(command):
                total_fare = calculator.calculate_fare(trip.stopped_time, trip.moving_time)

                save_trips( trip.stopped_time, trip.moving_time, total_fare)
                print("trip finished")

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")
