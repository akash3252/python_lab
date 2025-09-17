color_list1=input("enter color for list 1(comma seperated: )").split(',')
print(color_list1)
color_list2=input("enter color for list 2(comma seperated: )").split(',')
print(color_list2)
unique_color=[color for color in color_list1 if color not in color_list2]
print("colors from colorlist one that not in list 2:")
print(unique_color)