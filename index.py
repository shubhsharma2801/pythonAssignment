#flask is used for templating html
from flask import Flask, request, render_template
app = Flask(__name__)

import csv
import datetime
import collections
from collections import Counter
#instance of order to store data
class Order:
    def __init__(self,date,phone,name,amount):
        format_str='%Y-%m-%d';
        self.date = datetime.datetime.strptime(date, format_str)
        self.phone = phone
        self.name=name
        self.amount=amount
    def __init__(self):
        pass
orderList = []
countDictforhtml={}
nameOrderdict ={}
orderCountDict={}
totalOrderAmount=0
#reading of csv file and appending it into list

with open('/Users/shubhamsharma/Documents/node-js-playlist/Assignment/customerdata.txt') as csv_file:
    line_count=0
    for line in csv_file:
        if(line_count == 0):
            header = line.split(',')
            header=[x.strip() for x in header]
            phoneIndex=header.index("Phone");
            amountIndex=header.index("Amount");
            nameIndex=header.index("Name");
            dateIndex=header.index("Date");
            print header
            line_count +=1
        else:
            data=line.split(',')
            ord =  Order()
            ord.phone=data[phoneIndex]
            ord.amount=data[amountIndex]
            ord.name=data[nameIndex]
            ord.date=data[nameIndex]
            orderList.append(ord)
            line_count +=1



#a dictonary to store name and number of time they ordered from the website
for order in orderList:
        if order.name in nameOrderdict:
            i=nameOrderdict[order.name]
            nameOrderdict[order.name]=i+1
        else:
            nameOrderdict[order.name]=1
#a dictonary to store count and set of name of person according to number of time they ordered
for x,y in nameOrderdict.items():
    if(y>=5):
        y='5+'
    if y in orderCountDict:
        nameSet=orderCountDict[y]
        nameSet.add(x)
        orderCountDict[y]=nameSet
    else:
        myset = set()
        myset.add(x)
        orderCountDict[y]=myset

#a new dictonary with order count and name count is to be made because Jinja template does not support len() in html template
for x,y in orderCountDict.items():
    print    x,':',len(y)
    countDictforhtml[x]=len(y)

#flask is used here for routing whenever url is hit it route it to 'homepage.html'
@app.route('/')
def hello_world():
    return render_template('homepage.html',countDictforhtml=countDictforhtml)
print 'Total order recived is ',len(orderList)
print 'Total amount of order recived is ',totalOrderAmount
print 'Name of customer who ordered only once'
for x in orderCountDict[1]:
    print '-',x
print 'Order: Count of customer'
