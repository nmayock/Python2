#Assignment: Password Validator

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
