import pandas as pd

data = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

#here we display the rows and columns of the dataset and the first 5 rows of the dataset
print(data.shape)
print(data.head())
print(data.describe())# this will give us the statistical summary of the dataset
print(data.isnull().sum()) # this will give us the count of null values in each column 
report = data.groupby('Category')['Sales'].sum()
print(report) # this will give us the total sales for each category in the dataset



top_items = data.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(5)
print(top_items)#top 5 products that are sold the most


top_cities = data.groupby('City')['Profit'].sum().sort_values(ascending=False).head(5)
print(top_cities)#top  5 cities that are making the most profit


loss_cities = data.groupby('City')['Profit'].sum().sort_values(ascending=True).head(5)
print(loss_cities)#top 5 cities that are making the least profit or facing losses


ship_count = data['Ship Mode'].value_counts()
print(ship_count)#here we are counting the number of times each shipping mode is used in the dataset 




print("\n Average Profit based on Discount:")
discount_analysis = data.groupby('Discount')['Profit'].mean()
print(discount_analysis)


data['Order Date'] = pd.to_datetime(data['Order Date']) 
data['Month'] = data['Order Date'].dt.month_name()  #highest sales month


print("\ntotal sales by month:")
monthly_sales = data.groupby('Month')['Sales'].sum().sort_values(ascending=False)
print(monthly_sales)


print("\n Customer Segment wise Sales:")
segment_report = data.groupby('Segment')['Sales'].sum()
print(segment_report)


print("\n Order Value  Range:")
print("most expensive order:", data['Sales'].max())
print("cheapest order:", data['Sales'].min())

#(Visualization) ---


import matplotlib.pyplot as plt



# 1. Category based graph 
graph_data = data.groupby('Category')['Sales'].sum()

# 2. Bar Chart 
graph_data.plot(kind='bar', color='skyblue', edgecolor='black')


plt.title('Total Sales by Category') 
plt.xlabel('Category Name')         
plt.ylabel('Total Sales ($)')        
plt.xticks(rotation=0)               


plt.show()


# SALES VS PROFIT chart


dual_data = data.groupby('Category')[['Sales', 'Profit']].sum()


dual_data.plot(kind='bar', figsize=(10, 6))


plt.title('Sales vs Profit: ')
plt.xlabel('Category')
plt.ylabel('Amount ($)')
plt.xticks(rotation=0) 
plt.grid(axis='y', linestyle='--', alpha=0.7) 


plt.show()

# PIE CHART 

print("\n Market Share  Pie Chart")
segment_data = data.groupby('Segment')['Sales'].sum()

plt.figure(figsize=(8, 8))
segment_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightskyblue', 'lightcoral'])
plt.title('Market Share')
plt.ylabel('') 
plt.show()