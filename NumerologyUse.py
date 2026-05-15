# Numerology Classes (use/main)

import Numerology as num
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
    myClient = num.Numerology(sNameNBM,sDOBNBM)

    print(f"Client Name: ", myClient.displayName)
    print(f"Client DOB: ", myClient.displayDOB)
    print(f"Life Path: ", myClient.lifePath)
    print(f"Attitude: ", myClient.attitude)
    print(f"Birthday: ", myClient.birthday)
    print(f"Personality: ", myClient.personality)
    print(f"Power Name: ", myClient.powerName)
    print(f"Soul: ", myClient.soul)




main()
