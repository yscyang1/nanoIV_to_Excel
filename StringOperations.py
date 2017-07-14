import os
from linecache import *

def ExtractFileNameFromFilePath(filename):
	head, tail = os.path.split(filename)
	return tail

def GetCell(inputfile, row, column):
	##########################################################
	##Gets the element at a given row/column from a text file.
	##Rows delimited by \n
	##Columns delimited by \t
	##########################################################

	inputfile.seek(0)
	row = getline(inputfile.name, row + 1)
	cell = row.split('\t')[column]
	cell = RemoveCharacterFromString(cell, '\n')
	return cell


def RemoveCharacterFromString(string, character):
	return string.replace(character, '')
	

def FindTextFileNamesInFolder(foldername):
	flist = []
	for root, dirlist, filelist in os.walk(foldername):
		for files in filelist:
			if files.endswith('.txt'):
				path = root.split('\\')
				if path[len(path) - 1] != 'skip':
					flist.append(os.path.join(root, files))
		

	return flist
	
