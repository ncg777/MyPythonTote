class Matrix:
    """
    Pointless and futile exercise of a Python class.
    """
    @classmethod
    def fromArray(self, arr):
        m = len(arr)
        n = len(arr[0])
        mat = Matrix(m,n)
        for i in range(m):
            for j in range(n):
                mat.set(i, j, arr[i][j])
        return mat

    def __init__(self, m=0, n=0, default_value=None):
        if not isinstance(m, int) or not isinstance(n, int):
            raise TypeError("Matrix dimensions must be integers")
        self.m = m
        self.n = n
        self.default_value=default_value
        self.locked = False
        self.data = [[default_value for _ in range(n)] for _ in range(m)]
        

    def check_lock(self):
        if self.locked == True:
            raise ValueError("Matrix is locked")

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def column_count(self):
        return self.n

    def row_count(self):
        return self.m

    def copy(self, p_mat):
        self.clear()
        self.m = p_mat.m
        self.n = p_mat.n
        self.default_value = p_mat.default_value
        self.data = [[self.default_value for _ in range(self.n)] for _ in range(self.m)]
        self.set_block(p_mat, 0, 0)

    def __str__(self):
        sb = []
        for i in range(self.m):
            row = [self.get(i, j) for j in range(self.n)]
            sb.append(' '.join(map(str, row)))
        return '\n'.join(sb)

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        if self.locked:
            raise ValueError("Matrix is locked")
        if 0 <= i < self.m and 0 <= j < self.n:
            self.data[i][j] = value
        else:
            raise ValueError("Index out of range")

    def clear(self):
        self.check_lock()
        self.data = [[self.default_value for _ in range(self.n)] for _ in range(self.m)]

    def append_row(self, l):
        self.insert_row(self.m, l)

    def append_rows(self, c):
        for i in range(c.m):
            self.append_row(c.get_row(i))

    def move_row(self, from_, to):
        if from_ == to:
            return
        if from_ < 0 or to < 0 or from_ >= self.m or to >= self.m:
            raise ValueError("Index out of bounds")
        row = self.get_row(from_)
        self.remove_row(from_)
        self.insert_row(to, row)

    def append_column(self, l):
        self.insert_column(self.n, l)

    def append_columns(self, c):
        for j in range(c.n):
            self.append_column(c.get_column(j))

    def move_column(self, from_, to):
        if from_ == to:
            return
        if from_ < 0 or to < 0 or from_ >= self.n or to >= self.n:
            raise ValueError("Index out of bounds")
        col = self.get_column(from_)
        self.remove_column(from_)
        self.insert_column(to, col)

    def set_block(self, p_mat, i0, j0):
        self.check_lock()
        mm = p_mat.m
        mn = p_mat.n
        if i0 < 0 or j0 < 0 or i0 + mm > self.m or j0 + mn > self.n:
            raise IndexError("Matrix index out of bounds")
        for i in range(mm):
            for j in range(mn):
                v = p_mat.get(i, j)
                if v == self.default_value:
                    continue
                self.set(i + i0, j + j0, v)

    def shift_columns_right(self, j):
        for row in self.data:
            row.insert(j, self.default_value)
        self.n += 1

    def shift_rows_down(self, i):
        self.data.insert(i, [0] * self.n)
        self.m += 1

    def insert_column(self, j, l):
        self.check_lock()
        if len(l) != self.m:
            raise ValueError("List size does not match matrix")
        self.shift_columns_right(j)
        for i, v in enumerate(l):
            self.set(i, j, v)

    def insert_row(self, i, l):
        self.check_lock()
        if len(l) != self.n:
            raise ValueError("List size does not match matrix")
        self.shift_rows_down(i)
        for j, v in enumerate(l):
            self.set(i, j, v)

    def remove_column(self, j):
        for row in self.data:
            row.pop(j)
        self.n -= 1

    def remove_row(self, i):
        self.data.pop(i)
        self.m -= 1

    def set_column(self, j, l):
        self.check_lock()
        if len(l) != self.m:
            raise ValueError("List size does not match matrix")
        for i, v in enumerate(l):
            self.set(i, j, v)

    def set_row(self, i, l):
        self.check_lock()
        if len(l) != self.n:
            raise ValueError("List size does not match matrix")
        for j, v in enumerate(l):
            self.set(i, j, v)

    def get_column(self, j):
        return [self.get(i, j) for i in range(self.m)]

    def get_row(self, i):
        return [self.get(i, j) for j in range(self.n)]

    def get_transpose(self):
        m = Matrix(self.n, self.m)
        for i in range(self.m):
            for j in range(self.n):
                m.set(j, i, self.get(i, j))
        return m

    def contains(self, el):
        for i in self.mat.keys():
            if el in self.mat[i].values():
                return True
        return False

    def distinct_rows_sorted(self):
        return sorted(list(set(tuple(row) for row in self.data)))

    def swap_rows(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def compare_rows(self, a, b):
        return self._compare_rows(self.data[a],self.data[b])
    
    def _compare_rows(self, a, b):
        if(len(a)==0):
            return 0;
        if(a[0]<b[0]):
            return -1
        elif(a[0]>b[0]):
            return 1
        else:
            return self._compare_rows(a[1:],b[1:])

    def partition(self, left, right, pivot_index):
        self.check_lock()
        self.swap_rows(pivot_index, right)
        store_index = left
        for i in range(left, right):
            if self.compare_rows(i, right) < 1:
                self.swap_rows(i, store_index)
                store_index += 1
        self.swap_rows(store_index, right)
        return store_index

    def sort_rows(self):
        self.quicksort(0, self.m - 1)

    def quicksort(self, left, right):
        if left < right:
            pivot_index = self.find_median_of_three(left, right)
            pivot_new_index = self.partition(left, right, pivot_index)
            self.quicksort(left, pivot_new_index - 1)
            self.quicksort(pivot_new_index + 1, right)

    def find_median_of_three(self, left, right):
        middle = (left + right) // 2
        tmp = Matrix(3, self.n)
        if left in self.data:
            tmp.data[0] = self.data[left]
        if middle in self.data:
            tmp.data[1] = self.data[middle]
        if right in self.data:
            tmp.data[2] = self.data[right]
        o = 2 - self.partition(0, 2, 0)
        return [left, middle, right][o]