import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Your data
def american_odds_to_implied_probability(moneyline_odds):
    if moneyline_odds > 0:
        probability = 100 / (moneyline_odds + 100)
    elif moneyline_odds < 0:
        probability = -moneyline_odds / (-moneyline_odds + 100)
    else:
        raise ValueError("Moneyline odds should not be zero.")

    return probability

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Your data
point = [25,45,28,32,23,25,18,31,34,45,17,26,22,26,34,37,22,31,29,22,27,35,20,23,40,10,22,34,22,21,20,31,38,30,26,43,27]
usage = [33.0,40.5,28.8,37.4,35.4,38.5,26.4,36.2,31.5,45.1,27.3,36.8,35.2,30.8,31.0,29.6,23.7,33.1,32.8,27.5,30.5,37.7,34.1,31.6,41.1,22.9,29.5,32.3,28.5,30.8,26.7,30.8,34.4,38.4,35.3,36.4,26.6]
true = [60.2,74.3,59.2,55.6,44.6,60.2,45.8,74.7,69.3,63.0,43.0,70.2,59.0,55.0,68.7,63.4,48.3,59.2,63.4,50.1,65.8,62.6,47.2,48.9,69.1,27.3,46.4,78.1,48.3,42.6,41.1,74.7,74.8,60.9,59.7,67.5,63.0]
fga = [19,25,21,27,24,19,17,19,21,39,18,15,16,21,23,27,21,24,22,18,17,24,19,20,25,17,18,20,21,22,23,19,21,22,20,27,21]
fgm = [10,14,11,12,10,9,6,12,11,15,7,8,6,8,14,14,7,12,11,6,9,12,7,7,14,4,4,13,7,7,8,11,13,9,11,15,11]
off_rat = [108.8,153.2,131.4,104.4,83.1,136.0,107.4,152.9,142.6,116,1,95.0,127.1,134.4,109.4,134.1,132.4,137.4,118.3,110.0,117.8,120.2,88.4,118.8,123.9,77.4,105.0,137.6,110.1,93.1,102.1,134.8,139.2,102.9,119.3,119.8,139.3]
print(len(off_rat))
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
for variable in [point, usage, true, fga, fgm, off_rat]:
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

line_odd = [[24.5,-275],[25.5,-225],[26.5,-180],[27.5,-150],[28.5,-125],[29.5,-105],[30.5,115],[31.5,135],[32.5,150]] 



line = 25
odds = 120
implied_prob = american_odds_to_implied_probability(odds)
# Count instances where predicted points are over the line

instances = np.sum(simulated_points >= line)
# Calculate the percentage

# Print the result
median_predicted_points = np.median(simulated_points)
print(f"Median value of predicted points: {median_predicted_points:.2f}")

mean_predicted_points = np.mean(simulated_points)
print(f"Mean value of predicted points: {mean_predicted_points:.2f}")

max_predicted_points = np.max(simulated_points)
print(f"Ceiling value of predicted points: {max_predicted_points:.2f}")

min_predicted_points = np.min(simulated_points)
print(f"Floor value of predicted points: {min_predicted_points:.2f}")

best_edge = 0
best_line = 0
best_odds = 0
best_percentage = 0
for line, odds in line_odd:
    implied_prob = american_odds_to_implied_probability(odds)
    
    instances = np.sum(simulated_points >= line)
    percentage = (instances / num_simulations) * 100
    
    edge = (percentage / 100 - implied_prob) * 100
    
    if edge > best_edge:
        best_edge = edge
        best_line = line
        best_odds = odds
        best_percentage = percentage

if best_edge ==0 & best_line == 0 & best_odds ==0:
    print("No lines are favorable")

else:
    print(f"Best Edge Against Sportsbooks:")
    print(f"Line: {best_line}, Odds: {best_odds}")
    print(f"Edge: {best_edge:.2f}%")
    print(f"Percentage of instances where predicted over best prop: {best_line}: {best_percentage}%")
    print("weights: ", weights)
    


for line, odds in line_odd:
    implied_prob = american_odds_to_implied_probability(odds)
    
    instances = np.sum(simulated_points >= line)
    percentage = (instances / num_simulations) * 100
    
    edge = (percentage / 100 - implied_prob) * 100
    
    print(f"Line: {line}, Odds: {odds}, Edge: {edge:.2f}%")



#Plot the distribution of weights
plt.hist(simulated_points.flatten(), bins=30, color='blue', alpha=0.7)
plt.axvline(x=best_line, color='red', linestyle='--', label='Best Line')
plt.title('Jalen Bunson Season Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
plt.show()