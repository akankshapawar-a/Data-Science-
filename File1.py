import numpy as np 

Physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
History = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

Physics = np.array(Physics)
History = np.array(History)

# Calculate means
mean_Physic = np.mean(Physics)
mean_History = np.mean(History)

# Calculate deviations from the mean
Ps_dev = Physics - mean_Physic
Hs_dev = History - mean_History

# Sum of product of deviations
s_dev_pro = np.sum(Ps_dev * Hs_dev)

# Sum of squared deviations
sq_Ps_dev = np.sum(Ps_dev**2)
sq_Hs_dev = np.sum(Hs_dev**2)

# Pearson's correlation coefficient
result = s_dev_pro / np.sqrt(sq_Ps_dev * sq_Hs_dev)

# Print the result to three decimal places
print(f"{result:.3f}")
