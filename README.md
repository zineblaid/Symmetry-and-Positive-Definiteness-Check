# Symmetry and Positive Definiteness Check

## Overview

This project checks whether a matrix satisfies the conditions required for Cholesky decomposition.

The program verifies matrix symmetry and tests positive definiteness using the determinants of the leading principal submatrices.

## Features

- Check whether a matrix is symmetric.
- Check positive definiteness using leading principal minors.
- Determine whether Cholesky decomposition is applicable.
- Use NumPy for matrix operations and determinant calculations.

## Technologies Used

- Python
- NumPy

## Installation

```bash
pip install numpy
```

## How to Run

```bash
python main.py
```

## Example

The program uses the following matrix:

\[
A =
\begin{bmatrix}
1 & 2 & 3 & -1 \\
2 & -1 & 9 & -7 \\
-3 & 4 & -3 & 19 \\
4 & -2 & 6 & -21
\end{bmatrix}
\]

The matrix is not symmetric. Therefore, Cholesky decomposition is not applicable to this matrix.

## Project Structure

```text
matrix-positive-definiteness-check/
├── main.py
├── README.md
└── .gitignore
```

## Learning Objectives

- Understand the conditions required for Cholesky decomposition.
- Test matrix symmetry.
- Explore positive definiteness and leading principal minors.
- Use NumPy for numerical computations.
