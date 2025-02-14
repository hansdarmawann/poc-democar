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
        MILEAGE_KEY: 12345.67,
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

def view_cars(license_plate=None, headers="keys", columns=None, available_only=None):
    """View car details based on license plate or all cars."""    
    try:       
        if license_plate:
            license_plate = license_plate.upper().replace(" ", "")
            filtered_cars = [car for car in cars if car[LICENSE_PLATE_KEY] == license_plate]
            if not filtered_cars:
                print("Data not found.")
                return
            data = filtered_cars
        else:
            data = cars

        # Filter data based on availability if available_only is True
        if available_only == True:
            data = [car for car in data if car[AVAILABLE_KEY] == "Yes"]
        elif available_only == False:
            data = [car for car in data if car[AVAILABLE_KEY] == "No"]
        elif available_only == None:
            data = [car for car in data]
            
        # If specific columns are provided, filter the data
        if columns:
            data = [{key: car[key] for key in columns} for car in data]

        print(tabulate(data, headers=headers, maxcolwidths=[15] * len(data[0])))
    except Exception as e:
        pass

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
    while True:
        license_plate = input("Input new car license plate to add: ").upper().replace(" ", "")
        if not license_plate:
            print("License plate cannot be empty!")
            continue
        if any(car[LICENSE_PLATE_KEY] == license_plate for car in cars):
            print("License plate already exists. Please enter a different license plate.")
            continue
        break

    while True:
        car_name = input("Input car name to add: ")
        if not car_name:
            print("Car name cannot be empty!")
            continue
        break

    while True:
        try:
            mileage = float(input("Input car mileage to add: "))
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
            
            while True:
                new_license_plate = input("Input new license plate to add (Press Enter to ignore): ").upper().replace(" ", "")
                if new_license_plate and any(car[LICENSE_PLATE_KEY] == new_license_plate for car in cars if car[LICENSE_PLATE_KEY] != license_plate):
                    print("License plate already exists. Please enter a different license plate.")
                    continue
                break
            
            car[LICENSE_PLATE_KEY] = new_license_plate or car[LICENSE_PLATE_KEY]
            
            new_car_name = input("Input new car name (Press Enter to ignore): ")            
            car[CAR_NAME_KEY] = new_car_name or car[CAR_NAME_KEY]
            
            while True:
                try:
                    mileage_input = input("Input new mileage (Press Enter to ignore): ")
                    if mileage_input == "":
                        break
                    mileage = float(mileage_input)
                    if mileage < 0:
                        print("Mileage cannot be negative!")
                        continue
                    car[MILEAGE_KEY] = float(round(mileage, 2))
                    break
                except ValueError:
                    print("Mileage must be a valid number!")
            
            print("Car information updated.")
            view_cars(car[LICENSE_PLATE_KEY])
            return
    print("Data not found.")


