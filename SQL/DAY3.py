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
