def x (arr):
    n = len(arr)

    for i in range (n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
              min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i] 

        return arr
    

number = input("Enter a list: ").split()
number = [int(num) for num in number]

sorted_number = x (number)

print("Sorted list:", sorted_number)
                           
