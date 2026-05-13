# Noah Mayock
# Assignment: SQL and Python
#Reflection:
# I have unfortunately allowed myself to get quite rusty in regards to SQL so this assignment was a nice way to re-introduce myself to the subject
# 
# Timing. I have burnt myself  out completely this semester, as I'm sure youll see by the time I finally get this in
#
# I knew this question sounded familiar, my appologies but I did copy and paste my answer from the last assignment. Also hopefully decorators werent a requirement for this one:
# Decorators work by allowing a function to take another function as an arguement and return another new function. This allows coders to extend and enhance the 
# capabilities of their functions without having to alter their original code. The property decorator allows you to turn class methods into managed attributes which
# lets you access/"get" the methods value while the actual logic is handled internally/behind the scenes.
#
# DDL 'defines'm the structure of the database, creates the tables and defines there attributes, columns, rows, data type requirements etc. DML deals with the data in that
# predefined structure. 
#
# The SELECT is deciding what tables to use and the join is linking them together based off shared collums
#
# 1. I technically learned this from being confused by the weekly course content examples but I did not know that the connection object to create a temporary cursor object rather#    than explicitly creating one. From what I've seen and I could probably definitely be wrong it is still best practice to create each object distinctly hense my code.
# 2. Dont take 17 credits your in your final semeste for "fun". It will not be fun. That being said I have thuroughly enjoyed every course and class I've had with you and I
#    consider myself incredibly lucky to have had you as a professor. Thank you, really and truly you have made an incredible impact on my life. 
#

import sqlite3
import csv
#I was importing Path from pathLib here but I dont think its necessary here.


DB_NAME = "SocialSecurity.db"

def createTables(connNBM):

    cursorNBM = connNBM.cursor()

    cursorNBM.execute("CREATE TABLE IF NOT EXISTS Employee (EmployeeID INTEGER PRIMARY KEY, Name TEXT NOT NULL)")
    cursorNBM.execute("CREATE TABLE IF NOT EXISTS Pay (EmployeeID INTEGER NOT NULL, Year INTEGER NOT NULL, Earnings REAL NOT NULL, PRIMARY KEY (EmployeeID, Year))")
    cursorNBM.execute("CREATE TABLE IF NOT EXISTS SocialSecurityMin (Year INTEGER PRIMARY KEY, Minimum REAL NOT NULL)")

    connNBM.commit()

def importData(connNBM):

    cursorNBM = connNBM.cursor()

    if cursorNBM.execute("SELECT COUNT(*) FROM Employee").fetchone()[0] > 0:
        print("Data already loaded, skipping import.")
        return

    filesToImportNBM = [
        ("Employee.txt",              "INSERT INTO Employee VALUES (?, ?)"),
        ("Pay.txt",                   "INSERT INTO Pay VALUES (?, ?, ?)"),
        ("SocialSecurityMinimum.txt", "INSERT INTO SocialSecurityMin VALUES (?, ?)"),]

    for sFileNameNBM, sSQLNBM in filesToImportNBM:
        with open(sFileNameNBM, 'r') as fileNBM:
            csvReaderNBM = csv.reader(fileNBM)
            next(csvReaderNBM)  # skip header
            cursorNBM.executemany(sSQLNBM, csvReaderNBM)

    connNBM.commit()
    print("Data imported successfully.")

def displayResults(connNBM):

    cursorNBM = connNBM.cursor()

    cursorNBM.execute("""
        SELECT e.Name, p.Year, p.Earnings, s.Minimum
        FROM Employee e
        JOIN Pay p ON p.EmployeeID = e.EmployeeID
        JOIN SocialSecurityMin s ON s.Year = p.Year
        ORDER BY e.Name, p.Year """)

    print(f"\n{'Name':<20}{'Year':<8}{'Earnings':>12}{'Minimum':>12}{'Qualifies':>12}")
    print("-" * 64)

    for record in cursorNBM.fetchall():
        sNameNBM      = record[0]
        iYearNBM      = record[1]
        fEarningsNBM  = float(record[2])
        fMinimumNBM   = float(record[3])
        sQualifiesNBM = "Yes" if fEarningsNBM >= fMinimumNBM else "No"

        print(f"{sNameNBM:<20}{iYearNBM:<8}{fEarningsNBM:>12,.2f}{fMinimumNBM:>12,.2f}{sQualifiesNBM:>12}")

def main():

    connNBM = sqlite3.connect(DB_NAME)
    createTables(connNBM)
    importData(connNBM)
    displayResults(connNBM)
    connNBM.close()

main()
