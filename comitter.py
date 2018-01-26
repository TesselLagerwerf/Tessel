#! /usr/bin/env python

import os

EmptyFile = open("counter", 'a')

num = range(0,5)

os.system('git pull')

for i in num:
	EmptyFile.write("1")
	os.system('git add --all :/')
	os.system('git commit -m "Adding a 1"')
	os.system('git push')
	os.system('git config --global push.default matching')
EmptyFile.close()

print "Done!"




















