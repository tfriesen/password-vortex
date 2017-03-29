#!/usr/bin/python2

import sys, getopt
from datetime import date


help_string = """Password-vortex!

Generate passwords commonly used in password rotation environments.

Options:

\t-h\t help

\t-m\t <min length> (default: 8)

\t-M\t <max length> (default: 100)

\t-d\t <start date>, in format YYYY-MM (default: today)

\t-l\t <months>, number of months to go back (default: 6)

\t-H\t include major holidays (ie Christmas, Easter) that occur during the time period (coming) (default: off)

\t-e\t <chars>, characters to append to the End of passwords, to generate more candidates. Use 's' for space. Only a single character 
\t\t is appended at a time. '!' and '.' are good candidates (default: none)

\t-s\t <chars>, characters to insert as a Separator between the month or season and the year. Use 's' for space. Only a single character 
\t\t is appended at a time. '!', '.', ',', '@', '#' and '_' are all good candidates (default: none). Vortex currently (and intentionally) 
\t\t only does one end character, OR one separator character per password candidate.

\t-c\t <complexity>, minimum password complexity allowed. In other words, a generated password must have this number of characters from 
\t\t different sets (upper, lower, number, etc). Microsoft environments generally require 3. (default: 2)

\t-x\t include common misspellings (ie Febuary, Autum) (coming) (default: off)

"""


month_list = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december" ]


seasons_list = [
    ["winter"],
    ["winter"],
    ["winter", "spring"],
    ["spring"],
    ["spring"],
    ["spring", "summer"],
    ["summer"],
    ["summer"],
    ["summer", "autumn", "fall"],
    ["autumn", "fall"],
    ["autumn", "fall"],
    ["autumn", "fall", "winter"] ]
    


def checkLen(passwd, min_len, max_len):
    return ( len(passwd) >= min_len and len(passwd)<= max_len )

def checkComplexity(passwd, min_complexity):
    complexity = 0
    
    if any(map(str.isupper, passwd)):
        complexity += 1
        
    if any(map(str.islower, passwd)):
        complexity += 1
    
    if any(map(str.isdigit, passwd)):
        complexity += 1
        
    if not passwd.isalnum() and len(passwd) > 0:
        complexity += 1
        
    return complexity >= min_complexity


def getDate(mydate):
    dates = mydate.split("-")
    return int(dates[0]), int(dates[1])


def formatCandidate(start, end, suffix_chars, separator_chars):
    candidates = []
    candidates.append(start + end)
    
    if len(suffix_chars) > 0:
        for char in suffix_chars:
            candidates.append(start+end+char)
    if len(separator_chars) > 0:
        for char in separator_chars:
            candidates.append(start+char+end)
            
    candidates.extend(map(str.capitalize, candidates))
    
    return candidates


def makeCandidates(start_year, start_month, num_months, suffix_chars, separator_chars, use_holidays, use_misspellings):
    candidates = []
    cur_month = start_month -1

    while (num_months > 0):
        cur_candidates = []
        if cur_month < 0:
            #TODO: check for overflow (negative years)
            start_year = start_year - 1
            cur_month = 11
            
        cur_candidates.extend(formatCandidate(month_list[cur_month][:3], str(start_year)[-2:], suffix_chars, separator_chars))
        cur_candidates.extend(formatCandidate(month_list[cur_month][:3], str(start_year), suffix_chars, separator_chars))
        cur_candidates.extend(formatCandidate(month_list[cur_month], str(start_year)[-2:], suffix_chars, separator_chars))
        cur_candidates.extend(formatCandidate(month_list[cur_month], str(start_year), suffix_chars, separator_chars))
        
        #add seasons. Will add duplicate entries, which are later removed
        for season in seasons_list[cur_month]:
            cur_candidates.extend(formatCandidate(season, str(start_year), suffix_chars, separator_chars))
            cur_candidates.extend(formatCandidate(season, str(start_year)[-2:], suffix_chars, separator_chars))
        
        num_months -= 1
        cur_month -= 1
        
        candidates.extend(cur_candidates)

    
    return candidates


def trimCandidates(candidates, min_len, max_len, min_complexity):
    new_candidates = []
    
    for candidate in candidates:
        if checkLen(candidate, min_len, max_len) and checkComplexity (candidate, min_complexity):
            new_candidates.append(candidate)
    
    #remove any duplicates before returning, https://www.peterbe.com/plog/uniqifiers-benchmark (comments)
    seen = set()
    seen_add = seen.add
    return [x for x in new_candidates if not (x in seen or seen_add(x))]
    

def main(argv):
    #set the defaults
    min_len = 8
    max_len = 100
    num_months = 6
    use_holidays = False
    suffix_chars = ""
    separator_chars = ""
    complexity = 2
    use_misspellings = False
    
    start_year = date.today().year
    start_month = date.today().month

    try:
        opts, args = getopt.getopt(argv,"hm:M:d:l:Hs:e:c:x")

    except getopt.GetoptError:
        print "Error in options.\n"
        print help_string
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print help_string
            sys.exit()
        elif opt == "-m":
            min_len = int(arg)
        elif opt == "-M":
            max_len = int(arg)
        elif opt == "-d":
            start_year, start_month = getDate(arg)
        elif opt == "-l":
            num_months = int(arg)
        elif opt == "-H":
            #use_holidays = True
            print "Holidays not currently implemented, sorry"
            sys.exit(2)
        elif opt == "-s":
            separator_chars = list(arg)
            #convert 's' to a space
            if "s" in separator_chars:
                separator_chars[separator_chars.index("s")] = " "
        elif opt == "-e":
            suffix_chars = list(arg)
            #convert 's' to a space
            if "s" in suffix_chars:
                suffix_chars[suffix_chars.index("s")] = " "
        elif opt == "-c":
            complexity = int(arg)
        elif opt == "-x":
            #use_misspellings = True
            print "Misspellings not currently implemented, sorry"
            sys.exit(2)            
        else:
            print "Error in options.\n"
            print help_string
            sys.exit(2)
            

    candidates = makeCandidates(start_year, start_month, num_months, suffix_chars, separator_chars, use_holidays, use_misspellings)
    candidates = trimCandidates(candidates, min_len, max_len, complexity)
    
    for candidate in candidates:
        print candidate


if __name__ == "__main__":
    main(sys.argv[1:])