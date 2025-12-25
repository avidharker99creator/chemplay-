# chem_utils.py

# Dictionary of common elements and their molar masses (g/mol)
MOLAR_MASS = {
    "H": 1.008,
    "C": 12.01,
    "O": 16.00,
    "N": 14.01,
    "Na": 22.99,
    "Cl": 35.45,
    "Ca": 40.08
}

def calculate_molar_mass(formula):
    """
    Calculates molar mass of a compound.
    Example: H2O → (2 * H) + (1 * O)
    """
    total_mass = 0
    i = 0

    while i < len(formula):
        element = formula[i]

        # Check if element has two letters (e.g., Na, Cl)
        if i + 1 < len(formula) and formula[i + 1].islower():
            element += formula[i + 1]
            i += 1

        # Check for subscript number
        count = 1
        if i + 1 < len(formula) and formula[i + 1].isdigit():
            count = int(formula[i + 1])
            i += 1

        total_mass += MOLAR_MASS[element] * count
        i += 1

    return total_mass
