
import numpy as np


def is_symmetric(matrix):
    """Check whether a matrix is symmetric."""
    return np.array_equal(matrix, matrix.T)


def is_positive_definite_by_minors(matrix):
    """Check positive definiteness using leading principal minors."""
    n = matrix.shape[0]

    for i in range(1, n + 1):
        submatrix = matrix[:i, :i]
        determinant = np.linalg.det(submatrix)

        if determinant <= 0:
            return False

    return True


def main():
    A = np.array([
        [1,  2,  3,  -1],
        [2, -1,  9,  -7],
        [-3, 4, -3,  19],
        [4, -2,  6, -21]
    ], dtype=float)

    if is_symmetric(A):
        print("The matrix is symmetric.")

        if is_positive_definite_by_minors(A):
            print(
                "The matrix is positive definite. "
                "Cholesky decomposition is applicable."
            )
        else:
            print(
                "The matrix is not positive definite. "
                "Cholesky decomposition is not applicable."
            )
    else:
        print(
            "The matrix is not symmetric. "
            "Cholesky decomposition is not applicable."
        )


if __name__ == "__main__":
    main()
