spam = ['cat','bat','rat','elephant']

print(spam[0:4])
print(spam[1:3])

print(spam[0:-1])

print(spam[:2])
print(spam[1:])

print(len(spam))

spam[1] = 'aardvark'
print(spam)

spam[2] = spam[1]
print(spam)

print([1, 2, 3] + ['A', 'B', 'C'])
print(['X','Y','Z'] * 3)

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

spam = ['cat','bat','rat','elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)