
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Your data
point = [22, 15, 24, 28, 22, 28, 10, 17, 18, 26, 12, 23]
usage = [32.4, 30.6, 29.4, 31.9, 26.7, 31.3, 25.9, 29.3, 30.6, 24.3, 23.4, 30.7]
true = [69.8, 43.6, 63.3, 47.2, 62.4, 70.1, 32.9, 45.3, 47.7, 65.0, 46.2, 58.2]
fga = [14, 15, 15, 27, 15, 16, 13, 17, 18, 20, 13, 18]
fgm = [9, 7, 7, 11, 8, 9, 3, 7, 8, 11, 6, 10]
off_rat = [124.1,85.6,112.3,91.5,127.0,123.1,73.0,98.0,89.3,131.7,75.4,122.0]

mean_point = np.mean(point)
std_dev_point = np.std(point)
mean_usage = np.mean(usage)
std_dev_usage = np.std(usage)
mean_true = np.mean(true)
std_dev_true = np.std(true)
mean_fga = np.mean(fga)
std_dev_fga = np.std(fga)
mean_fgm = np.mean(fgm)
std_dev_fgm = np.std(fgm)
mean_off_rat = np.mean(off_rat)
std_off_rat = np.std(off_rat)
# Number of simulations
num_simulations = 10000
actual_range = int(num_simulations/ len(point))
# Arrays to store simulated results
simulated_points = np.zeros((actual_range, len(point)))

# Calculate R-squared values for each variable
r2_values = []
for variable in [true, usage, fgm, fga, point, off_rat]:
    X = np.array(variable).reshape(-1, 1)
    linear_model = LinearRegression()
    linear_model.fit(X, point)
    y_pred = linear_model.predict(X)
    r2_values.append(r2_score(point, y_pred))

# Normalize R-squared values to create custom weights
weights = np.array(r2_values) / np.sum(r2_values)

# Simulate linear regression and prediction for points
for i in range(actual_range):
    # Add some random noise to the true, usage, and point values to simulate variability
    simulated_true = np.array(true) + np.random.normal(mean_true, std_dev_true, len(true))
    simulated_usage = np.array(usage) + np.random.normal(mean_usage, std_dev_usage, len(usage))
    simulated_point = np.array(point) + np.random.normal(mean_point, std_dev_point, len(point))
    simulated_fga = np.array(fga) + np.random.normal(mean_fga, std_dev_fga, len(fga))
    simulated_fgm = np.array(fgm) + np.random.normal(mean_fgm, std_dev_fgm, len(fgm))
    simulated_off_rat = np.array(off_rat) + np.random.normal(mean_off_rat, std_off_rat, len(off_rat))
    # Perform linear regression for points with custom weights
    X = np.array([simulated_true, simulated_usage, simulated_point, simulated_fga, simulated_fgm, simulated_off_rat]).T
    linear_model = LinearRegression()
    
    # Apply custom weights to each variable
    X_weighted = X * weights
    
    # Fit the model and predict points
    linear_model.fit(X_weighted, point)
    simulated_points[i, :] = linear_model.predict(X_weighted)

# Now simulated_points has the shape (num_simulations, len(point))

line = 15
# Count instances where predicted points are over the line

instances = np.sum(simulated_points >= line)
# Calculate the percentage
percentage = (instances / (num_simulations)) * 100

# Print the result
median_predicted_points = np.median(simulated_points)
print(f"Median value of predicted points: {median_predicted_points:.2f}")

mean_predicted_points = np.mean(simulated_points)
print(f"Median value of predicted points: {mean_predicted_points:.2f}")

max_predicted_points = np.max(simulated_points)
print(f"Ceiling value of predicted points: {max_predicted_points:.2f}")

min_predicted_points = np.min(simulated_points)
print(f"Floor value of predicted points: {min_predicted_points:.2f}")

print(f"Percentage of instances where predicted points are over the line: {percentage}%")

print(weights)
# Plot the distribution of weights
plt.hist(simulated_points.flatten(), bins=30, color='blue', alpha=0.7)
plt.title('Collin Sexton Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
plt.show()