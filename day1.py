f = open('day1_input.txt', 'r')
string = f.readlines()
word = string[0]
up = word.count('(')
down = word.count(')')
print(up - down)

