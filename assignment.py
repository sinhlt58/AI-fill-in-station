class Assignment:
    def __init__(self, letters, length):
        self.length = length    
        self.letters = letters
        self.board = [[None for x in range(length)] for x in range(length)]

    def assign(self, x, v):
        self.board[x[0]][x[1]] = v
    def unassign(self, x):
        self.board[x[0]][x[1]] = None
    def get_value(self, x):
        return self.board[x[0]][x[1]]
    def value_to_letter(self, v):
        return self.letters[v[0]][v[1]]
    def is_complete(self):
        return len(self.get_all_assgned_variables()) == self.length*self.length
    def get_all_unassigned_variables(self):
        result = []
        for x in self.get_all_variables():
            if not self.is_assigned(x):
                result.append(x)
        return result
    def get_all_assgned_variables(self):
        result = []
        for x in self.get_all_variables():
            if self.is_assigned(x):
                result.append(x)
        return result
    def get_all_variables(self):
        result = []
        for i in range(self.length):
            for j in range(self.length):
                result.append( (i, j) )
        return result
    def is_assigned(self, x): 
        return not self.board[x[0]][x[1]] is None
    def is_diff_all(self, v):
        for x in self.get_all_assgned_variables():
            if self.get_value(x) == v:
                return False
        return True
    def filter_constraints(self, x, constraints_x):
        result = []
        for c in constraints_x:
            for node in c:
                if node != x:
                    if not self.is_assigned(node):
                        index = constraints_x.index(c)
                        constraints_x[index] = None
                        break
        for c in constraints_x:
            if c != None:
                result.append(c)
        return result

    def get_left_neighbor(self, x):
        if x[1] == 0:
            return None
        if not self.is_assigned((x[0], x[1]-1)):
            return None  
        return (x[0], x[1]-1)

    def get_row_letters(self, i):
        row = ''
        for j in range(self.length):
            if self.is_assigned( (i, j) ):
                row += self.value_to_letter(self.get_value((i,j)))
            else:
                row += '#'
        return row

    def nice_print(self):
        #Niceprint.print_first_row()
        for i in range(self.length):
            line = ""
            for j in range(self.length):
                if not self.is_assigned( (i, j) ):
                    line += "#"
                else:
                    line += self.value_to_letter(self.get_value((i, j)))
            print line