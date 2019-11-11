from typing import List, Tuple, Callable
import math

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """ Adds corresponding elements """
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """ Subtractsubtractsv, w corresponding elements """
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """ Sums all corresponding elements """
    # check that vectors is not empty
    assert vectors, "no vectors are provided!"

    # check the vectors are the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """ Multiplies every element by c """
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """ Computes the element-wise average """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    """ Computes v_1 * v_2 + ... v_n * w_n """
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6


def sum_of_squares(v: Vector) -> float:
    """ Returns v_1*v_1 + ... + v_n*v_n  """
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14


def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))
assert magnitude([3, 4])


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))

# another type alias

Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]


def shape(A: Matrix) -> Tuple[int, int]:
    """ returns (# of rows, # of columns of A) """
    n_rows = len(A)
    n_cols = len(A[0]) if A else 0
    return n_rows, n_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns


def get_row(A: Matrix, i: int) -> Vector:
    """ returns the i-th row of A (as a vector) """
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    """ returns the j-th column of A (as a vectort) """
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    returns a num_rows x num_cols matrix
    whose (i, j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """ returns the n x n identity matrix """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]
