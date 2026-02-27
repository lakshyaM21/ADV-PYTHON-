""" 


NAME - LAKSHYA MANSHARAMANI 
CSE- AIML , SECTION- B 
ENROLLEMENT NO. - 0157AL231117
6TH SEM, LNCT&S 
ADVANCE PYTHON BATCH - 19 
WED-FRI, 2:40- 5:00 P.M.



"""


# Q1 Reverse an Array

arr = [1,2,3,4,5]
l = 0
r = len(arr) - 1

while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

print(arr)


# Q2 Find the Maximum & Minimum Element

arr = [4,2,9,1,5]

print("Max:", max(arr))
print("Min:", min(arr))


# Q3 Find the Sum of Elements

arr = [1,2,3,4,5]
sum1 = 0
for i in arr:
    sum1+= i

print(sum1)


# Q4 Find the Second Largest Element

arr = [10, 20, 4, 45, 99]
arr = list(set(arr))   
arr.sort()

if len(arr) >= 2:
    print(arr[-2])
else:
    print("No second largest element exist")



# Q5 Count Frequency of Elements

arr = [1,2,2,3,1,4,2]
seen = []

for i in arr:
    if i not in seen:
        print(i, "-", arr.count(i))
        seen.append(i)



# Q6 Check if Array is Sorted

arr = [1,2,3,4,5]

if arr== sorted(arr):
    print("Array is sorted")
else:
    print("Not sorted")



# Q7  Rotate array to the right by k positions.

arr=[1,2,3,4,5,6,7]
k=int(input("enter the k positions u want to move:"))
k=k%len(arr)
new_arr= arr[-k:]+arr[:-k]
print(arr)
print(new_arr)


# Q8 Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

arr=[2,3,4,1,5,6,7]
print(arr)
target=int(input("enter your target:"))
till_last=len(arr)
for i in range(till_last):
    for j in range(i+1,till_last):
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])
            

# Q9 Remove Duplicates from Array: Remove duplicates from the array while maintaining order.

arr=[1,1,2,2,3,3,1,2,4,5,6,7,8,9,2,2]
seen=set()
res=[]
for i in arr:
    if i not in seen:
        seen.add(i)
        res.append(i)

print(res)


# Q10 Merge Two Sorted Arrays

arr1= [1,2,2,3,4,5]
arr2= [1,2,3,4,6,7]
i = 0
j = 0
res = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        res.append(arr1[i])
        i += 1
    else:
        res.append(arr2[j])
        j += 1

# add remaining elements
while i < len(arr1):
    res.append(arr1[i])
    i += 1

while j < len(arr2):
    res.append(arr2[j])
    j += 1

print(res)


# Q11 Remove given Element from Array

arr = [1,2,3,2,4,2,5]
print(arr)
element =int(input("enter ele you want to remove: "))

arr = [i for i in arr if i != element]
print(arr)


# Q12 Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

arr=[1,2,3,5]
n=5
total= (n*(n+1))//2
arr_sum=sum(arr)
print(total-arr_sum)
    

# Q13 Find Duplicates in an Array

arr = [1,2,3,2,4,5,1,5,4,2,1,7,9]
duplicates=set()
seen=set()
for i in arr:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)        
print(list(duplicates))


# Q14 Find Intersection of Two Arrays: Find the common elements between two arrays.

arr1=[1,2,3,4,5,6,7,6,5,4,3,2,1]
arr2=[13,2,1,4,54,32,67]

res=list(set(arr1) & set(arr2))
print(res)


# Q15 Find Union of Two Arrays

arr1=[1,2,3,4,5,6,7,6,5,4,3,2,1]
arr2=[13,2,1,4,54,32,67]

res=list(set(arr1) | set(arr2))
res.sort()
print(res)


# Q16 Check if Two Arrays Are Equal: if two arrays contain the same elements

arr1 = [1,2,3,4]
arr2 = [4,3,2,1]

print(sorted(arr1) == sorted(arr2))


# Q17  Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

arr = [16,17,4,3,5,2]
leaders = []
for i in range(len(arr)):
    if arr[i] >= max(arr[i:]):  
        leaders.append(arr[i])

