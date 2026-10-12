"""
Campus Connections (Routes)

Represent the connections between different locations and the distance between them.
Use a dictionary where the keys are locations, and the values are also dictionaries 
representing connected locations and the distance in meters.

Make sure the graph is bidirectional:
if Main Gate connects to CSE Block, CSE Block must also connect to Main Gate with the same distance.

Example format:
ROUTES = {
    "Main Gate": {
        "CSE Block": 120,
        "Canteen": 180,
    },
    "CSE Block": {
        "Main Gate": 120,
        "Library": 80,
        # Add more connections...
    },
    # Add more locations...
}
"""

ROUTES = {
    "Main Gate": {
        "CSE Block": 120,
        "Canteen": 180,
        "Admin Block": 150,
    },
    "CSE Block": {
        "Main Gate": 120,
        "Library": 80,
        "Canteen": 100,
    },
    "Library": {
        "CSE Block": 80,
        "Auditorium": 110,
        "Admin Block": 90,
    },
    "Canteen": {
        "Main Gate": 180,
        "CSE Block": 100,
        "Auditorium": 130,
    },
    "Admin Block": {
        "Main Gate": 150,
        "Library": 90,
    },
    "Auditorium": {
        "Library": 110,
        "Canteen": 130,
    },
}


