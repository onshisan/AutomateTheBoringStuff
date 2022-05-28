# Local scopes cannot use variables in other scopes
def spam():
	eggs = 99
	bacon()
	print(eggs)

def bacon():
	ham = 101
	eggs = 0

spam()

# Global variables can be read from a local scope
def spam2():
	print(eggs)
eggs = 42
spam2()
print(eggs)

# Local and global variables with the same name
def spam3():
	eggs = 'spam local'
	print(eggs)

def bacon3():
	eggs = 'bacon local'
	print(eggs)
	spam3()
	print(eggs)

eggs = 'global'
bacon3()
print(eggs)