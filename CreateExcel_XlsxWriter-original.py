import xlsxwriter

class ExcelFileCreator_XlsxWriter(object):

	electrolyte_rowoffset_ = 0
	electrolyte_columnoffset_ = 0

	pH_rowoffset_ = 1
	pH_columnoffset_= 1


	concentration_rowoffset_ = 2
	concentration_columnoffset_ = 2





	def __init__(self):

		self.workbooklist_ = []
		self.devicelist_ = []

	def workbooklist(self):
		return self.workbooklist_


	def CreateExcelFiles(self, devicelist):
		print('Creating excel file(s)\n')
		self.devicelist_ = devicelist
		self.CreateWorkbooks()

		self.CreateSheets()

		self.WriteContent()

		self.CloseWorkbooks()

		return

	def CreateWorkbooks(self):
		for i in range(len(self.devicelist_)):
			print('Creating new workbook\n')
			self.workbooklist_.append(xlsxwriter.Workbook(self.devicelist_[i].title() + '.xlsx'))

		return
		
	def CreateSheets(self):
		for i in range(len(self.workbooklist_)):
			for j in range(len(self.devicelist_[i].modificationlist())):
				self.workbooklist_[i].add_worksheet(self.devicelist_[i].modificationlist()[j].title())

		return


	def WriteContent(self):
		for i in range(len(self.devicelist_)):
			for j in range(len(self.devicelist_[i].modificationlist())):
				self.WriteContentToSheet(self.workbooklist_[i].worksheets()[j], self.devicelist_[i].modificationlist()[j])

		return

	def WriteContentToSheet(self, sheet, modification):
		currentrow = 0
		currentcolumn = 0
		concentration_rowspan = 0
		ivblock_rowspan = 0
		ivblock_columnspan = 0


		for i in range(len(modification.electrolytelist())):
			self.WriteElectrolyte(sheet, currentrow + self.electrolyte_rowoffset_, self.electrolyte_columnoffset_, modification.electrolytelist()[i])
			for j in range(len(modification.electrolytelist()[i].pHlist())):
				self.WritepH(sheet, currentrow + self.pH_rowoffset_, self.pH_columnoffset_, modification.electrolytelist()[i].pHlist()[j])
				for k in range(len(modification.electrolytelist()[i].pHlist()[j].concentrationlist())):
					self.WriteConcentration(sheet, currentrow + self.concentration_rowoffset_, self.concentration_columnoffset_, modification.electrolytelist()[i].pHlist()[j].concentrationlist()[k])

					for l in range(len(modification.electrolytelist()[i].pHlist()[j].concentrationlist()[k].ivblocklist())):
						currentcolumn = 0
						currentcolumn = currentcolumn + self.concentration_columnoffset_ + 1
						maxrows = 0

						for m in range(l):
							currentcolumn = currentcolumn + modification.electrolytelist()[i].pHlist()[j].concentrationlist()[k].ivblocklist()[m - 1].nocols() + 1

						for m in range(l+1):
							if modification.electrolytelist()[i].pHlist()[j].concentrationlist()[k].ivblocklist()[m].norows() > maxrows:
								maxrows = modification.electrolytelist()[i].pHlist()[j].concentrationlist()[k].ivblocklist()[m].norows()
							
						self.WriteIVBlock(sheet, currentrow + self.concentration_rowoffset_ + 1, currentcolumn, modification.electrolytelist()[i].pHlist()[j].concentrationlist()[k].ivblocklist()[l])
					print('current row (before) = ' + str(currentrow))
					print('max rows = ' + str(maxrows))

					currentrow = currentrow + self.concentration_rowoffset_ + maxrows
					print('current row (after) = ' + str(currentrow))

			currentrow = currentrow + 3

								
						#currentcolumn = currentcolumn + self.electrolyte_columnoffset_ + self.pH_columnoffset_ + self.concentration_offset_ + 
						#self.WriteIVBlock(sheet, currentrow + self.ivblock_rowoffset_, currentcolumn + self.ivblock_columnoffset_, ivblock)

	
		return





	def WriteElectrolyte(self, sheet, row, column, electrolyte):
		sheet.write_string(row, column, electrolyte.title())
		return

	def WritepH(self, sheet, row, column, pH):
		sheet.write_string(row, column, pH.title())
		return

	def WriteConcentration(self, sheet, row, column, concentration):
		sheet.write_string(row, column, concentration.title())

	def WriteIVBlock(self, sheet, row, column, ivblock):
		self.WriteIVBlockDateTime(sheet, row, column, ivblock)
		self.WriteIVBlockContents(sheet, row, column, ivblock)
		return

	def WriteIVBlockDateTime(self, sheet, row, column, ivblock):
		sheet.write_string(row, column, ivblock.date())
		sheet.write_string(row, column + 1, ivblock.time())
		return

	def WriteIVBlockContents(self, sheet, row, column, ivblock):
		ivblocklines = ivblock.data().split('\n')
		
		for i in range(len(ivblocklines )- 1):
			linecolumns = ivblocklines[i].split('\t')
			for j in range(len(linecolumns)):
	
				try:
					sheet.write(row + i + 1, column + j, float(linecolumns[j]))
				except:
					sheet.write(row + i + 1, column + j, str(linecolumns[j]))
			

		
		return








	def CloseWorkbooks(self):
		for i in range(len(self.workbooklist_)):
			self.workbooklist_[i].close()

		return

	



