from tabulate import tabulate
import datetime
import os
import platform

# Constants
LICENSE_PLATE_KEY = "license_plate"
CAR_NAME_KEY = "car_name"
MILEAGE_KEY = "mileage"
AVAILABLE_KEY = "available"
BORROWER_NAME_KEY = "borrower_name"
CONTACT_KEY = "contact"
BORROW_DATE_KEY = "borrow_date"
RETURN_DATE_KEY = "return_date"
REASON_KEY = "reason"

# Initial car data
cars = [
    {
        LICENSE_PLATE_KEY: "B1071PDM",
        CAR_NAME_KEY: "Range Rover P615",
        MILEAGE_KEY: 12345.678,
        AVAILABLE_KEY: "No",
        BORROWER_NAME_KEY: "Fitra Eri",
        CONTACT_KEY: "081234567891",
        BORROW_DATE_KEY: datetime.date(2024, 6, 24),
        RETURN_DATE_KEY: datetime.date(2024, 6, 30),
        REASON_KEY: "Review Purpose"
    },
    {
        LICENSE_PLATE_KEY: "B1010LKX",
        CAR_NAME_KEY: "Mercedes Benz G63 AMG",
        MILEAGE_KEY: 901.23,
        AVAILABLE_KEY: "Yes",
        BORROWER_NAME_KEY: "",
        CONTACT_KEY: "",
        BORROW_DATE_KEY: "",
        RETURN_DATE_KEY: "",
        REASON_KEY: ""
    }
]

def view_cars(license_plate=None):
    """View car details based on license plate or all cars."""
    if license_plate:
        license_plate = license_plate.upper().replace(" ", "")
        filtered_cars = [car for car in cars if car[LICENSE_PLATE_KEY] == license_plate]
        if not filtered_cars:
            print("Data not found.")
            return
        data = filtered_cars
    else:
        data = cars

    print(tabulate(data, headers="keys", maxcolwidths=[15] * len(data[0])))

def delete_car(license_plate):
    """Delete a car from the list based on license plate."""
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car[LICENSE_PLATE_KEY] == license_plate:
            if car[AVAILABLE_KEY] == "Yes":
                cars.remove(car)
                print("Data deleted.")
            else:
                print("The car must be returned before it can be deleted.")
            return
    print("Data not found.")

def add_car():
    """Add a new car to the list."""
    license_plate = input("Input car license plate: ").upper().replace(" ", "")
    if not license_plate:
        print("License plate cannot be empty!")
        return

    if any(car[LICENSE_PLATE_KEY] == license_plate for car in cars):
        print("License plate already exists. Please enter a different license plate.")
        return

    car_name = input("Input car name: ")
    if not car_name:
        print("Car name cannot be empty!")
        return

    while True:
        try:
            mileage = float(input("Input car mileage: "))
            if mileage < 0:
                print("Mileage cannot be negative!")
                continue
            break
        except ValueError:
            print("Mileage must be a valid number!")

    new_car = {
        LICENSE_PLATE_KEY: license_plate,
        CAR_NAME_KEY: car_name,
        MILEAGE_KEY: mileage,
        AVAILABLE_KEY: "Yes",
        BORROWER_NAME_KEY: "",
        CONTACT_KEY: "",
        BORROW_DATE_KEY: "",
        RETURN_DATE_KEY: "",
        REASON_KEY: ""
    }
    cars.append(new_car)
    print("Car added successfully.")
    view_cars(license_plate)


def update_car(license_plate):
    """Update car information based on license plate."""
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car[LICENSE_PLATE_KEY] == license_plate:
            view_cars(license_plate)
            car[LICENSE_PLATE_KEY] = input("Input new license plate to add (Press Enter to ignore): ") or car[LICENSE_PLATE_KEY]
            car[CAR_NAME_KEY] = input("Input new car name (Press Enter to ignore): ") or car[CAR_NAME_KEY]
            while True:
                try:
                    mileage_input = input("Input new mileage (Press Enter to ignore): ")
                    if mileage_input == "":
                        break
                    mileage = float(mileage_input)
                    if mileage < 0:
                        print("Mileage cannot be negative!")
                        continue
                    car[MILEAGE_KEY] = round(mileage, 2)
                    break
                except ValueError:
                    print("Mileage must be a valid number!")
            print("Car information updated.")
            view_cars(car[LICENSE_PLATE_KEY])
            return
    print("Data not found.")

