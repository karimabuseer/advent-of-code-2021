with open('input_depths.txt') as depths_file:
    depths_array = depths_file.readlines()

depths_array = [int(depth.strip()) for depth in depths_array] 

answer_counter = 0
i = 0 
for depth in depths_array:
    current_sliding_window = depth + depths_array[i + 1] + depths_array[i + 2]
    next_sliding_window = depths_array[i + 1] + depths_array[i + 2] + depths_array[i + 3]
    if current_sliding_window < next_sliding_window:
        answer_counter += 1
    if i == len(depths_array) - 4:
        break
    i += 1


print(answer_counter)
