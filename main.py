from datetime import datetime, timedelta

def humidity_tracker():
    while True:
        print("1. View Humidity\n2. Add Humidity\n3. Exit")
        user_choice = input("Enter the number of your choice: ")

        if user_choice == "1":
            #display data from previous entries
            with open("humidity.txt", "r") as file:
                data = file.read()
                if data:
                    print("\nHumidity Log:")
                    print(data)
                else:
                    print("\nNo data found.")
        elif user_choice == "2":
            humidity_warm = input("Enter the humidity of the warm side: ")
            print(f"{humidity_warm}%")

            humidity_cold = input("Enter the humidity of the cold side: ")
            print(f"{humidity_cold}%")

            todays_date = input("Enter today's date(YYYY-MM-DD): ")
            print(todays_date)

            with open("humidity.txt", "a") as file:
                file.write(f"{todays_date}: Warm Side {humidity_warm}%, Cold Side {humidity_cold}%\n")

            print("\nHumidity data logged successfully!")

        elif user_choice == "3":
            print("Exiting the humidity tracker.")
            break

        else:
            print("Invalid choice. Please enter 1,2, or 3")


def temperature_tracker():
    while True:
        print("1. View Temperature\n2. Add Temperature\n3. Exit")
        user_choice = input("Enter the number of your choice: ")

        if user_choice == "1":
            #display data from previous entries
            with open("temperature.txt", "r") as file:
                data = file.read()
                if data:
                    print("\nTemperature Log:")
                    print(data)

        elif user_choice == "2":
            temperature_warm = input("Enter the temperature of the warm side: ")
            print(f"{temperature_warm}°")

            temperature_cold = input("Enter the temperature of the cold side: ")
            print(f"{temperature_cold}°")

            todays_date = input("Enter today's date(YYYY-MM-DD): ")
            print(todays_date)

            with open("temperature.txt", "a") as file:
                file.write(f"{todays_date}: Warm Side: {temperature_warm}°, Cold Side: {temperature_cold}°\n")

                print("Temperature logged successfully!")

        elif user_choice == "3":
            print("Exiting temperature tracker.")
            break

        else:
            print("Invalid. Please type 1, 2, or 3.")


def weight_tracker():
    while True:
        print("1. View Weight\n2. Add Weight\n3. Exit")
        user_choice = input("Enter the number of your choice: ")

        if user_choice == "1":
            with open("weight.txt", "r") as file:
                data = file.read()
                if data:
                    print("\nWeight Log:")
                    print(data)

        elif user_choice == "2":
            weight = input("Enter the weight of Bishamon: ")
            print(f"{weight}g")

            todays_date = input("Enter today's date(YYYY-MM-DD): ")
            print(todays_date)

            with open("weight.txt", "a") as file:
                file.write(f"{todays_date}: Weight: {weight}g\n")
                print("Weight logged successfully!")

        elif user_choice == "3":
            print("Exiting weight tracker.")
            break

        else:
            print("Invalid. Please type 1, 2, or 3")

def feeding_tracker():
    while True:
        print("1. View Feeding\n2. Add Feeding\n3. Exit")
        user_choice = input("Enter the number of your choice: ")

        if user_choice == "1":
            with open("feeding.txt", "r") as file:
                data = file.read()
                if data:
                    print("\nFeeding Log:")
                    print(data)

        elif user_choice == "2":
            feeding_date = input("Enter the last date Bishamon got fed(YYYY-MM-DD): ")
            print(f"{feeding_date}")

            with open("feeding.txt", "a") as file:
                file.write(f"Last fed: {feeding_date}\n")
                print("Feeding logged successfully!")

        elif user_choice == "3":
            print("Exiting feeding tracker.")
            break

        else:
            print("Invalid. Please type 1, 2, or 3")

def cage_cleaning_tracker():
    while True:
        print("1. View Cage Cleaning\n2. Add Cage Cleaning\n3. Exit")
        user_choice = input("Enter the number of your choice: ")

        if user_choice == "1":
            with open("cage.txt", "r") as file:
                data = file.read()
                if data:
                    print("\nCage Cleaning Log:")
                    print(data)

        elif user_choice == "2":
            cleaning_date = input("Enter the last date Bishamon's cage got cleaned(YYYY-MM-DD): ")
            print(f"{cleaning_date}")

            with open("cage.txt", "a") as file:
                file.write(f"Last fed: {cleaning_date}\n")
                print("Cage cleaning logged successfully!")

        elif user_choice == "3":
            print("Exiting cage cleaning tracker.")
            break

def shedding_tracker():
    while True:
        print("1. View Shedding Dates\n2. Add Shedding Dates\n3. Exit")
        user_choice = input("Enter the number of your choice: ")

        if user_choice == "1":
            with open("shedding.txt", "r") as file:
                data = file.read()
                if data:
                    print("\nShedding Log:")
                    print(data)

        elif user_choice == "2":
            shedding_start_date = input("Enter when Bishamon started shedding(YYYY-MM-DD): ")
            print(f"{shedding_start_date}")
            shedding_end_date = input("Enter when Bishamon finished shedding(YYYY-MM-DD): ")
            print(f"{shedding_end_date}")

            with open("shedding.txt", "a") as file:
                file.write(f"Last Shed Start Date: {shedding_start_date}, Last Shed End Date: {shedding_end_date}\n")
                print("Shedding logged successfully!")

        elif user_choice == "3":
            print("Exiting shedding tracker.")
            break

#choose what you want to record or track, main menu interface
def main_menu():
    while True:
        print("How is Bishamon doing today?")
        print("1. Humidity\n2. Temperature\n3. Weight\n4. Feeding\n5. Cleaning\n6. Shedding\n7. Exit")

        user_choice = input("Enter the number for what you would like to track: ")

        if user_choice == "1":
            humidity_tracker()
        elif user_choice == "2":
            temperature_tracker()
        elif user_choice == "3":
            weight_tracker()
        elif user_choice == "4":
            feeding_tracker()
        elif user_choice == "5":
            cage_cleaning_tracker()
        elif user_choice == "6":
            shedding_tracker()
        elif user_choice == "7":
            print("Exiting tracker.")
            break
        else:
            print("Invalid choice. Please type 1, 2, 3, 4, 5, 6, or 7")

main_menu()


