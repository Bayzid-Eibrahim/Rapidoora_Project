import pandas as pd
import os

print("--- Developed by CEO Bayzid ---")

# ১. কিছু কাল্পনিক ডেটা তৈরি করা
data = {
    'Product': ['Bike Ride', 'Food Delivery', 'Courier', 'Bike Ride', 'Food Delivery'],
    'Amount_Tk': [120, 350, 60, 150, 420],
    'Driver': ['Rahim', 'Karim', 'Rahim', 'Sujon', 'Karim']
}

# ২. ডেটা ফ্রেমে রূপান্তর (Excel-এর মতো টেবিল)
df = pd.read_csv('sales_data.csv') if os.path.exists('sales_data.csv') else pd.DataFrame(data)

# ৩. অ্যানালাইসিস রিপোর্ট
print("\n[📊 Today's Report]")
total_sales = df['Amount_Tk'].sum()
avg_sales = df['Amount_Tk'].mean()
top_product = df['Product'].mode()[0]

print(f"💰 Total Revenue: {total_sales} Tk")
print(f"📈 Average Order: {avg_sales} Tk")
print(f"🏆 Top Service: {top_product}")

# ৪. নতুন ডেটা সেভ করা (CSV ফাইল হিসেবে)
df.to_csv('sales_data.csv', index=False)
print("\n✅ Data saved to 'sales_data.csv' in your project folder.")
