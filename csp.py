class Csp:
    def __init__(self, dictionary, frequency_list, constraints):
        self.dictionary = dictionary
        self.frequency_list = frequency_list
        self.constraints = constraints
        self.debug = False
        self.number_expanded_nodes = 0
        self.value_heuristic = "no"

    def get_all_constraints(self):
        return self.constraints.constraints

    def get_constraint_of_variable(self, x):
        result = []
        for c in self.constraints.constraints:
            for node in c:
                if node == x:
                    result.append(c)
        return result

    def get_all_bi_constrains(self):
        result = []
        for c in self.constraints.constraints:
            if len(c) == 2:
                result.append(c)
        return result

    def is_in_dictionary(self, word):
        return word in self.dictionary

    def is_normal_positive_frequency(self, pair):
        return self.is_positive_frequency_by_position(pair, 0)

    def is_positive_frequency_by_position(self, pair, position_of_pair):
        if self.frequency_list[pair][position_of_pair] > 0:
            return True
        return False

    def is_on_debug_mode(self):
        return self.debug

    def get_normal_pair_frequency(self, pair):
        return self.get_new_pair_frequency(pair, 0)

    def get_new_pair_frequency(self, pair, position_of_pair):
        return self.frequency_list[pair][position_of_pair]

    def is_use_better_greedy(self):
        return self.value_heuristic == "better_greedy" or self.value_heuristic == "more_better"

    def get_position_pair(self, x1, x2):
        if x1 is None or x2 is None:
            return 0
        for bi_c in self.get_all_bi_constrains():
            if (x1 == bi_c[0] and x2 == bi_c[1]) or (x1 == bi_c[1] and x2 == bi_c[0]):
                if (bi_c[0][0] == 0 and bi_c[1] != (0,2)) or (bi_c[0][1] == 0 and bi_c[1] != (2,0)):
                    return 0
        return 1


