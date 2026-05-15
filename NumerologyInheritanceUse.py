# Noah Mayock
# Assignment: Numerology Inheritance

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
