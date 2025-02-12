# Capstone Project 1: Proof of Concept: Demo Car Lending System at XYZ Dealer by Hans Darmawan (JCDS2602)

## 1. Background

XYZ Dealer is a prominent car dealership in Indonesia that offers a variety of car brands. To promote their vehicles, the dealer invests in demo cars, which customers can borrow under certain conditions. However, the current manual process for recording these loans presents several challenges:

- **Inefficient Operations**: The existing borrowing process is cumbersome, leading to delays, errors, and dissatisfaction among both internal and external customers.
- **Data Management Limitations**: Manual recording makes it difficult to track the availability of demo cars, resulting in potential misinformation.

## 2. Gap Analysis

The analysis reveals significant gaps between the current system and user needs:

- **Human Error in Manual Recording**: The reliance on manual processes increases the likelihood of errors and slows down the confirmation of demo car availability.
- **Lack of Real-Time Data Tracking**: The current system does not provide real-time information on demo car availability, complicating effective monitoring and management.

## 3. Objectives

The primary goal of this Capstone Project is to develop a proof of concept for a simple demo car loan system. This system will manage the car loan process with full CRUD (Create, Read, Update, Delete) functionality, implemented without file or database operations.

## 4. Project Scope (Scope of Work)

- Development of a user-friendly interface for managing demo car loans.
- Implementation of core functionalities to handle car data efficiently.

## 5. Requirements Analysis

- **Functional Requirements**:
  - Ability to view, add, update, and delete car records.
  - Track borrowing and returning of demo cars.
  - Ensure data integrity and minimize errors.

## 6. System Design

The system is designed to efficiently manage the demo car lending process through a structured data model and a set of functional operations.

### Data Structure

The system utilizes a list of dictionaries to represent the car data. Each dictionary contains the following keys and their corresponding values:

- **`license_plate`**: (String) The unique identifier for the car.
- **`car_name`**: (String) The name of the car model.
- **`mileage`**: (Float) The mileage of the car.
- **`available`**: (String) Indicates whether the car is available for borrowing ("Yes" or "No").
- **`borrower_name`**: (String) The name of the person borrowing the car.
- **`contact`**: (String) The contact number of the borrower.
- **`borrow_date`**: (Date) The date when the car was borrowed.
- **`return_date`**: (Date) The date when the car is expected to be returned.
- **`reason`**: (String) The reason for borrowing the car.

### CRUD Functions

The system implements the following core functions to manage the demo car lending process:

- **`view_cars(license_plate=None)`**: Displays car details based on the license plate or all cars if no plate is provided.
- **`add_car()`**: Allows users to add a new car to the system with validation for unique license plates and valid mileage.
- **`update_car(license_plate)`**: Updates existing car details based on the provided license plate.
- **`borrow_car(license_plate)`**: Facilitates the borrowing of a car if it is available, collecting necessary borrower information.
- **`return_car(license_plate)`**: Processes the return of a borrowed car, updating its availability status.
- **`delete_car(license_plate)`**: Deletes a car from the system if it is available.

### Libraries Used

- **`tabulate`**: This library is used to format and display the car data in a readable table format, enhancing the user interface for viewing car details.
- **`datetime`**: This library is utilized for handling date and time operations, allowing the system to manage borrowing and return dates effectively.
- **`os`**: This library is used to clear the console screen, improving user experience by providing a cleaner interface.
- **`platform`**: This library helps determine the operating system, allowing the system to use the appropriate command for clearing the screen.

## 7. Implementation

- The implementation is encapsulated in a Python script, which includes all necessary functionalities for managing the demo car lending process.

## 8. Testing Methods

- Testing will focus on verifying the functionality of the implemented features, ensuring that the system meets the outlined objectives and requirements.

## 9. Conclusion

This project aims to streamline the demo car lending process at XYZ Dealer, enhancing efficiency and customer satisfaction through a structured and automated system. By addressing the identified gaps, the proposed solution will facilitate better management of demo cars and improve overall operational effectiveness.
