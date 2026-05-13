# Noah Mayock
# Assignment: Real Estate Analyzer 
# Reflection:
#  I enjoyed this assingment as a whole, I think the ability to work with CSVs is a great skill to have and has a plethora of applications. My dad is a real estate
#  appraiser so I'd like to make this program more univerally usable with CSVs with variable metadata and structure, maybe using regex to parse the meta data and 
#  assign the record[x] based on that.
#
#  Honestly this assignment wasn't too bad. It felt like a nice progression from the first two and I was able to use them as a frame work to start as well as   
#  the python 1 version of this assignment. It was interesting to go back and look at that and see the difference in how I wrote the getMedian function then.
#
#  I used the csv module to import the data. It just made the most sense and of course we had your example. The only thing I changed was using next rather than
#  [1:] to skip the header/metadata and adding error handling for FileNotFound.
#
#  I used 4 dictionaries. I could have used 3 and done print(f"...") to out put the general summary data but I had already written a dictionary based summary function 
#  so I figured why not just put that data in a dict as well.
#
#  1. I learned to different ways to update dictionary values, the one seen below and dict.setdefaults(). I'm not sure which is better, but I went with the method you
#     showed in the help session because I only learned about the dict.setdefaults from Tyler/substack and didnt want to use something from an outside source or copy
#     Tylers idea.
#  2. This is somewhat outside the scope of the actual assignment but Tyler was under the weather the past week so I tried to lighten his load and help people with
#     questions/issues. It was illuminating. Huge respect to you, Tyler and past/present SI's because I did not expect it to be so difficult to help someone who is 
#     explicitly asking for your help. I also found it was a fine line to walk trying to gently nudge them In the right direction without spoiling their learning      
#     process or giving away the answer. Overall it was still very rewarding and I enjoyed seeing different peoples approaches.

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
