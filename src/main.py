"""
Main Application & Input Validation

Tie all modules together to run the campus navigator:
1. Get the list of locations and print them.
2. Ask the user for a source and destination.
3. Validate user input (e.g. check if locations exist, source is not destination).
4. Call find_shortest_route() from navigator.
5. Call display_route() to show the result.
"""

from locations import get_locations
from routes import ROUTES
from navigator import find_shortest_route
from display import display_route


def main():
    print("========================================")
    print("       SVECW CAMPUS NAVIGATOR")
    print("========================================")

    # 1. Get locations from get_locations()
    locations = get_locations()

    # 2. Print available locations
    print("\nAvailable Locations:")
    for location in locations:
        print(f"- {location}")
    print()

    # 3. Ask the user for 'source' and 'destination'
    source_input = input("Enter source: ").strip()
    dest_input = input("Enter destination: ").strip()

    # 4. Add Input Validation
    location_lookup = {loc.lower(): loc for loc in locations}

    if not source_input or source_input.lower() not in location_lookup:
        print(f"\nError: '{source_input}' is not a valid campus location.")
        return

    if not dest_input or dest_input.lower() not in location_lookup:
        print(f"\nError: '{dest_input}' is not a valid campus location.")
        return

    source = location_lookup[source_input.lower()]
    destination = location_lookup[dest_input.lower()]

    # 5. Call find_shortest_route(ROUTES, source, destination)
    route, distance = find_shortest_route(ROUTES, source, destination)

    # 6. Call display_route(route, distance)
    display_route(route, distance)


if __name__ == "__main__":
    main()


