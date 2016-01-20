import re

stock = {} # {} => dictionary
optimize = [] # [] => list
process = [] #() => tupples

def setTupple(cmd, line):
	name = cmd[0]
	delay = cmd[-1]
	need = {}
	result = {}

	parenthesis = line.strip().split("(")
	if len(parenthesis) == 3:
		nd = parenthesis[1].strip().split(")")[0].split(";")
		res = parenthesis[2].strip().split(")")[0].split(";")
	elif len(parenthesis) == 1:
		nd = []
		res = []
	elif len(parenthesis) == 2:
		tmp = parenthesis[1].strip().split(")")[1]
		if tmp.count(':') == 2:
			nd = parenthesis[1].strip().split(")")[0].split(";")
			res = []
		else:
			nd = []
			res = parenthesis[1].strip().split(")")[0].split(";")
	else:
		print "ERROR"
		exit()

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
