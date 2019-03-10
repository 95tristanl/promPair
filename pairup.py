import random


def promPair():
	girls = ["Claire", "Sarah", "Jenna", "Molly", "Abby", "Izzy"]
	boys = ["Luke", "Nathan", "James", "Shane", "Damien", "Austin"]
	b_matrix = generateInterests(boys, girls)
	g_matrix = generateInterests(girls, boys)
	printer(b_matrix)
	printer(g_matrix)
	calcPairs(boys, b_matrix, g_matrix) #return a lst of pairs


def calcPairs(boys, b_matrix, g_matrix):
	possibilities = {} #all possibilities
	for boy in boys:
		for gal in b_matrix[boy]:
			pair = boy + "_" + gal
			b_val = b_matrix[boy][gal]
			g_val = g_matrix[gal][boy]
			possibilities[pair] = (b_val * b_val) + (g_val * g_val)
	poses = sorted(possibilities.items(), key=lambda kv: kv[1]) #sorted possibilites
	pairs = {}
	already = {}
	for p in poses: #walk thru and eliminate pairings where a person has a match already since data structure is sorted
		name = p[0]
		num = p[1]
		l = p[0].split("_")
		if l[0] not in already and l[1] not in already:
			pairs[name] = num
			already[l[0]] = num
			already[l[1]] = num
	printer(pairs)


def generateInterests(a_lst, b_lst):
	matrix = {}
	leng = len(b_lst)
	for a in a_lst:
		tmp_lst = b_lst[:]
		tmp_dic = {}
		for b in range(leng):
			r = random.randint(0, len(tmp_lst) - 1)
			popped = tmp_lst.pop(r)
			tmp_dic[popped] = b+1
		matrix[a] = tmp_dic
	return matrix


def printer(dic):
	print(" ")
	for key in dic:
		print(key + " : " + str(dic[key]))
	print(" ")


def printerTup(lst):
	print(" ")
	for tup in lst:
		print(tup[0] + " : " + str(tup[1]))
	print(" ")
