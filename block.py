# -*- coding: utf-8  -*-
"""
Pywikipedia script that allows the blocking and unblocking of specific users, or a list of users.

When using a file to block/unblock users en masse, please be sure to separate the usernames with a comma-space ", " instead of new lines, otherwise the masse block/unblock won't work.

Available parameters:

-autoblock               Automatically block the last IP address and any subsequent IP addresses used by this account
-block                   User to block
-expiry                  Expiry time for the block. Defaults to 2 weeks
-fileblock               Block a list of users from a text file en masse
-fileunblock             Unblock a list of users from a text file en masse
-reason                  Reason for the block
-reblock                 Reblocks the user if a block is already in place
-unblock                 User to unblock

"""

#
# (C) Corey Chambers, 2014
#
# http://c.wikia.com/wiki/User:Cörey
#
# Distributed under the terms of the MIT license.
#

import userlib
import wikipedia as pywikibot

from userlib import *

def main():
	autoBlock            = False
	blockExpiry          = '2 weeks'
	blockFile            = ''
	blockUser            = False
	blockUsers           = False
	reason               = 'Unblocked/blocked user.'
	reBlock              = False
	unblockFile          = ''
	unblockUser          = False
	unblockUsers         = False
	user                 = ''
	users                = ''
	userToBlock          = ''
	userToUnblock        = ''

	for arg in pywikibot.handleArgs():
		if arg == "-autoblock":
			autoBlock = True

		elif arg.startswith("-block"):
			if arg == "-block":
				user = pywikibot.input(u'Username to block: ')
				userToBlock = user
				userToBlock = User(pywikibot.getSite(), userToBlock)
				blockUser = True
			elif arg.startswith("-block:"):
				user = arg[7:]
				userToBlock = user
				userToBlock = User(pywikibot.getSite(), userToBlock)
				blockUser = True

		elif arg.startswith("-expiry"):
			if arg == "-expiry":
				blockExpiry = pywikibot.input(u'Expiry time for block: ')
			elif arg.startswith("-expiry:"):
				blockExpiry = arg[8:]

		elif arg.startswith("-fileblock"):
			if arg == "-fileblock":
				blockFile = pywikibot.input(u'Block users file: ')
			elif arg.startswith("-fileblock:"):
				blockFile = arg[11:]
				blockUsers = True

		elif arg.startswith("-fileunblock"):
			if arg == "-fileunblock":
				unblockFile = pywikibot.input(u'Unblock users file: ')
			elif arg.startswith("-fileunblock:"):
				unblockFile = arg[13:]
				unblockUsers = True

		elif arg.startswith("-reason"):
			if arg == "-reason":
				reason = pywikibot.input(u'Please enter a reason: ')
			elif arg.startswith("-reason:"):
				reason = arg[8:]

		elif arg == "-reblock":
			reBlock = True

		elif arg.startswith("-unblock"):
			if arg == "-unblock":
				user = pywikibot.input(u'Username to unblock: ')
				userToUnblock = user
				userToUnblock = User(pywikibot.getSite(), userToUnblock)
				unblockUser = True
			elif arg.startswith("-unblock:"):
				user = arg[7:]
				userToUnblock = user
				userToUnblock = User(pywikibot.getSite(), userToUnblock)
				unblockUser = True

		else:
			pywikibot.showHelp()


	if blockUser:
		userToBlock.block(onAutoblock=autoBlock, noCreate=True, reBlock=reBlock, reason=reason, expiry=blockExpiry)
		pywikibot.output(u'\03{lightpurple}%s has been blocked.' % user)

	if blockUsers:
		f  = open(blockFile)
		users = [word.strip() for line in f.readlines() for word in line.split(', ') if word.strip()]
		for item in users:
			userToBlock = User(pywikibot.getSite(), item)
			userToBlock.block(onAutoblock=autoBlock, noCreate=True, reBlock=reBlock, reason=reason, expiry=blockExpiry)
			pywikibot.output(u'\03{lightpurple}%s has been blocked.' % item)
			pass

	if unblockUser:
		userToUnblock.unblock(reason=reason)
		pywikibot.output(u'\03{lightpurple}%s has been unblocked.' % user)

	if unblockUsers:
		f  = open(unblockFile)
		users = [word.strip() for line in f.readlines() for word in line.split(', ') if word.strip()]
		for item in users:
			userToUnblock = User(pywikibot.getSite(), item)
			userToUnblock.unblock(reason=reason)
			pywikibot.output(u'\03{lightpurple}%s has been unblocked.' % item)
			pass

if __name__ == '__main__':
	try:
		main()
	except:
		pywikibot.output(u'\03{lightred}Oops, something went wrong! Please double check your parameters and try again.')
	finally:
		pywikibot.stopme()
