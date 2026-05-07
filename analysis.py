import pandas as pd
import sqlite3

df = pd.read_excel("data/sales_data.xlsx")

df.columns = df.columns.str.strip().str.lower()
df["returned"] = df["returned"].str.strip().str.lower()

df["order_date"] = pd.to_datetime(df["order_date"], origin="1899-12-30", unit="D")


conn = sqlite3.connect("data/sales_project.db")

df.to_sql("sales", conn, if_exists="replace", index=False)


query = """
SELECT *
FROM sales
WHERE returned = 'yes';
"""

returns_df = pd.read_sql_query(query, conn)

# Which products have the highest returned revenue?
total_product_returns_revenue = returns_df.groupby("product")["revenue"].sum().sort_values(ascending=False)

# Laptops have the highest return revenue
print(total_product_returns_revenue)


# Which regions have the highest returned revenue?
regional_returns_revenue = returns_df.groupby("region")["revenue"].sum().sort_values(ascending=False)

# South Florida has the highest returned revenue
print(regional_returns_revenue)


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
print(avg_returned_data.to_string())
print(avg_retained_data.to_string())


# What percentage of total revenue came from returned orders?
query = """
SELECT SUM(revenue) AS total_revenue
FROM sales
"""

total_revenue = pd.read_sql_query(query, conn)

print(total_revenue)

query = """
SELECT SUM(revenue) AS total_returned_revenue
FROM sales
WHERE returned = 'yes'
"""

total_returned_revenue = pd.read_sql_query(query, conn)

total_returned_revenue_percentage = round(
    total_returned_revenue["total_returned_revenue"].iloc[0] / total_revenue["total_revenue"].iloc[0], 2
) * 100

# 4% of total revenue came from returned orders
print(total_returned_revenue_percentage)


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
