import sys

import numpy as np

ROWS = 3
COLS = 4

def input_data(seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    a = rng.integers(-5, 7, size=(ROWS, COLS), dtype=int)
    b = rng.integers(-5, 7, size=(ROWS, COLS), dtype=int)
    return a, b

def solve(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.hstack((a[:, [1, 3]], b[:, [1, 3]]))


def _print_matrix(title: str, m: np.ndarray) -> None:
    print(title)
    for row in m:
        print(" ", " ".join(f"{int(x):4d}" for x in row))

def _print_matrix_2x2(title: str, m: np.ndarray) -> None:
    print(title)
    for row in m:
        print(" ", " ".join(f"{int(x):4d}" for x in row))

def output_results(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> None:
    _print_matrix("Матриця A (3x4):", a)
    _print_matrix("Матриця B (3x4):", b)
    _print_matrix("Матриця C (парні стовпчики A і B: 2-й та 4-й):", c)

    _print_matrix_2x2("Підмасив у нижньому правому куті матриці A (2x2):", a[-2:, -2:])
    _print_matrix_2x2("Підмасив у верхньому лівому куті матриці B (2x2):", b[:2, :2])


def _parse_seed(argv: list[str]) -> int:
    seed = 20260422
    if len(argv) >= 2:
        try:
            seed = int(argv[1])
        except ValueError:
            seed = 20260422
    return seed


def main(argv: list[str]) -> int:
    seed = _parse_seed(argv)
    print("Лабораторна робота №3 (КС13, Липневський Матвій)")
    print("Генерація 2 матриць 3x4 у діапазоні (-5..6), seed=", seed, "\n", sep="")

    a, b = input_data(seed)
    c = solve(a, b)
    output_results(a, b, c)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

