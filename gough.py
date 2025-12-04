from math import pi

# baker's percentages (as decimals)
BAKERS_PCT = {
    "flour": 0.592,   # 59.2%
    "water": 0.367,   # 36.7%
    "yeast": 0.0022,  # 0.22%
    "salt": 0.0148,   # 1.48%
    "sugar": 0.0111,  # 1.11%
    "olive_oil": 0.0185, # 1.85%
}

DOUGH_FACTOR = 2.387  # grams per square inch for "Regular" thickness

def dough_ball_weight(diameter_in_inches: float, factor: float = DOUGH_FACTOR) -> float:
    """Calculate dough ball weight in grams for a given pizza diameter."""
    radius = diameter_in_inches / 2.0
    area = pi * (radius ** 2)
    return area * factor

def ingredient_weights(dough_weight_g: float) -> dict:
    """Return ingredient weights (grams) given a total dough ball weight."""
    return {name: round(dough_weight_g * pct, 1) for name, pct in BAKERS_PCT.items()}

def pretty_print(diameter: float):
    db = dough_ball_weight(diameter)
    ingredients = ingredient_weights(db)
    print(f"\nPizza diameter: {diameter:.0f}\"  →  Dough ball: {db:.0f} g")
    print("Ingredients (g):")
    for name, amt in ingredients.items():
        print(f"  {name:10s}: {amt}")

# Examples
pretty_print(12)
pretty_print(13)
