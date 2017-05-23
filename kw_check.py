
from itertools import groupby 

from collections import Counter

import argparse

"""
To do:

Ask user where they want to get the files and data from:
-from Google Drive
-from local file
-from a url 
-input manually

"""



kw_list = []

parsed_kws = []

present_kws = {}

missing_kws = []

def check_kws(kws_file, text_file):

	with open(kws_file, 'r') as fp:
		content = fp.readlines()
		for i in content:
			kw_list.append(i.replace('\n', ''))
			
			
	tp=open(text_file, 'r')

	print 'Checking for the following keywords ', kw_list

	text = tp.read().split()

	words_count = [(k, len(list(g))) for k, g in groupby(sorted(text))]
	#print(words_count)

	for k,v in words_count:
		for i in kw_list:
			if k == i:
				present_kws.update({i:v})
				print k, ' appears in this text ', v, ' time(s)'

	for y in kw_list:
		if y not in present_kws:
			missing_kws.append(y)

	print 'The following keywords are not present in the text ', missing_kws

def main():

	try:

		parser = argparse.ArgumentParser()
		parser.add_argument('kws_file', help='Enter the name of the keywords file')
		parser.add_argument('text_file', help='Enter the name of the file you wish to check for keywords')
		args = parser.parse_args() 

		kws_file = args.kws_file
		text_file = args.text_file 

		check_kws(kws_file, text_file)

	except:
		print 'Please run the program again with --h to get more information'


if __name__ == "__main__":
	main()



		
	
