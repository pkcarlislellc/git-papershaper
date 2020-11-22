import sys			# allows for direct OS command execution
import getopt			# allow graceful failure if bad command line
import os			# allows for resolving ~/home folder
import random			# permits generating a random number
import time 			# necessary to make program re-run periodically
from os.path import expanduser 
galleryread = expanduser("~/com.pkcarlisle/papershaper/gallery/")
gallerylist = expanduser("~/com.pkcarlisle/papershaper/gallerylist.txt")	
webcamlist = expanduser("~/com.pkcarlisle/papershaper/webcamgrab.txt")
papershaperpath = expanduser("~/com.pkcarlisle/papershaper/")
gallerypath = expanduser("~/com.pkcarlisle/papershaper/gallery/")			# By default files will be located in
currentpapershaper = expanduser("~/com.pkcarlisle/papershaper/papershaper.jpg")	# and read from, and written to
homelog = expanduser("~/com.pkcarlisle/papershaper/papershaper.log")		# the user's ~/com.pkcarlisle/papershaper/ folder
errorfile = expanduser("~/com.pkcarlisle/papershaper/papershaper_error.jpg")
err_state_critical = 0								# a check that all user arguments are within valid spec
sleeptime = 0									# a counter for time between wallpaper changes


while 1:
 if len(sys.argv) == 1:		# user has not selected options, use defaults
	defaultsource = 'g'	# set defaults if no user options given
	sleeptime = 1200	# convert user entered minutes to seconds, set default to 20 minutes
	break 					
 if len(sys.argv) == 2:	
	print "Usage:"
	print "python papershaper-python-2.py [g | w | m ] [minutes]"
	print "g - get random wallpaper image from user's local/offline gallery in " + galleryread
	print "w - get random wallpaper image online from listing of webcams in " + webcamlist
	print "m - Max Random: get random wallpaper from offline gallery OR a random image from online webcam"
	print "minutes is the minutes to delay between refreshes, default is 20 minutes if NO options are used."
	print "Example: python papershaper-python-2.py m 30 - refresh randomly from either source every 30 minutes"
	print "If you specify the first option (g or w or m) then you must specify minutes."
	print "Default usage: python papershaper-python-2.py - refresh randomly from offline/local gallery every 20 minutes"
	print "\n"
	print "For best results, run papershaper-python-2.py from a startup script or as a Startup Application."
	print "\n"
	print "The Paper Shaper"
	print "(C)2014,2019.  Distributed under the GNU General Public License compliments of P. K. Carlisle LLC " 
	print "at www.pkcarlisle.com. Notes to mail@pkcarlisle.com. Follow on Twitter @pkcarlislellc."
	exit(1)

 if len(sys.argv) == 3:	

	 if str(sys.argv[1]) == 'g':
		defaultsource = str(sys.argv[1])	
	 elif str(sys.argv[1]) == 'w':
		defaultsource = str(sys.argv[1])	
	 elif str(sys.argv[1]) == 'm':
		defaultsource = str(sys.argv[1])
	 else:
		print "Invalid option(s).  Type python papershaper.py -help for help."
		exit(1)

	 if str.isdigit(sys.argv[2]) == False:
		print "Invalid option(s).  Type python papershaper.py -help for help."
		exit(1)
	 elif str.isdigit(sys.argv[2]) == True:
		sleeptime = float(sys.argv[2])
		sleeptime = sleeptime * 60		# convert user entered minutes to seconds
		break
	 else:
		sleeptime = 20				# convert user entered minutes to seconds, set default to 20 minutes
		sleeptime = sleeptime * 60		# convert user entered minutes to seconds
		break

 if len(sys.argv) > 3:				# This only happens if user options invalid
	print "Invalid option(s).  Type python papershaper.py -help for help."
	exit(1)







