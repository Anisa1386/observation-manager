Observation Manager

Project Description

Observation Manager is a Python project for managing astronomical observations. It allows users to add, display, and search observations, save data to an SQLite database or a CSV file, calculate exposure statistics, and visualize exposure times using a bar chart.

Features

- Add a new observation
- Display all observations
- Search observations by target name
- Save observations to an SQLite database
- Export observations to a CSV file
- Display a bar chart of exposure times
- Calculate average exposure time
- Find maximum exposure time
- Find minimum exposure time
- Calculate total exposure time

Project Files

- "main.py": Main menu and program functions
- "observation.py": Observation classes
- "database.py": Database saving functions
- "visualization.py": Data visualization
- "README.md": Project description and usage instructions
- "observation.db": SQLite database file, created when data is saved
- "observations.csv": CSV file, created when observations are exported

Requirements

- Python 3
- Matplotlib

The "sqlite3" and "csv" modules are included with Python.

How to Run

1. Make sure all Python files are in the same project folder.

2. Install Matplotlib if it is not already installed:
   
   "pip install matplotlib"

3. Run "main.py" using Python.

How to Use

When the program starts, select an option from the main menu.

1. Add observation: Enter the target name, observer name, filter name, and exposure time in seconds.
2. Show observations: Display observations added during the current program session.
3. Search observation: Search for an observation by its target name.
4. Save to database: Save the current observations to the SQLite database.
5. Save to CSV: Export the current observations to a CSV file.
6. Show graph: Display a bar chart of target names and exposure times.
7. Average exposure: Calculate the average exposure time in seconds.
8. Maximum exposure: Display the maximum exposure time in seconds.
9. Minimum exposure: Display the minimum exposure time in seconds.
10. Total exposure: Calculate the total exposure time in seconds.
11. Exit: Close the program.

Example

An observation can be entered using the following sample data:

- Target name: Moon
- Observer name: Anisa
- Filter name: R
- Exposure time: 150 seconds

Notes

- Exposure times are entered in seconds.
- Statistics are calculated using the observations currently available in memory.
- Saving data to the database or CSV file does not automatically load previously saved observations when the program starts.
