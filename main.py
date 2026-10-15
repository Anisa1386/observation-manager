from observation import Observation
from database import save_to_db
from visualization import show_graph
import csv


observations = []


def add_observation():
    target = input("Target name: ")
    observer = input("Observer name: ")
    filter_name = input("Filter name: ")
    exposure = float(input("Exposure time in seconds: "))

    obs = Observation(target, observer, filter_name, exposure)
    observations.append(obs)
    print("Observation added successfully!")


def show_observations():
    for obs in observations:
        print(obs.summary_info())


def search_observation():
    target = input("Enter target name: ")

    for obs in observations:
        if obs.target.lower() == target.lower():
            print(obs.summary_info())
            return

    print("Observation not found.")

def average_exposure():
    if not observations:
        print("No observations available.")
        return
    total = sum(obs.exposure for obs in observations)
    average = total / len(observations)
    print(f"Average exposure: {average} seconds")


def max_exposure():
    if not observations:
        print("No observations available.")
        return
    maximum = max(obs.exposure for obs in observations)
    print(f"Maximum exposure: {maximum} seconds")


def min_exposure():
    if not observations:
        print("No observations available.")
        return
    minimum = min(obs.exposure for obs in observations)
    print(f"Minimum exposure: {minimum} seconds")


def total_exposure():
    if not observations:
        print("No observations available.")
        return
    total = sum(obs.exposure for obs in observations)
    print(f"Total exposure: {total} seconds")

def save_to_csv():
    with open("observations.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "target" ,
            "observer" ,
            "filter" ,
            "exposure (s)"
        ]
        
        writer = csv.DictWriter(file,fieldnames = fieldnames)

        writer.writeheader()

        for obs in observations:
            row = {
                "target": obs.target,
                "observer":obs.observer,
                "filter": obs.filter,
                "exposure (s)":obs.exposure}

            
        writer.writerow(row)
    print("Observations saved to CSV successfully!")
def main():
    while True:
        print("\n1. Add observation")
        print("2. Show observations")
        print("3. Search observation")
        print("4. Save to database")
        print("5. Show graph")
        print("6. Average exposure")
        print("7. Maximum exposure")
        print("8. Minimum exposure")
        print("9. Total exposure")
        print("10. save to csv")
        print("11. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_observation()
        elif choice == "2":
            show_observations()
        elif choice == "3":
            search_observation()
        elif choice == "4":
            save_to_db(observations)
            print("Observations saved.")
        elif choice == "5":
            show_graph(observations)
        elif choice == "6":
            average_exposure()
        elif choice == "7":
            max_exposure()
        elif choice == "8":
            min_exposure()
        elif choice == "9":
            total_exposure()
        elif choice == "10":
             save_to_csv()
        elif choice == "11":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()