import time


def calculate_fare(sec_stopped, sec_moving):
    '''
    funcion para calcular tarifa
    :param sec_stopped: 0.02€/s
    :param sec_moving: 0.05€/s
    '''
    fare = sec_stopped * 0.02 +  sec_moving * 0.05
    print(f"total tarifa:{fare}")
    return fare

def taximeter():
    '''
    funcion para las opciones del taximetro
    '''
    print("welcome to F5 taximeter")
    print("Available commands: 'start','stop','move', 'finish', 'exit'\n")
    trip_activate=False
    start_time=0
    stopped_time=0
    moving_time=0
    state=None
    state_start_time=0

    while True:
        command=input(">").strip().lower()
        if command == "start":
            if trip_activate:
                print("Error, a trip is already started")
                continue
            trip_activate=True
            start_time=time.time()
            stopped_time=0
            moving_time=0
            state="stopped"
            state_start_time=time.time()
            print("Trip started. Initial state: 'stopped")
        elif command in ("stop","move"):
            if not trip_activate:
                print("Error. No active trip, please start first")
                continue
            duration=time.time() -state_start_time
            if state=="stopped":
                stopped_time+=duration
            else:
                moving_time+=duration

            state = 'stopped' if command == "stop" else 'moving'
            state_start_time = time.time()
            print(f"State changed to '{state}'.")

        elif command == "finish":
            if not trip_activate:
                print("Error: No active trip to finish.")
                continue


            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration


            total_fare = calculate_fare(stopped_time, moving_time)
            print(f"\n--- Trip Summary ---")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")


            trip_active = False
            state = None

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")

if __name__ == "__main__":
    taximeter()