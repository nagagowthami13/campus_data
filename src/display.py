"""
Output & Display Formatting

Neatly display the chosen route and the total distance to the user in the terminal.

Example output:
    Shortest route:
    Main Gate -> CSE Block -> Library

    Total distance: 200 m
"""


def display_route(route, distance):
    """
    Display the route and distance in a user-friendly format.

    Args:
        route (list): List of location names in order.
        distance (int/float): The total distance of the route.
    """
    if not route:
        print("\nNo route found between the specified locations.")
        return

    print("\nShortest route:")
    print(" -> ".join(route))
    print(f"\nTotal distance: {distance} m")


