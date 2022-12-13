

#main.py

from gui import *
from calculator import *

def main():
    gui() #Create the GUI
    num1, num2 = getInput() #Get user input from the GUI
    result = add(num1, num2) #Calculate result
    displayResult(result) #Display result to the user

if __name__ == '__main__':
    main()