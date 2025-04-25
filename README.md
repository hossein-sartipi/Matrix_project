# Matrix Operations with Python

This Python project is designed to perform various operations on matrices. It allows users to create matrices, perform row operations (scaling, row swapping, and row addition/subtraction), and convert matrices into echelon form.

---

## 📌 Features

- **Create Row**: The program allows you to create rows in a matrix, where each element is checked and converted into a rational number.
- **Create Matrix**: You can input rows of a matrix, ensuring consistency in row lengths and displaying the matrix.
- **Row Operations**:
  1. **Scale Row (opp_1)**: Multiply a row by a constant.
  2. **Swap Rows (opp_2)**: Swap two rows in the matrix.
  3. **Row Addition/Subtraction (opp_3)**: Add a constant multiple of one row to another row.
- **Convert to Echelon Form**: The program can convert any matrix into row echelon form using Gaussian elimination.
- **Interactive Interface**: Users can interact with the program via the terminal, providing inputs for matrix creation, row operations, and more.
  
---

## 🛠️ Requirements:

- Python 3.x
- **SymPy** library for symbolic mathematics (`pip install sympy`)

Install with:

```bash
pip install sympy
```

---

## 🚀 How to Use:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hossein-sartipi/matrix-operations.git
   cd matrix-operations

2. **Run the Program:**
   Execute the *main.py* file to start the interactive matrix operations interface.
``` bash
python main.py
```
The program will prompt you to input matrix rows, and then you can perform various operations such as scaling, swapping rows, adding rows, or converting the matrix into echelon form.

3. **Available Operations:**
   - **opp_1 (1):** Scale a row by a constant.
   - **opp_2 (2):** Swap two rows.
   - **opp_3 (3):** Add/subtract a constant multiple of one row to another.
   - **echelon (4):** Convert the matrix to row echelon form.
   - **new matrix (5):** Start a new matrix.
   - **exit (6):** Exit the program.

---

## Functions:
- **create_row(row):** Validates and converts a row to rational numbers.
- **create_matrix():** Allows user to input the matrix, row by row.
- **show_matrix(matrix):** Displays the matrix.
- **opp_1(matrix, columns_number, rows_number):** Scales a specific row by a constant.
- **opp_2(matrix, rows_number):** Swaps two rows.
- **opp_3(matrix, columns_number, row_numbers):** Adds a constant multiple of one row to another.
- **echelon(A):** Converts the matrix A into row echelon form.
- **get_row(i):** Prompts the user to input a row index.
- **get_constant():** Prompts the user to input a constant.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

