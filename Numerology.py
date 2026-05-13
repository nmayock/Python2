# Noah Mayock
# Numerology Classes (class)

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
        
        #normalized name & dob ... I dont think this is even necesarry since the char to int func returns zero if not alpha
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
           

  
 



