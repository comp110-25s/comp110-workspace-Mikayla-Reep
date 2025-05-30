"""Examples of set and dictionary syntax."""

pids: set[int] = {710000000, 712345678}

pids.add(730120710)

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

for key in ice_cream:
    print(key)

for key in ice_cream:
    print(ice_cream[key])
