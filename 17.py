from typing import List
import numpy as np

# def get_neighbors(array: np.ndarray, x, y, z):
#     return array[x-1:x+1,y-1:y+1,z-1:z+1]


def apply_rules(array: np.ndarray) -> np.ndarray:
    new = np.zeros(shape=array.shape, dtype=int)
    w, h, d = array.shape
    for x in range(w):
        for y in range(h):
            for z in range(d):
                slced = array[x - 1:x + 2, y - 1:y + 2, z - 1:z + 2]
                slc = slced.flatten()
                if array[x, y, z]:
                    new[x, y, z] = 2 <= len(slc[slc == 1]) - 1 <= 3
                else:
                    new[x, y, z] = len(slc[slc == 1]) == 3
    return new


def apply_rules2(array: np.ndarray) -> np.ndarray:
    """
    Doesn't work
    """
    new = np.zeros(shape=array.shape, dtype=int)
    w, h, d, d2 = array.shape
    for x in range(w):
        for y in range(h):
            for z in range(d):
                for u in range(d2):
                    slced = array[x - 1:x + 2, y - 1:y + 2, z - 1:z + 2, u - 1:u + 2]
                    slc = slced.flatten()
                    if array[x, y, z, u]:
                        new[x, y, z, u] = 2 <= len(slc[slc == 1]) - 1 <= 3
                    else:
                        new[x, y, z, u] = len(slc[slc == 1]) == 3
    return new


def main_1(inp: List[str]):
    array = np.zeros(shape=(len(inp), len(inp), len(inp)), dtype=int)
    array[0] = [[x == "#" for x in l.strip()] for l in inp]
    array = np.pad(array, 1)
    for _ in range(6):
        array = np.pad(array, 1)
        array = apply_rules(array)
    ar = array.flatten()
    return len(ar[ar == 1])


def main_2(inp: List[str]):
    array = np.zeros(shape=(len(inp), len(inp), len(inp), len(inp)), dtype=int)
    array[0][0] = [[x == "#" for x in l.strip()] for l in inp]
    array = np.pad(array, 1)
    for _ in range(6):
        array = np.pad(array, 1)
        array = apply_rules2(array)
    ar = array.flatten()
    return len(ar[ar == 1])


if __name__ == "__main__":
    with open("17.txt") as f:
        inp = f.readlines()
    print(main_1(inp))
    print(main_2(inp))
