# Exif Extrator
##Local Shutter Count

This script was created for local counting of clicks from my Nikon camera.

For this to run, you will need only Python 3, pip and pyexiv2.
You may install then (in Ubuntu) by typing the following commands in your console
```
apt install python3
apt install python3-pip
python3 -m pip install pyexiv2
```
This script was tested on Ubuntu and with .NEF Nikon files

While there is only one flag accepted from metadata, it's easily to add new flags and commands by editing object FLAGS.

```
./exif_extractor.py <file> <options>
```

# How to add new flags?

Just edit the script adding the tag to be retrieving and the options user will need to enter.

```
FLAGS = {
  "<example tag>": "-e","--example"
}
```
