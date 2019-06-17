EXCERCISE 3

CREATE TABLE Player(
PId INTEGER CONSTRAINT pk PRIMARY KEY,
PName VARCHAR2(20) CONSTRAINT nn NOT NULL,
Ranking INTEGER)

___________________________________________________________________________________________________________________________

EXCERCISE 4
TName VARCHAR2(30) NOT NULL,
StartDt DATE NOT NULL,
EndDt DATE NOT NULL,
Prize INTEGER NOT NULL)
______________________________________________________________________________________________________________________________
ASS 2
CREATE TABLE Shopper(
ShopperId INTEGER PRIMARY KEY,
ShopperName VARCHAR2(20) CONSTRAINT nn NOT NULL,
Gender CHAR(6) CONSTRAINT sho_gender_ck CHECK(Gender IN('Male','Female')),
MobileNo INTEGER CONSTRAINT nn1 NOT NULL,
Address VARCHAR2(50));
_________________________________________________________________________________________________________________________
ASS 4
CREATE TABLE ARTICLE(
ArCode CHAR(5) PRIMARY KEY CHECK (ArCode LIKE'A%'),
ArName VARCHAR2(30) NOT NULL, 
Rate NUMBER(8,2),
Quantity NUMBER(4) DEFAULT 0 CHECK (Quantity>=0),
Class CHAR(1) CHECK(Class IN('A','B','C'))
);
________________________________________________________________________________________________________________________-
ASS 5
CREATE TABLE Store(
Name VARCHAR2(20) PRIMARY KEY,
Location VARCHAR2(30) NOT NULL,
ManagerName VARCHAR2(30) UNIQUE
)
__________________________________________________________________________________________________________________________
ASS 6
ALTER TABLE STORE RENAME COLUMN Name TO StoreName
___________________________________________________________________________________________________________________________
ASS 7
CREATE TABLE Bill(
BillNo NUMBER PRIMARY KEY,
StoreName VARCHAR2(20) REFERENCES Store(StoreName),
ShopperId NUMBER REFERENCES Shopper(ShopperId),
ArCode CHAR(5) REFERENCES Article(ArCode),
Amount NUMBER,
BillDate DATE, 
Quantity NUMBER(4) DEFAULT 1 CHECK (Quantity>0)
)
____________________________________________________________________________________________________________________________
ASS 8
CREATE TABLE Supplier(
Supplierid VARCHAR2(6) PRIMARY KEY,
Name VARCHAR2(30),
ContactNo VARCHAR2(15) NOT NULL,
Emailid VARCHAR2(30)
);
___________________________________________________________________________________________________________________________
ASS 9
ALTER TABLE Supplier ADD CITY VARCHAR2(10)
____________________________________________________________________________________________________________________________
ASS 10.
ALTER TABLE Supplier DROP (Emailid)
___________________________________________________________________________________________________________________________
ASS 11
CREATE TABLE City(
City VARCHAR2(20) UNIQUE
);
___________________________________________________________________________________________________________________________
ASS 12
ALTER TABLE CITY DROP (City)
___________________________________________________________________________________________________________________________
ASS 14
ALTER TABLE Address MODIFY state VARCHAR2(20)
