import os

def parse_input(filename): 
    left_list = []
    right_list = [] 

    # open + parse input file 
    with open(filename, 'r') as file: 
        for line in file: 
            left, right = line.strip().split()

            left_list.append(int(left))
            right_list.append(int(right))

    return left_list, right_list

def find_distance(left_list, right_list): 

    # sort both lists 
    left_list.sort()
    right_list.sort()

    # initialize pointers
    left_ptr = 0
    right_ptr = 0  
    total = 0 # initialize counter 

    while left_ptr < len(left_list) and right_ptr < len(right_list): 
        diff = abs(left_list[left_ptr] - right_list[right_ptr])
        total += diff 

        left_ptr += 1
        right_ptr += 1 
    
    return total


left_list, right_list = parse_input("input.txt")
total_distance = find_distance(left_list, right_list)
print(total_distance)