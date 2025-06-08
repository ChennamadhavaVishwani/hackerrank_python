
n = int(input().strip())

initial_set = set(map(int, input().strip().split()))


m = int(input().strip())


for _ in range(m):
    operation_info = input().strip().split()
    operation = operation_info[0]
    length_of_other_set = int(operation_info[1])  

    other_set = set(map(int, input().strip().split()))

    if operation == "intersection_update":
        initial_set.intersection_update(other_set)
    elif operation == "update":
        initial_set.update(other_set)
    elif operation == "symmetric_difference_update":
        initial_set.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        initial_set.difference_update(other_set)

print(sum(initial_set))
