# Capstone Project 1: Proof of Concept: Demo Car Lending System at XYZ Dealer by Hans Darmawan (JCDS2602)
## 1. Background

XYZ Dealer is one of the dealers that sells various car brands in Indonesia. The dealer invests in demo cars as a way to promote the cars they sell. In certain situations, there is an option for customers to borrow the demo car. When borrowing a demo car, XYZ Dealer will record the loan with a form. This is a challenge in itself, because:

- **Demo Car Operations Become Less Efficient and Effective:** This inefficient and effective borrowing process can cause delays, errors, and customer dissatisfaction, both internal and external customers.
- **Limitations in Data Management:** The manual recording method often makes it difficult to track the availability of demo cars, which can lead to misinformation.

## 2. Gap Analysis

From the background that has been written previously, there are major gaps between the current system and user needs that have not been met, including:

- **Manual Recording Causes Human Error:** The manual system is prone to human error and a slow confirmation process for the availability of demo cars.
- **Inability to Track Data in Real-Time:** The available system has the potential to not provide real-time demo car availability information. As a result, this will make it difficult to monitor and manage demo cars effectively and efficiently.

## 3. Objectives

- This Capstone Project is intended to conduct a proof of concept for a simple demo car loan system that functions to manage the car loan process, including CRUD (Create, Read, Update, Delete) functionality. This implementation will be carried out without using file or database operations.

## 4. Project Scope (Scope of Work)

- This system will be built using the Python programming language.
- There are 2 lists of dictionaries that will be created, namely car data and loan information data.

- All data will be stored in memory.
- The system will include:
- Functionality to add new car loan data.
- Functionality to view the list of car loans.
- Functionality to update existing loan information.
- Functionality to delete loan data.
- This system is designed as a capstone project and will not include formal evaluation and feedback.

## 5. Requirements Analysis

- **Functional Requirements:**
- User can add new loans with information such as loan ID, borrower name, loan date, and car details.
- User can view all existing loans.
- User can update existing loan information.
- User can delete loans from the system.

## 6. System Design -> Customizing.

- **Data Structure:**
- The loan data will be stored in a Python list or dictionary. Each entry will contain loan information. Example data structure: `[{'id': 1, 'name': 'John Doe', 'date': '2024-03-08', 'car_details': 'Toyota Camry'}, ...]`

- **CRUD Functions:**
- `create_rental(id, name, date, car_details)`: Add a new rental.
- `read_rentals()`: Display all rentals.
- `update_rental(id, name=None, date=None, car_details=None)`: Update information about an existing rental.
- `delete_rental(id)`: Remove a rental from the system.

## 7. Implementation
- Attached to the [...].py file

## 8. Testing Methods -> Tentative -> Optional, focus on implementation
- Attached to the Test Script.xlsx file
- **Unit Testing:** Each function (create_rental, read_rentals, update_rental, delete_rental) will be tested individually to ensure its functionality meets the specifications. Testing will verify whether the function produces the expected output for a variety of inputs, including boundary cases and error cases (e.g., trying to delete a non-existent rental).

- **Integration Testing:** This test will verify the interaction between the functions. For example, whether the data created by the create_rental function can be read correctly by the read_rentals function.

## 9. Conclusion -> Customizing

This proof of concept aims to demonstrate that a demo car rental system can be developed using a simple and effective approach. With the implementation of basic CRUD features, this system can provide an efficient solution for managing car rentals, as well as being a basis for further development in the future. Since this is a capstone project, formal evaluation and user feedback are not within the scope of this proof of concept.