# Noah Mayock
# Numerology Classes (use/main)
# Reflection:
#           I really enjoyed learning about OOP in python, I've taken C# and am taking Java and I feel like those are much more OOP based from the start whereas python feels like
#           if can be used just as easily (more easily based on my previous experience) for scripting and procedural programming so its very cool to be able to implement
#           OOP in a language I actually enjoy. (I wanted to like java but its so cumbersome and the syntax is horrific) 
#
#           The hardest thing for me this assigment was honestly everything outside of it. I've had jobs before while in school but never like what I'm doing now. Only being able to attend one 
#           two weekly classes is not only a bummer because I really love going to your classes(I promise I'm not just shooting for bonus points) but it all kind of started melting together 
#           especially with two numerology based assignments back to back and my original code was, as you said, overly complex just because I wanted to try all of the cool stuff I was seeing
#           in class and on the videos. Its just a lot more difficult balancing school and work than I expected with the 4 day schedule; still very worth it and I'm happy/grateful to be here.
#
#           I think the planetary weight converter would be the best to rewrite using classes. Create an object with name and weight and then store the conversions in a dict and apply them in the 
#           _init_ with the calculations and then use getters to return the results in the main/use. I'm actually not sure how that would work as far as creating the pickle file and if I tried to 
#           figure that out right now I'd have a great time but be late for work.
#
#           1. I was trying to do so many things that worked, but not efficiently, I kept trying to implement everything youve shown/I've learned at once and it made a mess, sometimes
#              the simplest way to do something is the best. 
#
#           2. This is kind of cheap as I have not taken the time to figure out your ascii/unicode converter but I swear I will be this weekend. Stuff like that reaffirms my love of programing.
#              Theres SO many ways to accomplish the same task and if your willing to put the time in you can create these (to me as an amatuer) insane solutiotions to problems. I love puzzles 
#              and programming is, at least to me, the best puzzle there is because of how many potentially correct answers there are to a single question.
#              
#
#

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
