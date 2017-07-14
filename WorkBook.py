from IVBlock import *
from Tab import *

class WorkBook(object):
	title_ = ''
	tablist_ = []
	def __init__(self, ivblock):
		self.title_ = ivblock.devicename()
		self.AddIVBlock(ivblock)

	def set_title(self, title):
		self.title_ = title
		return

	def title(self):
		return self.title_

	def AddIVBlock(self, ivblock):
		addtab = True

		for i in range(len(self.tablist_)):
			if ivblock.modification() == self.tablist_[i].title():
				self.tablist_[i].AddIVBlock(ivblock)
				addtab = False

		if addtab == True:
			self.AddTab(ivblock)

		return

	def AddTab(self, ivblock):
		print('Adding tab\n')
		tab = Tab(ivblock)
		self.tablist_.append(tab)
		return


	def SortIVBlockList(self):
		return
		