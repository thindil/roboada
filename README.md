## General information

RoboAda is the bundle of small Python scripts which helps create RoboDoc
documentation from Ada code. At this moment here are available two scritps:

## Roboada.py

RoboAda its short for *Add ROBODoc templates to Ada code*. It is very simple,
ugly and not optimized script to add ROBODoc documentation to Ada specification
files (.ads) based on existing comments in them. It support comments written
above and below code. This files are part of other, ultra-hyper-secret project
:)

### Usage

This file will convert Ada code files (*.ads* and *.adb*) from this same
directory where this script is. Modified files will be placed in subdirectory
*result* in this same directory. Thus to use it, put it to directory with your
code (or copy your code to directory where scrip is) and type:

* If you want to document only *.ads* files: `./roboada.py`
* If you want to document only *.adb* files: `./roboada.py internal`
* If you want to document all Ada source (*.ads* and *.adb*):
  `./roboada.py all`

## Generatedocs.py

ROBODoc have problems with Ada attributes: it is visible when option
`--syntaxcolors` is used. To fix this problem, you can use this script. It fix
all attributes in generated HTML files.

### Usage

First, it generate documentation with selected ROBODoc configuration file and
then, it scan selected directory (and its subdirectories) for HTML files and
if it find inside them incorrect Ada attribute, the script will replace it
with valid HTML code and replace old HTML file with new. It can take two
optional arguments: first is path (absolute or relative) to the configuration
file for ROBODoc, second is the path (absolute or relative) to the directory
to scan.

* `./generatedocs.py` will generate documentation by using file
**robodocada.rc** from this same directory and then it will scan current
directory (and its subdirectories) for HTML files and correct them if needed.
* `./generatedocs.py others/robodocada.rc` will generate documentation by using
the ROBODoc configuration file **others/robodocada.rc** and then it will scan
current directory (and its subdirectories) for HTML files and correct them
if needed.
* `./generatedocs.py others/robodocada.rc docs` will generate documentation
by using the ROBODoc configuration file **others/robodocada.rc** and then it
will scan subdirectory *docs* (and its subdirectories) of current directory for
HTML files and correct them.

## Generatedocs.tcl

It is Tcl version of above script. It can be a bit better than Python version.
It usage is exactly that same like Python version.

## Robodocada.rc

To create ROBODoc documentation from Ada sources, you must use as a ROBODoc
configuration file *robodocada.rc*. Thus, after creating documented code with
**roboada.py**, to create documentation with many files type: `robodoc
--src result --doc docs --multidoc --rc robodocada.rc`.

## License

Files **roboada.py**, **generatedocs.py**, **generatedocs.tcl** are distributed
under MIT license.

File **robodocada.rc** is in public domain.

## Others

I strongly recommend to read [ROBODoc documentation](https://rfsber.home.xs4all.nl/Robo/pages/robodoc-49942-user-manual.html).
Especially if you want to extend this script.

----

And standard footer :)

That's all for now, and probably I forgot about something important ;)

Bartek thindil Jasicki
