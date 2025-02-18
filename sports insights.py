import csv

def load_data(file_name):
    """Loads CSV data into a list"""
    data = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        return []
    if len(data) > 1:
        return data[1:]
    return []

def append_data(file_name, data):
    """Appends new data to the CSV file"""
    try:
        file = open(file_name, mode='r')
        file_exists = True
    except FileNotFoundError:
        file_exists = False
    
    file = open(file_name, mode='a', newline='')
    writer = csv.writer(file)
    if file_exists == False:
        if 'schedule' in file_name:
            headers = ["Sport", "Date", "Time", "Venue"]
        else:
            headers = ["Sport", "Team1", "Team2", "Winner"]
        writer.writerow(headers)
    writer.writerow(data)
    file.close()

def add_event(schedule_file, results_file):
    """Adds a new event to the schedule file and allows adding a result"""
    sport = input("Enter Sport: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    time = input("Enter Time (HH:MM): ")
    venue = input("Enter Venue: ")
    data = [sport, date, time, venue]
    append_data(schedule_file, data)
    print("Event added successfully!")
    
    while True:
        add_result = input("Do you want to enter results for this event? (yes/no): ")
        if add_result.lower() == "yes":
            team1 = input("Enter Team 1: ")
            team2 = input("Enter Team 2: ")
            winner = input("Enter Winner: ")
            result_data = [sport, team1, team2, winner]
            append_data(results_file, result_data)
            print("Result added successfully!")
        else:
            break

def display_schedule(schedule_file):
    """Displays the sports event schedule"""
    schedule = load_data(schedule_file)
    if schedule:
        print("\n--- Event Schedule ---")
        for event in schedule:
            print("Sport: " + event[0] + ", Date: " + event[1] + ", Time: " + event[2] + ", Venue: " + event[3])
    else:
        print("No events scheduled.")

def display_results(results_file):
    """Displays match results"""
    results = load_data(results_file)
    if results:
        print("\n--- Match Results ---")
        for result in results:
            print("Sport: " + result[0] + ", " + result[1] + " vs " + result[2] + ", Winner: " + result[3])
    else:
        print("No match results available.")

def team_rankings(results_file):
    """Computes and displays team rankings based on wins"""
    results = load_data(results_file)
    if results:
        rankings = []
        for result in results:
            winner = result[3]
            found = False
        for item in rankings:
            if item[0] == winner:
                item[1] += 1
                found = True
                break
        if not found:
            rankings.append([winner, 1])
        print("\n--- Team Rankings ---")
        sorted_rankings = []
        for item in rankings:
            sorted_rankings.append(item)
        for i in range(len(sorted_rankings)):
            for j in range(i + 1, len(sorted_rankings)):
                if sorted_rankings[i][1] < sorted_rankings[j][1]:
                    sorted_rankings[i], sorted_rankings[j] = sorted_rankings[j], sorted_rankings[i]
        for team, wins in sorted_rankings:
            print(team + " has " + str(wins) + " victories")
    else:
        print("No team rankings available.")

def main():
    schedule_file = "lakshya_schedule.csv"  # Expected CSV with columns: Sport, Date, Time, Venue
    results_file = "lakshya_results.csv"  # Expected CSV with columns: Sport, Team1, Team2, Winner
    
    while True:
        print("\nLakshya Sports Fest 2025 Insights")
        print("1. View Event Schedule")
        print("2. View Match Results")
        print("3. View Team Rankings")
        print("4. Add New Event")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_schedule(schedule_file)
        elif choice == '2':
            display_results(results_file)
        elif choice == '3':
            team_rankings(results_file)
        elif choice == '4':
            add_event(schedule_file, results_file)
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def run_program():
    main()
run_program()


