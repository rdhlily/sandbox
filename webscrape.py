# Practice Webscraper to be used to pull data
import os
os.getcwd() #currently in users/lilyfalk, so to get to python folder will need to specify

from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
page

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)  #contents of webpage - have information from webpage as text, can extract in a few different ways

title_index = html.find("<title>")
title_index
start_index = title_index + len("<title>")
start_index
end_index = html.find("</title>")
end_index

title = html[start_index:end_index]
title
#------------------------------------
#More complicated HTML
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title

# Working with regular expressions
import re  #regular expressions use metacharacters to denote patterns
re.findall("ab*c", "ac")  #"*" denotes zero or more of whatever comes just before the *. ac is the test case
# ^ match any part of string that begins with a and ends with c and has zero or more instances of b between the two
re.findall("ab*c", "acc")
re.findall("ab*c", "abcac")
re.findall("ab*c", "abdc")
#^last one is empty... too many letters?
#This findall is case sensitive. Ust IGNORECASE to change that
re.findall("ab*c", "ABC")
re.findall("ab*c", "ABC", re.IGNORECASE)

#A period can stand for any single character
re.findall("a.c", "abc")  #find all a - c separated by single character
re.findall("a.c", "abbc")
re.findall("a.c", "ac")
re.findall("a.c", "acc")

#".*" stands for any character repeated any number of times
re.findall("a.*c", "abc")
re.findall("a.*c", "abbc")
re.findall("a.*c", "ac")

#re.search() - search for particular pattern in string
#More complicated because it returns an object called a MatchObject
#MatchObject stores different groups of data - might be matches inside other matches
#re.search () returns every possible result.
#calling .group() on a MatchObject will return first and most inclusive result - in most cases that is what you want
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()

#re.sub() - (short for subsitute) for parsing out text - 
