from in_put import Input
from niceprint import Niceprint
from util import PriorityQueue
from assignment import Assignment
from constraint import Constraint
from csp import Csp
from domain import Domain

import time
import sys
import getopt
from random import randint

def is_consitency_value(assignment, csp, x, v):
    if not assignment.is_diff_all(v):
        return False
    all_constraints_of_x = csp.get_constraint_of_variable(x)
    filtered_constraints = assignment.filter_constraints(x, all_constraints_of_x)
    for c in filtered_constraints:
        w = ''
        for node in c:
            if node != x:
                w += assignment.value_to_letter(assignment.get_value(node))
            else:
                w += assignment.value_to_letter(v)
        if len(w) == assignment.length-1:
            if not csp.is_positive_frequency(w):
                return False
        if len(w) == assignment.length:
            if not csp.is_in_dictionary(w):
                return False
    return True

def forward_checking(assignment, csp, domain, x):
    new_domain = {}
    neighbor_nodes = []

    all_constraints_of_x = csp.get_constraint_of_variable(x)
    for c in all_constraints_of_x:
        for node in c:
            if node != x and not assignment.is_assigned(node):
                neighbor_nodes.append(node)
    neighbor_nodes = list(set(neighbor_nodes))

    for ax in assignment.get_all_assgned_variables():
        new_domain[ax] = [assignment.get_value(ax)]
    for uax in assignment.get_all_unassigned_variables():
        if uax in neighbor_nodes:
            a = []
            for v in domain[uax]:
                if (is_consitency_value(assignment, csp, uax, v)):
                    a.append(v)
            new_domain[uax] = a
            if len(a) == 0:
                return False
        else:
            new_domain[uax] = domain[uax]
    return new_domain

def greedy_heristic_domain(assignment, csp, domain, x):
    result = []
    greedy_info = []
    priority_queue = PriorityQueue()
    left_neighbor = assignment.get_left_neighbor(x) 
    letter_left_neighbor = ''
    if left_neighbor is None:
        letter_left_neighbor = '$'
    else:
        value_l_neighbor = assignment.get_value(left_neighbor)
        letter_left_neighbor = assignment.value_to_letter(value_l_neighbor)
    for v in domain[x]:
        pair = letter_left_neighbor + assignment.value_to_letter(v) 
        frequeyncy = csp.frequecy_list[pair]
        priority_queue.push((v, frequeyncy), -frequeyncy)
    while not priority_queue.isEmpty():
        v, f = priority_queue.pop()
        result.append(v)
        greedy_info.append(f)
    return result, greedy_info

def better_heristic_domain(assignment, csp, domain, x):
    result = []
    greedy_info = []
    priority_queue = PriorityQueue()
    constraints_x = csp.get_constraint_of_variable(x)
    filtered_constraints = assignment.filter_constraints(x, constraints_x)
    binary_constraints = []
    for c in filtered_constraints:
        if len(c) == 2:
            binary_constraints.append(c)
    number_of_bi_cstrs = len(binary_constraints)

    for v in domain[x]:
        f = 1
        avarage_f = 1
        if number_of_bi_cstrs > 0:
            for bi_c in binary_constraints:
                pair = ''
                for node in bi_c:
                    if node != x:
                        pair += assignment.value_to_letter(assignment.get_value(node))
                    else:
                        pair += assignment.value_to_letter(v)
              
                f *= csp.frequecy_list[pair]
            avarage_f = f
        else:
            pair = '$' + assignment.value_to_letter(v)
           
            avarage_f *= csp.frequecy_list[pair]

        priority_queue.push((v, avarage_f), -avarage_f)

    while not priority_queue.isEmpty():
        v, f = priority_queue.pop()
        result.append(v)
        greedy_info.append(f)
    return result, greedy_info

def minimum_remaining_value(assignment, csp, domain, x):
    result = []
    priority_queue = PriorityQueue()
    for v in domain[x]:
        assignment.assign(x,v)
        infer_domain = forward_checking(assignment, csp, domain, x)
        remaing_values = 0
        for unassigned_x in assignment.get_all_unassigned_variables():
            remaing_values += len(domain[unassigned_x])
        if remaing_values > 0:
            priority_queue.push(v, 1-remaing_values)
        else:
            priority_queue.push(v, 0)
        assignment.unassign(x)
    while not priority_queue.isEmpty():
        result.append(priority_queue.pop())
    return result

