import re

stock = {}

def setTupple(cmd, line):
	name = cmd[0]
	delay = cmd[-1]
	need = {}
	result = {}

	parenthesis = line.strip().split("(")
	nd = parenthesis[1].strip().split(")")[0].split(";")
	res = parenthesis[2].strip().split(")")[0].split(";")

	for n in nd:
		tmp = n.split(":")
		need[tmp[0]] = tmp[1]

	for r in res:
		tmp = r.split(":")
		if (tmp[0] not in stock):
			stock[tmp[0]] = 0
		result[tmp[0]] = tmp[1]
	
	return (name, need, result, delay)

def	parse_file(fd):
	t_list = fd.read().splitlines()
	process = []
	optimize = []

	for i, lines in enumerate(t_list):
		line = lines.strip().split("#")[0]
		if (line != ""):
			cmd = line.strip().split(":")
			if (len(cmd) == 2):
				if (cmd[0] != "optimize"):
					stock[cmd[0]] = cmd[1]
				else:
					tmp = re.sub('[()]', '', cmd[1])
					optimize.extend(tmp.strip().split(";"))
			else:
				process.append(setTupple(cmd, line))
	print stock
	print process
	print optimize