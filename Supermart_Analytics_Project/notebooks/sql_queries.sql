-- Select the top 5 cities with the highest sales
SELECT City, SUM(Sales) AS Total_Sales FROM sales_data 
GROUP BY City ORDER BY Total_Sales DESC LIMIT 5;

-- Yearly Sales Trends
SELECT Order_Year, SUM(Sales) AS Total_Sales FROM sales_data 
GROUP BY Order_Year ORDER BY Order_Year;

-- Monthly Sales Trends
SELECT Month, SUM(Sales) AS Total_Sales FROM sales_data 
GROUP BY Month ORDER BY FIELD(Month, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');

-- Category-wise Sales
SELECT Category, SUM(Sales) AS Total_Sales FROM sales_data 
GROUP BY Category ORDER BY Total_Sales DESC;

-- Profit Analysis by Region
SELECT Region, SUM(Profit) AS Total_Profit FROM sales_data 
GROUP BY Region ORDER BY Total_Profit DESC;

-- Discount vs Sales Effect Analysis
SELECT Discount, AVG(Sales) AS Avg_Sales FROM sales_data 
GROUP BY Discount ORDER BY Discount ASC;
