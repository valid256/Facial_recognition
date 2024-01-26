import matplotlib.pyplot as plt
import numpy as np

# Create sample data for natural and deepfake images based on the description
np.random.seed(0)

# Parameters for natural images
mean_natural, std_natural = 120, 30  # Higher mean, lower std
natural = np.random.normal(mean_natural, std_natural, 1000)

# Introduce some skewness and bimodality
natural = np.concatenate((natural, np.random.normal(200, std_natural, 1000)))

# Parameters for deepfake images
mean_deepfake, std_deepfake = 100, 40  # Lower mean, higher std
deepfake = np.random.normal(mean_deepfake, std_deepfake, 1000)

# Introduce some skewness and bimodality
deepfake = np.concatenate((deepfake, np.random.normal(180, std_deepfake, 1000)))

# Plotting the histograms
plt.figure(figsize=(10, 6))
plt.hist(natural, bins=30, alpha=0.7, label='Natural Images')
plt.hist(deepfake, bins=30, alpha=0.7, label='Deepfake Images')
plt.title('Histogram of Pixel Values for Natural and Deepfake Images')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
