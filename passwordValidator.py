#Noah Mayock 
#Assignment: Password Validator
#Reflection:
#I really just enjoyed getting back into python, this felt like a great refresher with some cool new things added.
#It took me a little bit to figure out how to iterate over the password once for the character requirements. At first I was 
#using any() for those checks but you and Tyler thankfully put a stop to that.
#Combining similar tasks whereever possible and making sure I used the most efficient methods. At first I was using casefold()
#rather than lower/upper() to case match but there was no need to use the more aggresive method so I switched.
#I learned a lot more about string methods and how to efficiently use them.
#I learned more about truth value testing, when I first wrote some of these checks I was checking if a list was empty 
#using the len(list) == 0 instead of just if/if not list:.

#func for initial extraction:

def initialSlice(sNameNBM):
    sInitialsNBM = "".join(i[0] for i in sNameNBM.split())
    return sInitialsNBM

#func for required  chars

def reqChars(sPasswordNBM):
    lsSpecCharsNBM = ['!', '@', '#', '$', '%', '^']
    bUpperNBM = False
    bLowerNBM = False
    bNumberNBM = False
    bSpecialNBM = False
    for char in sPasswordNBM:
        if char.isupper():
            bUpperNBM = True
        elif char.islower():
            bLowerNBM = True
        elif char.isdigit():
            bNumberNBM = True
        elif char in lsSpecCharsNBM:
            bSpecialNBM = True
        if bUpperNBM and bLowerNBM and bNumberNBM and bSpecialNBM:
            break
    return {
            "uppercase": bUpperNBM,
            "lowercase": bLowerNBM,
            "number": bNumberNBM,
            "special": bSpecialNBM }

#func for duplicate chars

def dupeChars(sPasswordNBM):
    dictCharsNBM = {}
    for chars  in sPasswordNBM:
        if chars in dictCharsNBM:
            dictCharsNBM[chars] += 1
        else:
            dictCharsNBM[chars] = 1
    return dictCharsNBM

#Single function for validation

def validatePassword(sPasswordNBM, sInitialsNBM):
    #creates an empty list to store error messages
    lsErrorsNBM = []
    #length check:
    if len(sPasswordNBM) < 8 or len(sPasswordNBM) > 12:
        lsErrorsNBM.append("Password must be between 8 and 12 characters")
    #pass/Pass present check:
    if sPasswordNBM.lower().startswith("pass"):
        lsErrorsNBM.append("Password cannot start with Pass")
    #character requirements check:
    dictReqChars = reqChars(sPasswordNBM)
    if not dictReqChars["uppercase"]:
        lsErrorsNBM.append("Password must contain at least 1 uppercase letter")
    if not dictReqChars["lowercase"]:
        lsErrorsNBM.append("Password must contain at least 1 lowercase letter")
    if not dictReqChars["number"]:
        lsErrorsNBM.append("Password must contain at least 1 number")
    if not dictReqChars["special"]:
        lsErrorsNBM.append("Password must contain at least 1 of these special characters: ! @ # $ % ^")
    #user initials check:
    if sPasswordNBM.lower().find(sInitialsNBM.lower()) != -1:
        lsErrorsNBM.append("Password must not contain user initials")    
    #duplicate character check:
    dictCharsNBM = dupeChars(sPasswordNBM)
    #creates empty list to store duplicate chars and count:
    lsDupesNBM = []
    for char, count in dictCharsNBM.items():
        if count > 1:
            lsDupesNBM.append(f"{char}: {count} times.")
    if lsDupesNBM:
        lsErrorsNBM.append("These characters repeat more than once:\n" + "\n".join(lsDupesNBM))        
    #Return failed checks or None if all clear:
    if lsErrorsNBM:
        return "\n".join(lsErrorsNBM) 
    else:
        return None

#Main program logic:

def main():
    sNameNBM = input("Enter full name such as John Smith: ")
    sInitialsNBM = initialSlice(sNameNBM)
    while True:
        sPasswordNBM = input("Enter a new password: ")
        sResultNBM = (validatePassword(sPasswordNBM, sInitialsNBM))
        if sResultNBM:
            print(sResultNBM)
        else:
            print("Password is valid and okay to use")
            break
main()
