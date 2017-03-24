#!/usr/bin/env python
# -*- coding:utf-8
"""
pyconsole.py
Run a snippet in the Python console of inkscape.

:Author: WANG Longqi <iqgnol@gmail.com>
:Date: 2017-03-24
:Version: v0.1

This file is extracted and extended from WriteTeX.
"""

import inkex
import os
import sys
import textwrap


class PyConsole(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("-i", "--input",
                                     action="store", type="string",
                                     dest="input", default="",
                                     help="Input String")
        self.OptionParser.add_option("-x", "--exec",
                                     action="store", type="string",
                                     dest="useexec", default="false",
                                     help="Use exec instead of eval")
        self.OptionParser.add_option("-g", "--tosvg",
                                     action="store", type="string",
                                     dest="tosvg", default="false",
                                     help="Output to SVG")

    def effect(self):
        if self.options.useexec == "true":
            exec(self.options.input)
            try:
                output
            except NameError:
                output = "No output."
        else:
            output = eval(self.options.input)
        if self.options.tosvg == "true":
            wrapped = textwrap.wrap(str(output))
            output = ""
            size = self.unittouu('11')
            lineheight = self.unittouu('18')
            for line in wrapped:
                output += '<tspan x="%g" dy="%s" font-size="%s">' % (
                    self.view_center[0], lineheight,size)+line+"</tspan>"
            doc = inkex.etree.fromstring(
                '<text font-size="%s" x="%g" y="%g">%s</text>' % (
                    size,
                    self.view_center[0],
                    self.view_center[1],
                    output))
            self.current_layer.append(doc)
        else:
            inkex.errormsg(str(output))
        return

if __name__ == '__main__':
    e = PyConsole()
    e.affect()
