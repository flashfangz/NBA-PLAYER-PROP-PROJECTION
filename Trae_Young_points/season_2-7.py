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

def get_team_avg_points_allowed(team_name):
    if team_name in team_points_allowed:
        return team_points_allowed[team_name]
    else:
        raise ValueError("Team name not found in the data.")
    
def calculate_avg_adjusted_difference(points, team_points_allowed):
    X = np.array(points).reshape(-1, 1)
    y = np.array([team_points_allowed[team] for team in opponent_teams]).reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    avg_adjusted_difference = np.mean(y - y_pred)
    return avg_adjusted_difference

team_points_allowed = {
    'ATL': 24.72, 'BOS': 26.81, 'BKN': 25.58, 'CHA': 24.34, 'CHI': 21.47,
    'CLE': 24.78, 'DAL': 24.18, 'DEN': 24.05, 'DET': 27.20, 'GSW': 25.91,
    'HOU': 24.12, 'IND': 24.85, 'LAC': 23.7, 'LAL': 25.76, 'MEM': 24.36,
    'MIA': 23.32, 'MIL': 26.76, 'MIN': 23.5, 'NOP': 26.26, 'NYK': 22.85,
    'OKC': 23.85, 'ORL': 26.10, 'PHI': 22.59, 'PHX': 25.8, 'POR': 25.97,
    'SAC': 24.40, 'SAS': 27.20, 'TOR': 22.51, 'UTA': 23.82, 'WAS': 24.69
}
opponent_team = "BOS"

# Get the average points allowed by MEM against players of the same position
opp_avg_points_allowed = get_team_avg_points_allowed(opponent_team)
# Your data
point = [25,35,32,26,30,30,15,18,36,21,13,28,31,13,24,40,24,21,30,30,30,31,35,38,35,19,30,32,45,13,33,26,43,38,22,15,27,41,22,22,23,24,20,18,23]
usage = [24.7,24.9,25.3,30.0,31.1,30.7,24.5,28.6,33.4,26.2,32.9,30.6,35.3,33.1,28.0,31.7,26.1,28.0,29.7,30.8,29.4,30.3,33.5,43.7,36.7,32.1,35.3,35.4,38.5,24.0,40.1,26.8,37.8,23.8,25.2,26.0,31.1,43.4,30.0,24.5,26.9,33.6,26.2,31.4,34.1]
true = [75.1,75.4,89.5,62.3,51.2,65.7,62.5,52.7,64.4,45.7,35.5,49.7,56.6,32.2,67.3,73.1,56.9,52.3,55.4,64.3,71.2,69.6,74.0,63.6,59.0,63.0,57.3,55.4,62.4,39.1,55.7,71.0,58.6,92.6,59.8,47.0,56.6,62.7,48.2,62.4,52.4,49.6,55.7,44.1,44.9]
fga = [14,8,21,17,20,24,18,12,14,24,19,17,22,23,18,13,19,18,17,24,22,18,17,21,29,27,12,24,28,29,14,27,17,31,17,14,12,19,27,18,15,18,22,14,16,19]
fgm = [8,12,12,9,9,9,6,5,11,6,4,7,11,4,6,11,7,6,11,10,10,8,11,15,13,5,11,13,15,3,12,9,12,13,5,4,7,12,5,7,7,9,5,4,4]
off_rat = [136.8,139.1,138.4,123.1,112.5,143.0,94.9,98.4,135.1,112.7,78.6,105.9,105.3,78.1,122.6,137.2,118.4,105.9,124.7,117.8,139.6,141.6,131.7,113.1,123.1,115.6,110.6,118.9,136.4,91.1,107.7,150.2,130.0,170.4,127.2,121.2,119.6,131.2,100.2,128.2,118.0,111.9,125.1,94.4,92.4]
opponent_teams = ['LAC', 'GSW', 'PHX', 'LAL', 'TOR', 'DAL', 'CLE', 'ORL', 'SAS', 'WAS', 'IND', 'PHI', 'ORL', 'IND', 'OKC', 'WAS', 'SAC', 'CHI', 'MEM', 'MIA', 'HOU', 'DET', 'CLE', 'TOR', 'TOR', 'DEN', 'BKN', 'MIL', 'SAS', 'CLE', 'BOS', 'WAS', 'BKN', 'IND', 'PHI', 'NYK', 'MIA', 'ORL', 'OKC', 'NOP', 'WAS', 'MIN', 'MIL', 'NYK', 'CHA']
last = 30

point = point[:last]
usage = usage[:last]
true = true[:last]
fga = fga[:last]
fgm = fgm[:last]
off_rat = off_rat[:last]
opponent_teams = opponent_teams[:last]


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
simulated_points = np.zeros(num_simulations)

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
    simulated_points[i * len(point):(i + 1) * len(point)] = linear_model.predict(X_weighted)

# Now simulated_points has the shape (num_simulations, len(point))

line_odd = [[16.5,-557],[17.5,-450],[18.5,-350],[19.5,-275],[20.5,-215],[21.5,-170],[22.5,-140],[23.5,-140],[24.5,-110],[25.5,125],[26.5,145],[27.5,175],[28.5,200],[29.5,240]] 


adjusted_simulated_points = simulated_points + (np.mean(simulated_points) - opp_avg_points_allowed)
#adjusted_simulated_points = simulated_points

# Calculate the percentage

# Print the result
parley_line = 21.5
parley_odd = -170
model_instances = np.sum(adjusted_simulated_points >= parley_line)
model_percentage = (model_instances / num_simulations) * 100
print(f"Chance for line to hit: {model_percentage:.2f}%")
parley_edge = (model_percentage / 100 - american_odds_to_implied_probability(parley_odd)) * 100
print(f"Edge against sportsbook with line: {parley_line}: {parley_edge:.2f}%.")


median_predicted_points = np.median(adjusted_simulated_points)
print(f"Median value of predicted points: {median_predicted_points:.2f}")

mean_predicted_points = np.mean(adjusted_simulated_points)
print(f"Mean value of predicted points: {mean_predicted_points:.2f}")

max_predicted_points = np.max(adjusted_simulated_points)
print(f"Ceiling value of predicted points: {max_predicted_points:.2f}")

min_predicted_points = np.min(adjusted_simulated_points)
print(f"Floor value of predicted points: {min_predicted_points:.2f}")

opp_avg_points_allowed = get_team_avg_points_allowed(opponent_team)

best_edge = 0
best_line = 0
best_odds = 0
best_percentage = 0
for line, odds in line_odd:
    implied_prob = american_odds_to_implied_probability(odds)
    
    instances = np.sum(adjusted_simulated_points >= line)
    percentage = (instances / num_simulations) * 100
    
    edge = (percentage / 100 - implied_prob) * 100
    
    if edge > best_edge:
        best_edge = edge
        best_line = line
        best_odds = odds
        best_percentage = percentage

if best_edge == 0 and best_line == 0 and best_odds == 0:
    print("No lines are have any edges")

else:
    print(f"Best Edge Against Sportsbooks:")
    print(f"Line: {best_line}, Odds: {best_odds}")
    print(f"Edge: {best_edge:.2f}%")
    print(f"Percentage of instances where predicted over best value prop: {best_line}: {best_percentage}%")
    print("weights: ", weights)
    

#Plot the distribution of weights
plt.hist(adjusted_simulated_points.flatten(), bins=30, color='blue', alpha=0.7)
plt.axvline(x=best_line, color='red', linestyle='--', label='Best value Line')
plt.axvline(x=line, color='green', linestyle='--', label='Parley Line')

plt.title('Trae Young Season Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
plt.show()