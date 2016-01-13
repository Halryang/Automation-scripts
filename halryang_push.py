#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import subprocess
import os

os.chdir('/Users/JF/Dropbox/halryang.github.io/')

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Pushed"])
subprocess.call(["git", "push", "-u", "origin", "master"])