from IVBlock import *
from ElectrolyteCategory import *

class ModificationCategory(object):
	


	def __init__(self, ivblock):
		self.title_ = ''
		self.electrolytelist_ = []
		self.title_ = ivblock.modification()
		self.AddIVBlock(ivblock)
		return



	def AddIVBlock(self, ivblock):
		addelectrolyte = True

		for i in range(len(self.electrolytelist_)):
			if ivblock.electrolyte() == self.electrolytelist_[i].title():
				self.electrolytelist_[i].AddIVBlock(ivblock)
				addelectrolyte = False

		if addelectrolyte == True:
			self.AddElectrolyte(ivblock)

		return

	def AddElectrolyte(self, ivblock):
		electrolyte = ElectrolyteCategory(ivblock)
		self.electrolytelist_.append(electrolyte)
		return



	def set_title(self, title):
		self.title_ = title
		return

	def title(self):
		return self.title_

	def electrolytelist(self):
		return self.electrolytelist_

