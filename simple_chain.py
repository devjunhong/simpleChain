#!/usr/bin/python

class Block(object):
	def __init__(self):
		print("Block") 

class Chain(object): 
	def __init__(self): 
		print("Chain") 

def main(): 
	b = Block()
	c = Chain() 

if __name__ == "__main__":
	main()