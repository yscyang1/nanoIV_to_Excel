from StringOperations import *
import IVBlock as ivblock


##Parses a file and creates an IVBlock
class InputFileParser():
	norows = 0
	nocols = 0

	##STANDARD FORMAT: "STANDARD" = DEVICETYPE-YY-MM-DD_MODIFICATION_CONCENTRATION(mM)_ELECTROLYTE_PH_INDEX.TXT
	##e.g.: PET-DC-15-08-05_nomod_100mM_KCl_pH10_0.txt    
	##Date is the fabrication date!


	def Parse_InputFile(self, filename, filenameformat, inputformat):
		newivblock = ivblock.IVBlock()

		parse_success = True

		try:
			self.Parse_InputFile_FileName(self,filename, filenameformat, newivblock, parse_success)
			self.Parse_InputFile_Contents(self, filename, inputformat, newivblock, parse_success)
		except:
			parse_success = False

		if parse_success == True:
			return newivblock

		else:
			#print('\nCould not read file: ' + filename + '!\n')
			return False

	
	

	def Parse_InputFile_FileName(self, filename, filenameformat, newivblock, parse_success):
		if filenameformat == 'INPUTFILE_FILETITLE_STANDARDFORMAT':
			print(filenameformat)
			self.Parse_InputFile_FileName_StandardFormat(self, filename, newivblock, parse_success)

		return


	
	def Parse_InputFile_FileName_StandardFormat(self, filename, newivblock, parse_success):

		filename = ExtractFileNameFromFilePath(filename)

		filename_element_list = filename.split('_')

		newivblock.set_device(filename_element_list[0])

		#print(newivblock.device())

		newivblock.set_modification(filename_element_list[1])

		#print(newivblock.modification())

		newivblock.set_concentration_string(filename_element_list[2])

		#print(newivblock.concentration_string())

		newivblock.set_concentration_int(int(newivblock.concentration_string().replace('mM', '')))

		#print(newivblock.concentration_int())

		newivblock.set_electrolyte(filename_element_list[3])

		#print(newivblock.electrolyte())

		newivblock.set_pH(filename_element_list[4])

		#print(newivblock.pH())

		newivblock.set_index(filename_element_list[5][0:-4])



		#print(newivblock.index())

		return


	def Parse_InputFile_Contents(self, filename, inputformat, newivblock, parse_success):

		inputfile = open(filename, 'r')

		if inputformat == 'INPUTFILE_FILECONTENTS_nanoIVFORMAT':
			self.Parse_InputFile_Contents_nanoIVFormat(self, inputfile, newivblock, parse_success)

		return

	def Parse_InputFile_Contents_nanoIVFormat(self, inputfile, newivblock, parse_success):
		
		
		
		newivblock.set_date(self.nanoIVFormat_GetDate(self, inputfile))
		
		

		newivblock.set_time(self.nanoIVFormat_GetTime(self, inputfile))
		
		

		
		newivblock.set_data(self.nanoIVFormat_GetData(self, inputfile))
		
		newivblock.set_norows(self.GetRows(self, inputfile))
		
		newivblock.set_nocols(self.GetColumns(self, inputfile))
		
		return

	def nanoIVFormat_GetDate(self, inputfile):
		
		date = GetCell(inputfile, 0, 0)
		return date


	def nanoIVFormat_GetTime(self, inputfile):
		
		time = GetCell(inputfile, 0, 1)
		return time

	def nanoIVFormat_GetData(self, inputfile):
		
		inputfile.seek(0)
		inputfile.readline()

		data = inputfile.read()	
		return data


	def GetRows(self, inputfile):
		
		inputfile.seek(0)
		junk = inputfile.read()
		rowlist = junk.split('\n')
		
		norows = len(junk.split('\n')) - 1
		print('no rows (GetRows) = ' + str(norows))
		return norows
		

	def GetColumns(self, inputfile):
		
		inputfile.seek(0)
		inputfile.readline()
		junk = inputfile.readline()
		nocols = len(junk.split('\t'))
		return nocols

		






