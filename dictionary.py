students= {
    "Anu" :340,
    "Teena" :458,
    "John" :300
}
asc_by_name = dict(sorted(students.items()))
print("SORTED BY NAME(ascending):")
print(asc_by_name)
desc_by_name = dict(sorted(students.items(),reverse=True))
print("SORTED BY NAME(descending):")
print(desc_by_name)