# Assignment: SQL and Python

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
