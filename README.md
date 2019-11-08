Document Clustering with Python
================

<img src='header_short.jpg'>

This repo is for extracting publications from the "pubmed" database for use with data science projects. It is based on the RESTfulAPI.client provided by pubmed. 
You can find more about the formats supported at:

<a href=https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/tmTools/RESTfulAPIs.html>https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/tmTools/RESTfulAPIs.html</a>


Currently, it extarcts the articles (sourceid, sourcedb,text, denotations) corresponding to pmids in a file and returns articles in json format.
It can also extarct PubTator and BioC(xml) formatted data. But, it stores them as complete xml/ PubTator strings for each entry in a single file. 

For Future
----------
<ul>
<li> Implementing code for correct formating of pubtator and bioc(xml) outputs.
<li> Redirecting to other sources of extracting the article if the RESTful url fails; 
	Extracting from entrez (e.g. "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=25752562") etc.
</ul>



### How the repo is set up

To extract pubmed articles run 'extract_publications.py'.
usage:
	python extract_publications.py -i [inputfile] -o [outputfile] -b [bioconcept] -f [format]
	Where:
	<ul>
	<li> <b>inputfile:</b> a file with a pmid list
	<li> <b>outputfile:</b> the file that will store the result
	<li> <b>bioconcept: </b> We support five kinds of bioconcepts, i.e., Gene, Disease, Chemical, Species, Mutation. When 'BioConcept' is used, all five are included
	<li> <b>format:</b> PubTator (tab-delimited text file), BioC (xml), and JSON
	</ul>
	Default values:
	<ul>
	<li>inputfile = ''
	<li>bioconcept = 'BioConcept'
	<li>format = 'json'
	<li>outputfile='data.txt'
	</ul>
	Example:
	python extract_publications.py -i example/gold_set.pmid -o example/train.json -f json


There is an example folder with 
<ul>
<li> Training and test files with a set of pmids - gold_set.pmid, test_set.pmid
<li> The corresponding article outputs in json, xml and pubtator formats - train.json, train.xml, train.pubtator, test.json, test.xml, test.pubtator
</ul>
