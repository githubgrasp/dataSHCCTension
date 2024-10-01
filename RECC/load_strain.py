import math
import numpy as np


with open("ld.dat", "r") as f:
    data = [line.strip().split() for line in f]


def calculate_value(row):
    x1, x2, x3, x4 = row 
    return (float(x3)-float(x2))/0.8

def extract_stress(row):
    x1, x2, x3, x4 = row 
    return x4



strain_values = [calculate_value(row) for row in data]
load_values = [extract_stress(row) for row in data]

strain_array = np.array(strain_values)  
load_array = np.array(load_values)  
new_values = np.column_stack((strain_array, load_array)) 


with open("ls.dat", "w") as f:
    for value in new_values:
        x1, x2 = value
        f.write(str(x1) + ' '+str(x2)+"\n")
        

