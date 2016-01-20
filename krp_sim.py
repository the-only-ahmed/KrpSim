#!/usr/bin/env python
import os
import os.path
import sys
import argparse
from parser import *
from jyim import mainProgram

def check_fileExistance(path):
	if os.path.isfile(path):
		if os.access(path, os.R_OK):
			fd = open(path, 'r')
			return fd
		else:
			print("File can't be opened")
			exit()
	else:
		print("File doesn't exist")
		exit()

def error_manager(args):
	fd = None
	if (args.file != None and args.delay != None):
		fd = check_fileExistance(args.file[0])
	else:
		print "usage: " + sys.argv[0] + " [-h] [-f FILE] [-d DELAY]"
		exit()
	try:
	   val = int(args.delay[0])
	except ValueError:
	   	print("That's not an int!")
		exit()
	if fd is not None:
		parse_file(fd)
	else:
		print "fd is None"
		exit()
	return val

def	main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="add configuration file", nargs=1)
	parser.add_argument("-d", "--delay", help="add delay", nargs=1)
	args = parser.parse_args()

	val = error_manager(args)
	mainProgram(stock, process, optimize, val)

main()
