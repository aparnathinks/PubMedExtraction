import getopt
import json
import sys
from urllib import request

import requests

inputfile = ''
bioconcept = 'BioConcept'
fformat = 'json'
outputfile='data.txt'

try:
	options, remainder = getopt.getopt(sys.argv[1:], 'i:o:b:f:', ['inputfile=','outputfile=','bioconcept=','format='])
except getopt.GetoptError as err:
	print("\npython RESTful.client.get.py -i [inputfile] -o [outputfile] -b [bioconcept] -f [format] \n")
	print( "\t bioconcept: We support five kinds of bioconcepts, i.e., Gene, Disease, Chemical, Species, Mutation. When 'BioConcept' is used, all five are included.\n")
	print ("\t inputfile: a file with a pmid list\n")
	print ("\t outputfile: the file that will store the result\n")
	print ("\t format: PubTator (tab-delimited text file), BioC (xml), and JSON\n\n")
	sys.exit(0)
														 
for opt, arg in options:
	if opt in ('-i', '--inputfile'):
		inputfile = arg
	elif opt in ('-o', '--outputfile'):
		outputfile= arg
	elif opt in ('-b', '--bioconcept'):
		bioconcept = arg
	elif opt in ('-f', '--format'):
		fformat = arg

pmids=list()

try:
		
	fh = open(inputfile)

	

	for pmid in fh:
		pmids.append(pmid.rstrip('\r\n'))

	fh.close()


except IOError:
	print("Can't open %s", inputfile)
except:
	fh.close()
	print("Unexpected error:", sys.exc_info()[0])
	raise	







# for JASON - create dictionary DS to store results
	
if fformat.lower().strip()=='json':
	json_dict=dict()


for pmid in pmids:
	url_Submit = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/" + bioconcept + "/" + pmid + "/" + fformat + "/"

	
	

	
	# for JASON
	
	if fformat.lower().strip()=='json':



		try:
			result=requests.get(url_Submit)	
		except requests.exceptions.RequestException as err:
	    		print ("OOps: Request error",err)
		except requests.exceptions.HTTPError as errh:
	    		print ("Http Error:",errh)
		except requests.exceptions.ConnectionError as errc:
	    		print ("Error Connecting:",errc)
		except requests.exceptions.Timeout as errt:
			print ("Timeout Error:",errt)
			print ("Do you want to try again (Y/n)-")
			ch=input()
			if ch.strip().lower()=='y':
				result=requests.get(url_Submit)
			else:
				print("Exiting...")
				sys.exit(0)
		except:
			print("Something went wrong while trying the url")
			sys.exit(0)




		data=json.loads(result.text)

		print(data[0])
		json_dict[pmid]=data[0]
	
		try:
		
			with open(outputfile, 'a') as outfile:
				json.dump(data[0], outfile)
		except IOError:
			print("Can't open %s", outputfile)
		except:
	    		print("Unexpected error:", sys.exc_info()[0])
	    		raise

	
	
	else:
		
		# for PubTator and BioC formats
		
		# Just dumps the string output to a file at the moment. 
		# We can write code to format this later
		 
		try:
			urllib_result = request.urlopen(url_Submit)
		except urllib.error.URLError(err):
			print("pmid=",pmid," temporarily failed to fetch")

		data=str(urllib_result.read())
		print(data)

		try:
		
			with open(outputfile, 'a') as outfile:
				outfile.write(data)
		except IOError:
			print("Can't open %s", outputfile)
		except:
	    		print("Unexpected error:", sys.exc_info()[0])
	    		raise	
		




