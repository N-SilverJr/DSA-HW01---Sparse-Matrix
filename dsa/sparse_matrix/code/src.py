"""
This module implements a custom SparseMatrix class to load sparse matrices
from a file, perform addition, subtraction, and multiplication, while ensuring
no use of restricted Python libraries.
"""

class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        self.data = {}  # {(row, col): value}
        self.num_rows = 0
        self.num_cols = 0

        if matrix_file_path:
            self._load_from_file(matrix_file_path)
        elif num_rows is not None and num_cols is not None:
            self.num_rows = num_rows
            self.num_cols = num_cols

    def _parse_entry(self, line):
        line = line.strip()
        if not line:
            return None
        if not (line.startswith('(') and line.endswith(')')):
            raise ValueError("Input file has wrong format")

        content = line[1:-1]
        parts = content.split(',')
        if len(parts) != 3:
            raise ValueError("Input file has wrong format")

        try:
            r = int(parts[0].strip())
            c = int(parts[1].strip())
            v = int(parts[2].strip())
        except Exception:
            raise ValueError("Input file has wrong format")

        return (r, c, v)

    def _load_from_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('rows='):
                self.num_rows = int(stripped.split('=')[1].strip())
            elif stripped.startswith('cols='):
                self.num_cols = int(stripped.split('=')[1].strip())
            else:
                entry = self._parse_entry(stripped)
                if entry:
                    r, c, v = entry
                    self.set_element(r, c, v)

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix size mismatch for addition")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (r, c), v in self.data.items():
            result.set_element(r, c, v)

        for (r, c), v in other.data.items():
            result.set_element(r, c, result.get_element(r, c) + v)

        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix size mismatch for subtraction")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (r, c), v in self.data.items():
            result.set_element(r, c, v)

        for (r, c), v in other.data.items():
            result.set_element(r, c, result.get_element(r, c) - v)

        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix size mismatch for multiplication")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (r1, c1), v1 in self.data.items():
            for c2 in range(other.num_cols):
                v2 = other.get_element(c1, c2)
                if v2 != 0:
                    result.set_element(r1, c2, result.get_element(r1, c2) + v1 * v2)

        return result

    def __str__(self):
        output = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (r, c), v in sorted(self.data.items()):
            output += f"({r}, {c}, {v})\n"
        return output

# Main user interaction
if __name__ == "__main__":
    print("Select matrix operation: add, subtract, multiply")
    operation = input("Enter operation: ").strip().lower()

    file1 = input("Enter path to first matrix file: ").strip()
    file2 = input("Enter path to second matrix file: ").strip()

    try:
        A = SparseMatrix(matrix_file_path=file1)
        B = SparseMatrix(matrix_file_path=file2)

        if operation == 'add':
            result = A.add(B)
        elif operation == 'subtract':
            result = A.subtract(B)
        elif operation == 'multiply':
            result = A.multiply(B)
        else:
            raise ValueError("Invalid operation")

        print("\nResult Matrix:")
        print(result)

    except Exception as e:
        print(f"Error: {e}")
