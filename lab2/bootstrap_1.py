import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
       
    x = np.random.choice(sample, (iterations,sample_size))
    data_mean = np.mean(x)
    print(data_mean)
    iterations_mean = []
    for i in range(iterations):
        y = x[i, :]
        iterations_mean.append(np.mean(y))
    print(iterations_mean)
    lower, upper = np.percentile(iterations_mean, (2.50, 97.50))
    print(lower, upper)
    return


if __name__ == "__main__":
    sample = np.array([1,2,3,4,5,6,7,8,9,0,12,24,45,67,78,88,22,64])
    boostrap(sample, 10, 5)
    
	


	
