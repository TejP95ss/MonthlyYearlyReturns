import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import numpy as np
import yfinance as yf
from datetime import datetime
import scipy
def RelativeReturnCharter(list):
    x = [i+1 for i in range(len(list))]
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
def LongTimePeriodEndingAverage(list):
    Values = []
    for x in range(len(list)):
        Value = 1
        for i, j in enumerate(list[x]):
            Value = (1 + (j/100)) * Value
            if i == len(list[x]) - 1:
                Values.append(Value)
    ArrayValues = np.array(Values)
    print((np.mean(ArrayValues) - 1)*100)

def AverageMonthChart(list):
    XValueList = []
    for x in range(len(list)):
        XValueList.append(len(list[x]))
    BigList = [[] for l in range(max(XValueList))]
    for x in range(len(list)):
        for a in range(len(list[x])):
            CurrentValue = list[x][a]
            BigList[a].append(CurrentValue)
    xvalues = [s + 1 for s in range(max(XValueList))]
    y = []
    for g in BigList:
        if len(g) == 0:
            continue
        p = np.mean(g)
        ActualValue = (p/100) + 1
        y.append(round(ActualValue, 4))
    plt.plot(xvalues, y)
    plt.xlabel("Days")
    plt.ylabel("Relative Change Since the beginning")
    plt.title("Average Relative Change During the Month over the past 33 years.")
    plt.show()
# def AverageYearlyChart(list):
#     XValueList = [p+1 for p in range(253)]
#     BigList = [[] for q in range(254)]
#     for x in range(33):
#         for a in range(len(list[x])):
#             CurrentValue = list[x][a]
#             BigList[a].append(CurrentValue)
#     y = []
#     for g in BigList:
#         if len(g) == 0:
#             continue
#         p = np.mean(g)
#         ActualValue = (p/100) + 1
#         y.append(round(ActualValue, 4))
#     NewY = y[:-1]
#     plt.plot(XValueList, NewY)
#     plt.xlabel("Days")
#     plt.ylabel("Relative Change Since the beginning")
#     plt.title("Average Relative Change During the Month over the past 33 years.")
#     plt.show()

def FiveNumberSummary(list):
    Values = []
    for x in range(len(list)):
        for j in range(len(list[x])):
            Value = list[x][j]
            Values.append(Value)
    ArrayValues = np.array(Values)
    Percentiles = np.percentile(ArrayValues, [25, 50, 75])
    Min = min(ArrayValues)
    Max = max(ArrayValues)
    print(f'Min = {Min}')
    print(f'Q1 = {Percentiles[0]}')
    print(f'Med = {Percentiles[1]}')
    print(f'Q3 = {Percentiles[2]}')
    print(f'Max = {Max}')
    print(f'Mean = {round(np.mean(ArrayValues), 5)}')
    print(f'Standard Deviation = {round(np.std(ArrayValues), 5)}')
    plt.hist(ArrayValues, 50, rwidth=.95, color='skyblue')
    plt.xlabel("Daily Percent Changes")
    plt.ylabel("Frequency")
    plt.show()

def DailyAbsoluteAverage(list):
    Values = []
    for x in range(len(list)):
        Temp = []
        for j in range(len(list[x])):
            Value = list[x][j]
            Temp.append(Value)
            if j == len(list[x]) - 1:
                Absolute = [abs(Number) for Number in Temp]
                AverageofAbsolute = np.mean(Absolute)
                Values.append(AverageofAbsolute)
    ArrayValues = np.array(Values)
    print(round(np.mean(ArrayValues), 10))

def MinimumDrawdownAverage(list):
    Values = []
    for x in range(len(list)):
        Temp = []
        Value = 1
        for j in range(len(list[x])):
            Value = (1 + (list[x][j]/100)) * Value
            Temp.append(Value)
            if j == len(list[x]) - 1:
                Add = min(Temp)
                Values.append(round(Add, 5))
    ArrayValues = np.array(Values)
    print((ArrayValues - 1) * 100)
    print(round((np.mean(ArrayValues) - 1)*100, 5))

