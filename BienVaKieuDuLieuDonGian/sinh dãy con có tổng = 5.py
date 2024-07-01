def find_subsets_with_repetition(numbers, target_sum, partial=[]):
    current_sum = sum(partial)

    # Kiểm tra nếu tổng của dãy con hiện tại bằng target_sum
    if current_sum == target_sum:
        print(partial)
        return

    # Nếu tổng vượt quá target_sum thì dừng
    if current_sum >= target_sum:
        return

    for i in range(len(numbers)):
        find_subsets_with_repetition(numbers, target_sum, partial + [numbers[i]])

# Danh sách các số
numbers = [1, 2, 3, 4, 5]

# Tổng cần tìm
target_sum = 5

# Tìm các dãy con có tổng bằng target_sum
find_subsets_with_repetition(numbers, target_sum)
