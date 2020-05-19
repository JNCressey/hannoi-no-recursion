# The Tower of Hanoi game is often used as an example to introduce using
# a top-down recursive approach for solving problems.
# Here I solve the Tower of Hanoi game using a bottom-up iterative approach.

from sys import version_info
if version_info[0]<3 or (version_info==3 and version_info[1]<5):
    raise Exception("Must be using at least Python 3.5 for typing.")

import typing
from typing import Tuple, List, Dict

#from typing_extensions import Literal # 3.5 <= Python version < 3.8
if version_info[0]==3 and version_info[1]<8:
    pretty_version = (
        f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
        )
    raise Exception(
        (     "typing.Literal is new in version 3.8." + "\n"
            + f"You're using Python version {pretty_version}." + "\n"
            + "Use typing_extensions.Literal instead."
            )
        )
from typing import Literal # Python version >= 3.8

Position = Literal["A", "B", "C"]
Move = Tuple[Position, Position]

class Solution:
    def __init__(
            self,
            number_of_disks: int,
            moves: List[Move],
            start: Position = "A",
            end: Position = "C",
        ) -> None:
        self.number_of_disks = number_of_disks
        if start=="A" and end=="C":
            self.moves = moves
        else:
            moves_a_to_c = move_relabling(moves, start, end)
            self.moves = moves_a_to_c
    
    
    def relabled_moves(
            self,
            new_start: Position,
            new_end: Position,
        ) -> List[Move]:
        return move_relabling(
            self.moves,
            "A",
            "C",
            new_start,
            new_end,
        )

    
    def pretty_print_moves(self) -> None:
        for move in self.moves:
            print( f"Move disk from {move[0]} to {move[1]}." )


def move_relabling(
        moves: List[Move],
        old_start: Position,
        old_end: Position,
        new_start: Position = "A",
        new_end: Position = "C",
    ) -> List[Move]:
    old_middle = other_position(old_start, old_end)
    new_middle = other_position(new_start, new_end)
    relabling = {
        old_start: new_start,
        old_middle: new_middle,
        old_end: new_end,
        }
    return [
        (
            relabling[move[0]],
            relabling[move[1]],
            )
        for move in moves
        ]


def other_position(pos1: Position, pos2: Position) -> Position:
    count: Dict[Position, int] = {
        "A":0,
        "B":0,
        "C":0,
        }
    count[pos1]+=1
    count[pos2]+=1
    pos3: Position = min(count, key=count.get)
    return pos3


if __name__ == "__main__":
    N: int = 3 # parameter. Number of disks in the tower.

    solution = Solution(0, [])
    moves: List[Move]
    for n in range(0, N+1):
        moves = (     solution.relabled_moves("A", "B")
                    + [("A", "C")]
                    + solution.relabled_moves("B", "C")
            )
        solution = Solution(n, moves)
    solution.pretty_print_moves()
