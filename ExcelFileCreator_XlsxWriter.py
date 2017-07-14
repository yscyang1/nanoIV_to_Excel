from xlsxwriter import *

class ExcelFileCreator_XlsxWriter(object):

	

	def __init__(self):

		self.devicelist_ []
		self.workbooklist_ = []
		

	def CreateExcelFiles(self, devicelist, titleformat, contentsformat):
		self.devicelist_ = devicelist
		self.CreateWorkbooks(self.devicelist_, titleformat)

	def CreateWorkbooks(self, titleformat, contentsformat):
		if titleformat == 'OUTPUTFILE_FILETITLE_STANDARDFORMAT':
			CreateWorkbooks_STANDARDFORMAT()


	def CreateWorkbooks_STANDARDFORMAT(self):
		for i in range(len(self.devicelist_.devicelist())):
			self.workbooklist_.append(Workbook(devicelist.devicelist()[i].title() + '.xlsx'))
		


