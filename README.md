# password-vortex
A python tool for generating passwords commonly used when password rotation is enforced

Enforcing password rotation is bad. Users (myself included) are lazy, and when forced to regularly update their passwords will
fall back on common, predictable themes, usually centered around the current date.

For example, a user updating his or her password every month might use the following scheme:

```
January2017!
February2017!
March2017!
etc
```

If updating every 4 months, a user might employ the seasons:

```
Fall16
Winter16
Spring17
etc
```

Basically I got tired of generating or updating new password lists for every pen test, and so: password-vortex!

## Usage ##

Prints to standard out, one password per line.

```bash
python vortex.py [options]
```

## Options

**-m** <min length> (default: 8)

**-M** <max length> (default: 100)

**-d** <start date>, in format YYYY-MM (default: today)

**-l** <months>, number of months to go back (default: 6)

**-H** include major holidays (ie Christmas, Easter) that occur during the time period (coming)

**-s** <special chars>, special characters to append to the end of passwords, to generate more candidates. Use 's' for space. Only a single character is appended at a time. '!' and '.' are good candidates (default: none)

**-c** <complexity>, minimum password complexity allowed. In other words, a generated password must have this number of characters from different sets (upper, lower, number, etc). Microsoft environments generally require 3. (default: 2)



## Examples

```./vortex.py -m8 -d 2015-10 -l 2 -s ! -c 3 -H```

Should generate (be sure to escape that '!')

```
sep2015!
Sep2015!
september2015!
september15!
September2015
September2015!
September15
September15!
oct2015!
Oct2015!
october2015!
october2015!
October2015
October2015!
halloween2015!
halloween15!
Halloween15!
Halloween2015
Halloween2015
Halloween2015!
Fall2015
fall2015!
Autumn15
Autumn15!
autumn15!
```

Plus maybe Canadian thanksgiving. Also, this list was manually generated, so I may have missed one and the order is wrong.
