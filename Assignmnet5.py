import math

def read_file(filepath):
    # Open and read the file
    with open(filepath, 'r') as file:
        header = file.readline().strip().split(',')
        data = [line.strip().split(',') for line in file]
    return header, data

def display_data(header, data):
    print(f"{header[0]:<15}{header[1]} {header[2]} {header[3]}")
    print('-'*40)
    for row in data:
        print(f"{row[0]:<15}{row[1]} {row[2]} {row[3]}")

def take_input():
    from_date = input("Enter from date (YYYY-MM-DD): ")
    to_date = input("Enter to date (YYYY-MM-DD): ")
    return from_date, to_date

def filter_data(data, from_date, to_date):
    filtered_data = [row for row in data if from_date <= row[0] <= to_date]
    return filtered_data

def calc_avg_cal(data):
    if not data:
        return 0
    total_cal = 0
    for row in data:
        total_cal += sum(int(cal) for cal in row[1:])
    avg_cal = total_cal / (len(data) * 3)  # Assuming 3 meals per day
    return avg_cal

def calc_standard_deviation(data, avg_cal):
    if not data:
        return 0
    variance = sum((int(cal) - avg_cal) ** 2 for row in data for cal in row[1:]) / (len(data) * 3)
    return math.sqrt(variance)

def highest_day_cal(data):
    if not data:
        return 0, 0
    highest_day = data[0][0]
    highest_cal = sum(int(cal) for cal in data[0][1:])
    for row in data:
        total_cal = sum(int(cal) for cal in row[1:])
        if total_cal > highest_cal:
            highest_cal = total_cal
            highest_day = row[0]
    return highest_day, highest_cal

def highest_per_meal(data):
    if not data:
        return 0
    highest_meal = max(int(cal) for row in data for cal in row[1:])
    return highest_meal

def display_output(from_date, to_date, avg_cal, sd, hd, hc):
    print("\nResults:")
    print(f"From Date: {from_date}")
    print(f"To Date: {to_date}")
    print(f"Average Calories: {avg_cal}")
    print(f"Standard Deviation: {sd}")
    print(f"Highest Calories in a Day: {hd}")
    print(f"Highest Calories in a Single Meal: {hc}")

def main():
    filepath = 'calories_data.csv'
    header, data = read_file(filepath)

    display_data(header, data)

    from_date, to_date = take_input()
    filtered_data = filter_data(data, from_date, to_date)

    avg_cal = calc_avg_cal(filtered_data)
    sd = calc_standard_deviation(filtered_data, avg_cal)
    hd, hc = highest_day_cal(filtered_data)

    # Display the results
    display_output(from_date, to_date, avg_cal, sd, hd, hc)

# Run the main function
main()
