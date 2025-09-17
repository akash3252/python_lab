color_input=input("enter color names seperated by commas")
color_list=[color.strip() for color in color_input.split(',')]
if len(color_list)>0:
    print("first color",color_list[0])
    print("second color",color_list[-1])
else:
    print("no colors")