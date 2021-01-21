import sqlite3
import sys
from sqlite3 import Error


class DB:
    # SQLite Data types:
    #    NULL
    #    INTEGER: signed integer, max 8 bytes.
    #    REAL: floating point value, 8-byte
    #    TEXT: text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
    #    BLOB: blob of data, stored exactly as it was input.

    # "__init__" in python is similar to constructors in Java, and will execute each time you are creating a new object
    # "Self" parameter references the current instance of the class, similar to "this" in Java

    # Create the connection
    def __init__(self, dbFileName):

        try:
            self.dbFileName = dbFileName
            self.conn = sqlite3.connect(self.dbFileName + '.db')
            self.cur = self.conn.cursor()
            print("DB initialized in the current directory.")
        except Error as e:
            print(e)



    # executed Insert, update or delete
    def exec(self, command):
        self.cur.execute(command)
        self.conn.commit()

    # execute select command
    def fetch(self, command):
        self.cur.execute(command)
        return self.cur.fetchall()

    # close the connection
    def close(self):
        self.conn.close()


def main():
    db = DB('medical')

    """ 
    implement your menu of option to choose
    ask for user choice
    select, insert update, delete data base on user request
    """

    def menu():
        print("Which table are you interested in altering/searching?")
        print("1. Patient")
        print("2. Hospital")
        print("3. Medicine")
        print("4. Examines")
        print("5. Takes")
        print("6. Lab")
        print("7. Manufactures")
        print("8. Prescribes")
        print("9. Doctor")
        print("10. Exit Database")
    loop = True
    def hospitalMenu():
        print("1. Insert a new hospital")
        print("2. Delete a hospital based on it's name")
        print("3. Delete hospital(s) where the rating is less than entered")
        print("4. Find which hospital has billed the most patients")
        print("5. Exit hospital table")

    def patientMenu():
        print("1. Output name of patients and how many medications they take")
        print("2. Add a patient")
        print("3. Get number of patients less than a certain age at each hospital")
        print("4. Exit patient table")

    def labMenu():
        print("1. Insert a new lab ")
        print("2. Update lab name and phone number according to labID")
        print("3. Delete a lab accourding to lab_ID")
        print("4. Exit lab table ")
    def medMenu():
        print("1. Insert a medicine ")
        print("2. Decrease price of all medicines above a certain amount ")
        print("3. Delete a medicine by med_id")
        print("4. Exit medicine table")

    def exMenu():
        print("1. Insert doctor/patient relation")
        print("2. Find how many patients each doctor has and where they work")
        print("3. Find doctors who have more than the average # of patients\nand where they work")
        print("4. Exit examines table")

    def takesMenu():
        print("1. Insert relation")
        print("2. Find Patient information for those allergic to a certain medicine")
        print("3. Delete relation")
        print("4. Exit Takes table")
    def manMenu():
        print("1. Add manufactures relation")
        print("2. Find the number of medicines a specific lab makes")
        print("3. Find name and phone number of all labs who make a certain medicine")
        print("4. Exit Manufactures table")
    def preMenu():
        print("1. Add prescription")
        print("2. Find most prescribed medication and # of times it's prescribed")
        print("3. How many doctors prescribe each medication")
        print("4. Exit Prescribes menu")
    def docMenu():
        print("1. Insert new doctor")
        print("2. Delete doctor ")
        print("3. Find Doctors with at a certain hospital with more than a certain years of experience")
        print("4. Get average salary for each specialty")
        print("5. Exit doctors table")
# Creating all the tables
    try:
        db.exec(
            "CREATE TABLE Hospital(Hname VARCHAR(20) NOT NULL,Haddress VARCHAR(20) NOT NULL,rating INT CHECK (rating >-1 AND rating <11),BID INT NOT NULL,PRIMARY KEY (Hname));")
    except Error as e:
        print(e)
