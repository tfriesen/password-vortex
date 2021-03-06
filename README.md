# password-vortex
A python tool for generating passwords commonly used when password rotation is enforced.

Enforcing password rotation is bad. Users (myself included) are lazy, and when forced to regularly update their passwords will
fall back on common, predictable themes, usually centered around the current date.

For example, a user updating his or her password every month might use the following scheme:

```
January2017!
February2017!
March2017!
...
```

If updating every 4 months, a user might employ the seasons:

```
Fall_16
Winter_16
Spring_17
...
```

Basically I got tired of generating or updating new password lists for every pen test, and so: password-vortex!

## Usage ##

Prints to standard out, one password per line.

```bash
vortex.py [options]
```

## Options

**-h** help

**-m** \<min length\> (default: 8)

**-M** \<max length\> (default: 100)

**-d** \<start date\>, in format YYYY-MM (default: today)

**-l** \<months\>, number of months to go back (default: 6)

**-H** include major holidays (ie Christmas, Easter) that occur during the time period (coming) (default: off)

**-e** \<chars\>, characters to append to the **e**nd of passwords, to generate more candidates. Multiple characters can be specified, but only a single character is appended at a time. '!' and '.' are good candidates (default: none)

**-s** \<chars\>, characters to insert as a **s**eparator between the month or season and the year. Multiple characters can be specified, but only a single character is appended at a time. '!', '.', ',', '@', '#' and '_' are all good candidates (default: none). Vortex currently (and intentionally) only does one end character, OR one separator character per password candidate.

**-c** \<complexity\>, minimum password complexity allowed. In other words, a generated password must have this number of characters from different sets (upper, lower, number, symbol). Microsoft environments generally require 3. (default: 2)

**-x** include common misspellings (ie Febuary, Autum) (coming) (default: off)


## Examples

```vortex.py -m 8 -d 2015-02 -l 2 -s . -c 3 -e !```

Will generate (careful with that "!" in bash)

```
feb2015!
feb.2015
Feb2015!
Feb.2015
february15!
february.15
February15
February15!
February.15
february2015!
february.2015
February2015
February2015!
February.2015
winter2015!
winter.2015
Winter2015
Winter2015!
Winter.2015
winter15!
winter.15
Winter15
Winter15!
Winter.15
jan2015!
jan.2015
Jan2015!
Jan.2015
january15!
january.15
January15
January15!
January.15
january2015!
january.2015
January2015
January2015!
January.2015
```


## FAQ

### Any tips for using this tool?

If you can afford extra password guesses, go back further than you think you need to. User accounts are frequently abandoned (ie an employee leaves) and not properly disabled. Users are also very good at avoiding rotating their passwords, if they can. On my own pentests I've found accounts using passwords that would seem to be 3+ years old, despite much shorter expiration policies.

### Why don't you include passwords where the year comes first?

Because I have never ever ever once seen a password in that format. People just don't think 2015March, it's always March2015.

### Why don't allow multiple end characters to be appended or as separators?

While you will occasionally see a user use two special characters at the end (ie March2015!!), it's pretty rare, and the point of this tool is to create passwords that are very commonly used.

### Why don't password candidates get separator AND suffix characters? Why only one or the other?

See previous answer.

### Who decides what counts as a 'major' Holiday?

I do.

### How effective is this tool? How common are passwords like these in the real world?

In my experience, about 2-3% of users will use a password rotation scheme that would be covered by this tool, when password rotation is enforced. That may not sound like a lot, but even in an organization of just 100 valid accounts, there will almost certainly be more than one account that would be cracked.

### How can I protect my organization?

The best thing to do is turn off password rotation! I know this may sound crazy, as that's what the infosec experts have been advising for decades, but we've recently come to realize that password rotation hurts much more than it helps. But that is a topic that would take much more than a FAQ to address.


