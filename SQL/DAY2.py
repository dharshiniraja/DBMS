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
