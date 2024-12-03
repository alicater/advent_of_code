def calc_distance (input_file):
    left_list = []
    right_list = []
    with open(input_file, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    # print(left_list)
    # print(right_list)

    total = 0
    for i in range(len(left_list)):
        left_num = left_list[i]
        right_num = right_list[i]
        difference = left_num - right_num
        if difference < 0:
            difference = -difference
        total += difference

    print(f"Total Distance: {total}")

def sim_score(input_file):
    left_list = []
    right_list = []
    with open(input_file, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    similarity_score = 0
    for left in left_list:
        count_right = right_list.count(left)
        similarity_score += left*count_right

    print(similarity_score)


input_file = "day1.txt"
calc_distance(input_file)
sim_score(input_file)
