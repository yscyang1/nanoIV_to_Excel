from openpyxl import Workbook

def CreateExcelFile_OpenPyXL(devicelist, titleformat, contentsformat):
	workbooklist = CreateExcelWorkbooks(devicelist, 'OUTPUTFILE_FILETITLE_STANDARDFORMAT')


def CreateExcelWorkbooks(devicelist, titleformat):
	if titleformat == 'OUTPUTFILE_FILETITLE_STANDARDFORMAT':
		CreateExcelWorkbooks_STANDARDFORMAT(devicelist)

def CreateExcelWorkbooks_STANDARDFORMAT(devicelist):
	workbooklist = []
	
	for i in range(len(devicelist.devicelist())):
		workbooklist.append(Workbook())



