#Assignment: Planetary Weights Dictionaries

import pickle
import inputPromptValidationModule as ivm

#conversion factor dict as a constant

CONVERSION_FACTOR = {"Earth": 1.0, #added for referrence when reading history
                     "Mercury": 0.38,
                     "Venus": 0.91,
                     "Moon": 0.165,
                     "Mars": 0.38,
                     "Jupiter": 2.34,
                     "Saturn": 0.93,
                     "Uranus": 0.92,
                     "Neptune": 1.12,
                     "Pluto": 0.066}

#function to unpickle program history

def unPickleDict(historyFileNBM: str) -> dict:
    
    dictReadNBM = {} 
    try:
        with open(historyFileNBM, 'rb') as inputFile:
            dictReadNBM = pickle.load(inputFile)
            return dictReadNBM
    except FileNotFoundError:
        return {} #had pass here originally but that made it so I had to use or {} in the main when trying to unpickle if no pickle file exists

#func to handle program history output:

def historyHandler(dictBackupNBM: dict) -> None: 
    
    if dictBackupNBM:
        sDisplayHistNBM = input("Would you like to see the history y/n: ").lower()
        if sDisplayHistNBM == "y":       
            for sNameNBM, dictPersonsWeightNBM in dictBackupNBM.items():
               formatDict(sNameNBM, dictPersonsWeightNBM)
               
#func to format dictionary output

def formatDict(sNameNBM: str, dictPersonsWeightNBM: dict) -> None:
    
    print(f"{sNameNBM}, here are your weights on our Solar System's planets.")
    for sPlanetNBM, fPlanetWeightNBM in dictPersonsWeightNBM.items():
        sWeightMsgNBM = f"Weight on {sPlanetNBM}:" #I think this is the correct way to get the desired output of <planet>: 
        print(f"{sWeightMsgNBM:<20}{fPlanetWeightNBM:>10.2f}")

#func for name/weight input & validation

def userInputs(dictBackupNBM: dict) -> tuple[str, float]:

    while True:
        sNameNBM = input("What is your name (enter key to quit): ").title() #used .title() instead of capitalize incase user enters full name
        if not sNameNBM:
            return None, None 
        if sNameNBM in dictBackupNBM:
            print(f"{sNameNBM} is already in the history file. Enter a unique name.")
            continue # sends back to top instead of asking for weight after repeated name
        fWeightNBM = ivm.inputFloatValidation("What is your weight: ", 0.0)
        return sNameNBM, fWeightNBM    

#func for weight calc

def weightConv(fWeightNBM: float) -> dict: 
    
    dictPersonsWeightNBM = {}
    for sPlanetNBM, fFactorNBM in CONVERSION_FACTOR.items():
        dictPersonsWeightNBM[sPlanetNBM] = fWeightNBM * fFactorNBM
    return dictPersonsWeightNBM

#func to pickle backup File

def pickleDict(dictSaveNBM: dict) -> None:      
    with open("nmPlanetaryWeights.db", "wb") as backupFile:
        pickle.dump(dictSaveNBM, backupFile)

#Main program logic

def main(): #testing ground 
 
    dictPlanetHistoryNBM = unPickleDict("nmPlanetaryWeights.db")
    historyHandler(dictPlanetHistoryNBM)
    while True: #Loop for mutiple enter till blank string  is entered 
        sNameNBM, fWeightNBM = userInputs(dictPlanetHistoryNBM)  
        if not sNameNBM: #truth value test to exit loop  if user enters blank string for name
            break
        dictPersonsWeightNBM = weightConv(fWeightNBM)
        formatDict(sNameNBM, dictPersonsWeightNBM) 
        dictPlanetHistoryNBM[sNameNBM] = dictPersonsWeightNBM

    pickleDict(dictPlanetHistoryNBM) 
                                    
main()
