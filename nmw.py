class nmw:
    def __init__(self, g, m, d):
        self.g = g
        self.d = d
        self.m = m
        self.ww = []
        self.zz = []

    def compare(self, x, y):  # Compares sequence elements x and y to determine the match/difference score
        if x == y:
            return self.m
        else:
            return self.d

    def F(self, a, b):  # Creates & returns the score matrix f
        r = len(a)  # number of rows
        c = len(b)  # number of columns
        f = [[0 for _ in range(c + 1)] for _ in range(r + 1)]  # a matrix of zeros
        for i in range(r + 1):  # filling the first column
            f[i][0] = i * self.g
        for j in range(c + 1):  # filling the first row
            f[0][j] = j * self.g
        for i in range(1, r + 1):  # filling the rest of the matrix
            for j in range(1, c + 1):
                f[i][j] = max(f[i - 1][j] + self.g, f[i][j - 1] + self.g,
                              f[i - 1][j - 1] + self.compare(a[i - 1], b[j - 1]))
        return f

    def EnumerateAlignments(self, x, y, f, w, z):  # Gets a list of all alignments when x, y are strings
        i = len(x)
        j = len(y)
        if i == j == 0:  # The end of the recursivity
            self.ww.append(w)
            self.zz.append(z)
        if i > 0 and j > 0 and f[i][j] == f[i - 1][j - 1] + self.compare(x[i - 1], y[j - 1]):  # Diagonal result
            self.EnumerateAlignments(x[0:i - 1], y[0:j - 1], f, x[i - 1] + w, y[j - 1] + z)
        if i > 0 and f[i][j] == f[i - 1][j] + self.g:  # Top result
            self.EnumerateAlignments(x[0:i - 1], y, f, x[i - 1] + w, "-" + z)
        if j > 0 and f[i][j] == f[i][j - 1] + self.g:  # Left result
            self.EnumerateAlignments(x, y[0:j - 1], f, "-" + w, y[j - 1] + z)
        return self.ww, self.zz

    def EnumerateAlignments_lines(self, x, y, f, w, z):  # Gets a list of all alignments when x, y are line lists
        i = len(x)
        j = len(y)
        if i == j == 0:
            self.ww.append(w)
            self.zz.append(z)
        if i > 0 and j > 0 and f[i][j] == f[i - 1][j - 1] + self.compare(x[i - 1], y[j - 1]):  # Diagonal result
            self.EnumerateAlignments_lines(x[0:i - 1], y[0:j - 1], f, [x[i - 1]] + w, [y[j - 1]] + z)
        if i > 0 and f[i][j] == f[i - 1][j] + self.g:  # Top result
            self.EnumerateAlignments_lines(x[0:i - 1], y, f, [x[i - 1]] + w, ["-"] + z)
        if j > 0 and f[i][j] == f[i][j - 1] + self.g:   # Left result
            self.EnumerateAlignments_lines(x, y[0:j - 1], f, ["-"] + w, [y[j - 1]] + z)
        return self.ww, self.zz

    def idk(self):
        # alignments creation -----------------------------------------------------------------------------------------
        """w = ""
        z = ""
        j = c
        i = r
        while j > 0 and i > 0:  # tracing-back
            if f[i][j] == f[i - 1][j - 1] + self.compare(self.a[i - 1], self.b[j - 1]):  # diagonal result
                w += self.a[i - 1]
                z += self.b[j - 1]
                j -= 1
                i -= 1
            elif f[i][j] == f[i - 1][j] + self.g:  # top result
                w += self.a[i - 1]
                z += "-"
                i -= 1
            else:
                w += "-"
                z += self.b[j - 1]
                j -= 1
        while i > 0:
            w += self.a[i - 1]
            z += '-'
            i -= 1
        while j > 0:
            w += '-'
            z += self.b[j - 1]
            j -= 1
        w = w[::-1]
        z = z[::-1]
        return f, w, z"""
