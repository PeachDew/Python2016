a = [9,8,7,6,5,4,3,2,1]

def linear_search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1

print("Linear: ", linear_search(a,2), linear_search(a, 10))

def binary_search(a, target):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print("Binary: ", binary_search(a,2), binary_search(a, 10))

def binary_recur(a, target, high, low):
    mid = (high + low) // 2
    if low > high:
        return -1
    elif a[mid] == target:
        return mid
    elif a[mid] > target:
        return binary_recur(a, target, high, mid + 1)
    else:
        return binary_recur(a, target, mid - 1, low)

print("RBinary: ", binary_recur(a, 2, len(a), 0), binary_recur(a, 10, len(a), 0))

def bubble(a):
    passes = len(a) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(passes):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        passes -= 1
    return a

print("Bubble sort: ", bubble(a))

def insertion(a):
    for i in range(1,len(a)):
        j = i - 1
        temp = a[i]
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return a

def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        return quicksort([x for x in a[1:] if x < a[0]]) + [a[0]] + quicksort(x for x in a[1:] if x>= a[0])                         
    
print("Insertion sort: ", insertion(a))
print("Quick sortL ", quicksort(a))
            
