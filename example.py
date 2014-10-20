import slowfast

title = "sorted reverse list"
one = "l = sorted(l);l.reverse()"
two = "l = sorted(l, reverse=True)"
setup = "l = [1, 2, 3, 5]"
slowfast.compare(title, one, two, setup)
