# carbon_sequestration.py

def calculate_carbon(trees_planted, co2_per_tree=21.77):
    """
    Estimate carbon sequestration in kg per year.
    Default CO2 absorption per tree: 21.77 kg/year
    """
    return trees_planted * co2_per_tree

# Example usage
trees = 100
print(f"Estimated CO2 absorbed per year: {calculate_carbon(trees)} kg")
