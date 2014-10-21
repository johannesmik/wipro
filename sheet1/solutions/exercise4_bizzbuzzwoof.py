for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print i
    else:
        if i % 3 == 0:
            print "bizz",
        if i % 5 == 0:
            print "buzz",
        if i % 7 == 0:
            print "woof",
        print ""
