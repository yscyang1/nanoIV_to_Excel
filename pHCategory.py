from IVBlock import *
from ConcentrationCategory import *
from SortingOperations import *

class pHCategory(object):
	


	def __init__(self, ivblock):
		self.title_ = ''
		self.concentrationlist_ = []
		self.title_ = ivblock.pH()
		self.AddIVBlock(ivblock)
		return

	

	def AddIVBlock(self, ivblock):
		addconcentration = True

		for i in range(len(self.concentrationlist_)):
			if ivblock.concentration_string() == self.concentrationlist_[i].title():
				self.concentrationlist_[i].AddIVBlock(ivblock)
				addconcentration = False

		if addconcentration == True:
			self.AddConcentration(ivblock)

		return

	def AddConcentration(self, ivblock):
		concentration = ConcentrationCategory(ivblock)
		self.concentrationlist_.append(concentration)
		return

	def SortConcentrationList(self):
		moves = 1
		while moves != 0:
			moves = 0
			for i in range(len(self.concentrationlist_) - 1):
				concentration1 = int(self.concentrationlist_[i].title().replace('mM', ''))
				concentration2 = int(self.concentrationlist_[i + 1].title().replace('mM', ''))
				
				
				if concentration1 > concentration2:
				
					self.concentrationlist_[i], self.concentrationlist_[i+1] = SwitchElements(self.concentrationlist_[i], self.concentrationlist_[i+1])				
				
					moves = moves + 1





	def set_title(self, title):
		self.title_ = title
		return

	def title(self):
		return self.title_

	def concentrationlist(self):
		return self.concentrationlist_