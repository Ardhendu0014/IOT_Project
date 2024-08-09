import datetime

# Function to generate simulated temperature data
def generate_temperature_data(filename, start_time, num_entries):
    with open(filename, 'w') as file:
        current_time = start_time
        for _ in range(num_entries):
            temperature = 20.0 + (current_time.minute % 10) + (current_time.second % 5)  # Simulated temperature
            file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}: {temperature:.1f}\n")
            current_time += datetime.timedelta(minutes=1)

# Define the start time and number of entries
start_time = datetime.datetime(2024, 8, 9, 10, 0, 0)
num_entries = 10

# Generate the data file
generate_temperature_data("C:\\IoTProject\\temperature_data.txt", start_time, num_entries)

