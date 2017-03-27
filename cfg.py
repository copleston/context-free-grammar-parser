import cfg_reader
import pprint as pprint
from collections import OrderedDict
import string

class CFG():
	def __init__(self, v_in, t_in, r_in, s_in):
		self.variables = v_in
		self.terminals = t_in
		self.rules_0 = r_in
		self.start_0 = s_in
		self.rules = OrderedDict([("S0", "")])
		# Set up a dictionary of rules, which combines the productions for rules with the same variable
		self.in_dict = OrderedDict([(k,[]) for k in self.variables])
		self.rules.update(self.in_dict)
		self.create_rules()
		self.alpha = [i for i in list(string.ascii_uppercase) if i not in self.variables]

		# ** CREATE NEW START VARIABLE **
		print(20*'-', "CREATE NEW START VARIABLE", 20*'-')
		self.new_start_var()
		self.print_rules()

		# ** REMOVE UNIT RULES **
		print(20*'-', "REMOVE UNIT RULES", 20*'-')
		self.unit_rules()
		self.print_rules()

		# ** CONVERT REMAINING RULES **
		print(20*'-', "CONVERT REMAINING RULES", 20*'-')
		print(20*'-', "VARIABLES", 20*'-')
		self.replace_variables()
		self.print_rules()
		print(20*'-', "TERMINALS", 20*'-')
		self.replace_terminals()
		self.print_rules()


	def create_rules(self):
		for i in self.rules_0:
			rule = i.replace(" ","").split("->")
			# print("Create rules: ", rule)
			self.rules[rule[0]].append(rule[1])
			# print(self.rules)

	def print_rules(self):
		for k, v in self.rules.items():
			if type(v) == list:
				print(k, "->", "|".join(v))
			else:
				print(k, "->", v)

	def new_start_var(self):
		self.rules["S0"] = self.rules[self.start_0]

	def unit_rules(self):
		for k, v in self.rules.items():
			for i in v:
				if i in self.variables:
					self.rules[k].remove(i)
					self.rules[k].extend(self.rules[i])

	def replace_variables(self):
		# A_count = 0
		A_ref = {}
		A_dict = OrderedDict()

		for k, v in self.rules.copy().items():
			for i, x in enumerate(v):
				if len(x) > 1:
					if x[:-1] in A_ref.keys():
						self.rules[k][i] = A_ref[x[:-1]] + x[-1]
					else:
						val = self.alpha.pop(0)
						A_ref[x[:-1]] = val
						A_dict[val] = []
						A_dict[val].append(x[:-1])
						self.variables.append(val)

		self.rules.update(A_dict)

	def replace_terminals(self):
		U_ref = {}
		U_dict = OrderedDict()

		for k, v in self.rules.copy().items():
			for i, x in enumerate(v):
				if len(x) != 1:
					for j in x:
						if j in self.terminals:
							if j in U_ref.keys():
								self.rules[k][i] = self.rules[k][i].replace(j, U_ref[j])
							else:
								val = self.alpha.pop(0)
								U_ref[j] = val
								U_dict[val] = []
								U_dict[val].append(j)
								self.variables.append(val)
								self.rules[k][i] = self.rules[k][i].replace(j, U_ref[j])
		self.rules.update(U_dict)


class Var():
	def __init__(self):
		pass

def valid(x):
	if len(x) == 2:
		if (x[0] in self.variables) and (x[1] in self.variables):
			return True
	elif len(x) == 1:
		if (x in self.terminals) or (x == "e"):
			return True
	else:
		return False

class Rule():
	def __init__(self):
		pass


	var = ""
	production = []

class Production():
	def __init__(self, v_in):
		self.var = v_in

	def check_in_cnf(self):
		if len(x) == 2:
			if (x[0] in self.variables) and (x[1] in self.variables):
				return True
		elif len(x) == 1 and x in self.terminals:
			return True
		elif

for i in productions:
	if rule.var == start_variable and production == e:
		return True
	elif all(list(i) in variables):



	def refactor(self):
		pass

	def var_replace(self, this, that):
		pass



cfg = cfg_reader.File_reader("G0.txt")
cfg.print_cfg()
G0_in = cfg.get_cfg()
G0 = CFG(G0_in["variables"], G0_in["terminals"], G0_in["rules"], G0_in["start"])
