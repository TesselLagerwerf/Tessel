#! /usr/bin/env python

import os


EmptyFile = open("counter", 'a')

num = range(0,250)

for i in num:
	os.system('git pull')
	EmptyFile.write("1")
	os.system('git add --all :/')
	os.system('git commit -m "adding a 1"')
	os.system('git push')
EmptyFile.close()

print "Done!"




















