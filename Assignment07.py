# ---------------------------------------------------------------------------- #
# Title: Assignment07
# Description: Python Script to Demo Pickling and Error Handling
# ChangeLog (Who,When,What):
# Josh McMillen,11-30-2020,Original file
# ---------------------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
dic_pickle = {"Number_1": 2, "Number_2": 4}
file_pickles = "Binary_Pickles.Dat"
list_of_rows = []


# Processing  --------------------------------------------------------------- #
class Processor:
    # """  Performs Processing tasks """

    @staticmethod
    def write_row_to_binary_file(file_name, dic_row):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param dic_row: (dic) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "wb")
        pickle.dump(dic_row, file)
        file.close()
        return 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Display current numbers
        2) Update current numbers (Error Handling Demo)     
        3) Run computation
        4) Save numbers to file (Pickling Demo)
        5) Exit
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_dic(dic_row):
        """ Shows the current numbers

        :param dic_row: (dic) dictionary row you want to display
        :return: nothing
        """
        print(dic_row)
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_numbers():
        """ Asks users for new numbers and adds to dic row

        :return: (dict) row to be added
        """
        print("Input two integers (or do not to test error handling")
        number_1 = input("Number 1: ")
        while True:
            try:
                1/int(number_1)
            except ZeroDivisionError:
                print("Number 1: Please do not use zero as a number value")
                number_1 = input("Number 1: ")
                continue
            except ValueError:
                print("Number 1: Please use an integer")
                number_1 = input("Number 1: ")
                continue
            except Exception as e:
                print("Unknown error: ")
                print(e)
                print(type(e))
                print(e.__doc__)
                print(e.__str__())
                number_1 = input("Number 1: ")
                continue
            break

        number_2 = input("Number 2: ")
        while True:
            try:
                1 / int(number_2)
            except ZeroDivisionError:
                print("Number 2: Please do not use zero as a number value")
                number_2 = input("Number 2: ")
                continue
            except ValueError:
                print("Number 2: Please use an integer")
                number_2 = input("Number 2: ")
                continue
            except Exception as e:
                print("Unknown error: ")
                print(e)
                print(type(e))
                print(e.__doc__)
                print(e.__str__())
                number_2 = input("Number 2: ")
                continue
            break

        dic_row = {"Number_1": int(number_1), "Number_2": int(number_2)}
        return dic_row

    @staticmethod
    def print_computation(dic_row):
        """ Runs computation for given numbers

        :param dic_row: (dic) dictionary row you want to display the computation for
        :return: nothing
        """
        print("Number 1: " + str(dic_row["Number_1"]))
        print("Number 2: " + str(dic_row["Number_2"]))
        print("Sum: " + str(dic_row["Number_1"] + dic_row["Number_2"]))
        print("Product: " + str(dic_row["Number_1"] * dic_row["Number_2"]))
        print("Quotient (Number 1/Number 2: " + str(dic_row["Number_1"] / dic_row["Number_2"]))
        print("Quotient (Number 2/Number 1: " + str(dic_row["Number_2"] / dic_row["Number_1"]))
        print("Average: " + str((dic_row["Number_1"] + dic_row["Number_2"]) / 2))
        print()  # Add an extra line for looks


# Main Body of Script  ------------------------------------------------------ #
print("Welcome to the Python error handling and pickle demo!")
file = open(file_pickles, "wb")
pickle.dump(dic_pickle, file)
file.close()

while True:
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    if strChoice == '1':  # Display current numbers
        IO.print_current_dic(dic_pickle)
        continue  # to show the menu

    elif strChoice == '2':  # Update current numbers (Error Handling Demo)
        dic_pickle = IO.input_new_numbers()
        continue  # to show the menu

    elif strChoice == '3':  # Run computation
        IO.print_computation(dic_pickle)
        continue  # to show the menu

    elif strChoice == '4':  # Save numbers to file (Pickling Demo)
        Processor.write_row_to_binary_file(file_pickles, dic_pickle)
        print("Date saved to file: " + file_pickles)

        file = open(file_pickles, "r")
        for line in file:
            row = line
            list_of_rows.append(row)
        file.close()
        print()  # Add an extra line for looks
        print("What data looks like in file (Binary format):")
        print(list_of_rows)
        print()  # Add an extra line for looks
        print("Actual data:")
        print(dic_pickle)
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Closing Program")
        break  # and Exit
