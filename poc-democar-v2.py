from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional, List
from tabulate import tabulate
import os
import platform

# Data Model

@dataclass
class Car:
    license_plate: str
    car_name: str
    mileage: float
    available: bool = True
    borrower_name: Optional[str] = None
    contact: Optional[str] = None
    borrow_date: Optional[date] = None
    return_date: Optional[date] = None
    reason: Optional[str] = None

    def is_available(self) -> bool:
        return self.available

# Initial car data 

cars: List[Car] = [
    Car(
        license_plate="B1071PDM",
        car_name="Range Rover P615",
        mileage=12345.67,
        available=False,
        borrower_name="Fitra Eri",
        contact="081234567891",
        borrow_date=date(2024, 6, 24),
        return_date=date(2024, 6, 30),
        reason="Review Purpose"
    ),
    Car(
        license_plate="B1010LKX",
        car_name="Mercedes Benz G63 AMG",
        mileage=901.23,
        available=True
    )
]

# Input Helpers

def input_license_plate(prompt="Input license plate: ") -> str:
    while True:
        lp = input(prompt).upper().replace(" ", "")
        if not lp:
            print("License plate cannot be empty!")
            continue
        if len(lp) > 10:
            print("License plate length maximum is 10 characters!")
            continue
        return lp

def input_nonempty_string(prompt: str) -> str:
    while True:
        value = input(prompt)
        if not value.strip():
            print("Input cannot be empty!")
            continue
        return value.strip()

def input_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative!")
                continue
            return value
        except ValueError:
            print("Please input a valid number!")

def input_date(prompt: str) -> date:
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Core Functions

def view_cars(license_plate=None, headers="keys", columns=None, available_only=None):
    """View car details based on license plate or all cars."""
    try:
        if license_plate:
            license_plate = license_plate.upper().replace(" ", "")
            filtered_cars = [car for car in cars if car.license_plate == license_plate]
            if not filtered_cars:
                print("Data not found.")
                return
            data = filtered_cars
        else:
            data = cars

        if available_only is True:
            data = [car for car in data if car.available]
        elif available_only is False:
            data = [car for car in data if not car.available]

        if columns:
            data_to_display = [
                {col: getattr(car, col) for col in columns} for car in data
            ]
        else:
            data_to_display = [car.__dict__ for car in data]

        if not data_to_display:
            print("No data to display.")
            return

        for row in data_to_display:
            for key in ['borrow_date', 'return_date']:
                if key in row and isinstance(row[key], date):
                    row[key] = row[key].isoformat()

        print(tabulate(data_to_display, headers=headers, maxcolwidths=[15] * len(data_to_display[0])))

    except Exception as e:
        print(f"An error occurred: {e}")

def delete_car(license_plate):
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car.license_plate == license_plate:
            if car.available:
                while True:
                    sure = input("Are you sure you want to delete this car? (Yes / No): ").title().replace(" ","")
                    if sure == "Yes":
                        cars.remove(car)
                        print("Car deleted.")
                        return
                    elif sure == "No":
                        print("Car deletion aborted.")
                        return
                    else:
                        print("The input is not valid. You must choose between Yes or No.")
            else:
                print("The car must be returned before it can be deleted.")
            return
    print("Data not found.")

def add_car():
    while True:
        license_plate = input_license_plate("Input new car license plate to add: ")
        if any(car.license_plate == license_plate for car in cars):
            print("License plate already exists. Please enter a different license plate.")
            continue
        break

    car_name = input_nonempty_string("Input car name to add: ")
    mileage = input_float("Input car mileage to add: ")

    new_car = Car(
        license_plate=license_plate,
        car_name=car_name,
        mileage=mileage,
        available=True
    )
    cars.append(new_car)
    print("Car added successfully.")
    view_cars(license_plate)

def update_car(license_plate):
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car.license_plate == license_plate:
            view_cars(license_plate)
            
            while True:
                new_license_plate = input("Input new license plate to update (Press Enter to ignore): ").upper().replace(" ", "")
                if new_license_plate and any(c.license_plate == new_license_plate for c in cars if c.license_plate != license_plate):
                    print("License plate already exists. Please enter a different license plate.")
                    continue
                break
            
            if new_license_plate:
                car.license_plate = new_license_plate
            
            new_car_name = input("Input new car name (Press Enter to ignore): ")
            if new_car_name:
                car.car_name = new_car_name
            
            while True:
                mileage_input = input("Input new mileage (Press Enter to ignore): ")
                if mileage_input == "":
                    break
                try:
                    mileage = float(mileage_input)
                    if mileage < 0:
                        print("Mileage cannot be negative!")
                        continue
                    car.mileage = mileage
                    break
                except ValueError:
                    print("Mileage must be a valid number!")
            
            print("Car information updated.")
            view_cars(car.license_plate)
            return
    print("Data not found.")

