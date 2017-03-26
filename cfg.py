import cfg_reader

class CFG():
	def __init__(self, v_in, t_in, r_in, s_in):
		self.variables = v_in
		self.terminals = t_in
		self.rules = r_in
		self.start = s_in

	def create_rules(self):
		for i in self.rules:
			rule = i.replace(" ","").split("->")
			print(rule)


class Rule():
	def __init__(self):
		pass

	variable = ""
	production = []



cfg = cfg_reader.File_reader("G0.txt")
G0_in = cfg.get_cfg()

G0 = CFG(G0_in["variables"], G0_in["terminals"], G0_in["rules"], G0_in["start"])
print(id(G0))
G0.create_rules()
