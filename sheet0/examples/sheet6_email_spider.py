#!/usr/bin/python
import re
import urllib

__author__ = 'johannes'

def extractEmail(text):

    emails = set()
    # Original
    matches = re.finditer(r'[: ]([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)[" ]', text)

    matches = re.finditer(r'[: ]([a-zA-Z0-9._-]+(@|\(at\))[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)[" ]', text)
    for match in matches:
        print "found!"
        print match.group()
        emails.add(match.group(1))
    print "extracted emails, found: ", emails
    return emails

def extractLinks(text):
    links = set()

    matches = re.finditer(r'(http:\/\/[a-zA-Z0-9._/-]+)[" ]', text)
    for match in matches:
        links.add(match.group(1))
    print "extracted links, found: ", links

    return links

queue = ["http://www.in.tum.de/metanavigation/personen-services/dekanat.html"]
visited = set()
emails = set()

while len(queue) != 0 and len(visited) < 20:

    print "Die aktuelle Queue ist:"
    print queue
    print ""

    current_address = queue.pop()
    if current_address in visited:
        # bereits besucht
        continue
    else:
        visited.add(current_address)

    print "Opening", current_address

    try:
        text = urllib.urlopen(current_address).read()
    except IOError:
        print "# IOError!"
        continue

    # Get new links
    links = extractLinks(text)
    queue.extend(list(links))

    # Get new emails
    emails = emails.union(extractEmail(text))

print "I found %i emails :)" % len(emails)
print emails
