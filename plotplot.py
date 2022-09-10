from tkinter import W
from matplotlib import pyplot as plt
import numpy as np
import csv

#declaring empty list to append data from csv
x_data = []
y_data = []
x_int = []
y_int = []

#opening file to read and save contents
with open("data.txt", "r") as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #data names
            x_label = row[0]
            y_label = row[1]
            line_count += 1
        else:
            #appending to list
            x_data.append(row[0])
            y_data.append(row[1])
            line_count += 1



plt.scatter(x_data,y_data, color="k", linestyle="--", marker='.', label="All devs")
#axis label
plt.xlabel(x_label)
plt.ylabel(y_label)

#plot title
plt.title("Data plot")


#legend chronological
plt.legend()

#grid 
plt.grid(True)

#prevent padding
plt.tight_layout()


#save
pltname = str(input("What name do you want to save the file as? "))
filenm = pltname + ".png"
plt.savefig(filenm)

#show graph
plt.show()
