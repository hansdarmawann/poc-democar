from tabulate import tabulate
import datetime
import os
import platform

# Constants for dictionary keys
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
        # Filter cars based on license plate if provided
        if license_plate:
            license_plate = license_plate.upper().replace(" ", "")
            filtered_cars = [car for car in cars if car[LICENSE_PLATE_KEY] == license_plate]
            # If no cars match the license plate, notify the user
            if not filtered_cars:
                print("Data not found.")
                return
            data = filtered_cars
        else:
            # If no license plate is provided, use all cars
            data = cars

        # Filter data based on availability if available_only is True
        if available_only is True:
            data = [car for car in data if car[AVAILABLE_KEY] == "Yes"]
        elif available_only is False:
            data = [car for car in data if car[AVAILABLE_KEY] == "No"]

        # If specific columns are provided, filter the data to show only those columns
        if columns:
            data = [{key: car[key] for key in columns} for car in data]

        # Display the filtered data in a tabular format
        print(tabulate(data, headers=headers, maxcolwidths=[15] * len(data[0])))
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_car(license_plate):
    """Delete a car from the list based on license plate."""
    # Normalize the license plate input
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        # Check if the car with the given license plate exists
        if car[LICENSE_PLATE_KEY] == license_plate:
            # Check if the car is available for deletion
            if car[AVAILABLE_KEY] == "Yes":
                while True:
                    # Confirm deletion from the user (Normalize the Yes / No)
                    sure = input("Are you sure you want to delete this car? (Yes / No): ").title().replace(" ","")
                    if sure == "Yes":
                        # Remove the car from the list
                        cars.remove(car)
                        print("Car deleted.")
                        return
                    if sure == "No":
                        print("Car deletion aborted.")
                        return
                    else:
                        print("The input is not valid. You must choose between Yes or No.")
                        continue
            else:
                print("The car must be returned before it can be deleted.")
            return
    print("Data not found.")

def add_car():
    """Add a new car to the list."""
    while True:
        # Prompt user for the new car's license plate
        license_plate = input("Input new car license plate to add: ").upper().replace(" ", "")
        if not license_plate:
            print("License plate cannot be empty!")
            continue
        # Check if the license plate already exists
        if any(car[LICENSE_PLATE_KEY] == license_plate for car in cars):
            print("License plate already exists. Please enter a different license plate.")
            continue
        # Validate the length of the license plate
        if len(license_plate) >= 9:
            print('License plate length maximum is 9 characters!')
            continue
        break

    while True:
        # Prompt user for the car name
        car_name = input("Input car name to add: ")
        if not car_name:
            print("Car name cannot be empty!")
            continue
        break

    while True:
        try:
            # Prompt user for the car mileage
            mileage = float(input("Input car mileage to add: "))
            if mileage < 0:
                print("Mileage cannot be negative!")
                continue
            break
        except ValueError:
            print("Mileage must be a valid number!")

    # Create a new car dictionary with the provided details
    new_car = {
        LICENSE_PLATE_KEY: license_plate,
        CAR_NAME_KEY: car_name,
        MILEAGE_KEY: float(mileage),
        AVAILABLE_KEY: "Yes",
        BORROWER_NAME_KEY: "",
        CONTACT_KEY: "",
        BORROW_DATE_KEY: "",
        RETURN_DATE_KEY: "",
        REASON_KEY: ""
    }
    # Add the new car to the list
    cars.append(new_car)
    print("Car added successfully.")
    # Display the details of the newly added car
    view_cars(license_plate)

def update_car(license_plate):
    """Update car information based on license plate."""
    # Normalize the license plate input
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        # Check if the car with the given license plate exists
        if car[LICENSE_PLATE_KEY] == license_plate:
            # Display current car details
            view_cars(license_plate)
            
            while True:
                # Prompt user for a new license plate
                new_license_plate = input("Input new license plate to update (Press Enter to ignore): ").upper().replace(" ", "")
                # Check if the new license plate already exists
                if new_license_plate and any(car[LICENSE_PLATE_KEY] == new_license_plate for car in cars if car[LICENSE_PLATE_KEY] != license_plate):
                    print("License plate already exists. Please enter a different license plate.")
                    continue
                break
            
            # Update the license plate if provided, otherwise keep the old one
            car[LICENSE_PLATE_KEY] = new_license_plate or car[LICENSE_PLATE_KEY]
            
            # Prompt user for a new car name
            new_car_name = input("Input new car name (Press Enter to ignore): ")            
            car[CAR_NAME_KEY] = new_car_name or car[CAR_NAME_KEY]
            
            while True:
                try:
                    # Prompt user for new mileage
                    mileage_input = input("Input new mileage (Press Enter to ignore): ")
                    if mileage_input == "":
                        break
                    mileage = float(mileage_input)
                    if mileage < 0:
                        print("Mileage cannot be negative!")
                        continue
                    car[MILEAGE_KEY] = float(mileage)
                    break
                except ValueError:
                    print("Mileage must be a valid number!")
            
            print("Car information updated.")
            # Display the updated car details
            view_cars(car[LICENSE_PLATE_KEY])
            return
    print("Data not found.")

