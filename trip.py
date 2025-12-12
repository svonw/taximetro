import math
import time


class Trip:
    trip_activate = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    def __init__(self):
        pass


    @classmethod
    def start(cls, command):
        if cls.trip_activate:
            print("Error, a trip is already started")
            return
        else:
            cls.trip_activate = True
            cls.start_time = time.time()
            cls.stopped_time = 0
            cls.moving_time = 0
            cls.state = "stopped"
            cls.state_start_time = time.time()
            print("Trip started. Initial state: 'stopped")

    @classmethod
    def stop_move(cls, command):
        if not cls.trip_activate:
            print("Error. No active trip, please start first")
            return

        duration = math.ceil(time.time() - cls.state_start_time)

        if command == "stop":
            cls.stopped_time += duration
        else:
            cls.moving_time += duration

        cls.state = 'stopped' if command == "stop" else 'moving'
        cls.state_start_time = time.time()
        print(f"State changed to '{cls.state}'.")

    @classmethod
    def finish(cls, command):
        if not cls.trip_activate:
            print("Error: No active trip to finish.")
            return

        duration = math.ceil(time.time() - cls.state_start_time)
        if cls.state == 'stopped':
            cls.stopped_time += duration
        else:
            cls.moving_time += duration
        cls.trip_activate = False
        cls.state = None
        return True