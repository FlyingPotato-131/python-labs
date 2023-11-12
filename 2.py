instr = input()
lst = instr.split(' ')
lst = [int(i) for i in lst]
lst.sort()
print(lst[2] - lst[0])
