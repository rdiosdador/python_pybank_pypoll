#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


totalMonths = 0
totalPL = 0
value = 0
change = 0
dates = []
profits = []


# In[3]:


filepath = os.path.join("Resources","budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")


# In[4]:


with open(filepath, newline = "") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)
    
    #print(csv_head)
    
    first_row = next(csvreader)
    
    #print(first_row)
    
    totalMonths = 1
    
    totalPL += int(first_row[1])
    value = int(first_row[1])
    

    for row in csvreader:
        
        totalMonths += 1        
        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
         
        totalPL = totalPL + int(row[1])

   
    greatestIncrease = max(profits)
    greatestIndex = profits.index(greatestIncrease)
    greatestDate = dates[greatestIndex]

     
    greatestDecrease = min(profits)
    worstIndex = profits.index(greatestDecrease)
    worstDate = dates[worstIndex]

   
    avgChange = sum(profits)/len(profits)
    
    
    #print(profits.index(max(profits)))
    #print(profits.index(min(profits)))
    
      


# In[5]:


output = (
    f"Total Months: {totalMonths}\n"
    f"---------------------------------------------------- \n"
    f"Total P & L: {totalPL:,.2f}\n"
    f"Average P & L Change: ${avgChange:,.2f}\n"
    f"Greatest increase in P & L: {greatestDate} (${greatestIncrease:,.2f})\n"
    f"Greatest decrease in P & L: {worstDate} (${greatestDecrease:,.2f})\n"
)

print(output)
         


# In[6]:


with open(pathout, "w") as txt_file:
    txt_file.write(output)

