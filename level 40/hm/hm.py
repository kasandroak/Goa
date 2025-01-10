#CODEWARS!!!!

def bumps(road):
    # Count the number of bumps in the road
    bumps_count = road.count('n')
    
    # Check if the number of bumps is 15 or less
    if bumps_count <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"

# Example usage
print(bumps("n"))  # Output: "Woohoo!"
print(bumps("__nn_nnnn__n_n___n____nn__nnn"))  # Output: "Woohoo!"
print(bumps("nnn_n__n_n___nnnnn___n__nnn__"))  # Output: "Woohoo!"
print(bumps("_nnnnnnn_n__n______nn__nn_nnn"))  # Output: "Car Dead"
print(bumps("______n___n_"))  # Output: "Woohoo!"
print(bumps("nnnnnnnnnnnnnnnnnnnnn"))  # Output: "Car Dead"
