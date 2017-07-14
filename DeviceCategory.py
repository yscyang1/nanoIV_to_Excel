from IVBlock import *
from ModificationCategory import *
from SortingOperations import *

class DeviceCategory(object):
	

	def __init__(self, ivblock):
		self.modificationlist_ = []
		self.title_ = ivblock.device()
		self.AddIVBlock(ivblock)

	

	def AddIVBlock(self, ivblock):
		addmodification = True

		for i in range(len(self.modificationlist_)):
			if ivblock.modification() == self.modificationlist_[i].title():
				self.modificationlist_[i].AddIVBlock(ivblock)
				addmodification = False

		if addmodification == True:
			self.AddModification(ivblock)

		return

	def AddModification(self, ivblock):
		modification = ModificationCategory(ivblock)
		self.modificationlist_.append(modification)
		return

	def SortModificationList(self):
		moves = 1
		while moves != 0:
			moves = 0
			for i in range(len(self.modificationlist_) - 2):
				mod1 = self.modificationlist_[i].title()
				mod2 = self.modificationlist_[i + 1].title()
				if(mod2 == 'nomod'):
					self.modificationlist_[i], self.modificationlist_[i+1] = SwitchElements(self.modificationlist_[i], self.modificationlist_[i+1])
					moves = moves + 1



	def set_title(self, title):
		self.title_ = title
		return

	def title(self):
		return self.title_

	def modificationlist(self):
		return self.modificationlist_