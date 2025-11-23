file = open("file2.txt", "w") 
# Write multiple lines of text into the file 
file.write("hello world!\nwelcome to python programing\nThank you") 
# Close the file after writing 
file.close() 
# Create an empty list to store the lines 
list = [] 
# Open the same file in read mode ('r') 
file = open("file2.txt", "r") 
list = [line.strip() for line in file] 
# Close the file after reading 
file.close() 
# Print the list containing all lines from the file 
print(list) 