while 1:		# START A LOOP SO THAT PROGRAM RUNS ON A TIMED BASIS


 if defaultsource == 'g':
	cleanurlcommand = 'ls ' + gallerypath +'*.jpg > ' + gallerylist
	os.system(cleanurlcommand)
	datafileread = open(gallerylist,'r')				# file with list of gallery files
	total_file_lines_possible = 0					# Total lines (including comments) in the gallery list file
	while 1:
		stringread = datafileread.readline()[:-1]
		if not stringread: 					# if there is no string to read it must be EOF
			break
		else:
			total_file_lines_possible = 1 + total_file_lines_possible	# counts the total lines in the gallery file
			continue

	datafileread.close()								# Number of lines in the gallery file known, so close the file

	random_number_to_seek = random.randrange(1,total_file_lines_possible) # GENERATES A RANDOM NUMBER BETW 1 & THE TOTAL NUMBER OF LINES IN THE URLs FILE 
	if total_file_lines_possible == 1:
		random_number_to_seek = 1
	datafileread = open(gallerylist,'r')	# file with list of gallery images
	counter = 0
	while 1:
		while counter < random_number_to_seek:
			stringread = datafileread.readline()
			counter = 1 + counter
		tail = stringread[-5:-1]	# tail = .ext of file name
		if tail == '.jpg':		# we test if the line that we read from the URL list is a valid URL
			datafileread.close()	# close the file we had open for reading
			break			# we break out of further tests if we got a valid URL
		elif tail == 'jpg?':		# some URLs have a .jpg extension, some have a .jpg? extension, so we test for both
			datafileread.close()	# close the file we had open for reading
			break			# and break on either one since both are valid
		else:
			datafileread.close()	# if we didn't get a valid URL with our random number, reset everything, loop & try again
			random_number_to_seek = random.randrange(1,total_file_lines_possible)
			datafileread = open(gallerylist,'r')	# file to read from
			counter = 0

	# THIS SECTION CREATES THE COMMAND LINE STRING FROM THREE PARTS
	# THE COMMAND TO USE THE LYNX BROWSER
	# THE URL LYNX IS TO GO TO
	# AND THE PLACE TO DUMP THE FILE RETRIEVED

	raw_header_command = '/usr/bin/lynx -cookies -crawl -dump ' 
	raw_url_location = stringread[:-1]
	raw_file_save_location = ' > '
	cleanurlcommand = raw_header_command + raw_url_location + raw_file_save_location + currentpapershaper
	os.system(cleanurlcommand)

 elif defaultsource == 'w':

	datafileread = open(webcamlist,'r')				# file with list of gallery files
	total_file_lines_possible = 0					# Total lines (including comments) in the gallery list file
	while 1:
		stringread = datafileread.readline()[:-1]
		if not stringread: 					# if there is no string to read it must be EOF
			break
		else:
			total_file_lines_possible = 1 + total_file_lines_possible	# counts the total lines in the gallery file
			continue
	datafileread.close()								# Number of lines in the gallery file known, so close the file

	random_number_to_seek = random.randrange(1,total_file_lines_possible) # GENERATES A RANDOM NUMBER BETW 1 & THE TOTAL NUMBER OF LINES IN THE URLs FILE 
	if total_file_lines_possible == 1:
		random_number_to_seek = 1
	datafileread = open(webcamlist,'r')	# file with list of gallery images
	counter = 0
	while 1:
		while counter < random_number_to_seek:
			stringread = datafileread.readline()
			counter = 1 + counter
		tail = stringread[-5:-1]	# tail = .ext of file name
		if tail == '.jpg':		# we test if the line that we read from the URL list is a valid URL
			datafileread.close()	# close the file we had open for reading
			break			# we break out of further tests if we got a valid URL
		elif tail == 'jpg?':		# some URLs have a .jpg extension, some have a .jpg? extension, so we test for both
			datafileread.close()	# close the file we had open for reading
			break			# and break on either one since both are valid
		else:
			datafileread.close()	# if we didn't get a valid URL with our random number, reset everything, loop & try again
			random_number_to_seek = random.randrange(1,total_file_lines_possible)
			datafileread = open(webcamlist,'r')	# file to read from
			counter = 0

	# THIS SECTION CREATES THE COMMAND LINE STRING FROM THREE PARTS
	# THE COMMAND TO USE THE LYNX BROWSER
	# THE URL LYNX IS TO GO TO
	# AND THE PLACE TO DUMP THE FILE RETRIEVED

	raw_header_command = '/usr/bin/lynx -cookies -crawl -dump ' 
	raw_url_location = stringread[:-1]
	raw_file_save_location = ' > '
	cleanurlcommand = raw_header_command + raw_url_location + raw_file_save_location + currentpapershaper
	os.system(cleanurlcommand)

 elif defaultsource == 'm':

	cleanurlcommand = 'ls ' + gallerypath +'*.jpg > ' + gallerylist  # at this point, a listing of all gallery files exists.
	os.system(cleanurlcommand)
	raw_header_command = '/usr/bin/lynx -cookies -crawl -dump ' 
	raw_file_save_location = ' >> '
	cleanurlcommand = raw_header_command + webcamlist + raw_file_save_location + gallerylist
	os.system(cleanurlcommand)

	datafileread = open(gallerylist,'r')				# file with list of gallery files
	total_file_lines_possible = 0					# Total lines (including comments) in the gallery list file
	while 1:
		stringread = datafileread.readline()[:-1]
		if not stringread: 					# if there is no string to read it must be EOF
			break
		else:
			total_file_lines_possible = 1 + total_file_lines_possible	# counts the total lines in the gallery file
			continue

	datafileread.close()								# Number of lines in the gallery file known, so close the file

	random_number_to_seek = random.randrange(1,total_file_lines_possible) # GENERATES A RANDOM NUMBER BETW 1 & THE TOTAL NUMBER OF LINES IN THE URLs FILE 
	if total_file_lines_possible == 1:
		random_number_to_seek = 1
	datafileread = open(gallerylist,'r')	# file with list of gallery images
	counter = 0
	while 1:
		while counter < random_number_to_seek:
			stringread = datafileread.readline()
			counter = 1 + counter
		tail = stringread[-5:-1]	# tail = .ext of file name
		if tail == '.jpg':		# we test if the line that we read from the URL list is a valid URL
			datafileread.close()	# close the file we had open for reading
			break			# we break out of further tests if we got a valid URL
		elif tail == 'jpg?':		# some URLs have a .jpg extension, some have a .jpg? extension, so we test for both
			datafileread.close()	# close the file we had open for reading
			break			# and break on either one since both are valid
		else:
			datafileread.close()	# if we didn't get a valid URL with our random number, reset everything, loop & try again
			random_number_to_seek = random.randrange(1,total_file_lines_possible)
			datafileread = open(webcamlist,'r')	# file to read from
			counter = 0

	# THIS SECTION CREATES THE COMMAND LINE STRING FROM THREE PARTS
	# THE COMMAND TO USE THE LYNX BROWSER
	# THE URL LYNX IS TO GO TO
	# AND THE PLACE TO DUMP THE FILE RETRIEVED

	raw_header_command = '/usr/bin/lynx -cookies -crawl -dump ' 
	raw_url_location = stringread[:-1]
	raw_file_save_location = ' > '
	cleanurlcommand = raw_header_command + raw_url_location + raw_file_save_location + currentpapershaper
	os.system(cleanurlcommand)

 else:
	print "Invalid option(s).  Type python papershaper.py -help for help."
	raw_header_command = '/usr/bin/lynx -cookies -crawl -dump ' 
	raw_file_save_location = ' > '
	cleanurlcommand = raw_header_command + errorfile + raw_file_save_location + currentpapershaper
	os.system(cleanurlcommand)
	datafilewrite = open(homelog,'w')	# log the url to record error
	datafilewrite.write(errorfile)
	datafilewrite.close()
	exit(1)


# THIS LAST SECTION LOGS THE SPECIFIC GRAPHIC RETRIEVED ABOVE IN CASE THERE IS NEED TO REVIEW IT

 datafilewrite = open(homelog,'w')	# log the url to filter really ugly cams
 datafilewrite.write(raw_url_location)
 datafileread.close()
 datafilewrite.close()

 time.sleep(sleeptime)
