from IVBlock import *
from DeviceCategory import *


class DeviceList(object):
	devicelist_ = []

	#def __init__(self):
		

	def AddIVBlock(self, ivblock):
		if(ivblock == False):
			#print('bad device!\n')
			return

		adddevice = True

		for i in range(len(self.devicelist_)):
			if ivblock.device() == self.devicelist_[i].title():
				self.devicelist_[i].AddIVBlock(ivblock)
				adddevice = False

		if adddevice == True:
			self.AddDevice(ivblock)

		return

	def AddDevice(self, ivblock):
		device = DeviceCategory(ivblock)
		self.devicelist_.append(device)

		return



	def devicelist(self):
		return self.devicelist_



	def SortCategoryTree(self):
		for device in self.devicelist_:
			device.SortModificationList()
			for modification in device.modificationlist():
				for electrolyte in modification.electrolytelist():
					electrolyte.SortpHList()
					for pH in electrolyte.pHlist():
						pH.SortConcentrationList()
						for concentration in pH.concentrationlist():
							concentration.SortIVBlockList()

		return

	def PrintCategoryTree(self):
		for device in self.devicelist_:
			print(device.title())
			for modification in device.modificationlist():
				print('\t' + modification.title())
				for electrolyte in modification.electrolytelist():
					print('\t\t' + electrolyte.title())
					for pH in electrolyte.pHlist():
						print('\t\t\t' + pH.title())
						for concentration in pH.concentrationlist():
							print('\t\t\t\t' + concentration.title())
							for ivblock in concentration.ivblocklist():
								print('\t\t\t\t\t' + ivblock.date() + '   ' + ivblock.time())

		return