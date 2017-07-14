import xlsxwriter
import matplotlib.pyplot as plt
import IVBlock

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

	def get_variableNames(ivblockline):
		# returns list of data labels, called var_names and 
		# column number/index where the word "average" appears, called avgCol

		linecolumn = ivblockline.split('\t')
		avgCol = ExcelFileCreator_XlsxWriter.check_for_data(linecolumn)

		var_names = []
		temp = []

		for j in range(1, avgCol[1]):
			temp.append(linecolumn[j])
		var_names.append(temp)

		for i in range(1, len(avgCol) - 1):
			temp = []
			for j in range(avgCol[i] + 2, avgCol[i + 1]):
				temp.append(linecolumn[j])
			var_names.append(temp)

		return avgCol, var_names

	def check_for_data(ivblockline):
		# Check if there is forward or reverse data
		# avgCol finds the column number where the word "average" appears

		avgCol = [0]
		for i in range(0, len(ivblockline)):
			if ivblockline[i] == "average":
				avgCol.append(i)
		# avgCol.append(len(ivblockline))

		return avgCol

	def get_data(variablenames, avgCol, ivblocklines):
		# get list of x and y data
		# also plots at the end

		columndata = []
		temp = []
		for i in range(len(ivblocklines)):
			linecolumns = ivblocklines[i].split('\t')
			for j in range(0, len(linecolumns)):
				for k in range(0, len(avgCol) - 1):
					for l in range(avgCol[k], avgCol[k+1]):
						temp.append([])  # need to rewrite to get rid of extra []
					if j == avgCol[0]: # get the first column (voltage)
						try:
							temp[j].append(float(linecolumns[j]))
						except:
							temp[j].append(linecolumns[j])
					if j > avgCol[k] and j < avgCol[k+1]: # get the rest of the columns, sans "average" column
						try:
							temp[j].append(float(linecolumns[j]))
						except:
							temp[j].append(linecolumns[j])
					j += 1
		print(variablenames)
		for k in range(0, avgCol[1]):
			temp[k].pop(0)
			columndata.append(temp[k])
		ExcelFileCreator_XlsxWriter.make_plot(variablenames[0], columndata, 1)
		columndata = []
		for k in range(1, len(avgCol) - 1):
			for l in range(avgCol[k] +1, avgCol[k+1]):
				temp[l].pop(0)
				columndata.append(temp[l])
			ExcelFileCreator_XlsxWriter.make_plot(variablenames[k], columndata, k + 1) 
			columndata =[]

		return 


	def make_plot(variablenames, columndata, index):
		#generate and save in folder plots

		global g_device, g_date, g_time, g_modification, g_electrolyte, g_concentration_string, g_concentration_int, g_pH, g_index, g_data

		xvals = [x for x in columndata[0] if x != ""]
		yvals = []
		for j in range(1, len(columndata)):
			temp = [y for y in columndata[j] if y != ""]
			yvals.append(temp)

		for sublist in range(0,len(yvals)):
			plt.plot(xvals, yvals[sublist], label = variablenames[sublist])
		plt.legend(loc = 'upper left')
		plt.xlabel('Voltage (V)')
		plt.ylabel('Current (A)')
		
		my_block = IVBlock.IVBlock()
		
		title = [my_block.concentration_string(), my_block.electrolyte(), my_block.pH(), my_block.modification(), str(variablenames[0])]
		plt_title = ""
		for each in title:
			plt_title += each
			plt_title += " "
		plt_title += str(index)

		save_name = ""
		name = [my_block.device(), my_block.modification(), my_block.concentration_string(), my_block.electrolyte(), my_block.pH(), my_block.index()]
		for each in name:
			save_name += each
			save_name += "_"
		save_name += ".png"

		plt.title(plt_title)
		plt.savefig(save_name, bbox_inches = 'tight')
		plt.show()

		return

	def WriteIVBlockContents(self, sheet, row, column, ivblock):
		ivblocklines = ivblock.data().split('\n')
				
		averageColumns, variableNames = ExcelFileCreator_XlsxWriter.get_variableNames(ivblocklines[0])
		
		ExcelFileCreator_XlsxWriter.get_data(variableNames, averageColumns, ivblocklines)
		# ExcelFileCreator_XlsxWriter.make_plot(variableNames, xvalues, yvalues)

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

	



