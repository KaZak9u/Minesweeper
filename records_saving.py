import json
import os

# Script for saving best results

RECORDS_FILE = 'game_records.json'


def calculate_time(seconds):  # Converts number of seconds into timestamp in format: hh:mm:ss
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def time_to_seconds(time_str):  # Converts timestamp in hh:mm:ss format into number od seconds
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds


def load_records():  # Load records dict from json file
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_records(records):  # Saves dict in a json file
    with open(RECORDS_FILE, 'w') as file:
        json.dump(records, file)


# Checks if the new time score is better than the saved one for a given dimensions and difficulty and saves new best
# score in json file
def update_record(dimensions, difficulty, time_str):
    records = load_records()
    time_in_seconds = time_to_seconds(time_str)
    dimensions = str(dimensions)
    difficulty = str(difficulty)
    if dimensions in records:
        if difficulty in records[dimensions]:
            best_time_in_seconds = time_to_seconds(records[dimensions][difficulty])
            if time_in_seconds < best_time_in_seconds:
                records[dimensions][difficulty] = time_str
        else:
            records[dimensions][difficulty] = time_str
    else:
        records[dimensions] = {}
        records[dimensions][difficulty] = time_str
    save_records(records)


if __name__ == '__main__':
    update_record(0, 0, '00:00:19')