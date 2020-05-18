## Python code for read file and sort and print the result in alphabetical order


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in line:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)