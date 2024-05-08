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

point = [22,22,44,62,46,16,26,52,16,34,31,20,24,20,35,10,21,35,20,20,24,26,27,28,34]
usage = [23.4,26.5,44.3,50.1,36.0,17.0,37.9,41.6,21.3,29.8,34.9,28.4,22.1,29.4,30.3,26.5,25.8,32.4,28.0,21.9,27.3,30.3,30.1,37.6,25.9]
true = [64.7,45.2,71.3,72.6,86.7,64.9,46.5,75.6,48.1,70.2,61.8,67.2,62.5,52.6,92.3,29.6,54.7,78.1,51/.4,54.3,50.1,48.6,51.5,38.9,78.7]
fga = [17,23,26,37,23,11,24,30,14,22,22,14,17,19,15,16,17,18,19,14,20,25,24,26,15]
fgm = [9,9,17,22,17,6,9,18,5,14,11,8,9,9,11,4,7,10,9,6,9,11,10,11,9]
off_rat = [135.0,107.2,127.9,136.0,161.8,117.1,106.0,148.2,118.9,155.0,124.5,100.5,126.7,109.3,141.5,82.9,112.8,156.6,105.1,118.5,125.4,111.2,97.8,108.2,165.1]
min =[36,41,36,38,35,41,36,37,38,39,34,34,37,35,37,31,37,37,36,40,36,38,41,37,40]
print(len(point))
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

line_odd = [[23.5,-450],[24.5,-350],[25.5,-275],[26.5,-215],[27.5,-170],[28.5,-140],[29.5,-120],[30.5,-100],[31.5,120],[32.5,140]] 



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
    
#Plot the distribution of weights
plt.hist(simulated_points.flatten(), bins=30, color='blue', alpha=0.7)
plt.axvline(x=best_line, color='red', linestyle='--', label='Best Line')
plt.title('Devin Booker Season Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
plt.show()