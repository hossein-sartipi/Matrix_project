# Matrix Operations with Python

This Python project is designed to perform various operations on matrices. It allows users to create matrices, perform row operations (scaling, row swapping, and row addition/subtraction), and convert matrices into echelon form.

### Features:
- **Create Row**: The program allows you to create rows in a matrix, where each element is checked and converted into a rational number.
- **Create Matrix**: You can input rows of a matrix, ensuring consistency in row lengths and displaying the matrix.
- **Row Operations**:
  1. **Scale Row (opp_1)**: Multiply a row by a constant.
  2. **Swap Rows (opp_2)**: Swap two rows in the matrix.
  3. **Row Addition/Subtraction (opp_3)**: Add a constant multiple of one row to another row.
- **Convert to Echelon Form**: The program can convert any matrix into row echelon form using Gaussian elimination.
- **Interactive Interface**: Users can interact with the program via the terminal, providing inputs for matrix creation, row operations, and more.

### Requirements:
- Python 3.x
- **SymPy** library for symbolic mathematics (`pip install sympy`)

### How to Use:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/matrix-operations.git
   cd matrix-operations
