import pandas as pd
import sqlite3

#-------------------------
# Data Loading + Cleaning
#-------------------------

df = pd.read_excel("data/sales_data.xlsx")

df.columns = df.columns.str.strip().str.lower()
df["returned"] = df["returned"].str.strip().str.lower()

df["order_date"] = pd.to_datetime(df["order_date"], origin="1899-12-30", unit="D")


conn = sqlite3.connect("data/sales_project.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

#-------------------------
# Return Impact Analysis
#-------------------------

query = """
SELECT *
FROM sales
WHERE returned = 'yes';
"""

returns_df = pd.read_sql_query(query, conn)

# Which products have the highest returned revenue?
total_product_returns_revenue = returns_df.groupby("product")["revenue"].sum().sort_values(ascending=False)

# Laptops have the highest return revenue
#print(total_product_returns_revenue)


# Which regions have the highest returned revenue?
regional_returns_revenue = returns_df.groupby("region")["revenue"].sum().sort_values(ascending=False)

# South Florida has the highest returned revenue
#print(regional_returns_revenue)


# Do returned orders have worse average revenue, profit, and profit margins than non-returned orders?
query = """
SELECT *
FROM sales
WHERE returned = 'no';
"""

non_returned_df = pd.read_sql_query(query, conn)

avg_returned_data = returns_df[['revenue', 'profit', 'profit_margin_pct']].mean()
avg_retained_data = non_returned_df[['revenue', 'profit', 'profit_margin_pct']].mean()

# Returned orders have worse average revenue, profit, and profit margin than non-returned orders
#print(avg_returned_data.to_string())
#print(avg_retained_data.to_string())


# What percentage of total revenue came from returned orders?
query = """
SELECT SUM(revenue) AS total_revenue
FROM sales
"""

total_revenue = pd.read_sql_query(query, conn)

#print(total_revenue)

query = """
SELECT SUM(revenue) AS total_returned_revenue
FROM sales
WHERE returned = 'yes'
"""

total_returned_revenue = pd.read_sql_query(query, conn)

#print(total_returned_revenue)

total_returned_revenue_percentage = round(
    total_returned_revenue["total_returned_revenue"].iloc[0] / total_revenue["total_revenue"].iloc[0] * 100, 2
)

# 4% of total revenue came from returned orders
#print(total_returned_revenue_percentage)


# Summary:
# Laptops have the highest return value
# South Florida has the highest return revenue
# Returned orders have worse average revenue, profit, and profit margin than non-returned orders
# 4% of total revenue came from returned orders

"""
FINDINGS:
1. Returned orders are less profitable than non-returned orders
2. 96% of orders are not returned
3. Possibly, South Florida either has the highest volume of returned orders or just the highest cost on customers.
To find out which, it'd be worth checking how many returned orders came from each region rather than depending on the revenue alone.
(Extra) 4. A customer review as to "why" they returned their order would allow for the business to boost profitability
"""

#-------------------------
# Product Return Rate Analysis
#-------------------------

# How many total orders does each product have?
product_order_count = df.groupby("product").size().sort_values(ascending=False)
#print(product_order_count)


# How many returned orders does each product have?
returned_order_count = returns_df.groupby("product").size().sort_values(ascending=False)
#print(returned_order_count)


# Calculation for return rate
return_rate = (returned_order_count / product_order_count * 100).fillna(0).sort_values(ascending=False)

# Webcam has the highest return rate
#print(return_rate)


"""
FINDINGS:
1. Mouse has the highest product order count despite Keyboard generating more revenue
2. Keyboard is the product returned the most
3. Webcam has the highest return rate despite it being returned only 5 times
4. Webcam is the worst-performing product proportionately due to its high return rate and lower total returns (Implementing a customer review system may allow for the business to identify why certain products experience higher return rates)
5. Docking Station is the best-performing product proportionately due to it having a return rate of 0% while still having existing orders
"""

#-------------------------
# Regional Return Rate Analysis
#-------------------------

# How many total orders does each region have?
regional_order_count = df.groupby("region")["product"].size().sort_values(ascending=False)

# How many returned orders does each region have?
regional_returned_count = returns_df.groupby("region")["product"].size().sort_values(ascending=False)

# What is the return rate per region?
regional_return_rate = (regional_returned_count / regional_order_count * 100).fillna(0).sort_values(ascending=False)

#print(regional_order_count)
#print(regional_returned_count)
#print(regional_return_rate)

# What percentage does each region take up in total returned orders?
regional_returned_revenue_percentage = round(regional_returns_revenue / total_returned_revenue["total_returned_revenue"].iloc[0] * 100, 2).sort_values(ascending=False)

#print(regional_returned_revenue_percentage)


"""
FINDINGS:
1. Southeast has the most total orders, North Florida has the least.
2. South Florida and Southeast are tied for most total returned orders, North Florida has the least.
3. Southwest is the proportionately worst-performing region due to it having an 8.75% return rate despite having only been returned 7 times
4. South Florida is the region accounting for most of the total revenue of returned orders
5. North Florida is the proportionately best-performing region due to it having a 1.3% return rate while having 73 total orders and only 1 return
"""

#-------------------------
# Customer Segment Return Analysis
#-------------------------

# Which segment places the most orders?
total_segment_orders = df.groupby("customer_segment")["product"].size().sort_values(ascending=False)

# Enterprise places the most orders
#print(total_segment_orders)


# Which segment generates the most returns?
total_segment_returns = returns_df.groupby("customer_segment")["product"].size().sort_values(ascending=False)

# Enterprise generates the most returns (very closely followed by Education)
#print(total_segment_returns)


# Which segment has the highest return rate?
segment_return_rate = (total_segment_returns / total_segment_orders * 100).fillna(0).sort_values(ascending=False)

# Education has the highest return rate (very closely followed by Enterprise)
#print(segment_return_rate)


# Which segment contributes most to returned revenue?
segment_return_revenue = returns_df.groupby("customer_segment")["revenue"].sum().sort_values(ascending=False)

# Consumer contributes most to returned revenue
#print(segment_return_revenue)


# Which customer segment is most profitable on average?
avg_segment_profit_margin = df.groupby("customer_segment")["profit_margin_pct"].mean().sort_values(ascending=False)

# Small Business is most profitable on average
#print(avg_segment_profit_margin)


"""
FINDINGS:
1. Enterprise places the most orders
2. Enterprise generates the most returned orders, though is very closely followed by Education
3. Education has the highest return rate, though is very closely followed by Enterprise despite Enterprise's higher total return count
4. Consumer contributes most to returned revenue despite Enterprise and Education both having more total returns
5. Small Business is the most profitable on average, though is very closely followed by Consumer, despite generating the least amount of revenue.
6. Enterprise is the least profitable on average despite it having the most orders.
"""

#-------------------------
# Product + Segment Analysis
#-------------------------

# How many total orders exist for each segment-product combination?
total_segment_orders_count = df.groupby(["customer_segment", "product"]).size().reset_index(name="order_count").sort_values(by=["customer_segment", "order_count"], ascending=[True, False])

print(total_segment_orders_count)


# How many returned orders exist for each segment-product combination?
total_segment_orders_returns_count = returns_df.groupby(["customer_segment", "product"]).size().reset_index(name="order_count").sort_values(by=["customer_segment", "order_count"], ascending=[True, False])

print(total_segment_orders_returns_count)


# Return Rate calculations per product per customer segment
merged_segment_order_count_df = pd.merge(total_segment_orders_count, total_segment_orders_returns_count, how="left", on=["customer_segment", "product"], suffixes=("_total", "_return")).fillna(0)

merged_segment_order_count_df["return_rate"] = (
    merged_segment_order_count_df["order_count_return"] /
    merged_segment_order_count_df["order_count_total"]
    * 100
)

final_segment_product_return_rates = merged_segment_order_count_df.sort_values(
    by=["customer_segment", "return_rate"],
    ascending=[True, False]
)

print(final_segment_product_return_rates.to_string())

"""
FINDINGS:
1. Consumer has the highest amount of Mouse orders respective to its segment
2. Education has ordered Keyboard, Monitor, and Mouse tied as the most ordered respective to its segment
3. Enterprise has the highest amount of Laptop orders closely followed by Mouse orders respective to its segment
4. Small Business has the highest amount of Keyboard orders closely followed by Mouse orders respective to its segment
5. Consumer has Laptop, Monitor, Mouse, and Webcam tied at the top for most returned orders respective to its segment
6. Education has Keyboard as the most returned product respective to its segment
7. Enterprise has Keyboard and Monitor tied to the top closely followed by Mouse for most returned orders respective to its segment
8. Small Business has Monitor closely followed by Keyboard as the most returned product respective to its segment
9. Webcam has the highest return rate for Consumer (13%) and Education (18%).
10. Monitor has the highest return rate for Enterprise (11%) and Small Business (14%).
11. Webcam and Monitor are both the proportionally worst-performing products across customer segments with Webcam taking the edge due to Webcam taking up two of the highest return rates despite being ordered less than Monitor across all customer segments
12. Docking Station is the proportionally best-performing product due to its 0% return rate across all customer segments despite existing orders, though it is still amongst one of the least ordered across all customer segments
13. Headphones is the proportionally second best-performing product due to its very low return rate across most customer segments and moderate total orders, being more practically successful than Docking Station due to higher total orders across most customer segments
"""
