# DSA-HW01---Sparse-Matrix

## Project Overview

This project implements a memory and runtime-optimized data structure for handling large sparse matrices. The program supports loading sparse matrices from files and performing mathematical operations including addition, subtraction, and multiplication.


## Directory Structure

```
/dsa/sparse_matrix/
├── code/
│   └── src.py(Main file of implementation)
└── sample_inputs/
    ├── Copy of easy_sample_02_1.txt
    ├── easy_sample_01_2.txt
|-- result_matrix.txt(File where the results of the addition, subtraction and multiplication of the matrices go) 
```

## Features

### Core Functionality
- **Memory-optimized storage**: Stores only non-zero elements to minimize memory usage
- **Runtime-optimized operations**: Efficient algorithms for matrix operations
- **File I/O**: Read sparse matrices from formatted text files
- **Mathematical operations**: Addition, subtraction, and multiplication
- **Error handling**: Robust input validation and exception handling

### Supported Operations
1. **Matrix Addition**: A + B (matrices must have same dimensions)
2. **Matrix Subtraction**: A - B (matrices must have same dimensions)  
3. **Matrix Multiplication**: A × B (columns of A must equal rows of B)

## Input File Format

The input files follow this specific format:

```
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)
(0, 165, -933)
(0, 1350, -89)
```

- **Line 1**: Number of rows in format `rows=N`
- **Line 2**: Number of columns in format `cols=N`
- **Subsequent lines**: Non-zero entries in format `(row, column, value)`
- All unlisted positions are assumed to be zero

## Class Structure

### SparseMatrix Class (Python Implementation)

#### Constructor
```python
SparseMatrix(matrix_file_path=None, num_rows=None, num_cols=None)
```
- **matrix_file_path**: Load matrix from specified file path
- **num_rows, num_cols**: Create empty matrix with specified dimensions

#### Data Structure
- **Internal storage**: Dictionary `{(row, col): value}` for efficient sparse representation
- **Attributes**: `num_rows`, `num_cols` for matrix dimensions

#### Core Methods
- `get_element(row, col)` - Retrieve element at specified position (returns 0 for unset positions)
- `set_element(row, col, value)` - Set element at specified position (removes entry if value is 0)
- `add(other)` - Matrix addition operation
- `subtract(other)` - Matrix subtraction operation  
- `multiply(other)` - Matrix multiplication operation
- `save_to_file(file_path)` - Save matrix to file in standard format
- `__str__()` - String representation for display and file output

#### Private Helper Methods
- `_load_from_file(file_path)` - Internal file loading logic
- `_parse_entry(line)` - Parse individual matrix entries with format validation

## Error Handling

The program handles various error conditions:

### Input Validation
- **File format errors**: Throws `ValueError("Input file has wrong format")` for:
  - Incorrect parenthesis format (must use standard parentheses)
  - Non-integer values (floating point values not allowed)
  - Malformed entries (incorrect number of comma-separated values)
- **Whitespace handling**: Automatically ignores empty/whitespace-only lines
- **Matrix operation validation**: Checks dimension compatibility:
  - Addition/Subtraction: "Matrix size mismatch for addition/subtraction"
  - Multiplication: "Matrix size mismatch for multiplication"

### Mathematical Constraints
- **Addition/Subtraction**: Requires matrices with identical dimensions
- **Multiplication**: Requires columns of first matrix to equal rows of second matrix

## Usage Instructions

### Execution
```bash
python src.py
```

The program will prompt you to:
1. Enter the desired operation (add, subtract, multiply)
2. Provide paths to input matrix files
3. View results and automatic file output


## Student Information

**Student Name**: Nshuti Shalom Silver Jr  

---

*This implementation focuses on efficiency, correctness, and proper software engineering practices while meeting all specified requirements for the sparse matrix operations assignment.*
