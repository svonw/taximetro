import csv
import datetime
import os


def save_trips( stopped_time, moving_time, total_fare):

    trips_counter = 0
    file_path = "trips_summary.csv"
    data_header=["Trip", "Stopped Time", "Moving Time", "Total Fare","Trip Time","Trip Day"]
    actual_datetime=datetime.datetime.now()
    trip_date=actual_datetime.strftime("%d-%m-%Y")
    trip_hour=actual_datetime.strftime(("%H:%M:%S"))


    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data_header)
            trips_counter = 1

    else:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            trips_counter = sum(1 for row in reader)

    data_row = [trips_counter, stopped_time, moving_time, total_fare, trip_date, trip_hour]

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data_row)
    print(f"Viaje #{trips_counter} añadido correctamente.")


    '''
        with open("trips_summary.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if (line.find("Trip") != -1):
                    trips_counter += 1
            

    with open("trips_summary.txt", "a") as file:
        file.write(f"--- Trip '{trips_counter}' Summary ---\n")
        file.write(f"Stopped time: {stopped_time:.1f} seconds\n")
        file.write(f"Moving time: {moving_time:.1f} seconds\n")
        file.write(f"Total fare: {total_fare:.2f}\n")
        file.write(f"--- Trip hour: {datetime.datetime.now().replace(microsecond=0)}\n")
        file.write("---------------------\n")
        '''