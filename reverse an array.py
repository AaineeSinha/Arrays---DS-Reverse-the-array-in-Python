n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
print(*arr[::-1])
