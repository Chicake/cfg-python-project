# read in the spreadsheet
import csv
import statistics

def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

# show sales per months in a list
def month():
    data = read_data()
    sales = []
    for row in data:
        sale = row['sales']
        month = row["month"]
        sales.append(month + ": " + sale)
    print(sales)
month()

# show total sales in 2018
def total():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    print('Total yearly sales: {}'.format(total))
total()

# show profit per months in a list
def profit_month():
    data = read_data()
    monthProfit = []
    for row in data:
        sale = row['sales']
        expenditure = row["expenditure"]
        month = row["month"]
        monthProfit.append(month + ": " + str((int(sale) - int(expenditure))))
    print(monthProfit)
profit_month()

# show total expenditure in 2018
def total_expenditure():
    data = read_data()
    expenditure = []
    for row in data:
        cost = int(row['expenditure'])
        expenditure.append(cost)
    total_expenditure = sum(expenditure)
    print('Total yearly expenditure: {}'.format(total_expenditure))
total_expenditure()

# show total profit for 2018
def total_profit():
    data = read_data()
    profit = []
    for row in data:
        sale = int(row['sales'])
        expenditure = int(row["expenditure"])
        profit.append(sale - expenditure)
    total_profit = sum(profit)
    print('Total yearly profit: {}'.format(total_profit))
total_profit()

# recreating the spreadsheet
field_names = ["year", "months", "sales", "expenditure"]
data = [
    {"year": 2018, "months": "jan", "sales": 6226, "expenditure": 3808},
    {"year": 2018, "months": "feb", "sales": 1521, "expenditure": 3373},
    {"year": 2018, "months": "mar", "sales": 1842, "expenditure": 3965},
    {"year": 2018, "months": "apr", "sales": 2051, "expenditure": 1098},
    {"year": 2018, "months": "may", "sales": 1728, "expenditure": 3046},
    {"year": 2018, "months": "jun", "sales": 2138, "expenditure": 2258},
    {"year": 2018, "months": "jul", "sales": 7479, "expenditure": 2084},
    {"year": 2018, "months": "aug", "sales": 4434, "expenditure": 2799},
    {"year": 2018, "months": "sep", "sales": 3615, "expenditure": 1649},
    {"year": 2018, "months": "oct", "sales": 5472, "expenditure": 1116},
    {"year": 2018, "months": "nov", "sales": 7224, "expenditure": 1431},
    {"year": 2018, "months": "dec", "sales": 1812, "expenditure": 3532}
    ]
with open('recreateSales.csv', 'w', encoding="UTF8", newline="") as csv_file:
        spreadsheet1 = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet1.writeheader()
        spreadsheet1.writerows(data)

# data analysis on glassdoor data using class content

# read in the data
def read_data():
    data = []

    with open('glassdoor gender pay gap.csv', 'r') as paygap_csv:
        spreadsheet = csv.DictReader(paygap_csv)
        for row in spreadsheet:
            data.append(row)
    return data
    spreadsheet.writerows(data)

# calculate the mean of base pay
def glassdoor_mean():
    data2 = read_data()
    average = []
    for row in data2:
        av = int(row["BasePay"])
        average.append(av)
    glassdoor_mean = statistics.mean(average)
    print('Mean base pay: {}'.format(glassdoor_mean))
glassdoor_mean()

# data analysis using external packages

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('glassdoor gender pay gap.csv')

#gap between male and female
total_gap = df.groupby("Gender")["BasePay"].mean()
print(total_gap)

#function for making bargraph
def bargraph(a):
    plt.figure(figsize=(8, 4))
    sns.barplot(x=a, y='BasePay', hue='Gender', data=df, ci=None, palette='Greens')
    plt.legend(loc=[1, 1], title='Gender')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.2)
    plt.show()

#comparing gender average base pay gap for each job title
bargraph("JobTitle")

#comparing gender average base pay gap for performance evaluation score
bargraph("PerfEval")

#comparing gender average base pay gap for seniority
bargraph("Seniority")