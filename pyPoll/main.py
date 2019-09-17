#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import csv


# In[9]:


filePath = os.path.join("Resources","election_data.csv")
pathOut = os.path.join("Resources","election_data_Analysis.txt")


# In[10]:


numVotes = 0
candidates = []
voteCounts = []


# In[11]:


with open(filePath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    line = next(csvreader)

    for line in csvreader:

        
        numVotes = numVotes + 1

        
        candidate = line[2]

    
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            voteCounts[candidate_index] = voteCounts[candidate_index] + 1
        
        else:
            candidates.append(candidate)
            voteCounts.append(1)


# In[12]:


percentages = []
maxVotes = voteCounts[0]
maxIndex = 0

for count in range(len(candidates)):
    votePercentage = voteCounts[count]/numVotes*100
    percentages.append(votePercentage)
    if voteCounts[count] > maxVotes:
        maxVotes = voteCounts[count]
        print(maxVotes)
        maxIndex = count
winner = candidates[maxIndex]


# In[13]:


output = (
    
    f"Election Results \n"
    f"----------------------------------- \n"
    f"Total Votes: {numVotes:,.2f}\n"
    f"{candidates[0]}: {percentages[0]:.2f}% ({voteCounts[0]:,.2f})\n"
    f"{candidates[1]}: {percentages[1]:.2f}% ({voteCounts[1]:,.2f})\n"
    f"{candidates[2]}: {percentages[2]:.2f}% ({voteCounts[2]:,.2f})\n"
    f"{candidates[3]}: {percentages[3]:.2f}% ({voteCounts[3]:,.2f})\n"
    f"----------------------------------- \n"
    f"Winner: {winner}\n"
    f"----------------------------------- \n"
)

print(output)


# In[14]:


with open(pathOut, "w") as txt_file:
    txt_file.write(output)

