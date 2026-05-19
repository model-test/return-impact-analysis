# Return Impact Analysis Using Python, Pandas, and SQL

#Project Overview
- This project analyzes how returned orders affect profitability using Python, Pandas, and SQL (sqlite).
- The analysis focuses on which products and regions generate the most returned revenue and comparing the profitability of returned vs non-returned orders.

## Tools Used
- Python
- Pandas
- SQLite
- SQL
- openpyxl

## Questions
1. Which products generate the highest returned revenue?
2. Which regions generate the highest returned revenue?
3. Do returned orders have worse average revenue, profit, and profit margins than non-returned orders?
4. What percentage of total revenue came from returned orders?
5. How many total orders does each product have?
6. How many returned orders does each product have?
7. How many total orders does each region have?
8. How many returned orders does each region have?
9. What is the return rate per region?
10. What percentage does each region take up in total returned orders?
11. Which segment places the most orders?
12. Which segment generates the most returns?
13. Which segment has the highest return rate?
14. Which segment contributes most to returned revenue?
15. Which customer segment is most profitable on average?
16. How many total orders exist for each segment-product combination?
17. How many returned orders exist for each segment-product combination?
18. What is the return rate for each product within each customer segment?
19. Which months have had the most total orders?
20. Which months have had the most returns?
21. What is the return rate per month?
22. Which months generate the most financial loss from returns?
23. How much total revenue does each month generate?

## Key Findings
### Return Impact Analysis
- Laptops have the highest return value
- South Florida has the highest return revenue
- Returned orders ahve worse average revenue, profit, and profit margins than non-returned orders
- 4% of total revenue came from returned orders
### Product Return Rate Analysis
- Mouse has the highest product order count despite Keyboard generating more revenue
- Keyboard is the product returned the most
- Webcam has the highest return rate despite it being returned only 5 times
- Webcam is the worst-performing product proportionately due to its high return rate and lower total returns (Implementing a customer review system may allow for the business to identify why certain products experience higher return rates)
- Docking Station is the best-performing product proportionately due to it having a return rate of 0% while still having existing orders
- High returned revenue does not necessarily imply the highest return rate.
### Regional Return Rate Analysis
- Southeast has the most total orders, North Florida has the least.
- South Florida and Southeast are tied for most total returned orders, North Florida has the least.
- Southwest is the proportionately worst-performing region due to it having an 8.75% return rate despite having only been returned 7 times
- South Florida is the region accounting for most of the total revenue of returned orders
- North Florida is the proportionately best-performing region due to it having a 1.3% return rate while having 73 total orders and only 1 return
### Customer Segment Return Analysis
- Enterprise places the most orders
- Enterprise generates the most returned orders, though is very closely followed by Education
- Education has the highest return rate, though is very closely followed by Enterprise despite Enterprise's higher total return count
- Consumer contributes most to returned revenue despite Enterprise and Education both having more total returns
- Small Business is the most profitable on average, though is very closely followed by Consumer, despite generating the least amount of revenue.
- Enterprise is the least profitable on average despite it having the most orders.
### Product + Segment Analysis
- Consumer has the highest amount of Mouse orders respective to its segment
- Education has ordered Keyboard, Monitor, and Mouse tied as the most ordered respective to its segment
- Enterprise has the highest amount of Laptop orders closely followed by Mouse orders respective to its segment
- Small Business has the highest amount of Keyboard orders closely followed by Mouse orders respective to its segment
- Consumer has Laptop, Monitor, Mouse, and Webcam tied at the top for most returned orders respective to its segment
- Education has Keyboard as the most returned product respective to its segment
- Enterprise has Keyboard and Monitor tied to the top closely followed by Mouse for most returned orders respective to its segment
- Small Business has Monitor closely followed by Keyboard as the most returned product respective to its segment
- Webcam has the highest return rate for Consumer (13%) and Education (18%).
- Monitor has the highest return rate for Enterprise (11%) and Small Business (14%).
- Webcam and Monitor are both the proportionally worst-performing products across customer segments with Webcam taking the edge due to Webcam taking up two of the highest return rates despite being ordered less than Monitor across all customer segments
- Docking Station is the proportionally best-performing product due to its 0% return rate across all customer segments despite existing orders, though it is still amongst one of the least ordered across all customer segments
- Headphones is the proportionally second best-performing product due to its very low return rate across most customer segments and moderate total orders, being more practically successful than Docking Station due to higher total orders across most customer segments
### Monthly Analysis
- March is the month with most total orders at 77 closely followed by July at 75 and February at 72.
- February is the month with most total returned orders at 8 very closely followed by December at 7 and October at 5.
- February is the month with the highest total return rate at 11% very closely followed by December at 10% and October at 8%.
- December is the month with the highest financial loss from returned orders at over $6.5K followed by February at $4.4K and September at $3.5K.
- December is the financially worst-performing month due to its moderate amount of orders yet high return rate.
- February is the proportionally worst-performing month despite its high order count due to it having the most returned orders and highest return rate.
- March and July are very similar and almost tied for being one of the proportionally best-performing months due to their high amount of orders yet very low and similar return rates with July taking the edge with slightly lower total returned orders, notably lower financial loss, and slightly lower return rate, though also has slightly lower total orders than March and generates $852.61 less total revenue.
- August is the proportionally best-performing month due to its moderate amount of orders yet extremely low return rate at 1% while being the 6th month with the highest total revenue at $5.6K and a total financial loss of only $515.41. Only 1 order has been returned.
- October is the month that generates the most revenue at $6.4K closely followed by March at $6.2K, May at $6.1K, and July at $6.1K.

## Future Improvements on This Project
- Investigate why specific regions experience higher returns
- Build a dashboard version of the analysis