# inserting values into hospital table
    try:
        db.exec("INSERT INTO Hospital ( Hname, Haddress,rating, BID ) VALUES('Grey Sloan', '123 medical dr', 9, 1210)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Hospital ( Hname, Haddress,rating, BID ) VALUES('Pack North', '777 notGood dr', 3, 1310)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Hospital ( Hname, Haddress,rating, BID ) VALUES('Good Medicine','999 notDead lane', 8, 1411)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Hospital ( Hname, Haddress,rating, BID ) VALUES('South Central', '221b oak', 4, 1111)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Hospital ( Hname, Haddress,rating, BID ) VALUES('Westside', '3423 oakland', 1, 1331)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Hospital ( Hname, Haddress,rating, BID ) VALUES('Great Hospital', '333 taregod', 1, 1991)")
    except Error as e:
        print(e)

    try:
        db.exec(
            "CREATE TABLE Doctor (Lname VARCHAR(20) NOT NULL,Specialty VARCHAR DEFAULT 'General',Years_Experienace INT NOT NULL,EmployeeID INT NOT NULL,EmployedBy VARCHAR(20) REFERENCES Hospital (Hname) ON DELETE CASCADE,Salary INT DEFAULT (80000) check (Salary >0),PRIMARY KEY (EmployeeID));")
    except Error as e:
        print(e)

    try:
        db.exec("INSERT INTO Doctor (Lname, Years_Experienace, EmployeeID, EmployedBy, Specialty)VALUES('yang', 18, 1234, 'Grey Sloan','Cardio')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Doctor (Lname, Years_Experienace, EmployeeID, EmployedBy, Salary)VALUES('Hunt', 1, 1235, 'Grey Sloan',90000)")
    except Error as e:
        print(e)

    try:
        db.exec("INSERT INTO Doctor (Lname, Years_Experienace, EmployeeID, EmployedBy,Specialty)VALUES('Karev', 19, 1111, 'Pack North','Pedeatrics')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Doctor (Lname, Years_Experienace, EmployeeID, EmployedBy, Salary)VALUES('Grey', 20, 1112, 'Grey Sloan', 900000)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Doctor (Lname, Years_Experienace, EmployeeID, EmployedBy, Salary)VALUES('Webber', 21, 2222, 'Pack North', 1000000)")
    except Error as e:
        print(e)

    try:
        db.exec("CREATE TABLE Patient (P_lastName VARCHAR(20),SSN NUMERIC(9,0) NOT NULL,Phone_number NUMERIC (10,0),Age INT NOT NULL,Billed_by INT NOT NULL REFERENCES Hospital (Hname),PRIMARY KEY (SSN));")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Patient(P_lastName, SSN, Age, Billed_by,Phone_number)VALUES ('ally', 123456789, 89, 1210, 9983545463)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Patient(P_lastName, SSN, Age, Billed_by,Phone_number)VALUES ('mcmillin', 234567891, 78, 1210,4758374657)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Patient(P_lastName, SSN, Age, Billed_by,Phone_number)VALUES ('martinez', 345678912, 32, 1310,8475647384)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Patient(P_lastName, SSN, Age, Billed_by,Phone_number)VALUES ('steward', 456789123, 19, 1111,9879990098)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Patient(P_lastName, SSN, Age, Billed_by,Phone_number)VALUES ('mark', 567891234, 34, 1234,9873990098)")
    except Error as e:
        print(e)
    try:
        db.exec("CREATE TABLE Medicine (\
Med_ID	INTEGER,\
Price	NUMERIC (3,2) DEFAULT 000.00,\
Mname	VARCHAR(20) NOT NULL,\
PRIMARY KEY(Med_ID));")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Medicine(Med_ID, PRICE, Mname)VALUES ('907', 900.90, 'mud')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Medicine(Med_ID, PRICE, Mname)VALUES ('908', 80.90, 'asperdim')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Medicine(Med_ID, PRICE, Mname)VALUES ('909', 90.90, 'treebark')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Medicine(Med_ID, PRICE, Mname)VALUES ('807', 990.90, 'eggg')")
    except Error as e:
        print(e)
    try:
        db.exec("CREATE TABLE Lab (\
Lab_ID INT,\
Lab_Name VARCHAR (20) NOT NULL,\
Lab_phone NUMERIC (10,0),\
Address VARCHAR(20),\
PRIMARY KEY(Lab_ID));")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Lab (Lab_ID, Lab_name, Address, Lab_phone)VALUES (420420, 'stateLab', '3032 creek dr', 9302948572)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Lab (Lab_ID, Lab_name,Address, Lab_phone)VALUES (420600, 'geeseoi', '9032 mockinline', 9008372939)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Lab (Lab_ID, Lab_name, Address, Lab_phone)VALUES (270420, 'colegenius', '9684 breaking bad lane', 2103427787)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Lab (Lab_ID, Lab_name, Address,Lab_phone)VALUES (520460, 'makedrugs', '123 cherry hill', 9406378888)")
    except Error as e:
        print(e)
    try:
        db.exec("CREATE TABLE Prescribes (\
Medicine_ID INT REFERENCES Medicine (Med_ID),\
Prescibed_By INT REFERENCES Doctor (EmployeeID),\
PRIMARY KEY (Medicine_ID, Prescibed_By)\
);")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Prescribes(Prescibed_By, Medicine_ID)VALUES(1234,907)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Prescribes(Prescibed_By, Medicine_ID)VALUES(1111,907)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Prescribes(Prescibed_By, Medicine_ID)VALUES(1234,807)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Prescribes(Prescibed_By, Medicine_ID)VALUES(2222,907)")
    except Error as e:
        print(e)

    try:
        db.exec("CREATE TABLE Manufactures (\
Lab_Number INT REFERENCES Lab (Lab_ID),\
Med_ID INT REFERENCES Medicine (Med_ID),\
PRIMARY KEY (Lab_Number, Med_ID)\
);")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Manufactures (Lab_Number, Med_ID)VALUES (420420, 907)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Manufactures (Lab_Number, Med_ID)VALUES (420600, 907)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Manufactures (Lab_Number, Med_ID)VALUES (420420, 807)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Manufactures (Lab_Number, Med_ID)VALUES (720420, 908)")
    except Error as e:
        print(e)
    try:
        db.exec("CREATE TABLE Examines (\
Patient_SSN NUMERIC (9,0) REFERENCES Patient (SSN) ON DELETE CASCADE,\
Doctor_ID INT REFERENCES Doctor (EmployeeID) ON DELETE CASCADE,\
PRIMARY KEY (Patient_SSN, Doctor_ID));")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Examines(Doctor_ID, Patient_SSN)VALUES(1234,123456789)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Examines(Doctor_ID, Patient_SSN)VALUES(1234,234567891)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Examines(Doctor_ID, Patient_SSN)VALUES(1235,345678912)")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT into Examines(Doctor_ID, Patient_SSN)VALUES(1112,456789123)")
    except Error as e:
        print(e)

    try:
        db.exec("CREATE TABLE Takes (\
P_SSN NUMERIC (9,0) REFERENCES Patient (SSN) ON DELETE CASCADE,\
M_ID INT REFERENCES Medicine (Med_ID) ON DELETE CASCADE,\
Symptoms CHAR (1) DEFAULT ('N') check (Symptoms='N' or Symptoms='Y'),\
PRIMARY KEY (P_SSN, M_ID));")
    except Error as e:
        print(e)

    try:
        db.exec("INSERT INTO Takes (P_SSN, M_ID, Symptoms)VALUES(123456789,907, 'Y')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Takes (P_SSN, M_ID, Symptoms)VALUES(123456789,908, 'N')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Takes (P_SSN, M_ID, Symptoms)VALUES(234567891,907, 'Y')")
    except Error as e:
        print(e)
    try:
        db.exec("INSERT INTO Takes (P_SSN, M_ID,Symptoms)VALUES(345678912,807, 'N')")
    except Error as e:
        print(e)
