# Exercise 21 - Write to a File

# 'r+' means both read and write mode
# opening a file with 'w' will immediately delete file contents
# numbers and objects must be strings in order to write to file

f_name = raw_input("Enter file name: ") + ".txt"

# Better Programming Practice for this
# because we use and close
# similar to C# 'using'

with open(f_name, 'w') as a_file:
    a_file.write("Hello World!")

# Alternative
open_file = open(f_name, 'r')
print(open_file.readline())
open_file.close() # this is bad if the program crashes before this
