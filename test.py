import numpy as np
import csv

products = []
stock = []
price = []
sales = []

with open("Grocery_Inventory_and_Sales_Dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        products.append(row["Product_Name"])

        stock.append(float(row["Stock_Quantity"]))

        price.append(
            float(
                row["Unit_Price"]
                .replace("$", "")
                .replace(",", "")
                .strip()
            )
        )

        sales.append(float(row["Sales_Volume"]))

products = np.array(products)
stock = np.array(stock)
price = np.array(price)
sales = np.array(sales)

# (1) 每個商品的總庫存價值
inventory_value = stock * price

# (2) 找出最暢銷商品
best_seller = np.argmax(sales)

# (3) 9折後收入
discount_revenue = sales * price * 0.9

with open("Grocery_Result.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Product_Name",
        "Stock_Quantity",
        "Inventory_Value",
        "Sales_Volume",
        "Discount_Revenue",
        "Best_Seller"
    ])

    for i in range(len(products)):
        writer.writerow([
            products[i],
            stock[i],
            inventory_value[i],
            sales[i],
            discount_revenue[i],
            i == best_seller
        ])

print("最暢銷商品：", products[best_seller])
print("銷售量：", sales[best_seller])

print("\n前五筆商品資料：")
for i in range(5):
    print(
        products[i],
        "\n庫存價值=", inventory_value[i],
        "\n9折收入=", discount_revenue[i]

    )