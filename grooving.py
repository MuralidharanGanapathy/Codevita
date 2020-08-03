for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    temp_arr = arr
    buffer_arr = [0] * len(arr)
    
    counter = 0
    
    while(buffer_arr != arr):
        counter += 1
        buffer_arr = [0] * len(arr)
        for i in range(len(arr)):
            buffer_arr[arr[i] - 1] = temp_arr[i]
            
        temp_arr = buffer_arr
    print(counter)
