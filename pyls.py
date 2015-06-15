#!/usr/bin/python

import os
import sys

def list_directory(directory='.'):
	os.system("/usr/bin/ls -hal %s | /usr/bin/grep '^d'; /usr/bin/ls -hal %s | /usr/bin/grep '^[^dt-]'; /usr/bin/ls -hal %s | /usr/bin/grep '^-'" % (directory, directory, directory))

def main():
	if sys.argv[1:]:
		list_directory(sys.argv[1])
	else:
		list_directory()

if __name__ == "__main__":
	main()

