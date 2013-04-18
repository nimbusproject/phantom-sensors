#!/usr/bin/python
# This file is part of tcollector.
# Copyright (C) 2010  StumbleUpon, Inc.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
# General Public License for more details.  You should have received a copy
# of the GNU Lesser General Public License along with this program.  If not,
# see <http://www.gnu.org/licenses/>.

#USER = "myphantomuser"
#PASSWORD = "mypassword"
#DOMAIN = "mydomain"

# DO NOT EDIT BELOW THIS POINT UNLESS YOU ARE ESPECIALLY CLEVER
def onload(options, tags):
  """Function called by tcollector when it starts up.

  Args:
    options: The options as returned by the OptionParser.
    tags: A dictionnary that maps tag names to tag values.
  """
  try:
    tags['domain'] = DOMAIN
  except NameError:
    pass

  try:
    tags['user'] = USER
  except NameError:
    pass

  try:
    tags['password'] = PASSWORD
  except NameError:
    pass
