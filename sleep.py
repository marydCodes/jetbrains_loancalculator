A = int(input())
B = int(input())
actual_hrs = int(input())

# check if A <= B
if A <= B:
    if actual_hrs < A:
        print("Deficiency")
    elif actual_hrs > B:
        print("Excess")
    elif actual_hrs > A and actual_hrs < B:
        print("Normal")