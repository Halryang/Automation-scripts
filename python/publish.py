#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import subprocess

from sys import argv
from datetime import datetime
from os.path import exists
import os

script, from_file = argv

# from_file 의 내용을 indata 변수로 지정합니다.
in_file = open(from_file)
indata = in_file.read()

# dt는 스크립트를 실행하는 날짜와 시각입니다.
dt = datetime.now()

# to_file은 argv로 받은 원본 파일명 앞에 지킬 포스트 폴더와 날짜를 넣어봅니다.
to_file_date = dt.strftime("%Y-%m-%d-")
to_file = '/Users/JF/Dropbox/halryang.github.io/_posts/' + to_file_date + from_file

# 지킬 포스트 폴더에 보내려는 파일명과 동일한 파일이 있는지 확인합니다.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# post_date는 지킬 포스트의 YAML 머리말에 들어가는 date 형식에 맞추었습니다.
post_date = dt.strftime("%Y-%m-%d" + ' ' + "%H:%M:%S")

# post_title, post_tags 변수값을 raw_input으로 받습니다.
post_title = raw_input("Title: ")
post_tags = raw_input("Tags: ")

# 이제 YAML 머리말을 indata 앞에 넣어 outdata를 만듭니다.

outdata = """---
layout: post
title: %s
date: %s
tags: %s
---
%s
""" % (post_title, post_date, post_tags, indata)

out_file = open(to_file, 'w')
out_file.write(outdata)

print "%s is copied to %s" % (from_file, to_file)

out_file.close()
in_file.close()

# GitHub에 add & commit & push

os.chdir('/Users/JF/Dropbox/halryang.github.io/')

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Post published"])
subprocess.call(["git", "push", "-u", "origin", "master"])