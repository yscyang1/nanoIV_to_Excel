from IVBlock import *

class Tab:
	title_ = ''
	electrolytelist_ = []


	def __init__(self, ivblock):
		self.title_ = ivblock.modification()
		return

	def set_title(self, title):
		self.title_ = title
		return

	def title(self):
		return self.title_

	def AddIVBlock(self, ivblock):
		addelectrolyte = True

		for i in range(len(self.electrolyte_)):
			if ivblock.electrolyte() == self.electrolytelist_[i].title():
				self.tablist_[i].AddIVBlock(ivblock)
				addtab = False

		if addtab == True:
			self.AddTab(ivblock)

		return