def return_car(license_plate):
    """Return the borrowed car information based on license plate."""
    # Check if there are any cars in the system
    if len(cars) == 0:
        print("Currently there are no cars available.")
        return
    
    # Normalize the license plate input
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        # Check if the car with the given license plate exists
        if car[LICENSE_PLATE_KEY] == license_plate:
            # Check if the car is currently borrowed
            if car[AVAILABLE_KEY] == "No":
                # Display current car details
                view_cars(license_plate)
                # Update the car's status to available
                car[AVAILABLE_KEY] = "Yes"
                # Clear borrower details
                car[BORROWER_NAME_KEY] = ""
                car[CONTACT_KEY] = ""
                car[BORROW_DATE_KEY] = ""
                car[RETURN_DATE_KEY] = ""
                car[REASON_KEY] = ""
                print("The car has been successfully returned.")
                # Display the details of the returned car
                view_cars(car[LICENSE_PLATE_KEY])
            else:
                print("The car is available and has no borrower yet.")
            return
    print("Data not found.")

def borrow_car(license_plate):
    """Borrow a car if it is available."""
    # Normalize the license plate input
    license_plate = license_plate.upper().replace(" ", "")
    for car in cars:
        # Check if the car with the given license plate exists
        if car[LICENSE_PLATE_KEY] == license_plate:
            # Check if the car is available for borrowing
            if car[AVAILABLE_KEY] == "Yes":
                while True:
                    # Prompt user for the borrower's name
                    car[BORROWER_NAME_KEY] = input("Input the borrower: ")
                    if not car[BORROWER_NAME_KEY]:
                        print("Borrower name cannot be empty!")
                    else:
                        break
                while True:
                    # Prompt user for the borrower's contact number
                    car[CONTACT_KEY] = input("Input the borrower contact number: ")
                    if car[CONTACT_KEY].isdigit():
                        break
                    else:
                        print("Invalid input format. Please input the proper contact number.")
                while True:
                    try:
                        # Prompt user for the borrow date
                        borrow_date_str = input("Input the borrow date (YYYY-MM-DD): ")
                        car[BORROW_DATE_KEY] = datetime.datetime.strptime(borrow_date_str, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                while True:
                    try:
                        # Prompt user for the return date
                        return_date_str = input("Input the return date (YYYY-MM-DD): ")
                        return_date = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()
                        # Validate that the return date is after the borrow date
                        if return_date < car[BORROW_DATE_KEY]:
                            print("Return date must be after borrow date. Please enter a valid return date.")
                        else:
                            car[RETURN_DATE_KEY] = return_date
                            break
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                while True:
                    # Prompt user for the reason for borrowing
                    car[REASON_KEY] = input("Input reason for borrowing: ")
                    if not car[REASON_KEY]:
                        print("Reason for borrowing cannot be empty!")
                    else:
                        break

                # Update the car's status to unavailable
                car[AVAILABLE_KEY] = "No"
                print("Car has been successfully borrowed.")
                # Display the details of the borrowed car
                view_cars(car[LICENSE_PLATE_KEY])
            else:
                print("The car is currently unavailable.")
            return
    print("Data not found.")

def clear_screen():
    """Clear the console screen."""
    os_name = platform.system()
    if os_name == 'Windows':
        os.system("cls")  # Clear screen for Windows
    else:
        os.system("clear")  # Clear screen for Unix/Linux

def continue_screen():
    """Pause the program and wait for user input to continue."""
    input("Press Enter to continue...")

def view_car_submenu():
    """Submenu for viewing cars."""
    # Check if there are any cars in the system
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
            # Prompt user for their choice
            view_option = int(input("Please input your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue_screen()
            clear_screen()
            continue

        if view_option == 1:
            # View all cars
            view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY])
            continue_screen()
            clear_screen()
        elif view_option == 2:
            while True:
                # Prompt user for a specific license plate to view
                license_plate = input("Please input the car that you want to view based on the license plate: ").upper().replace(" ", "")
                if license_plate == "":
                    print("You must input the license plate!")
                    continue
                break
            # View car details based on the provided license plate
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
    # Display current cars before adding a new one
    view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY, AVAILABLE_KEY])
    # Call the add_car function to add a new car
    add_car()
    continue_screen()
    clear_screen()

