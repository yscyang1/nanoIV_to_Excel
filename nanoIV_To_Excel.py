import os

#from xlwings import Workbook, Sheet, Range, Chart

#from WorkBookList import *

#from CreateExcel_XLWings import *
#from CreateExcel_OpenPyXL import *
from CreateExcel_XlsxWriter import *


from DeviceList import *
from IVBlock import *
from InputFileParser import *

from StringOperations import *

#finds files of form    DEVICE_MOD_SALT_pH_CONCENTRATION_#         PET-DC-15-08-17_nomod_KCl_pH8_100mM_0.txt
# filelist = FindTextFileNamesInFolder(r'C:\\Users\\zsiwy\\Desktop\\nanoIV_To_Excel\\Test\\PET-DC-15_08_17\\Second_Etch\\nomod')
filelist = FindTextFileNamesInFolder(r'C:\\Users\\zsiwy\\Desktop\\Crystal\\PET_Double_Conical\\16_08_15')

ivblocklist = []

devicelist = DeviceList()

for i in range(len(filelist)):
	newblock = InputFileParser.Parse_InputFile(InputFileParser, filelist[i], 'INPUTFILE_FILETITLE_STANDARDFORMAT', 'INPUTFILE_FILECONTENTS_nanoIVFORMAT')
	if newblock != False:
		devicelist.AddIVBlock(newblock)

devicelist.SortCategoryTree()
devicelist.PrintCategoryTree()



filecreator = ExcelFileCreator_XlsxWriter()
filecreator.CreateExcelFiles(devicelist.devicelist())

workbooklist = filecreator.workbooklist()

##CreatePlots(workbooklist)

