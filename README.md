# Lakshya Sports Insights

## Description
Lakshya Sports Insights is a Python-based project that manages event schedules, match results, and team rankings for Lakshya Sports Fest 2025. It allows users to add events, enter results, and view rankings using simple CSV storage without external libraries.

## Features
- **View Event Schedule**: Displays the list of scheduled sports events.
- **View Match Results**: Shows results of completed matches.
- **View Team Rankings**: Calculates and displays team rankings based on victories.
- **Add New Events**: Enables users to add new sports events to the schedule.
- **Enter Match Results**: Allows users to update results for completed matches.

## Requirements
- Python 3.x
- CSV files for storing data (automatically created if not present)

## Usage
1. Run the script using:
   ```sh
   python script.py
   ```
2. Choose an option from the menu:
   - **1**: View event schedule
   - **2**: View match results
   - **3**: View team rankings
   - **4**: Add a new event and match result
   - **5**: Exit

## File Structure
- `lakshya_schedule.csv` → Stores scheduled events.
- `lakshya_results.csv` → Stores match results.

## Notes
- No external libraries are required.
- Data is stored in CSV format for simplicity.
- The program ensures that all inputs are correctly stored and retrieved.

