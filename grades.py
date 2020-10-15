score = float(input())
max_score = float(input())
percent_score = (score / max_score)*100

if percent_score >= 90:
    print("A")
elif percent_score >= 80 and percent_score < 90:
    print("B")
elif percent_score >= 70 and percent_score < 80:
    print("C")
elif percent_score >= 60 and percent_score < 70:
    print("D")
else:
    print("F")