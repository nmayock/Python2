# Assignment: Real Estate Analyzer 

import csv
from pathlib import Path 

def getDataInput() -> list[str]:

    data_file = Path('RealEstateData.csv')
    try: #makes sure the data_file exists in the working directory
        with data_file.open(mode='r') as file:
           
            csvReaderNBM = csv.reader(file)
            next(csvReaderNBM)
            return list(csvReaderNBM)
    except FileNotFoundError:
        print(f"{data_file} not found, make sure it is in the the same directory as this program and run again.")
        return [] #returns an empty list for truth value test in main


def getMedian(lstPricesNBM: list) -> float:
    
    #Sorts the list of prices to find mid point
    lstSortedNBM = sorted(lstPricesNBM)
    #Gets length and mid point of sorted list
    iCountNBM = len(lstSortedNBM)
    iMiddleNBM = iCountNBM // 2

    #checks if list length is odd or even and calculates median accordingly
    if iCountNBM % 2 != 0: #odd length
        return float(lstSortedNBM[iMiddleNBM])
    return (lstSortedNBM[iMiddleNBM -1] + lstSortedNBM[iMiddleNBM]) / 2

#function to format summary output
def sumFormat(sSummaryTypeNBM: str, dictToSumNBM: dict) -> None:
    print(f"\n{sSummaryTypeNBM}:\n")
    for sKeyNBM, fResultNBM in dictToSumNBM.items():
        sCurrencyResultNBM = f"${fResultNBM:,.2f}"
        print(f"{sKeyNBM:<20}{sCurrencyResultNBM:>15}")

def main():

    #reads in data
    sDataNBM = getDataInput()
    if not sDataNBM: #empty list evaluates to false and ends the program cleanly with error message
        return
    
    #initialize list and dictionaries to add populate later
    lstPricesNBM = []
    dictCitiesNBM = {}
    dictZipCodesNBM = {}
    dictTypesNBM = {} 
    dictGeneralSumNBM = {}

    #Populates list and dictionaries with corresponding record
    for record in sDataNBM:
        
        try: #Checks price values can be converted to float, if not alerts user of bad data and skips it
            fPriceNBM = float(record[8])
        except ValueError:
            print(f"Invalid price: {record[8]}, skipping data.")
            continue
        sCityNBM = record[1]
        sZipNBM = record[2]
        sPTypeNBM = record[7]

        #appends prices to price list
        lstPricesNBM.append(fPriceNBM)

        #checks if keys are present in dict, if not it is initialized as a key with value of 0 before incrementing the value by fPriceNBM  
        dictCitiesNBM[sCityNBM] = dictCitiesNBM.get(sCityNBM, 0) + fPriceNBM
        dictZipCodesNBM[sZipNBM] = dictZipCodesNBM.get(sZipNBM, 0) + fPriceNBM
        dictTypesNBM[sPTypeNBM] = dictTypesNBM.get(sPTypeNBM, 0) + fPriceNBM

    #Populating general sum dictionary... not sure if this is the most efficient way
    dictGeneralSumNBM["Minimum"] = min(lstPricesNBM)
    dictGeneralSumNBM["Maximum"] = max(lstPricesNBM)
    dictGeneralSumNBM["Sum"] = sum(lstPricesNBM)
    dictGeneralSumNBM["Avg"] = sum(lstPricesNBM) / len(lstPricesNBM)
    dictGeneralSumNBM["Median"] =  getMedian(lstPricesNBM)
    
   
    #outputting summaries
    sumFormat("Summary of all values", dictGeneralSumNBM)
    sumFormat("Summary by city", dictCitiesNBM)
    sumFormat("Summary zip code", dictZipCodesNBM)
    sumFormat("Summary by property type", dictTypesNBM)

main()
