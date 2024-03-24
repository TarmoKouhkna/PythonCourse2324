# Create a dictionary describing you in as much detail as possible.
# Make sure to start from basic key:
# value pairs and go to deep nesting
# where value would be at least a list of dictionaries.

Mina = {
    "name": "Tarmo",
    "age": 57,

    "details": {
        "city": "Tallinn",
        "education": "Helsinki School of Economics"
    },

    "hobbies": ["cycling", "xc skiing", "music"],

    "favorites in music": {
        "Rock": ["AC/DC", "ZZ Top", "Muse"],
        "Jazz": {"Contemporary": ["Gregory Porter", "Allen Toussaint"]},
        "Classical": {"Composers": ["Mozart", "Max Richter", "Arvo Pärt"]}
    },

    "family and pets": [
        {"wife": "Speli", "married": "37 years"},
        {"daughter": "Liisi", "age": "36 years"},
        {"daughter": "Anna", "age": "31 years"},
        {"cat": "Tiiger", "age": "5"}
    ]
}
print(Mina)
