#!/usr/bin/env python
# Copyright (c) 2019 Bartek thindil Jasicki <thindil@laeran.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import glob
import os

if not os.path.exists('result'):
    os.makedirs('result')

for filename in glob.glob("*.ads"):
    # read whole file to list of lines
    with open(filename) as fn:
        content = fn.readlines()
    # add Robodocs template before each function, procedure and variable
    i = 0
    packagename = ""
    while i < len(content):
        line = content[i].strip()
        if line.startswith("package") and packagename == "":
            packagename = line.split(" ")[1]
        doclines = []
        if not line.startswith("--") and (line.startswith("procedure") or line.startswith("function") or line.find(":") > 0) and packagename != "":
            # parse function and procedures
            if line.startswith("procedure") or line.startswith("function"):
                if line.find("(") > -1:
                    line = line[: line.find("(")]
                doclines.append("-- ****f* " + packagename + "/" + line.split(" ")[1] + "\n");
            else:
                doclines.append("-- ****v* " + packagename + "/" + line[:line.find(":")] + "\n");
            newindex = i - 1
            if content[newindex].strip().startswith("-- ****"):
                newindex = i
            if content[newindex].strip().startswith("--"):
                doclines.append("-- FUNCTION\n")
                while content[newindex].strip().startswith("--"):
                    doclines.insert(3, content[newindex].strip() + "\n")
                    del(content[newindex])
            doclines.append("-- SOURCE\n")
            if len(doclines) > 3:
                i = newindex
            for j in range(len(doclines)):
                content.insert(i + j, doclines[j])
            i = i + len(doclines)
            line = content[i].strip()
            if line.startswith("procedure") or line.startswith("function"):
                bracketsopen = content[i].count("(") - content[i].count(")")
                while bracketsopen > 0:
                    i += 1
                    bracketsopen += (content[i].count("(") - content[i].count(")"))
                while content[i].find(";\n") == -1:
                    i += 1
                bracketsopen = content[i].count("(") - content[i].count(")")
                while bracketsopen > 0:
                    i += 1
                    bracketsopen += (content[i].count("(") - content[i].count(")"))
                while content[i + 1].strip().startswith("pragma"):
                    i += 1
            else:
                while content[i].find(";") == -1:
                    i += 1
            newindex = i + 1
            if content[newindex].strip().startswith("--") and len(doclines) < 3:
                doclines = []
                doclines.append("-- FUNCTION\n")
                while content[newindex].strip().startswith("--"):
                    doclines.append(content[newindex].strip() + "\n")
                    del(content[newindex])
                i = newindex
                for j in range(len(doclines)):
                    content.insert(i + j, doclines[j])
                i = i + len(doclines) - 1
            content.insert(i + 1, "-- ****\n")
            i += 2
            line = content[i].strip()
            if not line.startswith("--") and (line.startswith("procedure") or line.startswith("function") or line.find(":") > 0):
                i -= 1
        i += 1
    # save data to new file
    with open("result/" + filename, "w") as newfile:
        for line in content:
            newfile.write("%s" % line)