# done creating tables'
    while loop:
        menu()
        choice = int(input("Enter your choice ( a number from 1 to 10 ) \n"))
        if choice == 1:
            patientLoop = True
            print("you've chosen the patient table: Your options are: ")
            while patientLoop:
                patientMenu()
                pchoice = int(input("Which action would you like to perform? "))
                if pchoice ==1:

                    try:
                        rows = db.fetch("SELECT P_lastName,count(*) From Patient p, Takes t WHERE p.SSN=t.P_SSN GROUP BY P_lastName")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif pchoice ==2:
                    in1=input("Enter the patient's last name ")
                    in2 = input("Enter the patient's SSN ")
                    in3 = input("Enter the patient's age ")
                    in4 = input("Enter the billing ID of the hospital that billed them ")
                    in5 = input("Enter the patient's primary phone number ")
                    try:
                        db.exec("INSERT into Patient(P_lastName, SSN, Age, Billed_by, Phone_number)\
VALUES ('{a}', {b}, {c}, {d},{e})".format(a=in1, b=in2, c=in3, d=in4, e=in5))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Patient")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif pchoice == 3:
                    in1=int(input("Find patients younger than ____? "))
                    try:
                        rows= db.fetch("SELECT Hname ,count(*) FROM Patient p INNER JOIN Hospital h ON h.BID = p.Billed_by\
                     and p.age<{} GROUP by h.Hname".format(in1))
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif pchoice ==4:
                    patientLoop=False
                else:
                    print("Invalid choice, try again")
        elif choice == 2:
            hospitalLoop = True
            print("You've chosen the hospital table: Your options are: ")
            while hospitalLoop:
                hospitalMenu()
                hchoice = int(input("Which action would you like to perform? "))
                if hchoice == 1:
                    h = str(input("Enter a hospital name\n"))
                    address = str(input("Enter the address\n"))
                    hrating = int(input("Enter the rating (out of 10)\n"))
                    bill = int(input("enter the billing ID (a number) "))
                    args = (h, address, hrating, bill)

                    try:
                        db.exec('INSERT INTO Hospital (Hname, Haddress, rating, BID) VALUES{}'.format(args))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Hospital ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)

                elif hchoice == 2:
                    n2=input("Enter the name of the hospital you would like deleted ")
                    try:
                        db.exec("DELETE FROM Hospital WHERE Hname='{a}'".format(a=n2))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * From Hospital")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)

                elif hchoice == 3:
                    r=int(input("Delete hospitals with a rating of less than ___"))
                    try:
                        db.exec('DELETE FROM Hospital WHERE rating <{}'.format(r))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Hospital ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)

                elif hchoice == 4:
                    try:
                        rows = db.fetch("SELECT Hname, count(*) FROM Hospital h INNER JOIN\
                                        Patient p ON p.Billed_by = h.BID GROUP BY h.BID HAVING count(*)\
                                        =(SELECT max(mycount) FROM (SELECT count(*) mycount FROM Patient GROUP BY Billed_by));")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif hchoice == 5:
                    hospitalLoop = False
                else:
                    print("Error invalid choice, try again")

        elif choice == 3:
            medLoop=True
            print("You've chosen the medicine table: Your options are: ")
            while medLoop:
                medMenu()
                medchoice=int(input("Which operation would you like to perform? "))
                if medchoice == 1:
                    in1=int(input("Enter med_ID "))
                    in2 = float(input("Enter price "))
                    in3 = input("Enter name ")
                    try:
                        db.exec("INSERT into Medicine(Mname,PRICE, Med_ID )Values('{a}',{b},{c})".format(a=in3, b=in2,c= in1))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Medicine ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif medchoice == 2:
                    in1 = float(input("Decrease price of medicine above ___ price ? "))
                    in2 = float(input("Subrract what amount from price? "))
                    if in2>in1:
                        print("ERROR, subraction price must be lower than original price, try again")
                        in1 = float(input("Decrease price of medicine above ___ price ? "))
                        in2 = float(input("Subtract what amount from price? "))
                    try:
                        db.exec("UPDATE Medicine SET PRICE = PRICE - {b} WHERE PRICE > {a}".format(a=in1, b=in2))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Medicine ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif medchoice == 3:
                    in1=int(input("Enter the med_Id of the medicine you wish to delete "))
                    try:
                        db.exec("Delete From medicine Where Med_ID = {a}".format(a=in1))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Medicine ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif medchoice == 4:
                    medLoop = False
                else:
                    print("invalid choice try again")
        elif choice == 4:
            exLoop = True
            print("You've chosen the Examines table: Your options are: ")
            while exLoop:
                exMenu()
                exchoice = int(input("Which action would you like to take? "))
                if exchoice == 1:
                    in1 = int(input("Enter the doctor's employee number "))
                    in2 = int(input("Enter patients SSN" ))
                    try:
                        db.exec("INSERT into Examines(Doctor_ID, Patient_SSN)VALUES({a},{b})".format(a=in1,b=in2))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Examines ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif exchoice ==2:
                    try:
                        rows =db.fetch("SELECT Lname, EmployedBY, count(*) FROM Doctor d, Examines e WHERE e.Doctor_ID=d.EmployeeID\
                             GROUP BY d.EmployeeID")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif exchoice == 3:
                    try:
                        rows = db.fetch("SELECT Lname, count(*), EmployedBy From Doctor d, Examines e \
                                WHERE e.Doctor_ID = d.EmployeeID GROUP BY d.EmployeeID HAVING count(*)>\
                                (SELECT avg(mycount)FROM (SELECT count(*) mycount FROM Examines GROUP BY Doctor_ID));")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif exchoice == 4:
                    exLoop = False
                else:
                    print("Invalid choice, try again ")
        elif choice == 5:
            taksLoop = True
            print("You've chosen the Takes table: Your options are: ")
            while taksLoop:
                takesMenu()
                tc= int((input("Which action would you like to take? ")))
                if tc == 1:
                    in1 = int(input("Enter the Patient's SSN "))
                    in2 = int(input("Enter the Medicine ID "))
                    try:
                        db.exec("INSERT INTO Takes(P_SSN,M_ID)VALUES({a},{b})".format(a=in1, b=in2))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Takes ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif tc ==2:
                    in1=input("Enter a medicine name to see which patients are allergic to it ")
                    try:
                        rows=db.fetch("SELECT P_lastName, SSN, Phone_number FROM Patient p, Takes t\
                                 WHERE p.SSN =t.P_SSN AND t.Symptoms = 'Y' AND t.M_ID =(SELECT Med_ID FROM \
                                 Medicine WHERE Mname ='{a}')".format(a=in1))
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif tc ==3:
                    in1 = int(input("Enter the Patient SSN of the relation you would like to delete\n"))
                    in2 = int(input("Enter the Medicine ID of the relation you would like to delete\n"))
                    try:
                        db.exec("DELETE From Takes WHERE P_SSN = {a} AND M_ID = {b}".format(a=in1, b=in2))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Takes ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif tc ==4:
                    taksLoop=False
                else:
                    print("Error: invalid option, try again")
        elif choice == 6:
            labLoop = True
            print("You've chosen the lab table: Your options are: ")
            while labLoop:
                labMenu()
                lchoice = int(input("Which action would you like to perform? "))
                if lchoice == 1:
                    in1 = input("Enter the lab Id ")
                    in2 = input("Enter the Lab name ")
                    in3 = input("Enter the lab's phone number")
                    in4 = input("Enter the lab's address")
                    args =(in1, in2, in3, in4)
                    try:
                        db.exec("INSERT INTO Lab (Lab_name,Address, Lab_phone, Lab_ID) VALUES ('{a}','{b}',{c},{d})"\
                                .format(a=in2, b=in4, c=in3, d=in1))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Lab ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                if lchoice == 2:
                    in1 = int(input("Enter the lab_ID of the lab you wish to update"))
                    in2 = input("Enter the new lab name ")
                    in3 = input("Enter the new lab phone number ")
                    in4 = input("Enter the new address ")
                    try:
                        db.exec("UPDATE Lab SET Lab_name = '{a}', Address = '{b}', Lab_phone ={c} WHERE Lab_ID = {d}".format(a=in2, b=in4, c=in3, d=in1))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Lab ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                if lchoice == 3:
                    in1 = int(input("Enter the lab _ID of the lab you wish to delete "))
                    try:
                        db.exec("Delete from Lab Where Lab_ID = {a}".format(a=in1))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Lab ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                if lchoice == 4:
                    labLoop = False
        elif choice == 7:
            manloop= True
            print("You've chosen the Manufactures table: Your options are: ")
            while manloop:
                manMenu()
                manchoice = int(input("What would you like to do? "))
                if manchoice ==1:
                    in1 = int(input("Enter lab ID "))
                    in2 = int(input("Enter medicine ID "))
                    try:
                        db.exec("INSERT INTO Manufactures(Lab_Number, Med_ID)VALUES({a},{b})"\
                                .format(a=in1, b=in2))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Manufactures ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif manchoice ==2:
                    print("\nNames of labs and how many meds they make")
                    try:
                       rows= db.fetch("SELECT Lab_name, count(*) FROM Lab l, Manufactures m WHERE\
                                  l.Lab_ID =m.Lab_Number GROUP BY m.Lab_Number")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                    print("\n")
                elif manchoice ==3:
                    in1= input("Find where ____ medicine is made: enter med name ")
                    try:
                        rows = db.fetch("SELECT Lab_name, Lab_Phone, Address FROM Lab l, Manufactures m\
                                        WHERE l.Lab_ID=m.Lab_Number AND m.Med_ID =(SELECT \
                                        Med_ID FROM Medicine WHERE Mname='{a}')GROUP BY m.Lab_Number".format(a=in1))
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif manchoice ==4:
                    manloop= False
                else:
                    print("Error: invalid choice, try again ")
        elif choice == 8:
            preLoop = True
            print("You've chosen the Prescribes table: Your options are: ")
            while preLoop:
                preMenu()
                prechoice = int(input("Choose an action "))
                if prechoice == 1:
                    in1 = int(input("Enter the prescriber's EmployeeID "))
                    in2 = int(input("Enter prescribed medicine's ID"))
                    try:
                        db.exec("INSERT into Prescribes (Prescibed_By, Medicine_ID)Values({a},{b})"\
                                .format(a=in1, b=in2))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Prescribes ")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif prechoice == 2:
                    try:
                        rows = db.fetch("SELECT Mname, count(*) FROM Medicine m, Prescribes p WHERE \
                                 p.Medicine_ID=m.Med_ID GROUP BY m.Med_ID HAVING count(*) = (SELECT max\
                                 (mycount)FROM (SELECT count(*) mycount FROM Prescribes GROUP BY Medicine_ID))")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif prechoice ==3:
                    try:
                        rows =db.fetch("SELECT Mname, count(*) FROM Medicine m, Prescribes p WHERE\
                                 p.Medicine_ID=m.Med_ID GROUP BY m.Med_ID")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif prechoice ==4:
                    preLoop = False
                else:
                    print("ERROR: invalid choice, try again")
        elif choice == 9:
            docLoop = True
            print("You've chosen the Doctor table: Your options are: ")
            while docLoop:
                docMenu()
                dchoice = int(input("Choose an action "))
                if dchoice ==1:
                    in1 = input("Enter last name ")
                    in2 = input("Enter specialty ")
                    in3 = int(input("Enter years of experience "))
                    in4 = int(input("Enter employee ID "))
                    in5 = input("Enter hospital they work at ")
                    in6 = int(input("Enter salary "))
                    try:
                        db.exec("INSERT INTO Doctor (Lname, Specialty, Years_Experienace, EmployeeID,\
                                EmployedBy, Salary) VALUES('{a}','{b}',{c},{d},'{e}',{f})"\
                                .format(a=in1, b=in2, c=in3, d=in4, e=in5, f=in6))
                    except Error as e:
                        print(e)
                    try:
                        rows = db.fetch("SELECT * FROM Doctor")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif dchoice ==2:
                    in1 = int(input("Enter employee ID of the doctor you wish to delete "))
                    try:
                        db.exec("DELETE FROM Doctor WHERE EmployeeID ={a}".format(a=in1))
                    except Error as e:
                        print(e)

                    try:
                        rows = db.fetch("SELECT * FROM Doctor")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif dchoice ==3:
                    in1 = input("Which hospital are you searching at? ")
                    in2 = int(input("How many years of experience would you like your doctor to have? "))
                    try:
                        rows =db.fetch("SELECT Lname, Specialty FROM Doctor WHERE Years_Experienace >={a} AND EmployedBy='{b}'"\
                                 .format(a=in2, b=in1))
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif dchoice ==4:
                    try:
                        rows=db.fetch("SELECT Specialty, AVG(Salary) FROM Doctor GROUP BY Specialty")
                    except Error as e:
                        print(e)
                    for row in rows:
                        print(row)
                elif dchoice ==5:
                    docLoop = False
                else:
                    print("ERROR: invalid choice, try again ")

        elif choice == 10:
            print("Have a nice day!")
            loop = False
        else:
            print("Wrong option selection. Try again")



    # at the end close connection to the Database
    db.close()


if __name__ == '__main__':
    main()
