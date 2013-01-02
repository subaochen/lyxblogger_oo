#! /usr/bin/env python
# -*- coding: utf-8 -*-
#####################       A U T H O R       ##########################
#                                                                      #
#   Copyright 2010 Jack Desert                                         #
#   <jackdesert556@gmail.com>                                          #
#   <http://www.LetsEATalready.com>                                    #
#                                                                      #
######################      L I C E N S E     ##########################
#                                                                      #
#   This file is part of LyXBlogger.                                   #
#                                                                      #
#   LyXBlogger is free software: you can redistribute it and/or modify #
#   it under the terms of the GNU General Public License as published  #
#   by the Free Software Foundation, either version 3 of the License,  #
#   or (at your option) any later version.                             #
#                                                                      #
#   LyXBlogger is distributed in the hope that it will be useful,      #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of     #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the      #
#   GNU General Public License for more details.                       #
#                                                                      #
#   You should have received a copy of the GNU General Public License  #
#   along with LyXBlogger.  If not, see <http://www.gnu.org/licenses>. #
#                                                                      #
########################################################################

import sys

class Display:
    def __init__(self):
        self.indent = 4 * ' ' 

    def __pr3(self, text):
        # Use sys.stdout instead of print so results can be used for automated testing
        # For some reason a newline character is required to flush ?
        # That's okay, because we'll use str.rstrip on the other side
        text = str(text)  # This makes sure that anything printable can be passed through
        sys.stdout.write(text + '\n')
        # Each line must be flushed so it can be read by the other side.
        sys.stdout.flush()
      
    def print_format(self, in_format):
        msg = "Format: {0}".format(in_format)
        msg = self.__indent(msg)
        self.__pr3(msg)
        return(msg)


    def __indent(self, text):
        msg = self.indent + text
        return(msg)
