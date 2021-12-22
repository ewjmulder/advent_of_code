from src.util import *

instructions = Parser.from_file(INPUT).to_regex_match(f"{WORD} x={NUMBER}..{NUMBER},y={NUMBER}..{NUMBER},z={NUMBER}..{NUMBER}", [str, int, int, int, int, int, int])

cubes = []

for instruction in instructions:
    instruction[0] = True if instruction[0] == "on" else False


cpus = 16
total = len(instructions)
for i, instruction in enumerate(instructions):
    print(f"At instruction {i + 1} of {total}")

    [new_on_off, new_x_from, new_x_to, new_y_from, new_y_to, new_z_from, new_z_to] = instruction
    new_from = (new_x_from, new_y_from, new_z_from)
    new_to = (new_x_to, new_y_to, new_z_to)

    new_cubes = []
    for cube in cubes:
        (cube_from, cube_to) = cube
        (cube_x_from, cube_y_from, cube_z_from) = cube_from
        (cube_x_to, cube_y_to, cube_z_to) = cube_to

        intersection_x_from = max(cube_x_from, new_x_from)
        intersection_x_to = min(cube_x_to, new_x_to)
        intersection_y_from = max(cube_y_from, new_y_from)
        intersection_y_to = min(cube_y_to, new_y_to)
        intersection_z_from = max(cube_z_from, new_z_from)
        intersection_z_to = min(cube_z_to, new_z_to)
        # Optimization check: is there an intersection at all?
        if intersection_x_from == cube_x_from and intersection_x_to == cube_x_to and intersection_y_from == cube_y_from and intersection_y_to == cube_y_to and intersection_z_from == cube_z_from and intersection_z_to == cube_z_to:
            # Full overlap: no sub cubes to add
            pass
        elif intersection_x_from <= intersection_x_to and intersection_y_from <= intersection_y_to and intersection_z_from <= intersection_z_to:
            # Partial overlap: calculate sub cubes
            sub_cubes = []

            # Create 24 possible sub cubes
            # 123 ABC RST
            # 456 DEF UVW
            # 789 GHI XYZ

            # 1
            sub_cubes.append(((cube_x_from, cube_y_from, cube_z_from), (new_x_from - 1, new_y_from - 1, new_z_from - 1)))
            # 2
            sub_cubes.append(((new_x_from, cube_y_from, cube_z_from), (new_x_to, new_y_from - 1, new_z_from - 1)))
            # 3
            sub_cubes.append(((new_x_to + 1, cube_y_from, cube_z_from), (cube_x_to, new_y_from - 1, new_z_from - 1)))

            # A
            sub_cubes.append(((cube_x_from, cube_y_from, new_z_from), (new_x_from - 1, new_y_from - 1, new_z_to)))
            # B
            sub_cubes.append(((new_x_from, cube_y_from, new_z_from), (new_x_to, new_y_from - 1, new_z_to)))
            # C
            sub_cubes.append(((new_x_to + 1, cube_y_from, new_z_from), (cube_x_to, new_y_from - 1, new_z_to)))

            # R
            sub_cubes.append(((cube_x_from, cube_y_from, new_z_to + 1), (new_x_from - 1, new_y_from - 1, cube_z_to)))
            # S
            sub_cubes.append(((new_x_from, cube_y_from, new_z_to + 1), (new_x_to, new_y_from - 1, cube_z_to)))
            # T
            sub_cubes.append(((new_x_to + 1, cube_y_from, new_z_to + 1), (cube_x_to, new_y_from - 1, cube_z_to)))


            # 4
            sub_cubes.append(((cube_x_from, new_y_from, cube_z_from), (new_x_from - 1, new_y_to, new_z_from - 1)))
            # 5 - skip, this is the new one itself
            sub_cubes.append(((new_x_from, new_y_from, cube_z_from), (new_x_to, new_y_to, new_z_from - 1)))
            # 6
            sub_cubes.append(((new_x_to + 1, new_y_from, cube_z_from), (cube_x_to, new_y_to, new_z_from - 1)))

            # D
            sub_cubes.append(((cube_x_from, new_y_from, new_z_from), (new_x_from - 1, new_y_to, new_z_to)))
            # E - skip, this is the new one itself
            # sub_cubes.append(((new_x_from, new_y_from, new_z_from), (new_x_to, new_y_to, new_z_to)))
            # F
            sub_cubes.append(((new_x_to + 1, new_y_from, new_z_from), (cube_x_to, new_y_to, new_z_to)))

            # U
            sub_cubes.append(((cube_x_from, new_y_from, new_z_to + 1), (new_x_from - 1, new_y_to, cube_z_to)))
            # V
            sub_cubes.append(((new_x_from, new_y_from, new_z_to + 1), (new_x_to, new_y_to, cube_z_to)))
            # W
            sub_cubes.append(((new_x_to + 1, new_y_from, new_z_to + 1), (cube_x_to, new_y_to, cube_z_to)))


            # 7
            sub_cubes.append(((cube_x_from, new_y_to + 1, cube_z_from), (new_x_from - 1, cube_y_to, new_z_from - 1)))
            # 8
            sub_cubes.append(((new_x_from, new_y_to + 1, cube_z_from), (new_x_to, cube_y_to, new_z_from - 1)))
            # 9
            sub_cubes.append(((new_x_to + 1, new_y_to + 1, cube_z_from), (cube_x_to, cube_y_to, new_z_from - 1)))

            # G
            sub_cubes.append(((cube_x_from, new_y_to + 1, new_z_from), (new_x_from - 1, cube_y_to, new_z_to)))
            # H
            sub_cubes.append(((new_x_from, new_y_to + 1, new_z_from), (new_x_to, cube_y_to, new_z_to)))
            # I
            sub_cubes.append(((new_x_to + 1, new_y_to + 1, new_z_from), (cube_x_to, cube_y_to, new_z_to)))

            # X
            sub_cubes.append(((cube_x_from, new_y_to + 1, new_z_to + 1), (new_x_from - 1, cube_y_to, cube_z_to)))
            # Y
            sub_cubes.append(((new_x_from, new_y_to + 1, new_z_to + 1), (new_x_to, cube_y_to, cube_z_to)))
            # Z
            sub_cubes.append(((new_x_to + 1, new_y_to + 1, new_z_to + 1), (cube_x_to, cube_y_to, cube_z_to)))

            # For each sub cube: if it intersects with the cube, add it
            for sub_cube in sub_cubes:
                (sub_cube_from, sub_cube_to) = sub_cube
                (sub_cube_x_from, sub_cube_y_from, sub_cube_z_from) = sub_cube_from
                (sub_cube_x_to, sub_cube_y_to, sub_cube_z_to) = sub_cube_to
                intersection_x_from = max(cube_x_from, sub_cube_x_from)
                intersection_x_to = min(cube_x_to, sub_cube_x_to)
                intersection_y_from = max(cube_y_from, sub_cube_y_from)
                intersection_y_to = min(cube_y_to, sub_cube_y_to)
                intersection_z_from = max(cube_z_from, sub_cube_z_from)
                intersection_z_to = min(cube_z_to, sub_cube_z_to)
                if intersection_x_from <= intersection_x_to and intersection_y_from <= intersection_y_to and intersection_z_from <= intersection_z_to:
                    new_cubes.append(((intersection_x_from, intersection_y_from, intersection_z_from), (intersection_x_to, intersection_y_to, intersection_z_to)))
        else:
            # No overlap, just add cube to new_cubes
            new_cubes.append(cube)

    if new_on_off:
        new_cubes.append((new_from, new_to))
    cubes = new_cubes


def calc_volume(c):
    (fx, fy, fz), (tx, ty, tz) = c
    return (tx + 1 - fx) * (ty + 1 - fy) * (tz + 1 - fz)


total_volume = sum(calc_volume(cube) for cube in cubes)
print(total_volume)
