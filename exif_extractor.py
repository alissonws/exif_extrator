#!/usr/bin/env python3

HELP ="""
# usage: exif_extrator.py <file> <options>
# example: exif_extractor.py file.NEF --shutter-count

OPTIONS:
-S -s --shutter-count: Extract shutter count from exif file
-H -h --help: Show user instructions

Created by: Alisson W. Corrêa, alissonwcorrea@gmail.com
Last tested: 01/08/2020

This script is easly custumizable by adding more tags corresponding to comands in FLAGS object.
Providing a fancy name in object TAGS is optional.
"""


import sys

try:
	import pyexiv2
except ModuleNotFoundError:
	print(
	"""
It seems you do not have the needed package pyexiv2 installed.

If you have pip installed, you may install it by simply typing:

python -m pip install pyexiv2
	""")
except  Exception as e:
	print(
	"""
A critical error has rised while trying to import pyexiv2. This script will no be able to run.

Error: {}
	""".format(e))
	sys.exit(1)



TAGS = {
	"Shutter count":"Exif.Nikon3.ShutterCount",
}
FLAGS = {
	"help":["-h","-S","--help"],
	"Exif.Nikon3.ShutterCount":["-s","-S","--shutter-count"],
	"all":["-a","-A","--all"],
}

def called_flag(flag):
	"""
		Returns True if flag is defined by user
	"""
	for arg in sys.argv[2:]:
		if arg in FLAGS[flag]:
			return True
	return False


if len(sys.argv) == 1 or called_flag("help"):
	print(HELP)
else:
	file = sys.argv[1]

	md = pyexiv2.Image(file)

	if sys.argv[2:] != []:
		#Looping for flags
		for arg in sys.argv[2:]:
			if "-" in arg:
				if called_flag("all"):
					#Print all exif tags in file
					exif = md.read_exif()
					for m in exif:
						print(m + "=" + str(exif[m]))
					sys.exit(0)
				else:
					for arg in sys.argv[2:]:
						for flag in FLAGS:
							if arg in FLAGS[flag]:
								try:
									tag_exif = md.read_exif()[flag]

									tag_name = flag
									for tag in TAGS:
										if flag in TAGS[tag]:
											tag_name = tag

									print("{}: {}".format(tag_name,tag_exif))
									sys.exit(0)
								except KeyError:
									print("It was not possible to extract extract tag. Exception: KeyError: {}".format(e))
								except Exception as e:
										print("An unexpected error ocurred while retrieving tag {} \n\nError: {}".format(flag,e))

						print("Invalid flag {} provided".format(arg))
						sys.exit(1)
			else:
				print("Invalid argument {}".format(arg))
				sys.exit(1)
	else:
		print("No options provided, printing help\n")
		print(HELP)
		sys.exit(0)
