# 4. Write a program to implement 8-puzzle problem using A* Algorithm in Python

# Start State:
# 2 8 3
# 1 6 4
# 7   5

# Goal State:
# 1 2 3
# 8   4
# 7 6 5

# Heuristics:
# g(n) = Number of Displaced Tiles
# h(n) = Node depth
# f(n) = g(n) + h(n)


import copy
import networkx as nx
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [30, 30]


node_count: int = 0


class Board:
    def __init__(
        self, board: "list[list[int]]", parent: "Board | None" = None
    ) -> None:
        self.name: int = node_count
        self.board: list[list[int]] = board
        self.parent: "Board | None" = parent
        self.g: int = 0
        self.h: int = 0
        self.f: int = 0

    def __str__(self) -> str:
        print_board: list[list[str]] = [
            [f"{x}" if x != -1 else " " for x in y] for y in self.board
        ]

        string: str = ""
        string += f"+---+---+---+\n"
        string += (
            f"| {print_board[0][0]} | "
            + f"{print_board[0][1]} | "
            + f"{print_board[0][2]} |\n"
        )
        string += f"+---+---+---+\n"
        string += (
            f"| {print_board[1][0]} | "
            + f"{print_board[1][1]} | "
            + f"{print_board[1][2]} |\n"
        )
        string += f"+---+---+---+\n"
        string += (
            f"| {print_board[2][0]} | "
            + f"{print_board[2][1]} | "
            + f"{print_board[2][2]} |\n"
        )
        string += f"+---+---+---+"

        return string

    def empty_loc(self) -> "tuple[int, int]":
        return [
            (i, j)
            for (i, x) in enumerate(self.board)
            for j, y in enumerate(x)
            if y == -1
        ][0]

    def neighbours(self) -> "list[tuple[int, int]]":
        neighbour_count: int = 0
        neighbours: list[tuple[int, int]] = []

        if self.empty_loc()[0] - 1 > -1:
            neighbour_count += 1
            neighbours.append((self.empty_loc()[0] - 1, self.empty_loc()[1]))
        if self.empty_loc()[0] + 1 < len(self.board):
            neighbour_count += 1
            neighbours.append((self.empty_loc()[0] + 1, self.empty_loc()[1]))
        if self.empty_loc()[1] - 1 > -1:
            neighbour_count += 1
            neighbours.append((self.empty_loc()[0], self.empty_loc()[1] - 1))
        if self.empty_loc()[1] + 1 < len(self.board[0]):
            neighbour_count += 1
            neighbours.append((self.empty_loc()[0], self.empty_loc()[1] + 1))

        return neighbours

    def new_boards(self) -> "list[Board]":
        children: list[Board] = []

        for index, i in enumerate(self.neighbours()):
            new: list[list[int]] = copy.deepcopy(self.board)

            new[self.empty_loc()[0]][self.empty_loc()[1]], new[i[0]][i[1]] = (
                new[i[0]][i[1]],
                new[self.empty_loc()[0]][self.empty_loc()[1]],
            )

            global node_count
            node_count += 1

            new_board: Board = Board(board=new, parent=self)

            children.append(new_board)

        return children

    def calc_g(self, goal: "list[list[int]]") -> None:
        self.g = 0

        for i in range(len(goal)):
            for j in range(len(goal)):
                if goal[i][j] != self.board[i][j]:
                    self.g += 1

    def calc_h(self) -> None:
        current = self
        self.h = 0

        while current.parent is not None:
            self.h += 1
            current: Board = current.parent

    def calc_heuristics(self, goal: "list[list[int]]") -> None:
        self.calc_g(goal=goal)
        self.calc_h()

        self.f = self.g + self.h

    def return_g(self) -> int:
        return self.g

    def return_h(self) -> int:
        return self.h

    def return_f(self) -> int:
        return self.f


def is_equal(b1: "list[list[int]]", b2: "list[list[int]]") -> bool:
    return b1 == b2


def min_open(open_list: "list[Board]", goal: "list[list[int]]") -> Board:
    for x in open_list:
        x.calc_heuristics(goal=goal)

    heuristics: list[int] = [x.return_f() for x in open_list]

    return open_list[heuristics.index(min(heuristics))]


def draw_graph(
    graph: nx.Graph,
    labeldict: "dict[int, str]",
    final: Board,
    heuristicdict: "dict[int, str]",
) -> None:
    pos: dict = nx.drawing.nx_agraph.graphviz_layout(graph, prog="dot")
    nx.draw_networkx(
        G=graph,
        pos=pos,
        with_labels=True,
        node_color="white",
        node_size=1000,
    )

    nx.draw_networkx_labels(
        G=graph,
        pos=pos,
        labels=labeldict,
        font_family="Consolas",
        bbox=dict(
            facecolor="white",
            edgecolor="white",
            boxstyle="round, pad=1",
        ),
    )

    path = nx.shortest_path(graph, source=0, target=final.name)
    path_edges: list[tuple[None, None]] = list(zip(path, path[1:]))
    nx.draw_networkx_edges(
        G=graph, pos=pos, edgelist=path_edges, edge_color="r", width=2
    )

    pathlabels: dict = dict((key, labeldict[key]) for key in path)  # type: ignore

    nx.draw_networkx_labels(
        G=graph,
        pos=pos,
        labels=pathlabels,
        font_family="Consolas",
        bbox=dict(
            facecolor="white",
            edgecolor="black",
            boxstyle="round, pad=0.5",
        ),
    )

    heuristicpos: dict = {name: (x + 35, y) for name, (x, y) in pos.items()}

    nx.draw_networkx_labels(
        G=graph,
        pos=heuristicpos,
        labels=heuristicdict,
        font_family="Consolas",
    )

    plt.title("Solving the 8-Puzzle Problem using A* Search")
    plt.savefig("8puzzleastar.png")
    plt.show()


def main() -> None:
    open: list[Board] = list()
    closed: list[Board] = list()
    graph: nx.Graph = nx.Graph()

    goal: list[list[int]] = [[1, 2, 3], [8, -1, 4], [7, 6, 5]]
    root: Board = Board(board=[[2, 8, 3], [1, 6, 4], [7, -1, 5]])

    labeldict: dict[int, str] = {}
    heuristicdict: dict[int, str] = {}

    open.append(root)

    graph.add_node(root.name)

    labeldict[root.name] = f"{root.__str__()}"
    root.calc_heuristics(goal=goal)
    heuristicdict[root.name] = (
        f"g = {root.return_g()}\n"
        + f"h = {root.return_h()}\n"
        + f"f = {root.return_f()}"
    )

    while len(open) >= 0:
        current: Board = min_open(open_list=open, goal=goal)
        open.remove(current)

        closed.append(current)

        new_boards: list[Board] = current.new_boards()

        if is_equal(current.board, goal):
            draw_graph(
                graph=graph,
                labeldict=labeldict,
                final=current,
                heuristicdict=heuristicdict,
            )
            return
        else:
            for new in new_boards:
                valid: bool = False

                for o in open:
                    valid = valid or is_equal(current.board, o.board)

                for c in closed:
                    valid = valid or is_equal(current.board, c.board)

                if valid:
                    open.append(new)

                    if new.parent != None:
                        graph.add_edge(new.name, new.parent.name)

                        labeldict[new.name] = f"{new.__str__()}"
                        new.calc_heuristics(goal=goal)
                        heuristicdict[new.name] = (
                            f"g = {new.return_g()}\n"
                            + f"h = {new.return_h()}\n"
                            + f"f = {new.return_f()}"
                        )


if __name__ == "__main__":
    main()
