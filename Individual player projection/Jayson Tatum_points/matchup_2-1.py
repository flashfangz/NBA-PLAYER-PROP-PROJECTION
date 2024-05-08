import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Your data
point = [25,30,44,34,37,14,30,41,27]
usage = [22.7,35.9,36.1,38.3,36.9,21.6,28.8,33.2,27.2]
true = [60.3,49.5,65.9,70.2,63.6,50.0,72.7,77.1,69.9]
fga = [15,25,29,22,26,14,18,20,18]
fgm = [6,8,15,13,13,6,12,12,10]
off_rat = [137.2,94.1,125.6,108.5,136.6,118.4,118.6,147.0,156.4]
min = [41,47,44,34,34,28,40,37,29]

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
mean_min = np.mean(min)
std_min = np.std(min)

# Number of simulations
num_simulations = 10000
actual_range = int(num_simulations/ len(point))
# Arrays to store simulated results
simulated_points = np.zeros((actual_range, len(point)))

# Calculate R-squared values for each variable
r2_values = []
for variable in [point, usage, true, fga, fgm, off_rat, min]:
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
    simulated_min = np.array(min) + np.random.normal(mean_min, std_min,len(min))
    # Perform linear regression for points with custom weights
    X = np.array([simulated_true, simulated_usage, simulated_point, simulated_fga, simulated_fgm, simulated_off_rat, simulated_min]).T
    linear_model = LinearRegression()
    
    # Apply custom weights to each variable
    X_weighted = X * weights
    
    # Fit the model and predict points
    linear_model.fit(X_weighted, point)
    simulated_points[i, :] = linear_model.predict(X_weighted)

# Now simulated_points has the shape (num_simulations, len(point))

line = 25
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

print(f"Percentage of instances where predicted points are over {line}: {percentage}%")

print("weights: ", weights)

#Plot the distribution of weights
plt.hist(simulated_points.flatten(), bins=30, color='blue', alpha=0.7)
plt.xticks(range(0, 51, 10))
plt.title('Tatum Matchup Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
plt.show()