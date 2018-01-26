#! /usr/bin/env python

import os

num = range(0,5)

for i in num:
	open("counter", 'a').write("1")
	os.system('git add --all :/')
	os.system('git commit -m "Adding a 1"')
	os.system('git push')

EmptyFile.close()

print "Done!"




















