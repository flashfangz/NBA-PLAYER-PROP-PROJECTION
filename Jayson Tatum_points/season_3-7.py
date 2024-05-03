import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import scrap
import def_point_allowed

# Function to convert American odds to implied probability
def american_odds_to_implied_probability(moneyline_odds):
    if moneyline_odds > 0:
        probability = 100 / (moneyline_odds + 100)
    elif moneyline_odds < 0:
        probability = -moneyline_odds / (-moneyline_odds + 100)
    else:
        raise ValueError("Moneyline odds should not be zero.")
    return probability

# Function to calculate the average points allowed by a specific team against players of the same position
def get_team_avg_points_allowed(team_name):
    if team_name in team_points_allowed:
        return team_points_allowed[team_name]
    else:
        raise ValueError("Team name not found in the data.")
# Data for average points allowed by each team against players of the same position
team_points_allowed = def_point_allowed.team_points_allowed

opponent_team = "HOU"

# Get the average points allowed by MEM against players of the same position


point = scrap.point
true = scrap.true
usage = scrap.usage
fga = scrap.fga
fgm = scrap.fgm
off_rat = scrap.off_rat
min = scrap.min
opponent_teams = scrap.opponent_teams
last = 25

point = point[:last]
usage = usage[:last]
true = true[:last]
fga = fga[:last]
fgm = fgm[:last]
off_rat = off_rat[:last]
min = min[:last]
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

total_points_allowed = sum(team_points_allowed.values())
mean_points_allowed = total_points_allowed / len(team_points_allowed)
adjusted_matchup = 18.26/ mean_points_allowed
simulated_points *= adjusted_matchup

# Calculate adjusted simulated points
#adjusted_simulated_points = simulated_points + (opp_avg_points_allowed - np.mean(simulated_points))
adjusted_simulated_points = simulated_points
# Calculate the chance for the line to hit
parley_line = 24.5
parley_odd = -400
model_instances = np.sum(adjusted_simulated_points >= parley_line) * 100
model_percentage = (model_instances / num_simulations)

print(f"Chance for line to hit: {model_percentage:.2f}%")

# Calculate edge against sportsbook
parley_edge = (model_percentage / 100 - american_odds_to_implied_probability(parley_odd)) * 100
print(f"Edge against sportsbook with line: {parley_line}: {parley_edge:.2f}%.")

# Calculate statistics of predicted points
median_predicted_points = np.median(adjusted_simulated_points)
print(f"Median value of predicted points: {median_predicted_points:.2f}")

mean_predicted_points = np.mean(adjusted_simulated_points)
print(f"Mean value of predicted points: {mean_predicted_points:.2f}")

max_predicted_points = np.max(adjusted_simulated_points)
print(f"Ceiling value of predicted points: {max_predicted_points:.2f}")

min_predicted_points = np.min(adjusted_simulated_points)
print(f"Floor value of predicted points: {min_predicted_points:.2f}")

# Find the best edge against sportsbooks
line_odd = [[23.5,-300],[24.5,-250],[25.5,-200],[26.5,-150],[27.5,-125],[28.5,-105],[29.5,115]] 

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
    print("No lines have any edges")
else:
    print(f"Best Edge Against Sportsbooks:")
    print(f"Line: {best_line}, Odds: {best_odds}")
    print(f"Edge: {best_edge:.2f}%")
    print(f"Percentage of instances where predicted over best value prop: {best_line}: {best_percentage}%")

# Plot the distribution of predicted points
plt.hist(adjusted_simulated_points.flatten(), bins=30, color='blue', alpha=0.7)
plt.axvline(x=best_line, color='red', linestyle='--', label='Best Value Line')
plt.axvline(x=parley_line, color='green', linestyle='--', label='Parley Line')
plt.title('Distribution of Predicted Points')
plt.xlabel('Predicted Points')
plt.ylabel('Frequency')
plt.legend()
plt.show()
