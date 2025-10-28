# utils.py

def calculate_bricks(wall_dims, brick_dims):
    """
    Calculates the total number of bricks required for a wall.

    Args:
        wall_dims (dict): {"length": float, "height": float, "width": float}
        brick_dims (dict): {"length": float, "height": float, "width": float}

    Returns:
        int: total bricks required
    """
    wall_volume = wall_dims["length"] * wall_dims["height"] * wall_dims["width"]
    brick_volume = brick_dims["length"] * brick_dims["height"] * brick_dims["width"]

    if brick_volume == 0:
        return 0  # Prevent division by zero
    return int(wall_volume / brick_volume)
