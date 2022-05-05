from math import ceil

inp = input()
inp = inp.split(" ")

for i in range(len(inp)):
    inp[i] = int(inp[i])

print( ceil(inp[0]/inp[2]) * ceil(inp[1]/inp[2]))
