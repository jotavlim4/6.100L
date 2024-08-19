import func_for_find_roots as root

epsilon = 0.001
sum_of_roots = root.find_root(25, 2, epsilon) + root.find_root(-8, 3, epsilon) + root.find_root(16, 4, epsilon)
print(sum_of_roots)
