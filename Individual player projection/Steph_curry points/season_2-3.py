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
point = [20,37,46,33,25,26,27,15,9,26,30,36,25,13,18,27,30,33,7,37,17,24,34,31,22,26,29,35,16,32,25,38,30,23,34,28,30,21,42,24,41,27]
usage = [28.9,31.9,37.7,34.4,27.2,32.9,33.7,29.7,25.1,38.4,34.8,34.4,33.3,25.2,31.0,29.4,33.6,30.1,25.0,31.7,25.0,33.7,24.5,31.8,26.0,29.7,32.9,34.2,27.0,32.3,26.7,38.3,37.7,29.0,38.6,31.9,26.8,33.1,37.2,28.5,31.5,31.5]
true = [56.3,96.4,63.3,62.4,67.1,63.6,51.5,50.8,27.8,56.6,61.7,72.5,49.1,36.8,42.0,69.9,74.3,71.1,25.4,79.3,45.3,46.6,72.3,67.9,55.7,68.6,60.5,77.3,49.0,83.0,54.9,62.7,54.5,59.9,61.2,75.1,83.0,64.3,83.7,64.4,94.7,58.5]
fga = [17,17,35,26,16,20,24,13,14,19,23,20,25,15,21,18,18,21,12,22,17,24,20,18,18,15,20,20,15,14,21,25,24,17,26,16,15,15,22,16,19,20]
fgm = [6,12,17,13,7,11,8,4,2,7,11,12,9,3,7,11,9,11,2,14,5,8,10,8,7,8,8,11,6,8,8,11,9,6,12,8,9,7,15,6,14,8]
off_rat = [107.1,146.3,114.9,116.1,148.3,109.5,123.9,104.2,76.6,104.5,124.0,145.8,103.6,89.6,86.1,139.4,145.5,131.2,72.1,135.0,111.0,105.0,147.8,123.4,120.9,139.2,116.1,117.4,104.7,131.0,108.3,116.3,104.3,113.6,120.4,108.3,157.2,86.3,157.5,135.7,150.4,117.3]
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

line_odd = [[20.5,-400],[21.5,-325],[22.5,-260],[23.5,-210],[24.5,-180],[25.5,-140],[26.5,-125],[27.5,-105],[28.5,115],[29.5,130],[30.5,160]] 



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

if best_edge == 0 and best_line == 0 and best_odds == 0:
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
plt.title('Steph Curry Season Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
plt.show()