import re
from datetime import datetime

def isValidDateFormat(DateToTest: str) -> bool:

    # This code checks using regex to make sure a date
    # Positions STARTS 1 and 2 are numbers
    # Position 3 has - or /
    # Positions 4 and 5 are numbers
    # Position 6 has - or /
    # Positions 7,8,6,10 are numbers
    return bool(re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', DateToTest))

def isValidDate(sDateToTest: str) -> 'class datetime.datetime':

    # Checks to make sure it IS a VALID date:
    # 1 way into the function but 2 ways out:
    # -The string passed in is valid
    # -The string passed in is not valid
    #Replace Date Separators / or -:
    sDateToTest = sDateToTest.replace("/","").replace("-","")

    try:
        # Make sure it a valid date:
        datTest =  datetime.strptime(sDateToTest, '%m%d%Y') 
  
        return True
    except:
        return False
