## General information

RoboAda its short for *Add RoboDoc templates to Ada code*. It is very simple,
ugly and not optimized script to add RoboDoc documentation to Ada specification
files (.ads) based on existing comments in them. It support comments written
above and below code. At this moment it generate documentation only for
functions/procedures and variables. This files are part of other,
ultra-hyper-secret project :)

## Usage

This file will convert .ads files from this same directory where this script
is. Modified files will be placed in subdirectory *result* in this same
directory. Thus to use it, put it to directory with your code (or copy your
code to directory where scrip is) and type: `./roboada.py`

To create RoboDoc documentation from modified sources, you must use as a
RoboDoc configuration file *robodocada.rc*. Thus, after creating documented
code in first step, to create documentation with many files type: `robodoc
--src result --doc docs --multidoc --rc robodocada.rc`.

## License

File **roboada.py** is distributed under MIT license.
File **robodocada.rc** is in public domain.

## Others

I strongly recommend to read [RoboDoc documentation](https://rfsber.home.xs4all.nl/Robo/pages/robodoc-49942-user-manual.html).
Especially if you want to extend this script.

----

And standard footer :)

That's all for now, and probably I forgot about something important ;)

Bartek thindil Jasicki
