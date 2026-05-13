# Noah Mayock
# Assignment: Numerology Inheritance
# Reflection:
# I really enjoyed how simple the assignment was. I don't mean conceptually simple but moreseo the execution/implementation felt very logical and clean in the way
# that everything flowed/was inherited from the parent to the child to the use file. 
#
# I had a hard time with the placement of my meanings/descriptions. I originaly had them outside the class as a global constant would be but as you made clear, while it 
# should be treated as a constant, it is NOT global and should not be accecible to other child classes.
#
# Decorators work by allowing a function to take another function as an arguement and return another new function. This allows coders to extend and enhance the 
# capabilities of their functions without having to alter their original code. The property decorator allows you to turn class methods into managed attributes which
# lets you access/"get" the methods value while the actual logic is handled internally/behind the scenes.
#
# 1. I learned about protected variables and their usage. After making my meanings dictionary a protected variable I had tried just using _LP_DETAILS but thankfully 
#    pythons error messages pointed me in the correct direction and I reallized I would need self. in order to access this since it was now a protected class variable
#
# 2. This was my first time using inheritance in python and I really enjoy it. It felt like a breakthrough as far as understanding the power of OOP and classes when
#    creating modular programs.

import NumerologyLifePathDetails as numIn
import DateValidator as dv

#Ensuring a name is entered
def nameCheck() -> str:

    clientName = ""
  
    while not clientName: 

        clientName = input("Enter your name: ")
       
    return clientName

def dobCheck() -> str:

    clientDOB = ""

    #Validating date is entered, a  valid date and proper format
    while not clientDOB or not dv.isValidDateFormat(clientDOB) or not dv.isValidDate(clientDOB):
            
        clientDOB = input("Enter your birthday (MM/DD/YYYY or MM-DD-YYYY): ")

        if not dv.isValidDateFormat(clientDOB):
            print(f"{clientDOB} is not a properly formatted date, please enter a valid date.")

        elif not dv.isValidDate(clientDOB):
            print(f"{clientDOB} is formatted properly but is not a valid date, please enter a valid date.")

    return clientDOB

def main():
     
    sNameNBM = nameCheck()
    sDOBNBM = dobCheck()
    myClient = numIn.NumerologyInheritance(sNameNBM,sDOBNBM)

    print(f"{'Client Name:':<20}", myClient.displayName)
    print(f"{'Client DOB:':<20}", myClient.displayDOB)
    print(f"{'Life Path:':<20}", myClient.lifePath)
    print(f"{'Attitude:':<20}", myClient.attitude)
    print(f"{'Birthday:':<20}", myClient.birthday)
    print(f"{'Personality:':<20}", myClient.personality)
    print(f"{'Power Name:':<20}", myClient.powerName)
    print(f"{'Soul:':<20}", myClient.soul)   

    print(f"Life path meaning:  ", myClient.lifePathDetail)

main()
