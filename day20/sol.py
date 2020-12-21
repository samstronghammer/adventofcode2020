#!/usr/bin/python3
import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/..")
import util
import math
import parse
from parse import compile
import re

# It was fun to write a script to solve a jigsaw! I'll be updating this script-- it
# needs comments and further optimization. Two major considerations are the assumptions
# that there are no false edges and that the sea monsters don't overlap. Further
# algorithmic complexity would be required to solve these issues.

# Takes in two correctly oriented tiles and returns the vector of the difference in 
# location between them.
def get_tile_vector(tile, neighbor_tile):
    if tile[0] == neighbor_tile[-1]:
        return (0, 1)
    if tile[-1] == neighbor_tile[0]:
        return (0, -1)
    if "".join([line[0] for line in tile]) == "".join([line[-1] for line in neighbor_tile]):
        return (-1, 0)
    if "".join([line[-1] for line in tile]) == "".join([line[0] for line in neighbor_tile]):
        return (1, 0)
    raise Exception("Could not find matching edge between tiles")

# Takes in 
def orient_tile(tile, newtile):
    index_pair = None
    for i, edge in enumerate(get_basic_edges(tile)):
        for j, edge2 in enumerate(get_edges(newtile)):
            if edge == edge2:
                index_pair = (i, j)
                break
        if index_pair:
            break
    # No change
    if index_pair in {(1, 0), (0, 1), (2, 3), (3, 2)}:
        return newtile
    # Mirror over horizontal line
    if index_pair in {(0, 0), (1, 1), (3, 6), (2, 7)}:
        return newtile[::-1]
    rotated_tile = []
    for i in range(len(newtile)):
        rotated_tile.append("".join([x[i] for x in newtile][::-1]))
    return orient_tile(tile, rotated_tile)

def get_edges(tile):
    return [tile[0], tile[-1], \
    "".join([x[0] for x in tile]), \
    "".join([x[-1] for x in tile]), \
    tile[0][::-1], \
    tile[-1][::-1], \
    "".join([x[0] for x in tile[::-1]]), \
    "".join([x[-1] for x in tile[::-1]])]

def get_basic_edges(tile):
    return [tile[0], tile[-1], \
    "".join([x[0] for x in tile]), \
    "".join([x[-1] for x in tile])]

fn = f"{os.path.dirname(__file__)}/in.txt"

l = util.filetolist(fn)
# Append empty string in case input file lacks empty string at the end
l.append("")

p = compile("Tile {:d}:")
tiles = {}
newtileid = None
newtile = []
for line in l:
    r = p.parse(line)
    if r:
        fields = r.fixed
        newtileid = fields[0]
    else:
        if line:
            newtile.append(line)
        else:
            tiles[newtileid] = newtile
            newtile = []

edges = {}
part_1_ans = 1
corner = None
# Iterate over each pair of tiles and if they share an edge, 
for id, tile in tiles.items():
    total = 0
    for id2, tile2 in tiles.items():
        if id != id2 and not set(get_basic_edges(tile)).isdisjoint(get_edges(tile2)):
            if id in edges:
                edges[id].add(id2)
            else:
                edges[id] = {id2}
            total += 1
    if total == 2:
        part_1_ans *= id
        corner = id

print("Part 1 Solution:")
print(part_1_ans)

locs_to_tiles = {(0, 0): corner}
tiles_to_locs = {corner: (0, 0)}
active_tiles = {corner}
done_tiles = set()
fixed_tiles = {corner: tiles[corner]}
while len(active_tiles) > 0:
    active_tile = active_tiles.pop()
    done_tiles.add(active_tile)
    neighbor_ids = edges[active_tile]
    for id in neighbor_ids:
        if not id in done_tiles:
            active_tiles.add(id)
            fixed_tiles[id] = orient_tile(fixed_tiles[active_tile], tiles[id])
            piece_loc = util.vecadd(tiles_to_locs[active_tile], get_tile_vector(fixed_tiles[active_tile], fixed_tiles[id]))
            locs_to_tiles[piece_loc] = id
            tiles_to_locs[id] = piece_loc

supertile = []
minx = min(locs_to_tiles, key=lambda x: x[0])[0]
for y in range(max(locs_to_tiles, key=lambda x: x[1])[1], min(locs_to_tiles, key=lambda x: x[1])[1] - 1, -1):
    rowgroup = []
    for x in range(minx, max(locs_to_tiles, key=lambda x: x[0])[0] + 1):
        if x == minx:
            for r in fixed_tiles[locs_to_tiles[(x, y)]][1:-1]:
                rowgroup.append(r[1:-1])
        else:
            for i, r in enumerate(fixed_tiles[locs_to_tiles[(x, y)]][1:-1]):
                rowgroup[i] += r[1:-1]
    supertile += rowgroup


def is_sea_monster(loc, supertile):
    try:
        l1 = supertile[loc[1]][loc[0]:loc[0]+20]
        l2 = supertile[loc[1] + 1][loc[0]:loc[0]+20]
        l3 = supertile[loc[1] + 2][loc[0]:loc[0]+20]
        return re.match(r"[\.#]{18}#[\.#]", l1) and \
        re.match(r"#[\.#]{4}##[\.#]{4}##[\.#]{4}###", l2) and \
        re.match(r"[\.#]#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#", l3)
    except:
        return False

def count_sea_monsters(supertile):
    total = 0
    for y, line in enumerate(supertile):
        for x in range(len(line)):
            if is_sea_monster((x, y), supertile):
                total += 1
    return total

def orient_and_count_sea_monsters(supertile):
    num_sea_monsters = max(count_sea_monsters(supertile), count_sea_monsters(supertile[::-1]))
    if num_sea_monsters > 0:
        return num_sea_monsters
    rotated_tile = []
    for i in range(len(supertile)):
        rotated_tile.append("".join([line[i] for line in supertile][::-1]))
    return orient_and_count_sea_monsters(rotated_tile)

print("Part 2 Solution")
print(sum([line.count("#") for line in supertile]) - orient_and_count_sea_monsters(supertile) * 15)
