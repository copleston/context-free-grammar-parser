import cfg_reader
import pprint as pprint
from collections import OrderedDict

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



	def valid(self, x):
		if len(x) == 2:
			if (x[0] in self.variables) and (x[1] in self.variables):
				return True
		elif len(x) == 1:
			if (x in self.terminals) or (x == "e"):
				return True
		else:
			return False

	def create_rules(self):
		for i in self.rules_0:
			rule = i.replace(" ","").split("->")
			# print(rule)
			self.rules[rule[0]].append(rule[1])

	def print_rules(self):
		for k, v in self.rules.items():
			print(k, "->", "|".join(v))

	def new_start_var(self):
		self.rules["S0"] = self.rules[self.start_0]

	def unit_rules(self):
		for k, v in self.rules.items():
			for i in v:
				if i in self.variables:
					self.rules[k].remove(i)
					self.rules[k].extend(self.rules[i])

	def convert_remaining_rules(self):
		pass



class Rule():
	def __init__(self):
		pass

	variable = ""
	production = []


class Var():
	def __init__(self):
		pass



cfg = cfg_reader.File_reader("G0.txt")
cfg.print_cfg()
G0_in = cfg.get_cfg()
G0 = CFG(G0_in["variables"], G0_in["terminals"], G0_in["rules"], G0_in["start"])
