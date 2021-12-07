from abc import ABC, abstractmethod
from typing import Any

from src.util import *


class BaseSolution(ABC):

    def __init__(self):
        self.parser = None

    @abstractmethod
    def puzzle1(self) -> Any:
        pass

    @abstractmethod
    def puzzle2(self) -> Any:
        pass

    def run(self, puzzle: int, file: str):
        print("================= META =================")
        print(f"Puzzle: {puzzle}")
        print(f"File: {file}")
        print("================= DEBUG ================")
        self.parser = Parser.from_file(file)
        if puzzle == 1:
            solution = self.puzzle1()
        elif puzzle == 2:
            solution = self.puzzle2()
        else:
            raise ValueError(f"Unknown puzzle: {puzzle}")
        print("=============== SOLUTION ===============")
        print(solution)
