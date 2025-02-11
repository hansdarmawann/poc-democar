from tabulate import tabulate
import datetime
import os
import platform

# Data mobil
cars = [
    {
        "license_plate": "B1071PDM",
        "car_name": "Range Rover P615",
        "mileage": 12345.678,
        "available": "No",
        "borrower_name": "Fitra Eri",
        "contact": "081234567891",
        "borrow_date": datetime.date(2024, 6, 24),
        "return_date": datetime.date(2024, 6, 30),
        "reason": "Review Purpose"
    },
    {
        "license_plate": "B1010LKX",
        "car_name": "Mercedes Benz G63 AMG",
        "mileage": 901.23,
        "available": "Yes",
        "borrower_name": "",
        "contact": "",
        "borrow_date": "",
        "return_date": "",
        "reason": ""
    }
]

def main():
    try:
        print("""
        Welcome to XYZ Car Rental Demo System
        Please Select a Menu Below:
            1. View Data
            2. Add Car
            3. Update Car
            4. Delete Car
            5. Exit
        """)
        menu = int(input("Enter your input: "))
        if menu == 1:
            license_plate = input("Enter car license plate (leave blank to view all data): ")
            view_cars(license_plate)
            continue_program()
        elif menu == 2:
            add_car()
            continue_program()
        elif menu == 3:
            update_car_menu()
            continue_program()
        elif menu == 4:
            view_cars()
            print()
            license_plate = input("Enter car license plate: ")
            delete_car(license_plate)
            continue_program()
        elif menu == 5:
            print("Thank you, see you later!")
            exit()
        else:
            print("Invalid choice. Please enter again.")
    except Exception as e:
        print(f"Invalid input. Please enter again.")
        continue_program()



def view_cars(license_plate=None):
    try:
        if license_plate:
            license_plate = license_plate.upper().replace(" ", "")
            filtered_cars = [car for car in cars if car["license_plate"] == license_plate]
            if not filtered_cars:
                print("Data not found.")
                return
            data = filtered_cars
        else:
            data = cars

        print(tabulate(data, headers="keys", maxcolwidths=[9 for _ in range(9)]))
    except Exception as e:
        print(f"An error occurred while printing data: {e}")

def add_car():
    while True:
        license_plate = input("Enter car license plate: ").upper().replace(" ", "")
        if not license_plate:
            print("Car license plate cannot be empty!")
            continue

        if any(car["license_plate"] == license_plate for car in cars):
            print("Car license plate already exists. Please enter a different license plate.")
            continue

        print("Car license plate successfully entered.")
        break

    while True:
        car_name = input("Enter car name: ")
        if not car_name:
            print("Car name cannot be empty!")
            continue

        print("Car name successfully entered.")
        break

    while True:
        try:
            mileage = float(input("Enter car mileage: "))
            if mileage < 0:
                print("Mileage cannot be negative!")
                continue

            print("Data successfully entered.")
            break
        except Exception as e:
            print(f"Mileage must be entered as a whole number or decimal: {e}")

    new_car = {
        "license_plate": license_plate,
        "car_name": car_name,
        "mileage": mileage,
        "available": "Yes",
        "borrower_name": "",
        "contact": "",
        "borrow_date": "",
        "return_date": "",
        "reason": ""
    }
    cars.append(new_car)

def delete_car(license_plate=None):
    try:
        license_plate = license_plate.upper().replace(" ", "")
        for car in cars:
            if car["license_plate"] == license_plate:
                if car["available"] == "Yes":
                    cars.remove(car)
                    print("Data deleted.")
                else:
                    print("The car must be returned first before it can be deleted.")
                return
        print("Data not found.")
    except Exception as e:
        print(f"An error occurred while deleting data: {e}")

def update_car_menu():
    try:
        print("""
        You are in the update car menu.
        Please Select a Menu Below:
            1. Update Car
            2. Borrow Car
            3. Return Car
            4. Return To Main Menu
        """)
        menu = int(input("Enter your input: "))
        if menu == 1:
            license_plate = input("Enter car license plate: ").upper().replace(" ", "")
        elif menu == 2:
            license_plate = input("Enter car license plate: ").upper().replace(" ", "")
        elif menu == 3:
            view_cars()
            license_plate = input("Enter car license plate: ").upper().replace(" ", "")
            return_car(license_plate)
        elif menu == 4:
            print("Going back to main menu...")
            main()
        else:
            print("Invalid choice. Please enter again.")
    except Exception as e:
        print(f"Invalid input. Please enter again.")
        input("Press Enter to continue...")
        os_name = platform.system()
        if os_name == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        update_car_menu()

def return_car(license_plate=None):
    try:
        license_plate = license_plate.upper().replace(" ", "")
        for car in cars:
            if car["license_plate"] == license_plate:
                if car["available"] == "Yes":
                    print("The car is available which has no borrower yet.")
                else:
                    print("The car is returned.")
                    update_car = {
                        "license_plate": car["license_plate"],
                        "car_name": car["car_name"],
                        "mileage": car["mileage"],
                        "available": "Yes",
                        "borrower_name": "",
                        "contact": "",
                        "borrow_date": "",
                        "return_date": "",
                        "reason": ""
                    }
                    car.update(update_car)
                return
        print("Data not found.")
    except Exception as e:
        print(f"An error occurred while deleting data: {e}")

def continue_program():
    os_name = platform.system()
    input("Press Enter to continue...")
    if os_name == 'Windows':
        os.system("cls")
    else:
        os.system("clear")
    main()

if __name__ == "__main__":
    main()
