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

def find_similarity(left_list, right_list): 

    # left_ptr = 0 
    # # count = 0 
    # total_sim = 0 

    # while len(left_list) > 0: 
    #     count = 0 
    #     target = left_list[left_ptr]

    #     for i in range(len(right_list)): 
    #         if right_list[i] == target: 
    #             count += 1
    #     total_sim += (target * count)
    #     left_ptr += 1

    # return total_sim 
    right_counts = {} 
    for num in right_list: 
        if num in right_counts: 
            right_counts[num] += 1
        else: 
            right_counts[num] = 1 
    
    total_similarity = 0 

    for target in left_list: 
        count = right_counts.get(target, 0)
        total_similarity += target * count 

    return total_similarity

left_list, right_list = parse_input("input.txt")
similarity= find_similarity(left_list, right_list)
print(similarity) 