print(leaders)


# Q18 Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.

arr = [0,1,0,3,12]
non_zero = []
zero_count = 0

for i in arr:
    if i == 0:
        zero_count += 1
    else:
        non_zero.append(i)

res = non_zero + [0]*zero_count
print(res)


# Q19  Find Subarray with Given Sum

arr=[1,2,3,7,5]
target=12
start=0
c_sum=0
for i in range(len(arr)):
    c_sum+=arr[i]

    while c_sum>target:
        c_sum-=arr[start]
        start+=1

    if c_sum==target:
        arr=arr[start:i+1]
        print(arr)

# Q20  Rotate Array to the Left by k Positions

arr=[1,2,3,4,5]
k=int(input("enter k: "))
k=k%len(arr)
arr=arr[k:]+arr[:k]
print(arr)

# Q21  Find the Kth Smallest Element

arr=[7,10,4,3,20,15]
k=int(input("enter kth samllest value: "))
arr.sort()
print(arr[k-1])

# Q22 Find All Subarrays

arr=[1,2,3,4]
subarray=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        subarray.append(arr[i:j+1])
        
print(subarray)
        

# Q23 Maximum Sum Subarray (Kadane's Algorithm)

arr = [1,-1,3,2,1,-2]
current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)


# Q24 Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.

arr = [1,2,3,4,5,6,7,8]
arr.sort()
res = []
l = 0
r = len(arr) - 1

while l <= r:
    if l != r:
        res.append(arr[r])
        res.append(arr[l])
    else:
        res.append(arr[l])
    l += 1
    r -= 1

print(res)


# Q25  Find Majority Element: Find the element that appears more than n/2 times.

arr = [2,2,1,2,3,2,2]
n = len(arr)
for x in arr:
    if arr.count(x) > n//2:
        print("Majority:", x)
        break
else:
    print("No Majority")


# Q26  Find Peak Element: A peak element is greater than its neighbors. Find one such element.

arr=[5,3,2,1,7]
found=False
for i in range(len(arr)):
    if (i==0 or arr[i]> arr[i-1]) and (i==len(arr)-1 or arr[i]>arr[i+1]):
        print("peak :", arr[i])
        found=True 
        
if not found:
    print("no such peak element")
    

# Q27  Find the First Missing Positive: Find the smallest positive integer missing in the array.

arr = [3,4,-1,1]
s = set(arr)
i = 1
while True:
    if i not in s:
        print("missing no.",i)
        break
    i += 1


# Q28 Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.

arr = [2,0,2,1,1,0]
c0 = arr.count(0)
c1 = arr.count(1)
c2 = arr.count(2)
arr = [0]*c0 + [1]*c1 + [2]*c2

print(arr)


# Q29 Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers.

arr = [100,4,200,1,3,2]
longest = 0

for x in arr:
    count = 1
    num = x

    while num + 1 in arr:
        num = num + 1
        count += 1

    if count > longest:
        longest = count

print(longest)



#Q30 Product of Array Except Self

arr = [1,2,3,4]
result = []

for i in range(len(arr)):
    prod = 1
    for j in range(len(arr)):
        if i != j:
            prod = prod * arr[j]
    result.append(prod)

print(result)




#Q31 Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.

arr = [1,3,5,2,2]
n = len(arr)
for i in range(n):
    left = sum(arr[:i])
    right = sum(arr[i+1:])
    if left == right:
        print("Equilibrium index:", i)
        break
else:
    print("No equilibrium index")


# Q32  Find Maximum Product Pair: Find two elements whose product is maximum.
arr = [-10, -3, 5, 6]
arr.sort()
n = len(arr)
prod1 = arr[n-1] * arr[n-2]   
prod2 = arr[0] * arr[1]       
if prod1 > prod2:
    print("Pair:", arr[n-1], arr[n-2])
else:
    print("Pair:", arr[0], arr[1])



# Q33 Find Maximum Difference (j > i)
arr = [7,1,5,3,6,4]
max_diff = float('-inf')
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        max_diff = max(max_diff, arr[j] - arr[i])

print(max_diff)
























