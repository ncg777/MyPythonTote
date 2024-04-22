import unittest
from src.DataStructures.Matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_init(self):
        m = Matrix(2, 2)
        self.assertEqual(m.m, 2)
        self.assertEqual(m.n, 2)

    def test_lock(self):
        m = Matrix(2, 2)
        m.lock()
        with self.assertRaises(ValueError):
            m.set(0, 0, 1)

    def test_unlock(self):
        m = Matrix(2, 2)
        m.lock()
        m.unlock()
        m.set(0, 0, 1)  # Should not raise an exception

    def test_column_count(self):
        m = Matrix(2, 3)
        self.assertEqual(m.column_count(), 3)

    def test_row_count(self):
        m = Matrix(2, 3)
        self.assertEqual(m.row_count(), 2)

    def test_init_with_array(self):
        arr = [[1, 2], [3, 4]]
        m = Matrix.fromarr(arr)
        self.assertEqual(m.m, 2)
        self.assertEqual(m.n, 2)
        self.assertEqual(m.get(0, 0), 1)
        self.assertEqual(m.get(0, 1), 2)
        self.assertEqual(m.get(1, 0), 3)
        self.assertEqual(m.get(1, 1), 4)

    def test_copy(self):
        arr = [[1, 2], [3, 4]]
        m1 = Matrix.fromarr(arr)
        m2 = Matrix(2, 2)
        m2.copy(m1)
        self.assertEqual(m2.get(0, 0), 1)
        self.assertEqual(m2.get(0, 1), 2)
        self.assertEqual(m2.get(1, 0), 3)
        self.assertEqual(m2.get(1, 1), 4)

    def test_init_with_default_value(self):
        m = Matrix(2, 2, 5)
        self.assertEqual(m.get(0, 0), 5)
        self.assertEqual(m.get(0, 1), 5)
        self.assertEqual(m.get(1, 0), 5)
        self.assertEqual(m.get(1, 1), 5)

    def test_set_and_get(self):
        m = Matrix(2, 2)
        m.set(0, 0, 1)
        self.assertEqual(m.get(0, 0), 1)

    def test_clear(self):
        arr = [[1, 2], [3, 4]]
        m = Matrix.fromarr(arr)
        m.clear()
        self.assertEqual(m.get(0, 0), None)
        self.assertEqual(m.get(0, 1), None)
        self.assertEqual(m.get(1, 0), None)
        self.assertEqual(m.get(1, 1), None)

    def test_append_row(self):
        arr = [[1, 2], [3, 4]]
        m = Matrix.fromarr(arr)
        m.append_row([5, 6])
        self.assertEqual(m.get(2, 0), 5)
        self.assertEqual(m.get(2, 1), 6)

    def test_append_column(self):
        arr = [[1, 2], [3, 4]]
        m = Matrix.fromarr(arr)
        m.append_column([5, 6])
        self.assertEqual(m.get(0, 2), 5)
        self.assertEqual(m.get(1, 2), 6)

    def test_move_row(self):
        arr = [[1, 2], [3, 4]]
        m = Matrix.fromarr(arr)
        m.move_row(0, 1)
        self.assertEqual(m.get(0, 0), 3)
        self.assertEqual(m.get(0, 1), 4)
        self.assertEqual(m.get(1, 0), 1)
        self.assertEqual(m.get(1, 1), 2)

    def test_move_column(self):
        arr = [[1, 2], [3, 4]]
        m = Matrix.fromarr(arr)
        m.move_column(0, 1)
        self.assertEqual(m.get(0, 0), 2)
        self.assertEqual(m.get(0, 1), 1)
        self.assertEqual(m.get(1, 0), 4)
        self.assertEqual(m.get(1, 1), 3)

    def test_set_block(self):
        arr = [[1, 2], [3, 4]]
        m = Matrix.fromarr(arr)
        m.set_block(Matrix.fromarr([[5, 6], [7, 8]]), 0, 0)
        self.assertEqual(m.get(0, 0), 5)
        self.assertEqual(m.get(0, 1), 6)


    def test_sort_rows(self):
        # Test case 1: Sorting a matrix with distinct rows
        matrix = Matrix(3, 3)
        matrix.data = [[3, 2, 1], [1, 2, 3], [2, 1, 2]]
        matrix.sort_rows()
        self.assertEqual(matrix.data, [[1, 2, 3], [2, 1, 2], [3, 2, 1]])

        # Test case 2: Sorting a matrix with duplicate rows
        matrix = Matrix(3, 3)
        matrix.data = [[1, 2, 3], [1, 2, 3], [2, 1, 2]]
        matrix.sort_rows()
        self.assertEqual(matrix.data, [[1, 2, 3], [1, 2, 3], [2, 1, 2]])

        # Test case 3: Sorting a matrix with rows in reverse order
        matrix = Matrix(3, 3)
        matrix.data = [[3, 2, 1], [2, 1, 2], [1, 2, 3]]
        matrix.sort_rows()
        self.assertEqual(matrix.data, [[1, 2, 3], [2, 1, 2], [3, 2, 1]])

        # Test case 4: Sorting an empty matrix
        matrix = Matrix(0, 0)
        matrix.sort_rows()
        self.assertEqual(matrix.data, [])

        # Test case 5: Sorting a matrix with a single row
        matrix = Matrix(1, 3)
        matrix.data = [[3, 2, 1]]
        matrix.sort_rows()
        self.assertEqual(matrix.data, [[3, 2, 1]])

    def test_get_transpose(self):
        # Create a 2x3 matrix
        matrix = Matrix(2, 3)
        matrix.data = [[1, 2, 3], [4, 5, 6]]

        # Get the transpose of the matrix
        transposed_matrix = matrix.get_transpose()

        # Check that the transposed matrix has the correct dimensions
        self.assertEqual(transposed_matrix.m, 3)
        self.assertEqual(transposed_matrix.n, 2)

        # Check that the transposed matrix has the correct elements
        self.assertEqual(transposed_matrix.data, [[1, 4], [2, 5], [3, 6]])