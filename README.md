# Exif Extrator

This script was created for local counting of clicks from my Nikon camera.

While there is only one flag accepted from metadata, it's easily to add new flags and commands by editing object FLAGS.

```
./exif_extractor.py <file> <options>
```

# How to add new flags?

Just edit the script adding the tag to be retrieved and the options user will need to enter.

```
FLAGS = {
  "<example tag>": "-e","--example"
}
```