def MaximumSurgeAverage(list):
    Values = []
    for x in range(len(list)):
        Temp = []
        Value = 1
        for j in range(len(list[x])):
            Value = (1 + (list[x][j]/100)) * Value
            Temp.append(Value)
            if j == len(list[x]) - 1:
                Add = max(Temp)
                Values.append(round(Add, 5))
    ArrayValues = np.array(Values)
    print(round((np.mean(ArrayValues) - 1)*100, 5))

# def VIXSPXChangesCorrelation(VIXlist, SPXlist):
#     slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(VIXlist, SPXlist)
#     print(r_value**2)
#     ArrayVix = np.array(VIXlist)
#     # The following lines are there to plot the line of best fit and the scatter plot.
#     # Labels and title are also provided to the graph by the following lines
#     plt.plot(ArrayVix, (slope * ArrayVix) + intercept, color="red")
#     plt.scatter(VIXlist, SPXlist, c=np.random.rand(1, len(VIXlist)))
#     plt.title("SPX Daily percent changes vs. VIX percent changes from 1/2/1990 to 12/1/2022")
#     plt.xlabel("VIX % changes")
#     plt.ylabel("SPX % changes")
#     plt.show()

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
Buy = [[] for x in range(32)]
Sell = [[] for x in range(33)]
Q1 = [[] for x in range(33)]
Q2 = [[] for x in range(33)]
Q3 = [[] for x in range(33)]
Q4 = [[] for x in range(33)]
Mon = [[] for x in range(33)]
Tue = [[] for x in range(33)]
Wed = [[] for x in range(33)]
Thu = [[] for x in range(33)]
Fri = [[] for x in range(33)]
# next 2 lines assigns variables to the 2 different CSV files containing the data
SPX = pd.read_csv(r"C:\Users\ashis\PycharmProjects\MonthlyYearlyReturn\^SPX.csv")
VIX = pd.read_csv(r"C:\Users\ashis\PycharmProjects\MonthlyYearlyReturn\^VIX.csv")
PercentChanges = []
VIXPercentChanges = []
for x in range(8314):
    j = SPX.iloc[x, 1]
    i = SPX.iloc[x+1, 1]
    PercentChange = ((i/j) - 1) * 100
    PercentChanges.append(round(PercentChange, 3))
DecimalPercentChanges = [round(value/100, 6) for value in PercentChanges]
PercentChanges.insert(0, 1.78)
for x in range(8314):
    j = VIX.iloc[x, 1]
    i = VIX.iloc[x+1, 1]
    VIXPercentChange = ((i/j) - 1) * 100
    VIXPercentChanges.append(round(VIXPercentChange, 3))
DecimalPercentChanges = [round(value/100, 6) for value in VIXPercentChanges]
VIXPercentChanges.insert(0, -7)
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

# for x in range(8315):
#     if x <= 82 or x >= 8273:
#         continue
#     YearCounter = Dates[x].year - 1990
#     Month = Dates[x].month
#     if 1 <= Month <= 4:
#         Buy[YearCounter - 1].append(PercentChanges[x])
#     elif Month == 11 or Month == 12:
#         Buy[YearCounter].append(PercentChanges[x])
#     elif 5 <= Month <= 10:
#         Sell[YearCounter].append(PercentChanges[x])

# for x in range(8315):
#     YearCounter = Dates[x].year - 1990
#     Month = Dates[x].month
#     if 1 <= Month <= 3:
#         Q1[YearCounter].append(PercentChanges[x])
#     elif 4 <= Month <= 6:
#         Q2[YearCounter].append(PercentChanges[x])
#     elif 7 <= Month <= 9:
#         Q3[YearCounter].append(PercentChanges[x])
#     elif 10 <= Month <= 12:
#         Q4[YearCounter].append(PercentChanges[x])

# for x in range(8315):
#     YearCounter = Dates[x].year - 1990
#     DayofWeek = Dates[x].weekday()
#     if DayofWeek == 0:
#         Mon[YearCounter].append(PercentChanges[x])
#     elif DayofWeek == 1:
#         Tue[YearCounter].append(PercentChanges[x])
#     elif DayofWeek == 2:
#         Wed[YearCounter].append(PercentChanges[x])
#     elif DayofWeek == 3:
#         Thu[YearCounter].append(PercentChanges[x])
#     elif DayofWeek == 4:
#         Fri[YearCounter].append(PercentChanges[x])
