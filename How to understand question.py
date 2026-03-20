
''' 
How to start any question
Step 1: Read input format carefully
        Check:  
                1. single number?
                2. array?
                3. string?

Step 2: Write input code FIRST
        if number:
                n = int(input())
        if array:
                n = int(input()) 
                arr = list(map(int, input().split()))   
        if string:
                s = input()

Step 3: Think Logic 
        Ask yourself:
                1. Loop needed?
                2. Condition needed?
                3. Anuy formula?

Step 4: Write Core Logic
        Example (sum):
                total = 0
                for i in arr:
                    total += i

Step 5: Print Output
                print(total)

Full Example (How to Start + Finish)

Question: Sum of array
# Step 1: Input
n = int(input())
arr = list(map(int, input().split()))

# Step 2: Logic
total = 0
for i in arr:
total += i

Step 3:
print(total)
'''



# 1. Basic logic

n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("odd")


# 2. Arrays 

arr = list(map(int, input().split()))
print(sum(arr))
print(max(arr))


# 3. Strings

s = input()
print(s[:: -1])     # reverse


# 4. Mathematics/ Numbers

n = int(input())
fact = int(input())
for i in range(1, n+1):
    fact *= i
print(fact)


# 5. patterns

for i in range(1, 5):
    print("*" * i)


# 6. sorting and searching

arr = list(map(int, input().split()))
arr.sort()
print(arr)


