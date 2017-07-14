from IVBlock import *
from SortingOperations import *


class ConcentrationCategory(object):
	


	def __init__(self, ivblock):
		self.title_ = ''
		self.ivblocklist_ = []
		self.title_ = ivblock.concentration_string()
		self.AddIVBlock(ivblock)
		return

	def AddIVBlock(self, ivblock):
		self.ivblocklist_.append(ivblock)

	def ivblocklist(self):
		return self.ivblocklist_

	def SortIVBlockList(self):
		moves = 1
		while moves != 0:
			moves = 0
			for i in range(len(self.ivblocklist_) - 1):
				print('DEVICE = ' + str(self.ivblocklist_[i].time()))
				datelist1 = self.ivblocklist_[i].date().split('-')

				#if format is YY/MM/DD
				if len(datelist1) != 3:
					datelist1 = self.ivblocklist_[i].date().split('/')
				datelist2 = self.ivblocklist_[i+1].date().split('-')
				if len(datelist2) != 3:
					datelist2 = self.ivblocklist_[i].date().split('/')


				print (self.ivblocklist_[i].device() + '\n')
				print (self.ivblocklist_[i].modification() + '\n')
				print(self.ivblocklist_[i].concentration_string() + '\n')
				print (self.ivblocklist_[i+1].device() + '\n')
				print (self.ivblocklist_[i+1].modification() + '\n')
				print(self.ivblocklist_[i+1].concentration_string() + '\n')
				timelist1 = self.ivblocklist_[i].time().split(':')
				timelist2 = self.ivblocklist_[i+1].time().split(':')
				
				if datelist1[0] > datelist2[0]:
					self.ivblocklist_[i], self.ivblocklist_[i+1] = SwitchElements(self.ivblocklist_[i], self.ivblocklist_[i+1])
					moves = moves + 1


				elif datelist1[0] == datelist2[0]:
					if datelist1[1] > datelist2[1]:
						self.ivblocklist_[i], self.ivblocklist_[i+1] = SwitchElements(self.ivblocklist_, self.ivblocklist_[i+1])
						moves = moves + 1

					elif datelist1[1] == datelist2[1]:
						if datelist1[2] > datelist2[2]:
							self.ivblocklist_[i], self.ivblocklist_[i+1] = SwitchElements(self.ivblocklist_, self.ivblocklist_[i+1])
							moves = moves + 1


						elif datelist1[2] == datelist2[2]:
							if timelist1[0] > timelist2[0]:
								self.ivblocklist_[i], self.ivblocklist_[i+1] = SwitchElements(self.ivblocklist_[i], self.ivblocklist_[i+1])
								moves = moves + 1

							elif timelist1[0] == timelist2[0]:
								if timelist1[1] > timelist2[1]:
									self.ivblocklist_[i], self.ivblocklist_[i+1] = SwitchElements(self.ivblocklist_[i], self.ivblocklist_[i+1])
									moves = moves + 1

								elif timelist1[1] == timelist2[1]:
									if timelist1[2] > timelist2[2]:
										self.ivblocklist_[i], self.ivblocklist_[i+1] = SwitchElements(self.ivblocklist_[i], self.ivblocklist_[i+1])
										moves = moves + 1

		return




	def set_title(self, title):
		self.title_ = title
		return

	def title(self):
		return self.title_