class Csp:
    def __init__(self, dictionary, frequecy_list, constraints):
        self.dictionary = dictionary
        self.frequecy_list = frequecy_list
        self.constraints = constraints
        self.debug = False
        self.number_expanded_nodes = 0

    def get_all_constraints(self):
        return self.constraints.constraints

    def get_constraint_of_variable(self, x):
        result = []
        for c in self.constraints.constraints:
            for node in c:
                if node == x:
                    result.append(c)
        return result

    def is_in_dictionary(self, word):
        return word in self.dictionary

    def is_positive_frequency(self, pair):
        if self.frequecy_list[pair] > 0:
            return True
        return False
    def is_on_debug_mode(self):
        return self.debug
