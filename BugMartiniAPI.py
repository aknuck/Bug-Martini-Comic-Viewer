#BugMartiniAPI

import urllib,urllib2
import re

# Downloads a comic from the given link to a given destination
# Destination must be a name ending in .png
def download(link,destination):
	urllib.urlretrieve(link,destination)

# Returns a permalink to today's comic
def getTodays():
	html = urllib2.urlopen("http://www.bugmartini.com").read()
	regex = re.compile("<a href=\"http://www\.bugmartini\.com/comic/.+><span class=\\\"comment-balloon\\\">")
	for m in regex.finditer(html):
		return (m.group()[9:m.group().index("\"><span")])

# Returns a link to the image from the given link
def getImage(link):
	html = urllib2.urlopen(link).read()
	regex = re.compile("<meta property=\"og:image\" content=\".+\" />")
	for m in regex.finditer(html):
		return m.group()[35:m.group().index("/>")-2]

# Gets the name of the comic from the given link
def getName(link):
	html = urllib2.urlopen(link).read()
	regex = re.compile("http://www.bugmartini.com/comic/.+/#comments")
	for m in regex.finditer(html):
		name = m.group()[32:m.group().index("/#comments")]
	name = name[0].upper()+name[1:]
	regex = re.compile("-.")
	for m in regex.finditer(name):
		name = name[:m.start()+1]+name[m.start()+1].upper()+name[m.start()+2:]
	return name

# Returns a link to the previous comic to the one in the given link
# If it is the oldest comic, returns the given link
def previous(link):
	html = urllib2.urlopen(link).read()
	regex = re.compile("link rel=\"prev\" href=\".+\" />")
	for m in regex.finditer(html):
		return m.group()[22:m.group().index("/>")-2]
	return link

# Returns a link to the next comic to the one in the given link
# If it is the most recent comic, returns the given link
def next(link):
	html = urllib2.urlopen(link).read()
	regex = re.compile("link rel=\"next\" href=\".+\" />")
	for m in regex.finditer(html):
		return m.group()[22:m.group().index("/>")-2]
	return link