def return_car(license_plate):
    if not cars:
        print("Currently there are no cars available.")
        return
    
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car.license_plate == license_plate:
            if not car.available:
                view_cars(license_plate)
                car.available = True
                car.borrower_name = None
                car.contact = None
                car.borrow_date = None
                car.return_date = None
                car.reason = None
                print("The car has been successfully returned.")
                view_cars(car.license_plate)
            else:
                print("The car is available and has no borrower yet.")
            return
    print("Data not found.")

def borrow_car(license_plate):
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        if car.license_plate == license_plate:
            if car.available:
                while True:
                    borrower = input_nonempty_string("Input the borrower: ")
                    if borrower:
                        car.borrower_name = borrower
                        break
                while True:
                    contact = input("Input the borrower contact number: ")
                    if contact.isdigit():
                        car.contact = contact
                        break
                    else:
                        print("Invalid input format. Please input the proper contact number.")
                car.borrow_date = input_date("Input the borrow date (YYYY-MM-DD): ")
                while True:
                    return_date = input_date("Input the return date (YYYY-MM-DD): ")
                    if return_date < car.borrow_date:
                        print("Return date must be after borrow date. Please enter a valid return date.")
                    else:
                        car.return_date = return_date
                        break
                car.reason = input_nonempty_string("Input reason for borrowing: ")
                car.available = False
                print("Car has been successfully borrowed.")
                view_cars(car.license_plate)
            else:
                print("The car is currently unavailable.")
            return
    print("Data not found.")

# Utility Functions

def clear_screen():
    os_name = platform.system()
    if os_name == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def continue_screen():
    input("Press Enter to continue...")

# Submenus

def view_car_submenu():
    if not cars:
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
            view_cars(columns=['license_plate', 'car_name', 'mileage'])
            continue_screen()
            clear_screen()
        elif view_option == 2:
            while True:
                license_plate = input("Please input the car that you want to view based on the license plate: ").upper().replace(" ", "")
                if not license_plate:
                    print("You must input the license plate!")
                    continue
                break
            view_cars(license_plate, columns=['license_plate', 'car_name', 'mileage'])
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
    view_cars(columns=['license_plate', 'car_name', 'mileage', 'available'])
    add_car()
    continue_screen()
    clear_screen()

def manage_car_submenu():
    if not cars:
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
            view_cars(columns=['license_plate', 'car_name', 'mileage'])
            while True:
                license_plate = input("Input license plate of the car to update: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                if any(car.license_plate == license_plate for car in cars):
                    update_car(license_plate)
                    break
                else:
                    print("Car not found. Please input a valid license plate.")
            continue_screen()
            clear_screen()
        elif manage_option == 2:
            if all(not car.available for car in cars):
                print("All cars are borrowed.")
                continue_screen()
                clear_screen()
                break
            view_cars(available_only=True)
            while True:
                license_plate = input("Input license plate of the car to borrow: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                if any(car.license_plate == license_plate for car in cars):
                    borrow_car(license_plate)
                    break
                else:
                    print("Car not found. Please input a valid license plate.")
            continue_screen()
            clear_screen()
        elif manage_option == 3:
            if all(car.available for car in cars):
                print("All cars are available.")
                continue_screen()
                clear_screen()
                break
            view_cars(available_only=False)
            while True:
                license_plate = input("Input license plate of the car to return: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                if any(car.license_plate == license_plate for car in cars):
                    return_car(license_plate)
                    break
                else:
                    print("Car not found. Please input a valid license plate.")
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
    if not cars:
        print("Currently there are no cars available.")
        return
    
    view_cars(columns=['license_plate', 'car_name', 'mileage', 'available'])
    
    while True:
        license_plate = input("Input license plate of the car to delete: ").upper().replace(" ", "")
        if not license_plate:
            print("License plate cannot be empty!")
            continue
        if any(car.license_plate == license_plate for car in cars):
            delete_car(license_plate)
            break
        else:
            print("Car not found. Please check the license plate and try again.")
    
    continue_screen()
    clear_screen()

# Main Program Flow

def main():
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