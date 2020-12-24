# Program : Bitcoin Forecasting
# Based on data from 01/2011 to 12/2020
# Used only data at 1st and 16th date in each year because large amounts of data will slow the program running
# range of forecasting year should be between 2021-2030
import datetime
from forex_python.bitcoin import BtcConverter
print("---------- Bitcoin Forecasting Program ----------")
print("Please wait a minute...")
list_year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
list_x = []
list_y = []
dic_month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
b = BtcConverter()
month = 0
sum_xx = 0
sum_xy = 0
sum_x = 0
sum_y = 0
n = 0
for y in range(len(list_year)):
    for m in range(12):
        month += 1
        date_obj = datetime.datetime(list_year[y], m+1, 1, 18, 36, 28, 151012)
        list_y.append(b.get_previous_price('THB', date_obj))
        list_x.append(month)
for i in range(len(list_x)):
    sum_xy += list_x[i]*list_y[i]
    sum_x += list_x[i]
    sum_y += list_y[i]
    sum_xx += list_x[i]*list_x[i]
    n += 1
mean_x = sum_x / (i + 1)
mean_y = sum_y / (i + 1)
b_1 = (sum_xy-(sum_x*sum_y/n)) / (sum_xx-(n*mean_x*mean_x))
b_0 = mean_y - b_1*mean_x
m_bool = False
y_bool = False
while m_bool is False:
    rg_month = int(input("Please Select The Number of Month (1-12) : "))
    if 1 <= rg_month <= 12:
        m_bool = True
    else:
        print("----- Please enter a number between 1 and 12 ! -----")
        m_bool = False

while y_bool is False:
    rg_year = int(input("Please Enter The year that you want to Forecast (>= 2021) : "))
    if 2021 <= rg_year <= 2030:
        y_bool = True
    else:
        print("----- Please enter a year between 2021 and 2030 ! -----")
        y_bool = False
x = 120 + (rg_year - 2021)*12 + rg_month
y = b_0 + b_1 * x
print("Bitcoin Value at", dic_month[rg_month], rg_year, "is",  '%.2f' % y, "THB")

