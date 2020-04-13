sequence = [0, 0]
sequence[0] = sequence[1] = 1
for i in range(12):
    sequence.append(sequence[i]+sequence[i+1])
    print("Element {a}: {b}".format(a=i+1, b=sequence[i]))
