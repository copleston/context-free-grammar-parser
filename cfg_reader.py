class File_reader():
	cfg = {
		"variables" : [],
		"terminals" : [],
		"rules" : [],
		"start" : ""
	}

	def __init__(self, input_file = None):
		if input_file is None:
			"No file has been input!"
		else:
			self.read_cfg(input_file)
			self.read_input()

	def read_cfg(self, input_file):
		with open(input_file, 'r') as f:
			read_data = f.readlines() # Turn the input into a list

		global input_as_list # Make the input data available to the rest of hte application
		input_as_list = [i.strip('\n') for i in read_data if len(i) > 1] # Remove new-line characters and empty lines from the input

	def read_input(self):
		r = self._Reader()
		for i in input_as_list: # Change the read type to the correct specification using the strategy pattern
			if i == "/VARIABLES":
				r.set_read_type(self._Read_variables())
			elif i == "/TERMINALS":
				r.set_read_type(self._Read_terminals())
			elif i == "/RULES":
				r.set_read_type(self._Read_rules())
			elif i == "/START":
				r.set_read_type(self._Read_start())
			else:
				r.read(i)

	def get_cfg(self): # Return the CFG dictionary object
		return self.cfg

	def print_cfg(self): # Print each tuple of the CFG dictionary object
		print(20*'-', "REMOVE UNIT RULES", 20*'-')
		print("Variables: \t", self.cfg["variables"])
		print("Terminals: \t", self.cfg["terminals"])
		print("Rules: \t\t", self.cfg["rules"])
		print("Start: \t\t", self.cfg["start"])


	class _Reader(object):
		def __init__(self, strategy=None):
			self.action = strategy # Default strategy is set to 'None' in initialization of reader() object

		def set_read_type(self, read_type):
			self.action = read_type # Define which object will handle the reading of the line

		def read(self, line_in):
			self.action.read(self, line_in) # Use the read method of the currently defined strategy

	class _Read_tuples: # Interface for the read method
		def read(self):
			pass

	class _Read_variables(_Read_tuples): # read in variables from a comma delimited line
		@staticmethod
		def read(self, line_in):
			File_reader.cfg["variables"] = line_in.split(",")

	class _Read_terminals(_Read_tuples): # read in terminals from a comma delimited line
		@staticmethod
		def read(self, line_in):
			File_reader.cfg["terminals"] = line_in.split(",")

	class _Read_rules(_Read_tuples): # read a single rule and append it to the list of rules
		@staticmethod
		def read(self, line_in):
			File_reader.cfg["rules"].append(line_in)

	class _Read_start(_Read_tuples): # read the start variable
		@staticmethod
		def read(self, line_in):
			File_reader.cfg["start"] = line_in
