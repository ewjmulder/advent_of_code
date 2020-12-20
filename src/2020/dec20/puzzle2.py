from src.util import *
from dataclasses import dataclass, field
import math

tiles_data = open(INPUT).read().split("\n\n")

# corners = [2539, 3457, 3613, 1433]  # SAMPLE
# side = 3
# # corners = [2539, 3457, 3613, 1433]  # INPUT
# # side = 12
#
# # corners = [2539, 3457, 3613, 1433]  # INPUT
# # side = 12

tiles = {}
for tile_data in tiles_data:
    tile_lines = [line.strip() for line in parse_string_list_from_string(tile_data)]
    tile_number = int(tile_lines[0][5:9])
    tiles[tile_number] = parse_character_grid_from_lines(tile_lines[1:])

side = int(math.sqrt(len(tiles)))
print(side)
size = list(tiles.values())[0].width
print(size)


pieces = {tile_number: tile.get_all_orientations() for tile_number, tile in tiles.items()}
all_piece_numbers = {piece_number for piece_number in pieces.keys()}

print("pieces:", pieces)

solution = []
for i in range(0, side):
    solution.append([])
    for j in range(0, side):
        solution[i].append(-1)

def calc_matches(match_fun):
    matches = {}
    for piece_number, piece_orientations in pieces.items():
        for piece_orientation in piece_orientations:
            matches[piece_orientation] = set()
            for piece_number_2, piece_orientations_2 in pieces.items():
                if piece_number != piece_number_2:
                    for piece_orientation_2 in piece_orientations_2:
                        if match_fun(piece_orientation, piece_orientation_2):
                            matches[piece_orientation].add((piece_number_2, piece_orientation_2))
    return matches

def match_right_to_left(piece1, piece2):
    return piece1.get_column(piece1.width - 1) == piece2.get_column(0)

def match_bottom_to_top(piece1, piece2):
    return piece1.get_row(piece1.height - 1) == piece2.get_row(0)

matches_right_to_left = calc_matches(match_right_to_left)
matches_bottom_to_top = calc_matches(match_bottom_to_top)


def solve(piece_numbers_left, agg_solution: List[List], sol_col: int, sol_row: int):
    if len(piece_numbers_left) == 0:
        return agg_solution
    matches = []
    if sol_row == 0 and sol_col == 0:
        matches = [(piece_number, piece_orientation)
                   for piece_number in piece_numbers_left
                   for piece_orientation in pieces[piece_number]]
    elif sol_row == 0:
        matches = [(piece_number, piece_orientation) for piece_number, piece_orientation
                   in matches_bottom_to_top[agg_solution[sol_col - 1][sol_row]] if piece_number in piece_numbers_left]
    else:
        matches = [(piece_number, piece_orientation) for piece_number, piece_orientation
                   in matches_right_to_left[agg_solution[sol_col][sol_row - 1]] if piece_number in piece_numbers_left]

    for piece_number, piece_orientation in matches:
        agg_solution[sol_col][sol_row] = piece_orientation
        piece_numbers_left.remove(piece_number)
        new_sol_col = sol_col
        new_sol_row = sol_row + 1
        if new_sol_row == side:
            new_sol_col = sol_col + 1
            new_sol_row = 0
        sub_solution = solve(piece_numbers_left, agg_solution, new_sol_col, new_sol_row)
        if sub_solution:
            return sub_solution
        else:
            agg_solution[sol_col][sol_row] = -1
            piece_numbers_left.add(piece_number)
    return False


solution = solve(all_piece_numbers, solution, 0, 0)
print("solution:", solution)
solution_rows = []
for sol_row_num in range(0, side):
    for row_num in range(1, size - 1):
        solution_row = []
        for solution_cell in solution[sol_row_num]:
            solution_row += solution_cell.rows[row_num][1:-1]
        solution_rows.append(solution_row)


solution_grid = Grid[str](solution_rows)
print(solution_grid.rotate_right(1))

monster_lines = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
monster_grid = parse_character_grid_from_lines(parse_string_list_from_string(monster_lines)[1:])
monster_width = monster_grid.width
monster_height = monster_grid.height
solution_orientations = solution_grid.get_all_orientations()
solution_monsters = {}
solution_monster_coordinates = {}
for solution_orientation in solution_orientations:
    solution_monsters[solution_orientation] = 0
    solution_monster_coordinates[solution_orientation] = set()
    for row_num in range(0, solution_orientation.height):
        for col_num in range(0, solution_orientation.width):
            if row_num < solution_orientation.height - monster_height and col_num < solution_orientation.width - monster_width:
                possible_monster_rows = [[], [], []]
                for j in range(0, monster_height):
                    possible_monster_rows[j] = solution_orientation.rows[row_num + j][col_num:col_num + monster_width]
                monster_match = True
                for mon_row in range(0, monster_height):
                    for mon_col in range(0, monster_width):
                        if monster_grid[mon_row][mon_col] == "#":
                            if possible_monster_rows[mon_row][mon_col] != "#":
                                monster_match = False
                                break
                if monster_match:
                    solution_monsters[solution_orientation] += 1
                    for mon_row in range(0, monster_height):
                        for mon_col in range(0, monster_width):
                            if monster_grid[mon_row][mon_col] == "#":
                                solution_monster_coordinates[solution_orientation].add((row_num + mon_row, col_num + mon_col))

print(solution_monsters.values())
max_monsters = max(solution_monsters.values())
print(max_monsters)
solution_orientation_max_monsters = [solution_orientation for solution_orientation, monsters in solution_monsters.items() if monsters == max_monsters][0]
monster_coordinates = solution_monster_coordinates[solution_orientation_max_monsters]
print(len(monster_coordinates))

print(solution_orientation_max_monsters.count("#") - len(monster_coordinates))
