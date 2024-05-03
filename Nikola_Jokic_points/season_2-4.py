
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


def american_odds_to_implied_probability(moneyline_odds):
    if moneyline_odds > 0:
        probability = 100 / (moneyline_odds + 100)
    elif moneyline_odds < 0:
        probability = -moneyline_odds / (-moneyline_odds + 100)
    else:
        raise ValueError("Moneyline odds should not be zero.")

    return probability

# Your data
point = [27,27,26,31,31,42,34,25,25,27,27,4,29,34,13,19,26,26,18,31,31,8,24,26,4,25,23,22,36,21,32,39,38,30,9,18,26,32,36,35,35,28,33,25,27,28,22,29]
usage = [29.4,33.5,32.2,42.3,25.7,30.7,36.4,29.6,29.7,27.7,29.2,9.2,25.5,27.5,18.1,24.0,21.7,25.6,21.9,25.9,30.4,17.9,24.5,25.3,13.7,19.5,40.0,42.2,30.2,31.8,29.6,42.7,37.4,25.0,25.8,30.5,30.4,44.0,37.7,39.5,32.6,28.7,25.3,40.1,25.3,32.1,31.2,31.8]
true = [76.0,46.0,56.4,80.2,78.0,80.3,71.5,57.4,90.1,72.0,94.5,66.7,69.8,89.1,87.4,95.0,105.5,65.3,60.5,80.7,63.7,45.0,64.8,75.2,40.0,77.7,39.5,33.5,63.6,50.9,71.0,62.5,53.0,74.3,56.3,59.2,58.6,54.9,61.0,59.5,66.8,70.1,90.7,52.3,74.2,80.8,66.1,61.0]
fga = [16,25,16,18,19,20,22,20,13,17,9,3,19,16,7,10,11,2,14,17,23,8,15,12,5,13,26,32,23,18,19,29,31,18,8,13,20,23,26,25,24,16,16,23,16,16,14,22]
fgm = [11,10,8,13,13,15,14,11,12,11,8,2,13,13,6,9,11,4,8,12,13,3,8,8,2,9,9,9,13,9,12,17,14,12,4,8,10,8,13,14,15,9,14,11,12,12,8,12]
off_rat = [149.4,101.2,122.5,112.1,164.1,176.4,136.4,123.9,129.3,157.7,135.1,152.7,137.1,156.3,132.8,105.7,173,3,142.5,121.9,172.2,135.3,111.9,161.6,149.8,170.2,93.4,84.7,143.1,116.7,177.9,125.1,113.2,169.8,118.6,114.4,125.6,116.5,132.7,116.3,143.0,160.8,156.8,89.9,151.5,136.8,97.5,133.5]
min = [38,40,37,27,37,36,38,38,33,32,30,25,37,38,28,32,30,39,36,34,38,28,37,30,16,36,34,37,38,35,33,34,42,36,15,28,36,36,38,37,36,33,36,30,35,30,35,36]
print(len(min))
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
line_odd = [[21.5,-285],[22.5,-225],[23.5,-180],[24.5,-140],[25.5,-115],[26.5,105],[27.5,125],[28.5,150],[29.5,185]] 



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
    
    print(f"Line: {line}, Odds: {odds}, Projected chance: --{percentage} Edge: {edge:.2f}%")



#Plot the distribution of weights
plt.hist(simulated_points.flatten(), bins=30, color='blue', alpha=0.7)
plt.axvline(x=best_line, color='red', linestyle='--', label='Best Line')
plt.title('Nikola Jokic Season Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
"""1plt.show()thm-""""""""""""?|}"""