def get_most_constrained_variable(assignment, domain):
    unassigned_variables = assignment.get_all_unassigned_variables()
    most_variable = unassigned_variables[0]
    for x in unassigned_variables:
        if len(domain[x]) < len(domain[most_variable]):
            most_variable = x
    return most_variable

def select_unassigned_variable(assignment, csp, domain):
    if csp.most_variable == "no":
        return assignment.get_all_unassigned_variables()[0]
    if csp.most_variable == "yes":
        return get_most_constrained_variable(assignment, domain)
    
def get_domain_by_variable(assignment, csp, domain, x):
    if (csp.value_heuristic == "no"):
        return domain[x], []
    if (csp.value_heuristic == "greedy"):
        return greedy_heristic_domain(assignment, csp, domain, x)
    if (csp.value_heuristic == "better_greedy"):
        return better_heristic_domain(assignment, csp, domain, x)
    if (csp.value_heuristic == "mrv"):
        return minimum_remaining_value(assignment, csp, domain, x), []

def back_track(assignment, csp, domain):
    csp.number_expanded_nodes += 1
   
    if assignment.is_complete():
        return assignment, csp

    x = select_unassigned_variable(assignment, csp, domain)
    order_domain, greedy_info = get_domain_by_variable(assignment, csp, domain, x)

    if csp.is_on_debug_mode():
        Niceprint.print_row_debug(assignment, csp, x, order_domain, greedy_info)

    for v in order_domain:
        if (is_consitency_value(assignment, csp, x, v)):
            assignment.assign(x, v)
            if(csp.fwck == 1):
                inference_domain = forward_checking(assignment, csp, domain, x)
                if inference_domain:
                    result = back_track(assignment, csp, inference_domain)
                    if result:
                        return result
            else:
                result = back_track(assignment, csp, domain)
                if result:
                    return result
            assignment.unassign(x)
    return False

def back_tracking(dictionary, frequecy_list, letters, debug, value_heuristic="no", most_variable="no", fwck=0):
    assignment = Assignment(letters, 3)
    constraints = Constraint(3)
    csp = Csp(dictionary, frequecy_list, constraints)
    csp.debug = debug
    csp.value_heuristic = value_heuristic
    csp.most_variable = most_variable
    csp.fwck = fwck
    domain = Domain.get_default_domain(3)
    return back_track(assignment, csp, domain)

def main(argv):
    problem = 1
    debug = 0
    value_heuristic = "no"
    most_variable = "no"
    fwck = 0
    compare_mode = 0
    number_compare_inputs = 10

    try:
        opts, args = getopt.getopt(argv, "dp:h:mcfn:")
    except getopt.GetoptError:
        pass
        sys.exit(2)
    for flag, value in opts:
        if flag in ("-d"):
            debug = 1
        if flag == '-p':
            problem = int(value)
        if flag == '-h':
            value_heuristic = value
        if flag == '-m':
            most_variable = "yes"
        if flag == '-c':
            compare_mode = 1
        if flag == '-f':
            fwck = 1
        if flag == '-n':
            number_compare_inputs = int(value)

    source = Input()
    dictionary, frequecy_list = source.get_source()

    if(compare_mode):
        lot_of_letters = source.get_letter_matrix("1000_inputs")
        info = []
        r = randint(0, 900)
        for p in lot_of_letters[r:(r+number_compare_inputs)]:
            start_time1 = time.time()
            result_greedy = back_tracking(dictionary, frequecy_list, p, 0, "greedy", most_variable, fwck)
            finished_time1 = time.time()
            start_time2 = time.time()
            result_better_greedy = back_tracking(dictionary, frequecy_list, p, 0, "better_greedy", most_variable, fwck)
            finished_time2 = time.time()
            a1, c1 = result_greedy
            a2, c2 = result_better_greedy
            total_time1 = finished_time1 - start_time1
            total_time2 = finished_time2 - start_time2
            info.append((c1.number_expanded_nodes, c2.number_expanded_nodes, round(total_time1,9), round(total_time2,9)))
        Niceprint.print_row_compare(info)
    else:
        letters = source.get_letter_matrix("letters")
        start_time = time.time()
        result = back_tracking(dictionary, frequecy_list, letters[problem-1], debug, value_heuristic, most_variable, fwck)
        finished_time = time.time()
        if result:
            a, c = result
            print "++++++++++++Completed+++++++++++++"
            print "Total expanded nodes:", c.number_expanded_nodes
            print "Total time:", finished_time - start_time
            a.nice_print()
        else:
            print 
            print "No solution"

if __name__ == "__main__":
    main(sys.argv[1:])


















