nums = []
[nums.append(int(input())) for _ in range(100)]
max_value = max(nums)
print(f'{max_value}')
print(f'{nums.index(max_value)+1}')