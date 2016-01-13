#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import subprocess

from sys import argv
from os.path import exists
import os
import shutil

script, from_file = argv
to_file = '/Users/JF/Dropbox/halryang.github.io/images/' + from_file
link_path = '/images/' + '%s' % from_file

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

shutil.copy2(from_file, to_file)

def setClipboardData(data):
 p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
 p.stdin.write(data)
 p.stdin.close()
 retcode = p.wait()

setClipboardData(link_path)

# GitHub에 add & commit & push

os.chdir('/Users/JF/Dropbox/halryang.github.io/')

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Image file added"])
subprocess.call(["git", "push", "-u", "origin", "master"])