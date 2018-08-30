# Takes a file as input
# Each row of the file should have one string
# Will read all of the lines in the file, then print all of them in alphabetic order

with open('../files/variables_i_need.txt', 'r') as open_file:
    all_text = open_file.read()

each_line = all_text.split()
each_line.sort()

for line in each_line:
    print(line)
