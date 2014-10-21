t_celsius = 66.6

print "The state of water with temperature", t_celsius, "degree celsius:"

if t_celsius >= 100.0:
    print "Air"
elif t_celsius >= 0.0:
    print "Liquid"
else:
    print "Solid"

# A second solution, without using elif

if t_celsius >= 100.0:
    print "Air"
else:
    if t_celsius >= 0.0:
        print "Liquid"
    else:
        print "Solid"

# Another solution is:

if 100 <= t_celsius:
    print "Air"
if 0.0 <= t_celsius < 100.0:
    print "Liquid"
if t_celsius < 0:
    print "Solid"