def return_car(license_plate):
    """Return the borrowed car information based on license plate."""
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car[LICENSE_PLATE_KEY] == license_plate:
            if car[AVAILABLE_KEY] == "No":
                view_cars(license_plate)
                car[AVAILABLE_KEY] = "Yes"
                car[BORROWER_NAME_KEY] = ""
                car[CONTACT_KEY] = ""
                car[BORROW_DATE_KEY] = ""
                car[RETURN_DATE_KEY] = ""
                car[REASON_KEY] = ""
                print("The car has been successfully returned.")
                view_cars(car[LICENSE_PLATE_KEY])
            else:
                print("The car is available and has no borrower yet.")
            return
    print("Data not found.")

def borrow_car(license_plate):
    """Borrow a car if it is available."""
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car[LICENSE_PLATE_KEY] == license_plate:
            if car[AVAILABLE_KEY] == "Yes":
                car[BORROWER_NAME_KEY] = input("Inputower name: ")
                while True:
                    car[CONTACT_KEY] = input("Inputtact number: ")
                    if car[CONTACT_KEY].isdigit():
                        break
                    else:
                        print("Invalid input format. Please input the proper contact number.")
                while True:
                    try:
                        borrow_date_str = input("Inputrrow date (YYYY-MM-DD): ")
                        car[BORROW_DATE_KEY] = datetime.datetime.strptime(borrow_date_str, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                while True:
                    try:
                        return_date_str = input("Inputturn date (YYYY-MM-DD): ")
                        return_date = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()
                        if return_date < car[BORROW_DATE_KEY]:
                            print("Return date must be after borrow date. Please enter a valid return date.")
                        else:
                            car[RETURN_DATE_KEY] = return_date
                            break
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                car[REASON_KEY] = input("Input reason for borrowing: ")
                car[AVAILABLE_KEY] = "No"
                print("Car has been successfully borrowed.")
                view_cars(car[LICENSE_PLATE_KEY])
            else:
                print("The car is currently unavailable.")
            return
    print("Data not found.")

def clear_screen():
    """Clear the console screen."""
    os_name = platform.system()
    input("Press Inputr to continue...")
    if os_name == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def main():
    """Main function to run the car rental system."""
    while True:
        print("""
        Welcome to the XYZ Demo Car Lending System
        Please choose an option below:
            1. View Car
            2. Add Car
            3. Update Car
            4. Borrow Car
            5. Return Car
            6. Delete Car
            7. Exit
        """)
        try:
            menu = int(input("Input your choice: "))
            if menu == 1:
                license_plate = input("Input license plate (Press Enter to view all cars): ")
                view_cars(license_plate)
                clear_screen()
            elif menu == 2:
                view_cars()
                add_car()
                clear_screen()
            elif menu == 3:
                view_cars()
                license_plate = input("Input license plate of the car to update: ")
                update_car(license_plate)
                clear_screen()
            elif menu == 4:
                view_cars()
                license_plate = input("Input license plate of the car to borrow: ")
                borrow_car(license_plate)
                clear_screen()
            elif menu == 5:
                view_cars()
                license_plate = input("Input license plate of the car to return: ")
                return_car(license_plate)
                clear_screen()
            elif menu == 6:
                view_cars()
                license_plate = input("Input license plate of the car to delete: ")
                delete_car(license_plate)
                clear_screen()
            elif menu == 7:
                print("Thank you, see you next time!")
                break
            else:
                print("Invalid choice. Please try again.")
                clear_screen()
        except ValueError:
            print("Invalid input. Please enter a number.")
            clear_screen()

if __name__ == "__main__":
    main()
