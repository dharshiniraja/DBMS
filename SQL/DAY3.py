EXC 10
INSERT INTO Salesman(SId,SName,Location) VALUES(11,'Elizabeth','London');

***********************************************************************************************************************
EXC 11
INSERT INTO Product(Prodid,PDesc,Price,Category,Discount) VALUES(110,'Bat',50,'Sports',NULL);

***********************************************************************************************************************
EXC 12
SELECT * FROM Product

***********************************************************************************************************************
EXC 13
SELECT PRODID,PRICE,CATEGORY FROM Product

***********************************************************************************************************************
EXC 14
SELECT DISTINCT CATEGORY FROM Product

***********************************************************************************************************************
EXC 15
SELECT PRODID,PDESC,CATEGORY,DISCOUNT FROM Product WHERE CATEGORY='Apparel'

***********************************************************************************************************************
EXC 16
SELECT PRODID,PDESC,CATEGORY,DISCOUNT FROM Product WHERE PDESC IS NULL

***********************************************************************************************************************
EXC 17
SELECT PRODID,PDESC,CATEGORY,DISCOUNT FROM Product WHERE CATEGORY='Apparel' AND DISCOUNT>5

************************************************************************************************************************
EXC 18
UPDATE Product SET DISCOUNT=25 WHERE CATEGORY='Sports'

************************************************************************************************************************
EXC 19
UPDATE Product SET PRICE=50 WHERE CATEGORY='Apparel' AND PDESC='Trouser'

************************************************************************************************************************
EXC 20
UPDATE Salesman SET SNAME='Jenny',LOCATION='Bristol' WHERE SID=3

************************************************************************************************************************
EXC 21
DELETE FROM SaleDetail WHERE SALEID=1004

************************************************************************************************************************
EXC 22
DELETE FROM SaleDetail WHERE SALEID=1004

************************************************************************************************************************
ASS 16
INSERT INTO Article(ArCode,ArName,Rate,Quantity,Class) VALUES('A1001','Mouse',500,0,'C')

***********************************************************************************************************************
ASS 17
INSERT INTO Store(StoreName,Location,ManagerName) VALUES('Loyal World','Infy Campus, Mysore','Rohan Kumar')

***********************************************************************************************************************
ASS 18
INSERT INTO Bill(BillNo,StoreName,Shopperid,ArCode,Amount,BillDate,QuantitY) VALUES(1001,'Loyal World',101,'A1001',1000,'20-OCT-15',2)

********************************************************************************************************************************************
ASS 19
INSERT INTO Supplier VALUES('S501','Avaya Ltd',9012345678,'Mysore')

******************************************************************************************************************************
ASS 20
SELECT DESCR,PRICE FROM Item WHERE DESCR LIKE '%Hard disk'

******************************************************************************************************************************
ASS 21
SELECT QUOTATIONID,SNAME,ITEMCODE,QUOTEDPRICE,QDATE,QSTATUS FROM Quotation WHERE QSTATUS='Rejected' OR QSTATUS='Closed'

***************************************************************************************************************************
ASS 22
SELECT DESIGNATION,SALARY FROM EmpDetails WHERE DESIGNATION='Manager' OR DESIGNATION='Billing Staff'

*****************************************************************************************************************************
ASS 23
SELECT roid,location FROM RETAILOUTLET WHERE MANAGERID IS NULL

***************************************************************************************************************************
ASS 24
SELECT orderid, quotationid ,status FROM ORDERS WHERE ORDERDATE>='1-Dec-2014' AND ORDERDATE<='1-Jan-2015'

**************************************************************************************************************************
ASS 25
SELECT  ITEMCODE, DESCR , PRICE FROM Item WHERE  CATEGORY='B' AND DESCR LIKE '%Shirt' OR 
DESCR LIKE '% Skirt' AND CATEGORY='B'

**************************************************************************************************************************
ASS 26
SELECT DISTINCT DESIGNATION , SALARY FROM EMPDETAILS 

**************************************************************************************************************************
ASS 27
SELECT ITEMCODE,DESCR ,PRICE FROM ITEM 

**************************************************************************************************************************
ASS 28
SELECT quotationid, sname FROM quotation WHERE QSTATUS='Accepted' OR QSTATUS='Rejected'

**************************************************************************************************************************
ASS 29
SELECT  itemcode,DESCR, price FROM Item WHERE DESCR LIKE '_r%'

**************************************************************************************************************************
ASS 30
SELECT DISTINCT ITEMTYPE FROM ITEM 

**************************************************************************************************************************
ASS 31
SELECT  orderid, quotationid, status, pymtdate FROM ORDERS WHERE PYMTDATE IS NULL

**************************************************************************************************************************
ASS 32
SELECT DISTINCT ITEMTYPE,CATEGORY FROM ITEM 

**************************************************************************************************************************
ASS 33
SELECT EMPID,SALARY AS "Current Salary",SALARY*1.1 AS "New Salary",
SALARY*1.1-SALARY AS "Incremented Amount" FROM EMPDETAILS

**************************************************************************************************************************
ASS 34
INSERT INTO CITY VALUES('Mysore')

******************************************************************************************************************************************
ASS 35
INSERT INTO ADDRESS VALUES (350, 'Electronics City','Mysore',570018,'Karnataka')

******************************************************************************************************************************************
ASS 36
INSERT INTO Article VALUES('A1002','Keyboard',1000,10,'B')

*****************************************************************************************************************************************
ASS 37
SELECT QUOTATIONID,QDATE,QUOTEDPRICE FROM Quotation WHERE QUOTEDPRICE>1400 AND QUOTEDPRICE<2150

*******************************************************************************************************************************************
ASS 38
SELECT ITEMTYPE,DESCR,PRICE FROM Item WHERE PRICE>4000

********************************************************************************************************************************************
ASS 39
SELECT DESIGNATION,SALARY FROM EmpDetails WHERE (DESIGNATION='Billing Staff' OR DESIGNATION='Mananger') OR (SALARY>=2500 AND SALARY<=5000)


