from WorkBook import *
from IVBlock import *

class WorkBookList(object):
	workbooklist_ = []

	def AddIVBlock(self, ivblock):

		addworkbook = True

		for i in range(len(self.workbooklist_)):
			if ivblock.devicename() == self.workbooklist_[i].title():
				self.workbooklist_[i].AddIVBlock(ivblock)
				addworkbook = False

		if addworkbook == True:
			self.AddWorkBook(ivblock)

		return

	def AddWorkBook(self, ivblock):
		print('Adding workbook\n')
		workbook = WorkBook(ivblock)
		self.workbooklist_.append(workbook)
		return


	def SortIVBlockList(self):
		return