import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import numpy as np
import yfinance as yf
from datetime import datetime
def ReturnGather(list):
    x = [i for i in range(len(list))]
    y = []
    First = list[0]/100 + 1
    y.append(First)
    for j in range(1, len(list)):
        if j == 1:
            Value = First * (1 + (list[j]/100))
            y.append(Value)
        else:
            Value = y[-1] * (1 + (list[j]/100))
            y.append(Value)
    plt.plot(x, y)
    plt.xlabel("Days")
    plt.ylabel("Relative Change Since the beginning")
    plt.show()
def Average(list):
    Values = []
    for x in range(33):
        Value = 1
        for j in range(len(list[x])):
            Value = (1 + (list[x][j]/100)) * Value
            if j == len(list[x]) - 1:
                Values.append(Value)
    ArrayValues = np.array(Values)
    print((np.mean(ArrayValues) - 1)*100)
def MinimumDrawdownAverage(list):
    Values = []
    for x in range(33):
        Temp = []
        Value = 1
        for j in range(len(list[x])):
            Value = (1 + (list[x][j]/100)) * Value
            Temp.append(Value)
            if j == len(list[x]) - 1:
                Add = min(Temp)
                Values.append(round(Add, 5))
    ArrayValues = np.array(Values)
    print(round((np.mean(ArrayValues) - 1)*100, 5))
# The following two variables are declared to help separate percent changes into 33 different lists for 33 years.
Year = 1990
Counter = 0
Dates = []
# Creates 33 lists for the 33 years.
MegaList = [[] for x in range(33)]
Jan = [[] for x in range(33)]
Feb = [[] for x in range(33)]
Mar = [[] for x in range(33)]
Apr = [[] for x in range(33)]
May = [[] for x in range(33)]
Jun = [[] for x in range(33)]
Jul = [[] for x in range(33)]
Aug = [[] for x in range(33)]
Sep = [[] for x in range(33)]
Oct = [[] for x in range(33)]
Nov = [[] for x in range(33)]
Dec = [[] for x in range(33)]
# next 2 lines assigns variables to the 2 different CSV files containing the data
SPX = pd.read_csv(r"C:\Users\ashis\PycharmProjects\MonthlyYearlyReturn\^SPX.csv")
Vix = pd.read_csv(r"C:\Users\ashis\PycharmProjects\MonthlyYearlyReturn\^VIX.csv")
PercentChanges = []
for x in range(8314):
    j = SPX.iloc[x, 1]
    i = SPX.iloc[x+1, 1]
    PercentChange = ((i/j) - 1) * 100
    PercentChanges.append(round(PercentChange, 3))
DecimalPercentChanges = [round(value/100, 6) for value in PercentChanges]
PercentChanges.insert(0, 1.78)
for x in range(8315):
    Date = SPX.iloc[x, 0]
    CalendarDate = datetime.strptime(Date, '%Y-%m-%d')
    Dates.append(CalendarDate)
for x in range(8315):
    yearofchange = Dates[x].year
    if Year == yearofchange:
        MegaList[Counter].append(PercentChanges[x])
    else:
        Year += 1
        Counter += 1
        MegaList[Counter].append(PercentChanges[x])
for x in range(8315):
    YearCounter = Dates[x].year - 1990
    Month = Dates[x].month
    if Month == 1:
        Jan[YearCounter].append(PercentChanges[x])
    elif Month == 2:
        Feb[YearCounter].append(PercentChanges[x])
    elif Month == 3:
        Mar[YearCounter].append(PercentChanges[x])
    elif Month == 4:
        Apr[YearCounter].append(PercentChanges[x])
    elif Month == 5:
        May[YearCounter].append(PercentChanges[x])
    elif Month == 6:
        Jun[YearCounter].append(PercentChanges[x])
    elif Month == 7:
        Jul[YearCounter].append(PercentChanges[x])
    elif Month == 8:
        Aug[YearCounter].append(PercentChanges[x])
    elif Month == 9:
        Sep[YearCounter].append(PercentChanges[x])
    elif Month == 10:
        Oct[YearCounter].append(PercentChanges[x])
    elif Month == 11:
        Nov[YearCounter].append(PercentChanges[x])
    elif Month == 12:
        Dec[YearCounter].append(PercentChanges[x])
MinimumDrawdownAverage(Jan)
MinimumDrawdownAverage(Feb)
MinimumDrawdownAverage(Mar)
MinimumDrawdownAverage(Apr)
MinimumDrawdownAverage(May)
MinimumDrawdownAverage(Jun)
MinimumDrawdownAverage(Jul)
MinimumDrawdownAverage(Aug)
MinimumDrawdownAverage(Sep)
MinimumDrawdownAverage(Oct)
MinimumDrawdownAverage(Nov)
MinimumDrawdownAverage(Dec)
'''
This part is hashed out for the moment to decrease time needed to run the program
# The following 8 lines gather the 33 years worth of close data in SPX and VIX
start_date = '1990-01-01'
end_date = '2023-01-01'
ticker = '^SPX'
Spx = yf.download(ticker, start_date, end_date)['Close']
Spx.to_csv(f"{ticker}.csv")
ticker2 = '^VIX'
Vix = yf.download(ticker2, start_date, end_date)['Close']
Vix.to_csv(f"{ticker2}.csv")
HistoricalVol = []
for y in range(8295):
    Changes = []
    for z in range(20):
        g = SPX.iloc[z+y, 1]
        k = SPX.iloc[z+y+1, 1]
        LogChange = math.log(k/g) * 100
        Changes.append(LogChange)
    StandardDeviation = statistics.stdev(Changes)
    HVOL = math.sqrt(252) * StandardDeviation
    HistoricalVol.append(round(HVOL, 3))
VIXList = []
NewHVOL = []
for i in range(8295):
    j = Vix.iloc[i, 1]
    k = HistoricalVol[i]
    if j > 0:
        VIXList.append(round(j, 3))
        NewHVOL.append(HistoricalVol[i])
matrix = np.corrcoef(VIXList, NewHVOL)
corr = matrix[0,  1]
print(corr*corr)
a, b = np.polyfit(VIXList, NewHVOL, 1)
ArrayVix = np.array(VIXList)
# The following lines are there to plot the line of best fit and the scatter plot.
# Labels and title are also provided to the graph by the following lines
plt.plot(ArrayVix, (a*ArrayVix) + b, color="red")
plt.scatter(VIXList, NewHVOL, c=np.random.rand(1, len(NewHVOL)))
plt.title("20 Day Realized Volatility SPX vs. VIX from 1/2/1990 to 12/1/2022")
plt.xlabel("VIX")
plt.ylabel("20 Day Realized Volatility SPX")
plt.show()'''
