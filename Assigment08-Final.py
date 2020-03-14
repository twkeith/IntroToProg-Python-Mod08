# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KBurdette,3.10.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

import sys

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    """
    def __init__(self,product_name, product_price):
        print("Created the following product: " + product_name)
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        return self.__product_name + " costs $" + "{:.2f}".format(float(self.__product_price))

    @property
    def product_name(self):
        return self.__product_name

    @property
    def product_price(self):
        return self.__product_price

    @product_name.setter
    def product_name(self,val):
        self.__product_name = val

    @product_price.setter
    def product_price(self,val):
        self.__product_price = val


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

        add_product(product,list)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Burdette,3.12.2020, changed functions
    """

    @staticmethod
    def read_data_from_file(textfile):
        PList = []

        try:
            fileObj = open(textfile, "r")
            for line in fileObj:
                prod = line.strip()
                pair = prod.split(",")
                newprod = Product(pair[0],pair[1])
                PList.append(newprod)
            fileObj.close()
        except FileNotFoundError:
            print("File does not exist, I will create it for you.")
            newfileObj = open(textfile, "w")
            newfileObj.close()
        except Exception as ex:
            print("The following error occurred: ")
            print(ex)
            print("The program will now terminate.")
            sys.exit()
        return PList

    @staticmethod
    def save_data_to_file(textfile,PList):
        strList =[]
        for prod in PList:
            strList.append(prod.product_name + "," + str(prod.product_price) + "\n")
        fileObj = open(textfile, "w")
        fileObj.writelines(strList)
        fileObj.close()

    @staticmethod
    def add_product(pname, pprice, PList):
        prod = Product(pname,pprice)
        PList.append(prod)

    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Controls User Interactions

    methods:
        show_all_prices(list_of_products)

        display_menu()

        get_new_product() -> product_name, price

        ask_user_for_task() -> number of task

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Burdette,3.12.2020, changed functions
    """
    # TODO: Add docstring
    @staticmethod
    def show_all_prices(PList):
        for prods in PList:
            print(prods)

    # TODO: Add code to show menu to user
    @staticmethod
    def display_menu():
        """ Show users available options

        No Parameters
        No Returns
        """
        # Print Menu
        print("\t\tUser Menu For Reviews")
        print("\t\tType '1' to save the list to file")
        print("\t\tType '2' to add a product to the list")
        print("\t\tType '3' to show a list of all prices")
        print("\t\tType '4' to exit the program")

    # TODO: Add code to get product data from user
    @staticmethod
    def get_new_product():
        newprodname = input("What product do you wish to add: ")
        newprice = input("How much does it cost: ")

        while True:
            try:
                fltprice = float(newprice)
            except ValueError:
                newprice = input("Price must be a number. Enter again: ")
            except:
                newprice = input("Not sure what you did but please enter a number: ")
            else:
                return newprodname, fltprice

    # TODO: Add code to get user's choice
    @staticmethod
    def ask_user_for_task():
        """ Ask User What To Do

        :return: Text of users choice
        """
        # Ask user for menu input, test it make sure it is valid
        choice = 0
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Which menu selection do you want (1-4): ")
        return choice
    # TODO: Add code to show the current data from the file to user


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body


lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    IO.display_menu()
    pickedchoice = IO.ask_user_for_task()

    if pickedchoice == "1":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
    elif pickedchoice == "2":
        newprd, itsprice = IO.get_new_product()
        FileProcessor.add_product(newprd, itsprice, lstOfProductObjects)
    elif pickedchoice == "3":
        IO.show_all_prices(lstOfProductObjects)
    elif pickedchoice == "4":
        break

# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

