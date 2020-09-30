# -*- coding: utf-8 -*-
#Adopted from John McLevey - UWaterloo social networks lab - template -  for personal research
#https://github.com/mclevey

#       THIS SCRIPT CREATES A NEW PROJECT DIRECTORY


#import shutil

#from git import Repo
import os

import argparse

import datetime

now = datetime.datetime.now()

ap = argparse.ArgumentParser()

ap.add_argument("-d", "--dir", required=True,
                help = 'Directory Name')

#args = vars(ap.parse_args())
args = ap.parse_args()

if args.dir:
    os.mkdir(args.dir)
    os.chdir(args.dir)

cwd = os.getcwd()

print("Setting up the basic directory structure.")

directories = ['archive', 'code','data/clean', 'data/raw', 'docs/drafts','docs/abstracts', 'figures', 'lit', 'letters', 'logs']

for d in directories:
	if not os.path.exists(d):
		os.makedirs(os.path.join(cwd, d))


print("Creating readme.md -- remember to record project agreements!")
#print("Project Opened: "+now.strftime("%Y-%m-%d %H:%M")+" \n\nProject Purpose:\n\nRoles:\n\nCo-authorship Agreement:\n")

if not os.path.exists('readme.md'):
	readme = open('readme.md', 'w')
	readme.write("Project Opened: "+now.strftime("%Y-%m-%d %H:%M")+" \n\nProject Purpose:\n\nRoles:\n\nTeam\n\nAcknowledgements\n\nCo-authorship Agreement:")
	readme.close()



# initialize git

#print("Initializing git.")

#if not os.path.exists('.git'):
#	Repo.init()

#if not os.path.exists('.gitignore'):
#	ignore = open('.gitignore', 'w')
#	ignore.write('archive/\n.Rhistory\n.Rapp.history\n.Rproj.user/\n.httr-oauth\n/*_cache/\n/cache/\n*.utf8.md\n*.knit.md\n.ipynb_checkpoints\n*.icloud')
#	ignore.close()

print('Finished')