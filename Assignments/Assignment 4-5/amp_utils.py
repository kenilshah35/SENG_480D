import matplotlib.pyplot as plt
import numpy as np

mean_list = []

def plot_amplitude(q_num, ket_dict, fix_mean = None):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(ket_dict.keys(), height = ket_dict.values(), color = "yellowgreen")
    plt.axhline(y = mean(q_num**2, ket_dict, fix_mean), color='r', linestyle='-')
    
def mean(q_num, ket_dict, fix_mean = None):
    mean = 0 
    total = 0
    
    if fix_mean == True:
        return mean_list[-1]
    else:
        for i in ket_dict.values():
            total += i
        
        mean = total/q_num
        mean_list.append(mean)
        
        return mean
        