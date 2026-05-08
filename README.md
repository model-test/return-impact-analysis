# Return Impact Analysis Using Python, Pandas, and SQL

Project Overview
- This project analyzes how returned orders affect profitability using Python, Pandas, and SQL (sqlite).
- The analysis focuses on which products and regions generate the most returned revenue and comparing the profitability of returned vs non-returned orders.

Tools Used
- Python
- Pandas
- SQLite
- SQL
- openpyxl

Questions
1. Which products generate the highest returned revenue?
2. Which regions generate the highest returned revenue?
3. Do returned orders have worse average revenue, profit, and profit margins than non-returned orders?
4. What percentage of total revenue came from returned orders?

Key Findings
- Laptops have the highest return value
- South Florida has the highest return revenue
- Returned orders ahve worse average revenue, profit, and profit margins than non-returned orders
- 4% of total revenue came from returned orders
- Mouse has the highest product order count despite Keyboard generating more revenue
- Keyboard is the product returned the most
- Webcam has the highest return rate despite it being returned only 5 times
- Webcam is the worst-performing product proportionately due to its high return rate and lower total returns (Implementing a customer review system may allow for the business to identify why certain products experience higher return rates)
- Docking Station is the best-performing product proportionately due to it having a return rate of 0% while still having existing orders
- High returned revenue does not necessarily imply the highest return rate.

Future Improvements on This Project
- Add visualizations via Matplotlib
- Investigate why specific regions experience higher returns
- Build a dashboard version of the analysis
