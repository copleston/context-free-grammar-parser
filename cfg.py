import cfg_reader
from pprint import pprint
from collections import OrderedDict
import string
import itertools

class CFG():
	def __init__(self, v_in, t_in, r_in, s_in):
		self.variables = v_in
		self.terminals = t_in
		self.rules_0 = r_in
		self.start_0 = s_in
		self.rules = OrderedDict([("S0", "")])

		self.A_ref = {}
		self.A_dict = OrderedDict()
		self.U_ref = {}
		self.U_dict = OrderedDict()
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

		print(20*'-', "REMOVE EMPTY SET RULES", 20*'-')
		self.remove_e_rules()
		self.print_rules()
		self.unit_rules()

		#** CONVERT REMAINING RULES **
		print(20*'-', "CONVERT REMAINING RULES", 20*'-')
		while self.valid() is False:
			self.remove_e_rules()
			self.replace_variables()
			self.replace_terminals()
			self.print_rules()

		print(20*'-', "CFG IN CHOMSKY NORMAL FORM", 20*'-')
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

	def valid_rule_1(self, v):
		if len(v) == 2 and (set(v).issubset(self.variables)):
			# print("VALID 1")
			return True

	def valid_rule_2(self, v):
		if len(v) == 1 and v in self.terminals:
			# print("VALID 2")
			return True

	def valid_rule_3(self, k, v):
		if k == self.start_0 and v == "e":
			# print("VALID 3")
			return True

	def valid(self):
		"""Perform validation checks on each of the rules
		valid_rule_1 = A -> BC
		valid_rule_2 = A -> x
		valid_rule_3 = S -> e
		"""
		for k, v in self.rules.items():
			for i in v:
				if any([self.valid_rule_1(i), self.valid_rule_2(i), self.valid_rule_3(k, i)]):
					# print("Got a pass")
					pass
				else:
					# print("Got a fail")
					return False
		# print("CORRECT CFG")
		return True

	def new_start_var(self):
		self.rules["S0"] = self.rules[self.start_0]

	def unit_rules(self):
		for k, v in self.rules.items():
			for i in v:
				if i in self.variables:
					self.rules[k].remove(i)
					self.rules[k].extend(self.rules[i])

	def remove_e_rules(self):
		e_vars = []
		e_dict = OrderedDict()
		for k, v in self.rules.copy().items():
			for x in v:
				if x == "e":
					e_vars.append(k)
		for k, v in self.rules.copy().items():
			e_set = []
			for i, x in enumerate(v):
				if len(x) != 1:
					if any(j in list(x) for j in e_vars):
						y = list(x)
						for l in range(1, len(x)):
							for subset in itertools.combinations(y, l):
								if (any(subset) not in e_vars):
									if not set(subset).issubset(e_vars):
										e_set.append("".join(list(subset)))

			if len(e_set) > 0:
				e_dict[k] = list(set(e_set) - set(self.variables))
			# print(e_set)

		for i in e_dict.keys():
			self.rules[i].extend(e_dict[i])
			self.rules[i] = list(set(self.rules[i]))

		# Remove all "e"s from the CFG
		for k, v in self.rules.items():
			for i in v:
				if i == "e" and k != self.start_0:
					self.rules[k].remove(i)

	def replace_variables(self):
		for k, v in self.rules.copy().items():
			for i, x in enumerate(v):
				if len(x) > 1 and (len(x) != 2 and all(list(x)) not in self.variables):
						if x[:-1] in self.A_ref.keys():
							self.rules[k][i] = self.A_ref[x[:-1]] + x[-1]
						else:
							val = self.alpha.pop(0)
							self.A_ref[x[:-1]] = val
							if any(list(x[:-1])) not in self.variables:
								self.rules[k][i] = val + x[-1]
							self.A_dict[val] = []
							self.A_dict[val].append(x[:-1])
							self.variables.append(val)

		self.rules.update(self.A_dict)

	def replace_terminals(self):
		for k, v in self.rules.copy().items():
			for i, x in enumerate(v):
				if len(x) != 1:
					for j in x:
						if j in self.terminals:
							if j in self.U_ref.keys():
								self.rules[k][i] = self.rules[k][i].replace(j, self.U_ref[j])
							else:
								val = self.alpha.pop(0)
								self.U_ref[j] = val
								self.U_dict[val] = []
								self.U_dict[val].append(j)
								self.variables.append(val)
								self.rules[k][i] = self.rules[k][i].replace(j, self.U_ref[j])
		self.rules.update(self.U_dict)



cfg = cfg_reader.File_reader("G1.txt")
cfg.print_cfg()
G0_in = cfg.get_cfg()
G0 = CFG(G0_in["variables"], G0_in["terminals"], G0_in["rules"], G0_in["start"])
# w = input("Enter a string: ")
# w_len = len(w)
# print(w_len)
