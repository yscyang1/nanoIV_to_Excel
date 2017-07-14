from IVBlock import *
from pHCategory import *
from SortingOperations import *


class ElectrolyteCategory(object):



	def __init__(self, ivblock):
		self.title_ = ''
		self.pHlist_ = []
		self.title_ = ivblock.electrolyte()
		self.AddIVBlock(ivblock)
		return

	

	def AddIVBlock(self, ivblock):
		addpH = True

		for i in range(len(self.pHlist_)):
			if ivblock.pH() == self.pHlist_[i].title():
				self.pHlist_[i].AddIVBlock(ivblock)
				addpH = False

		if addpH == True:
			self.AddpH(ivblock)

		return

	def AddpH(self, ivblock):
		pH = pHCategory(ivblock)
		self.pHlist_.append(pH)
		return


	def SortpHList(self):
		moves = 1
		while moves != 0:
			moves = 0
			for i in range(len(self.pHlist_) - 1):
				pH1 = int(self.pHlist_[i].title().replace('pH', ''))
				pH2 = int(self.pHlist_[i + 1].title().replace('pH', ''))

				if pH1 > pH2:
					self.pHlist_[i], self.pHlist_[i+1] = SwitchElements(self.pHlist_[i], self.pHlist_[i+1])
					moves = moves + 1



	def set_title(self, title):
		self.title_ = title
		return

	def title(self):
		return self.title_


	def pHlist(self):
		return self.pHlist_