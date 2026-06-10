"""
Exception Handling & Debugging

Starter code for learning how to handle exceptions and debug Python programs.
Complete the tasks to master error handling and debugging techniques.
"""

import logging
from typing import List

# Task 3: Configure logging
# TODO: Set up logging configuration with appropriate level and format
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )


# Task 1: Handle Exceptions with Try-Except
def read_number_from_user() -> float:
    """
    Prompt user for a number and handle invalid input.
    
    TODO: Implement try-except to catch ValueError when user enters non-numeric input
    """
    user_input = input("Enter a number: ")
    # TODO: Wrap this in try-except
    number = float(user_input)
    return number


def divide_numbers(a: float, b: float) -> float:
    """
    Divide two numbers with proper exception handling.
    
    TODO: Handle ZeroDivisionError when b is 0
    """
    result = a / b
    return result


def read_file(filename: str) -> List[str]:
    """
    Read lines from a file with exception handling.
    
    TODO: Handle FileNotFoundError and other I/O exceptions
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


# Task 2: Use Else and Finally Blocks
def process_data_safely(data: str) -> int:
    """
    Process data with try-except-else-finally pattern.
    
    TODO: Implement complete error handling pattern:
    - try: attempt to convert data to integer
    - except: handle ValueError
    - else: process the number if no exception occurred
    - finally: always log that processing is complete
    """
    # TODO: Implement this function
    pass


# Task 2: Demonstrate Logging
def calculate_average(numbers: List[float]) -> float:
    """
    Calculate average of a list with logging.
    
    TODO: Add logging statements to:
    - Log when function is called (DEBUG level)
    - Log input validation (INFO level)
    - Log any errors (ERROR level)
    """
    # TODO: Add logging.debug() for function entry
    
    if not numbers:
        # TODO: Add logging.error() before raising or returning
        raise ValueError("Cannot calculate average of empty list")
    
    average = sum(numbers) / len(numbers)
    
    # TODO: Add logging.info() for result
    return average


# Task 4: Custom Exceptions (Stretch Goal)
class InsufficientFundsError(Exception):
    """Custom exception for bank account operations."""
    pass


class BankAccount:
    """Simple bank account with custom exception handling."""
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, amount: float) -> float:
        """
        Withdraw money from account.
        
        TODO: Raise InsufficientFundsError if withdrawal amount exceeds balance
        """
        # TODO: Check if amount > self.balance
        # TODO: Raise InsufficientFundsError with message like:
        #       "Insufficient funds! Available: ${balance}, Requested: ${amount}"
        
        self.balance -= amount
        return self.balance


# Example usage and testing
if __name__ == "__main__":
    # TODO: Test your exception handling implementations:
    
    # Test 1: Try reading a number with invalid input
    # try:
    #     num = read_number_from_user()
    # except ...:
    #     ...
    
    # Test 2: Try dividing by zero
    # try:
    #     result = divide_numbers(10, 0)
    # except ...:
    #     ...
    
    # Test 3: Try reading a non-existent file
    # try:
    #     lines = read_file("nonexistent.txt")
    # except ...:
    #     ...
    
    # Test 4: Try calculating average of empty list
    # try:
    #     avg = calculate_average([])
    # except ...:
    #     ...
    
    # Test 5: Try custom exception with insufficient funds
    # account = BankAccount("Alice", 100)
    # try:
    #     account.withdraw(150)
    # except InsufficientFundsError as e:
    #     print(f"Error: {e}")
    
    print("Uncomment and run the test cases above to practice exception handling!")
