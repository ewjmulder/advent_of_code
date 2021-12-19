from __future__ import annotations

from src.util import *
from typing import List, Set, Tuple, Dict
from dataclasses import dataclass


Beacon = Tuple[int, int, int]
Vector = Tuple[int, int, int]
X = 0
Y = 1
Z = 2


def distance_from_to(coord_from: Beacon, coord_to: Beacon) -> Vector:
    return coord_to[X] - coord_from[X], coord_to[Y] - coord_from[Y], coord_to[Z] - coord_from[Z]


@dataclass
class Scanner:
    number: int
    beacons: List[Beacon]
    beacon_relative_single: List[Tuple[Beacon, List[Vector]]] = None
    beacon_relative_all: Dict[Tuple[Beacon, Transformation], List[Vector]] = None

    def __post_init__(self):
        self.beacon_relative_single = [
            (beacon_from, [distance_from_to(beacon_from, beacon_to) for beacon_to in self.beacons])
            for beacon_from in self.beacons
        ]

        self.beacon_relative_all = {
            (beacon_from, transformation): [distance_from_to(transformation.apply(beacon_from), transformation.apply(beacon_to))
                                            for beacon_to in self.beacons]
            for beacon_from in self.beacons
            for transformation in transformations
        }


@dataclass
class Transformation:
    mapping: Dict[int, Tuple[int, int]]

    def __hash__(self):
        return hash(self.mapping[0][0]) * hash(self.mapping[0][1]) * hash(self.mapping[1][0]) * hash(self.mapping[1][1]) * hash(self.mapping[2][0]) * hash(self.mapping[2][1])

    def reverse(self) -> Transformation:
        new_mapping = {}
        for from_pos, (sign, to_pos) in self.mapping.items():
            new_mapping[to_pos] = (sign, from_pos)
        return Transformation(new_mapping)

    def apply(self, beacon: Beacon) -> Beacon:
        map_x = self.mapping[0]
        new_x = map_x[0] * beacon[map_x[1]]
        map_y = self.mapping[1]
        new_y = map_y[0] * beacon[map_y[1]]
        map_z = self.mapping[2]
        new_z = map_z[0] * beacon[map_z[1]]
        return new_x, new_y, new_z


transformations = [
    Transformation({X: (1, X), Y: (1, Y), Z: (1, Z)}),
    Transformation({X: (1, X), Y: (1, Z), Z: (-1, Y)}),
    Transformation({X: (1, X), Y: (-1, Y), Z: (-1, Z)}),
    Transformation({X: (1, X), Y: (-1, Z), Z: (1, Y)}),
    Transformation({X: (-1, X), Y: (1, Z), Z: (1, Y)}),
    Transformation({X: (-1, X), Y: (1, Y), Z: (-1, Z)}),
    Transformation({X: (-1, X), Y: (-1, Z), Z: (-1, Y)}),
    Transformation({X: (-1, X), Y: (-1, Y), Z: (1, Z)}),
    Transformation({X: (1, Y), Y: (1, Z), Z: (1, X)}),
    Transformation({X: (1, Y), Y: (1, X), Z: (-1, Z)}),
    Transformation({X: (1, Y), Y: (-1, Z), Z: (-1, X)}),
    Transformation({X: (1, Y), Y: (-1, X), Z: (1, Z)}),
    Transformation({X: (-1, Y), Y: (-1, Z), Z: (1, X)}),
    Transformation({X: (-1, Y), Y: (1, X), Z: (1, Z)}),
    Transformation({X: (-1, Y), Y: (-1, X), Z: (-1, Z)}),
    Transformation({X: (-1, Y), Y: (1, Z), Z: (-1, X)}),
    Transformation({X: (1, Z), Y: (-1, X), Z: (-1, Y)}),
    Transformation({X: (1, Z), Y: (-1, Y), Z: (1, X)}),
    Transformation({X: (1, Z), Y: (1, X), Z: (1, Y)}),
    Transformation({X: (1, Z), Y: (1, Y), Z: (-1, X)}),
    Transformation({X: (-1, Z), Y: (1, X), Z: (-1, Y)}),
    Transformation({X: (-1, Z), Y: (1, Y), Z: (1, X)}),
    Transformation({X: (-1, Z), Y: (-1, X), Z: (1, Y)}),
    Transformation({X: (-1, Z), Y: (-1, Y), Z: (-1, X)}),
]


