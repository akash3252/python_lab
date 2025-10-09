words=input("enter some  words")
vowels='aeiouAEIOU'
vowels_list=[char for char in words if char in vowels]
print("vowels in the words",vowels_list)