students={
    "Anu":[85,90,78],
    "Gowri":[72,68,91],
    "Vishnu":[95,88,85]
}
for name,marks in students.items():
    total=sum(marks)
    average=sum(marks)/len(marks)
    print(f"student: {name}")
    print(f"Total marks: {marks}")
    print(f"Average marks: {average:.2f}")
    print("."*20])