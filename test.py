import math
import random

def txtplot(nums):
    prec = 30
    width = len(nums)
    height = max(nums)
    scale = round(height/prec, 0-math.floor(math.log10(height/prec)))
    print(width, height, scale)
    print("plot:")
    for i in range(prec*2):
        line = "`"
        for num in nums:
            if num > (scale*(prec*2-i)):
                line += "X  "
            else:
                line += "   "
        if line.strip() != "`": print(line)
    

# Define team sizes and simulation count
team_size = 16
simulations = 10000

# Initialize variables for statistics
winners_list = []

# Function for weighted random choice with square scaling
def weighted_choice(team1_count, team2_count):
    # Define base probabilities (adjust as needed)
    base_prob1 = 0.5
    base_prob2 = 0.5

    # Calculate scaled probabilities with square of remaining members
    prob1 = base_prob1 * (team1_count**2 / (team1_count**2 + team2_count**2))
    prob2 = base_prob2 * (team2_count**2 / (team1_count**2 + team2_count**2))

    # Choose winner based on weighted probabilities
    return random.choices([1, 2], weights=[prob1, prob2])[0]

# Run simulations and collect data
for _ in range(simulations):
    team1 = [True] * team_size  # True represents a living member
    team2 = [True] * team_size
    team1_survivors = list(range(team_size))  # Track indices of alive members
    team2_survivors = list(range(team_size))

    while team1_survivors and team2_survivors:
        # Shuffle the trackers for random matchups
        random.shuffle(team1_survivors)
        random.shuffle(team2_survivors)

        for i in [0]:
            member1_index = team1_survivors[i]
            member2_index = team2_survivors[i]

            # Determine a winner using weighted random choice
            winner = weighted_choice(len(team1_survivors), len(team2_survivors))
            if winner == 1:
                team2_survivors.remove(member2_index)
                team2[member2_index] = False
            else:
                team1_survivors.remove(member1_index)
                team1[member1_index] = False

    # Add survivor count of the winning team to list
    if team1.count(True) > 0:
        winners_list.append(team1.count(True))
    else:
        winners_list.append(team2.count(True))

# Calculate statistics
winners_avg = sum(winners_list) / len(winners_list)
winners_std = round(
    (sum((winners - winners_avg) ** 2 for winners in winners_list))
    / (len(winners_list) - 1),
    2,
)

# Print the results
print(
    f"Average surviving members for winning teams after {simulations} simulations: {winners_avg:.2f}"
)
print(f"Standard deviation of surviving members for winning teams: {winners_std:.2f}")

winner_plot = [0]*(team_size+1)
for winner in winners_list:
    winner_plot[winner] += 1
print(winner_plot)
txtplot(winner_plot)
