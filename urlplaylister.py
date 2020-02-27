import string
import argparse
from sys import argv
from netflixtemplate import *
from hulutemplate import *
from youtubetemplate import *
from disneyplustemplate import *
from amazonprimevideotemplate import *

print "It's running!"

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	args = parser.parse_args()
	filename = str(args.filename)
	return (filename)

def gather_info(filename):
	print ("Active Playlist: " + filename)
	url = raw_input ("Please Enter the URL: ")
	vid_len = input ("Please Enter it's Length (in Minutes): ")
	vid_len_string = str(vid_len * 60 * 1000) # video length in milliseconds	
	return (url, vid_len_string)

def append_to_playlist(url,milliseconds,filename):

	if "netflix.com" in url:
		url = sanitize_netflix_url(url);
		with open(filename, 'a') as target:
			target.write(NTemplate.substitute(sUrl=url, sLength=milliseconds))
			# NTemplate is located in netflixtemplate.py
		print ("Netflix Item added to playlist, full playlist below.")
	elif "hulu.com" in url:
		with open(filename, 'a') as target:
			target.write(HTemplate.substitute(sUrl=url, sLength=milliseconds))
			# NTemplate is located in netflixtemplate.py
		print ("Hulu Item added to playlist, full playlist below.")		
	elif "youtube.com" in url:
		with open(filename, 'a') as target:
			target.write(YTemplate.substitute(sUrl=url, sLength=milliseconds))
			# NTemplate is located in youtubetemplate.py
		print ("Youtube Item added to playlist, full playlist below.")	
	elif "disneyplus.com" in url:
		with open(filename, 'a') as target:
			target.write(DTemplate.substitute(sUrl=url, sLength=milliseconds))
			# DTemplate is located in disneyplustemplate.py
		print ("Disney Plus Item added to playlist, full playlist below.")	
	elif "amazon.com" in url:
		with open(filename, 'a') as target:
			target.write(APVTemplate.substitute(sUrl=url, sLength=milliseconds))
			# APVTemplate is located in amazonprimevideotemplate.py
		print ("Amazon Prime Video Item added to playlist, full playlist below.")

def display_playlist():
	with open(filename, 'r') as target:
		print target.read()
	
def end_program():
	print "Thank you for using this software."
	quit()

def sanitize_netflix_url(unsanitized_netflix_url):
	sanitized_netflix_url = unsanitized_netflix_url.split('&', 1)[0];
	return (sanitized_netflix_url)

if __name__ == "__main__":

	filename = parse_arguments()
	url, vid_len_string = gather_info(filename)
	append_to_playlist(url,vid_len_string, filename)
	display_playlist()
	end_program()