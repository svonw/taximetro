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


    current_hour = datetime.datetime.now().hour
    calculator = create_calculator(current_hour)

    while True:
        command = input(">").strip().lower()
        if command == "start":
            Trip.start(command)

        elif command in ("stop", "move"):
            Trip.stop_move(command)

        elif command == "finish":

            if Trip.finish(command):
                total_fare = calculator.calculate_fare(Trip.stopped_time, Trip.moving_time)

                save_trips( Trip.stopped_time, Trip.moving_time, total_fare)
                print("trip finished")

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")
