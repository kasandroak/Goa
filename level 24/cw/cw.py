# Input: Get the number of wins and ties from the user
wins = input("Enter the number of wins: ")
ties = input("Enter the number of ties: ")

# Convert inputs to float
wins = float(wins)
ties = float(ties)

# Calculate points
points = wins * 1 + ties * 0.5

# Output the points earned
print("Points earned by the player:", points)