def return_car(license_plate):
    """Return the borrowed car information based on license plate."""
    if len(cars) == 0:
        print("Currently there are no cars available.")
        return

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
                while True:
                    car[BORROWER_NAME_KEY] = input("Input the borrower: ")
                    if not car[BORROWER_NAME_KEY]:
                        print("Borrower name cannot be empty!")
                    else:
                        break
                while True:
                    car[CONTACT_KEY] = input("Input the borrower contact number: ")
                    if car[CONTACT_KEY].isdigit():
                        break
                    else:
                        print("Invalid input format. Please input the proper contact number.")
                while True:
                    try:
                        borrow_date_str = input("Input the borrow date (YYYY-MM-DD): ")
                        car[BORROW_DATE_KEY] = datetime.datetime.strptime(borrow_date_str, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                while True:
                    try:
                        return_date_str = input("Input the return date (YYYY-MM-DD): ")
                        return_date = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()
                        if return_date < car[BORROW_DATE_KEY]:
                            print("Return date must be after borrow date. Please enter a valid return date.")
                        else:
                            car[RETURN_DATE_KEY] = return_date
                            break
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                while True:
                    car[REASON_KEY] = input("Input reason for borrowing: ")
                    if not car[REASON_KEY]:
                        print("Reason for borrowing cannot be empty!")
                    else:
                        break

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
    if os_name == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def continue_screen():
    input("Press Enter to continue...")

def view_car_submenu():
    """Submenu for viewing cars."""
    if len(cars) == 0:
        print("Currently there are no cars available.")
        return
    while True:
        print("""
        View Car Options:
            1. View All Cars
            2. View Cars Based on License Plate
            3. Back to Main Menu
        """)
        try:
            view_option = int(input("Please input your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue_screen()
            clear_screen()
            continue

        if view_option == 1:
            view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY])
            continue_screen()
            clear_screen()
        elif view_option == 2:
            while True:
                license_plate = input("Please input the car that you want to view based on the license plate: ").upper().replace(" ", "")
                if license_plate == "":
                    print("You must input the license plate!")
                    continue
                break
            view_cars(license_plate, columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY])
            continue_screen()
            clear_screen()
        elif view_option == 3:
            print("Going back to menu.")
            continue_screen()
            clear_screen()
            break
        else:
            print("Invalid choice. Please try again.")

def add_car_submenu():
    """Submenu for adding a car."""
    view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY, AVAILABLE_KEY])
    add_car()
    continue_screen()
    clear_screen()

def manage_car_submenu():
    """Submenu for managing cars (Update, Borrow, Return)."""
    if len(cars) == 0:
        print("Currently there are no cars available.")
        return
    while True:
        clear_screen()
        print("""
        Manage Car Options:
            1. Update Car
            2. Borrow Car
            3. Return Car
            4. Back to Main Menu
        """)
        try:
            manage_option = int(input("Please input your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue_screen()
            clear_screen()
            continue

        if manage_option == 1:
            view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY])
            while True:
                license_plate = input("Input license plate of the car to update: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                break
            update_car(license_plate)
            continue_screen()
            clear_screen()
        elif manage_option == 2:
            view_cars(available_only=True)
            while True:
                license_plate = input("Input license plate of the car to borrow: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                break
            borrow_car(license_plate)
            continue_screen()
            clear_screen()
        elif manage_option == 3:
            view_cars(available_only=False)
            while True:
                license_plate = input("Input license plate of the car to return: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                break
            return_car(license_plate)
            continue_screen()
            clear_screen()
        elif manage_option == 4:
            print("Going back to menu.")
            continue_screen()
            clear_screen()
            break
        else:
            print("Invalid choice. Please try again.")
            continue_screen()
            clear_screen()

def delete_car_submenu():
    """Submenu for deleting a car."""
    if len(cars) == 0:
        print("Currently there are no cars available.")
        return
        
    view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY, AVAILABLE_KEY])
    license_plate = input("Input license plate of the car to delete: ").upper().replace(" ", "")
    if not license_plate:
        print("License plate cannot be empty!")
        return
    delete_car(license_plate)
    continue_screen()
    clear_screen()

def main():
    """Main function to run the demo car lending system."""
    while True:
        print("""
        Welcome to the XYZ Demo Car Lending System
        Please choose an option below:
            1. View Car
            2. Add Car
            3. Manage Car (Update, Borrow, Return)
            4. Delete Car
            5. Exit
        """)
        try:
            menu = int(input("Please input your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue_screen()
            clear_screen()
            continue

        if menu == 1:
            clear_screen()
            view_car_submenu()
        elif menu == 2:
            clear_screen()
            add_car_submenu()
        elif menu == 3:
            clear_screen()
            manage_car_submenu()
        elif menu == 4:
            clear_screen()
            delete_car_submenu()
        elif menu == 5:
            print("Thank you, see you next time!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue_screen()
            clear_screen()

if __name__ == "__main__":
    main()
