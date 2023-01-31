#! python3
# openurl.py - Launches a url in the browser using an address from the 
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:

	# Get address from command line.
	address = ' '.join(sys.argv[1:])	
	
#TODO: Get address from clipboard.

else:
	#Get address from clipboard.
	address = pyperclip.paste()
	
#webbrowser.open('https://'+ address)
webbrowser.open(address)
	