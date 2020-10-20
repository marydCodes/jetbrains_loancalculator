N = int(input())
print(f"You will now receive {N} integer values.")
in_list = []

for i in range(N):
    n = int(input())
    in_list.append(n)

for num in in_list:
    if num%7==0:
        print(num**2)


