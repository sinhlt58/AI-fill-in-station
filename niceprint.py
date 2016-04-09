class Niceprint:
    @classmethod
    def print_first_row(self, cells, n):
        self.print_dashes(n)
        self.print_row(cells)
        self.print_dashes(n)

    @classmethod
    def print_dashes(self, n):
        l = ''
        for i in range(n):
            l += '-'
        print l

    @classmethod
    def print_row_debug(self, assignment, csp, next_x, order_domain, greedy_info):
            first_row_cells = ['crr_state', 'crr_depth', 'expanded_n',
                'next_var', 'next_vals', 'greedy_info']
            self.print_first_row(first_row_cells, 73)
            n = assignment.length
            
            if len(order_domain) > n:
                n = len(order_domain)
            
            for i in range(n):
                cells = ['' for k in range(6)]
                if i > assignment.length - 1:
                    cells[0] = ''
                else:
                    cells[0] = assignment.get_row_letters(i)
                if i == 0:
                    cells[1] = str(len(assignment.get_all_assgned_variables()))
                    cells[2] = str(csp.number_expanded_nodes)
                    cells[3] = str(next_x)
                cells[4] = ''
                if i >= 0 and i < len(order_domain):
                    cells[4] += assignment.value_to_letter(order_domain[i])
                    cells[5] = str(round(greedy_info[i], 9))
                self.print_row(cells)
            
            self.print_dashes(73)
            print '\n'

    @classmethod
    def print_row_compare(self, info):
        n = len(info)
        first_row_cells = ["problem", "grd_nodes", "b_grd_nodes", "grd_time", "b_grd_time", "grd_ebf", "b_grd_ebf"]
        self.print_first_row(first_row_cells, 85)
        for i in range(n):
            cells = ['' for k in range(len(first_row_cells))]
            cells[0] = str(i + 1)
            for j in range(4):
                cells[j+1] = str(info[i][j])
            cells[5] = ''
            cells[6] = ''
            self.print_row(cells)
        self.print_dashes(85)
        avarage_row = ["avg"]
        for k in range(4):
            s = 0
            for t in range(n):
                s += info[t][k]
            avarage_row.append(str(s))
        self.print_row(avarage_row)
        self.print_dashes(85)
                
    @classmethod
    def print_row(self, cells):
        l = ''
        n = len(cells)
        for i in range(n):
            l += '|'
            l += cells[i]
            for s in range(12 - (len(cells[i]) + 1)):
                l += ' '
        l += '|'
        print l

    @classmethod
    def print_domain(self, assignment, domain):
        for x in domain.keys():
            line = ""
            line += str(x) + " : "
            for v in domain[x]:
                line += str(assignment.value_to_letter(v)) + ", "
            print line
        print '\n'
