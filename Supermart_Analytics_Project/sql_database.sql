USE supermart_sales;

CREATE TABLE sales_data (
    Order_ID VARCHAR(50),
    Customer_Name VARCHAR(255),
    Category VARCHAR(255),
    Sub_Category VARCHAR(255),
    City VARCHAR(255),
    Order_Date DATE,
    Region VARCHAR(100),
    Sales FLOAT,
    Discount FLOAT,
    Profit FLOAT,
    State VARCHAR(255),
    Month VARCHAR(20),
    Order_Year INT
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_supermart_data.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ','  
ENCLOSED BY '"'  
LINES TERMINATED BY '\r\n'  
IGNORE 1 ROWS
(Order_ID, Customer_Name, Category, Sub_Category, City, Order_Date, Region, Sales, Discount, Profit, State, Month);


