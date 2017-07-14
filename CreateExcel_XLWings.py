#from xlwings import Workbook, Sheet, Range, Chart
from DeviceList import *
from DeviceCategory import *
from ModificationCategory import *
from ElectrolyteCategory import *
from pHCategory import *
from ConcentrationCategory import *

def CreateIVBlockExcelFile(devicelist, outputformat):
	if outputformat == 'STANDARD_OUTPUTFILE':
		CreateIVBlockExcelFile_STANDARD_OUTPUT(devicelist)
	return 

def CreateIVBlockExcelFile_STANDARD_OUTPUT(devicelist):

	workbooklist = []


	#create workbooks
	for i in range(len(devicelist.devicelist())):
		print('creating workbook')
		#create tabs
		#workbooklist.append(Workbook())
		#workbooklist[i].set_current

		#for j in range(len(devicelist.devicelist()[i].modificationlist())):
			#if Sheet.count() < j - 1:
				#Sheet.add('asdf')
				#Sheet(j).name('asdf')

		

	return
