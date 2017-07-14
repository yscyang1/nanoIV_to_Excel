import StringOperations as string


class IVBlock(object):

	


	def __init__(self):
		self.device_ = ''

		self.date_ = ''
		self.time_ = ''

		self.modification_ = ''

		self.concentration_string_ = ''
		self.concentration_int_ = 0

		self.electrolyte_ = ''

		self.pH_ = ''

		self.index_ = ''

		self.data_ = ''

		self.norows_ = 0
		self.nocols_ = 0

	##Get/Set
	def set_device(self, device):
		self.device_ = device

		return

	def device(self):
		
		return self.device_

	def set_date(self, date):
		self.date_ = date

		return
	
	def date(self):

		return self.date_


	def set_time(self, time):
		self.time_ = time

		return

	def time(self):

		return self.time_


	def set_modification(self, modification):
		self.modification_ = modification

		return

	def modification(self):

		return self.modification_


	def set_electrolyte(self, electrolyte):
		self.electrolyte_ = electrolyte

		return

	def electrolyte(self):

		return self.electrolyte_


	def set_concentration_string(self, concentration_string):
		self.concentration_string_ = concentration_string
		
		return

	def concentration_string(self):
		
		return self.concentration_string_


	def set_concentration_int(self, concentration_int):
		self.concentration_int_ = concentration_int
		
		return

	def concentration_int(self):
		
		return self.concentration_int_


	def set_pH(self, pH):
		self.pH_ = pH

		return

	def pH(self):
		
		return self.pH_

	def set_index(self, index):
		self.index_ = index
		
		return 

	def index(self):
		
		return self.index_

	def set_data(self, data):
		self.data_ = data
		
		return

	def data(self):
		
		return self.data_
		

	def set_norows(self, norows):
		self.norows_ = norows
		return

	def norows(self):
		return self.norows_

	def set_nocols(self, nocols):
		self.nocols_ = nocols
		return

	def nocols(self):
		return self.nocols_