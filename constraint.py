class Constraint:
    def __init__(self, length):
        self.constraints = []
        self.length = length
        for i in range(length):
            for j in range(length-1):
                self.constraints.append([(i,j), (i,j+1)])
                self.constraints.append([(j,i), (j+1,i)])
            self.constraints.append([(i,0), (i,1), (i,2)])
            self.constraints.append([(0,i), (1,i), (2,i)])
        for i in range(length-1):
            self.constraints.append([(i,i), (i+1,i+1)])
            self.constraints.append([(i,length-1-i), (i+1, length-2-i)])
        self.constraints.append([(0,0), (1,1), (2,2)])
        self.constraints.append([(0,2), (1,1), (2,0)])
