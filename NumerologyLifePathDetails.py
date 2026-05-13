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

VOWELS = set('aeiou')



class Numerology:

    #Character to number conversion (thank you for this its genuinely so cool):
    def __convertCharToInt(self, sCharNBM):
        return ((ord(sCharNBM.upper()) - 65) % 9 + 1) if sCharNBM.isalpha() else 0

    def __reduceNumber(self, iNumNBM):
        while len(str(iNumNBM)) > 1:
            iNumNBM = (iNumNBM % 10) + (iNumNBM // 10)
        return iNumNBM


    def __init__(self, sNameNBM, sDOBNBM):

        #using a display name and dob for result output while being able to normalize/process them a single time here
        self.__displayName = sNameNBM
        self.__displayDOB = sDOBNBM
        
        #normalized name & dob
        self.__name = sNameNBM.lower().replace(" ", "").replace("-", "").replace("'", "")
        self.__dob = sDOBNBM.replace("/", "").replace("-", "")


        #storing split DOB in vars for re use
        iMonthNBM = int(self.__dob[0:2])
        iDayNBM = int(self.__dob[2:4])
        iYearNBM = int(self.__dob[4:8])

        #attidude number calc
        self.__iAttitudeNBM = self.__reduceNumber(iMonthNBM + iDayNBM)

        #birth day number calc
        self.__iBirthDayNBM = self.__reduceNumber(iDayNBM)

        #life path number calc
        self.__iLifePathNBM = self.__reduceNumber(iMonthNBM + iDayNBM + iYearNBM)

        #personality number calc
        self.__iPersonalityNBM = self.__reduceNumber(sum(self.__convertCharToInt(char) for char in self.__name if char not in VOWELS))

        #soul num calc
        self.__iSoulNBM = self.__reduceNumber(sum(self.__convertCharToInt(char) for char in self.__name if char in VOWELS))

        #power name calc
        self.__iPowerNameNBM = self.__reduceNumber(self.__iSoulNBM + self.__iPersonalityNBM)

    #getters

    @property
    def displayName(self):
        return self.__displayName

    @property
    def displayDOB(self):
        return self.__displayDOB

    @property
    def attitude(self):
        return self.__iAttitudeNBM

    @property
    def birthday(self):
        return self.__iBirthDayNBM

    @property
    def lifePath(self):
        return self.__iLifePathNBM

    @property
    def soul(self):
        return self.__iSoulNBM

    @property
    def personality(self):
        return self.__iPersonalityNBM

    @property
    def powerName(self):
        return self.__iPowerNameNBM
           
class NumerologyInheritance(Numerology):

    #Using a protected variable for the const. dict since its only used by this child class
    _LP_DETAILS = {1: "The Independent: Wants to work/think for themselves.",
                   2: "The Mediator: Avoids conflict and wants love and harmony.",
                   3: "The Performer: Likes music, art and to perform or get attention.",
                   4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful.",
                   5: "The Adventurer: Likes to travel and meet others, often an extrovert.",
                   6: "The Inner Child: Is meant to be a parent and/or one that is young at heart.",
                   7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality.",
                   8: "The Executive: Gravitates towards money and power.",
                   9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way."}


    def __init__(self, sNameNBM, sDOBNBM):

        #Forces the parents __init__ to run before doing anything in this class so the lifePath and other calculataions are completed
        super().__init__(sNameNBM, sDOBNBM)

        #Using get with default return string incase no match is found in the const. dict, although
        #since lifePath can only return 1-9 LP_DETAILS[self.lifePATH] might be more efficient...
        self.__sLifePathDetailNBM = self._LP_DETAILS.get(self.lifePath, "No match found for life path number")

    @property
    def lifePathDetail(self):
        return self.__sLifePathDetailNBM
