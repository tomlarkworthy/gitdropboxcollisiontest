#!/usr/bin/env python
'''
Script for causing git push collisions in an upstream repository.
Designed for testing dropbox's robustness to push collisions.

To use: clone --bare this repo into a Dropbox folder
then clone the dropbox repo onto several machines.
run test.py from all the clients, from the same directory
they will write garbage and commit it to the repository and push it upstream to the drop box

author:Tom Larkworthy
'''
ITERATIONS = 1000
FILES = 3    #probability of 2 simultaneous pushes colliding = 1/FILES

from sh import git
import random


for i in range(ITERATIONS):
	file_choice = random.randrange(FILES)
	rand_file_name = "test_file%s.txt" % file_choice

	with open(rand_file_name, "w") as f:
		f.write(str(random.randrange(10000))) #probably no collisions
		
	
	git("add", rand_file_name)
	git("commit", message="no msg")
	git("fetch") 
	try:
		print git("merge", strategy="ours") 
	except:
		pass#might not need a merge, which will cause an ignorable message
	git("push") #the aim is to test collisions on a Dropbox folder by this being executed concurrently





