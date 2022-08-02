import requests
from argparse import ArgumentParser
import os

parser = ArgumentParser();

parser.add_argument('-u', '--url', type=str, help='Enter the URL (Eg:- https://google.com/ , https://example.com/index.php )');
parser.add_argument('-f', '--filename', type=str, help='Give any name to make file. (Eg:- example.html , example.php)')

args = parser.parse_args();

try: 
    os.mkdir("webpages") 
except OSError as error: 
    print("")

def clone():
	url = args.url;
	filen = args.filename;
	print("Web Cloner v1.0.0")
	print("---------------------------------------------------------------");
	print("---------------------------------------------------------------");
	print("Running...");
	print("---------------------------------------------------------------");
	print(" ");
	response=requests.get(url);
	print("---------------------------------------------------------------");
	print("");
	x = open("./webpages/"+filen,"w");
	x.write(str(response.text));
	x.close();
	print("File created.");
	print("Path : /webpages/"+str(filen));


clone();
print("---------------------------------------------------------------");
print("Bye Bye ...");


