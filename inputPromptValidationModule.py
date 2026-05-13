# Author: Prof. Brian Candido
# Purpose: Put user input and validation into a module for sharing and reuse
#
# This module provides functions to allow the input and data validation for
# -float value
# -int value
# -string value


#################################################################################
# inputFloatValidation Function                                                 #
# Parameter 1: Is the Prompt value that user will see on the screen             #
# Parameter 2: Indicates what the minimum value allowed is for example 0 or .01 #
#################################################################################

def inputFloatValidation(sPrompt, nMinNumberAllowed):    

  # Testing user input with while loop displaying error message if invalid

  # Default fValue to -1 to force entry into the loop:
  fValue = -1

  # Keep Looping until a valid float that was >= to the Minimun Number that was supplied:
  while fValue < nMinNumberAllowed:
    try:
        fValue = float(input(sPrompt))
        if fValue <  nMinNumberAllowed:
            print ("Input must be a numeric value greater or equal to: ", nMinNumberAllowed)
            continue
    except ValueError:
            print ("Input must be a numeric value greater or equal to: ", nMinNumberAllowed)
            continue
          
  # If code reaches here a valid float numeric value that was > then the nMinNumberAllowed    
  return fValue



#################################################################################
# inputIntValidation Function                                                   #
# Parameter 1: Is the Prompt value that user will see on the screen             #
# Parameter 2: Indicates what the minimum value allowed is for example 0 or .01 #
#################################################################################

def inputIntValidation(sPrompt, nMinNumberAllowed):    

  # Testing user input with while loop displaying error message if invalid

  # Default iValue to -1 to force entry into the loop:
  iValue = -1

  # Keep Looping until a valid float that was >= to the Minimun Number that was supplied:
  while iValue < nMinNumberAllowed:
    try:
        iValue = int(input(sPrompt))
        if iValue <  nMinNumberAllowed:
            print ("Input must be a numeric value greater or equal to: ", nMinNumberAllowed)
            continue
    except ValueError:
            print ("Input must be a numeric value greater or equal to: ", nMinNumberAllowed)
            continue
          
  # If code reaches here a valid int numeric value that was > then the nMinNumberAllowed    
  return iValue



#################################################################################
# inputStringValidation Function                                                #
# Parameter 1: Is the Prompt value that user will see on the screen             #
#################################################################################

def inputStringValidation(sPrompt):    
  
  # Default sValue to -1 to force entry into the loop:
  sValue = ""

  # Keep Looping until a valid float that was >= to the Minimun Number that was supplied:
  while sValue == "":
    sValue = input(sPrompt)
    if sValue ==  "":
       print ("Please supply an input value.")
       continue
          
  # If code reaches here a valid string was entered
  return sValue

