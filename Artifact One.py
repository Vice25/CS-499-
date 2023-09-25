# ============================================================================
# Name        : Lab1-3.cpp
# Author      : Victor Landi
# Version     : 1.0
# Copyright   : Copyright © 2017 SNHU COCE
# Description : Lab 1-3 Up to Speed in C++ CS-260 Enhancement: Ported to Python September 2023

# This program will allow the user to enter bid information, display bid information and exit the program.

#The Python functions and techniques used in this program were chosen for their suitability in achieving the following objectives:

# organizing data, user input/output, data manipulation, type conversion, and conditional execution.

# These choices follow Python best practices and coding conventions for clarity and maintainability.
# ============================================================================

# This program will hold and display bid information, this could be anything, in this case we want to store data which could be a bid for property with the following attributes:
# Title, Fund, Vehicle Id, and Bid Amount

# Define a class to hold bid information
class Bid:
    def __init__(self):
        self.item_title = ""  # Initialize item_title attribute
        self.fund = ""        # Initialize fund attribute
        self.vehicle_id = ""  # Initialize vehicle_id attribute
        self.bid_amount = 0.0 # Initialize bid_amount attribute

# Function to display bid information
def display_bid(bid):
    # Format the bid amount with two decimal places using the "{:.2f}".format() method
    bid_amount_str = "{:.2f}".format(bid.bid_amount)
    
    # Display bid information
    print("Title:", bid.item_title)
    print("Fund:", bid.fund)
    print("Vehicle:", bid.vehicle_id)
    print("Bid Amount:", bid_amount_str)

# Function to get bid information from the user
def get_bid():
    bid = Bid()  # Create an instance of the Bid class
    bid.item_title = input("Enter title: ")   # Get user input for item_title
    bid.fund = input("Enter fund: ")           # Get user input for fund
    bid.vehicle_id = input("Enter vehicle: ")  # Get user input for vehicle_id
    bid_amount_str = input("Enter amount: ")   # Get user input for bid_amount as a string
    
    # Check if the bid_amount_str contains two zeroes at the end and add another zero if needed
    if bid_amount_str.endswith("00"):
        bid_amount_str += "0"
    
    # Convert bid_amount_str to a float and assign it to bid_amount, while removing '$' and stripping any whitespace
    bid.bid_amount = float(bid_amount_str.replace('$', '').strip())
    return bid

# The main program
def main():
    the_bid = None  # Initialize the_bid as None

    while True:
        print("Menu:")
        print("  1. Enter Bid")
        print("  2. Display Bid")
        print("  9. Exit")

        choice = input("Enter choice: ")  # Get user choice as a string

        if choice == '1':
            the_bid = get_bid()  # Call the get_bid function to get bid information and assign it to the_bid
        elif choice == '2':
            if the_bid is not None:
                display_bid(the_bid)  # Call the display_bid function to display bid information if the_bid is not None
            else:
                print("No bid entered.")
        elif choice == '9':
            print("Good bye.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()  # Call the main function if the script is run as the main program
