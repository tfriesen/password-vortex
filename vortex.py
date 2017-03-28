#!/usr/bin/python2

import sys, getopt
from datetime import date


help_string = """Password-vortex!

Generate passwords commonly used in password rotation environments.
"""



full_month_list = [
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

abbrv_month_list = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec" ]




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


def makeCandidates(start_year, start_month, num_months, special_chars, use_holidays, use_misspellings):
    candidates = []
    cur_month = start_month -1

    while (num_months > 0):
        cur_candidates = []
        if cur_month < 0:
            #TODO: check for overflow (negative years)
            start_year = start_year - 1
            cur_month = 11
        cur_candidates.append(full_month_list[cur_month] + str(start_year))
        cur_candidates.append(full_month_list[cur_month] + str(start_year)[-2:])
        cur_candidates.append(abbrv_month_list[cur_month] + str(start_year))
        cur_candidates.append(abbrv_month_list[cur_month] + str(start_year)[-2:])
        
        candidates.extend(cur_candidates)
        candidates.extend(map(str.capitalize, cur_candidates))
        
        num_months -= 1
        cur_month -= 1

    
    cur_candidates = []
    if len(special_chars) > 0:
        for candidate in candidates:
            for char in special_chars:
                cur_candidates.append(candidate + char)
    
    candidates.extend(cur_candidates)
    
    return candidates


def trimCandidates(candidates, min_len, max_len, min_complexity):
    new_candidates = []
    
    for candidate in candidates:
        if checkLen(candidate, min_len, max_len) and checkComplexity (candidate, min_complexity):
            new_candidates.append(candidate)
    
    return new_candidates
    

def main(argv):
    #set the defaults
    min_len = 8
    max_len = 100
    num_months = 6
    use_holidays = False
    special_chars = ""
    complexity = 2
    use_misspellings = False
    
    start_year = date.today().year
    start_month = date.today().month

    try:
        opts, args = getopt.getopt(argv,"hm:M:d:l:Hs:c:x")

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
            special_chars = list(arg)
            #convert 's' to a space
            if "s" in special_chars:
                special_chars[special_chars.index("s")] = " "
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
            

    candidates = makeCandidates(start_year, start_month, num_months, special_chars, use_holidays, use_misspellings)
    candidates = trimCandidates(candidates, min_len, max_len, complexity)
    
    for candidate in candidates:
        print candidate

if __name__ == "__main__":
    main(sys.argv[1:])