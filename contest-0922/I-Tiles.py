w, h = map(int, input().split())
"""
Whenever a tile has two filled neighbors, there will only be one correct 
orientation to follow the conditions of the problem.
This way, when defining the tiles on the edges of the kitchen, 
the others will only have one orientation option to follow the conditions.
As there are 4 possible positions for each tile, the number of 
possibilities is 4^(w+h), however, only the color of the inner side 
of the tile is relevant to the others, so we only have 2 possibilities 
for that side, which leads us to 2^(w+h)
"""
print((2**(w+h)) % 998244353)