@dataclass
class Match:
    scanner_from: Scanner
    scanner_from_beacon_from: Beacon
    scanner_from_matched_beacon: Beacon
    scanner_to: Scanner
    scanner_to_beacon_from: Beacon
    scanner_to_transformation: Transformation
    scanner_to_matched_beacon: Beacon


def find_match(scanner_from: Scanner, scanner_to: Scanner):
    # TODO: store vestors in set directly?
    matches = 0
    for scanner_from_beacon_from, scanner_from_vectors in scanner_from.beacon_relative_single:
        scanner_from_vectors_set = set(scanner_from_vectors)
        for (scanner_to_beacon_from, scanner_to_transformation), scanner_to_vectors in scanner_to.beacon_relative_all.items():
            overlap = scanner_from_vectors_set.intersection(set(scanner_to_vectors))
            if len(overlap) >= 12:
                # Just pick a random overlapped vector to get the beacon reference from both scanners
                overlapped_vector = overlap.__iter__().__next__()
                index_overlapped_vector_from = scanner_from_vectors.index(overlapped_vector)
                scanner_from_matched_beacon = scanner_from.beacons[index_overlapped_vector_from]
                index_overlapped_vector_to = scanner_to_vectors.index(overlapped_vector)
                scanner_to_matched_beacon = scanner_to.beacons[index_overlapped_vector_to]
                matches += 1
                return Match(scanner_from, scanner_from_beacon_from, scanner_from_matched_beacon, scanner_to, scanner_to_beacon_from, scanner_to_transformation, scanner_to_matched_beacon)
    return None


scanner_beacons_sections = Parser.from_file(INPUT).to_sections()

scanners: List[Scanner] = []
for i, scanner_beacons_section in enumerate(scanner_beacons_sections):
    beacon_strings = Parser.from_string(scanner_beacons_section).to_lines()
    beacons: List[Beacon] = [tuple(int(word) for word in beacon_string.split(",")) for beacon_string in beacon_strings[1:]]
    scanners.append(Scanner(i, beacons))

matches = {}
for scanner_from_index, scanner_from in enumerate(scanners):
    for scanner_to in scanners:
        if scanner_from.number == scanner_to.number:
            continue
        match = find_match(scanner_from, scanner_to)
        if match is not None:
            print("Match found!", match.scanner_from.number, match.scanner_to.number)
            # print("From:", match.scanner_from.number, match.scanner_from_beacon_from, match.scanner_from_matched_beacon)
            # print("To  :", match.scanner_to.number, match.scanner_to_beacon_from, match.scanner_to_transformation, match.scanner_to_matched_beacon)
            f = match.scanner_from_beacon_from
            t = match.scanner_to_transformation.apply(match.scanner_to_beacon_from)
            scanner_position = (f[0] - t[0], f[1] - t[1], f[2] - t[2])
            matches[(scanner_from.number, scanner_to.number)] = (match, scanner_position)


all_beacons = set()
all_scanners = set()
graph = Graph.from_edges((f, t) for (f, t) in matches.keys() if t > f)
print(graph)
for scanner in scanners:
    path = graph.calc_shortest_path(scanner.number, 0)
    previous_scanner_position = None
    scanner_position = None if len(path) > 1 else (0, 0, 0)
    previous_match = None
    for i in range(len(path) - 1):
        step_from = path[i+1]
        step_to = path[i]
        (match, scanner_position) = matches[(step_from, step_to)]
        if previous_scanner_position:
            f = scanner_position
            t = match.scanner_to_transformation.apply(previous_scanner_position)
            scanner_position = (f[0] + t[0], f[1] + t[1], f[2] + t[2])
        previous_scanner_position = scanner_position
        previous_match = match
    all_scanners.add(scanner_position)

# print(all_beacons)
# print(len(all_beacons))
print(all_scanners)

max_dis = 0
for scanner_pos1 in all_scanners:
    for scanner_pos2 in all_scanners:
        dis = abs(scanner_pos1[0] - scanner_pos2[0]) + abs(scanner_pos1[1] - scanner_pos2[1]) + abs(scanner_pos1[2] - scanner_pos2[2])
        if dis > max_dis:
            max_dis = dis

print(max_dis)