def manage_car_submenu():
    """Submenu for managing cars (Update, Borrow, Return)."""
    # Check if there are any cars in the system
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
            # Prompt user for their choice
            manage_option = int(input("Please input your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue_screen()
            clear_screen()
            continue

        if manage_option == 1:
            # View all cars before updating
            view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY])
            while True:
                # Prompt user for the license plate of the car to update
                license_plate = input("Input license plate of the car to update: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                # Check if the license plate exists in the cars list
                if any(car[LICENSE_PLATE_KEY] == license_plate for car in cars):
                    update_car(license_plate)  # Call update function
                    break
                else:
                    print("Car not found. Please input a valid license plate.")
                    continue
            continue_screen()
            clear_screen()
        elif manage_option == 2:
            # Check if all cars are borrowed
            if all(car[AVAILABLE_KEY] == "No" for car in cars):
                print("All cars are borrowed.")
                continue_screen()
                clear_screen()
                break
            # View available cars before borrowing
            view_cars(available_only=True)
            while True:
                # Prompt user for the license plate of the car to borrow
                license_plate = input("Input license plate of the car to borrow: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                # Check if the license plate exists in the cars list
                if any(car[LICENSE_PLATE_KEY] == license_plate for car in cars):
                    borrow_car(license_plate)  # Call borrow function
                    break
                else:
                    print("Car not found. Please input a valid license plate.")
                    continue
            continue_screen()
            clear_screen()
        elif manage_option == 3:
            # Check if all cars are available
            if all(car[AVAILABLE_KEY] == "Yes" for car in cars):
                print("All cars are available.")
                continue_screen()
                clear_screen()
                break
            # View all cars before returning
            view_cars(available_only=False)
            while True:
                # Prompt user for the license plate of the car to return
                license_plate = input("Input license plate of the car to return: ").upper().replace(" ", "")
                if not license_plate:
                    print("License plate cannot be empty!")
                    continue
                # Check if the license plate exists in the cars list
                if any(car[LICENSE_PLATE_KEY] == license_plate for car in cars):
                    return_car(license_plate)  # Call return function
                    break
                else:
                    print("Car not found. Please input a valid license plate.")
                    continue
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
    # Check if there are any cars in the system
    if len(cars) == 0:
        print("Currently there are no cars available.")
        return
        
    # Display current cars before deletion
    view_cars(columns=[LICENSE_PLATE_KEY, CAR_NAME_KEY, MILEAGE_KEY, AVAILABLE_KEY])
    
    # Prompt user for the license plate of the car to delete
    while True:
        license_plate = input("Input license plate of the car to delete: ").upper().replace(" ", "")
        if not license_plate:
            print("License plate cannot be empty!")
            continue
        # Check if the license plate exists in the cars list
        if any(car[LICENSE_PLATE_KEY] == license_plate for car in cars):
            delete_car(license_plate)  # Call delete function
            break
        else:
            print("Car not found. Please check the license plate and try again.")
            continue
    
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
            # Prompt user for their choice
            menu = int(input("Please input your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue_screen()
            clear_screen()
            continue

        if menu == 1:
            clear_screen()
            view_car_submenu()  # Call view car submenu
        elif menu == 2:
            clear_screen()
            add_car_submenu()  # Call add car submenu
        elif menu == 3:
            clear_screen()
            manage_car_submenu()  # Call manage car submenu
        elif menu == 4:
            clear_screen()
            delete_car_submenu()  # Call delete car submenu
        elif menu == 5:
            print("Thank you, see you next time!")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")
            continue_screen()
            clear_screen()

if __name__ == "__main__":
    main()  # Run the main function to start the program
