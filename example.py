import slowfast

one = "l = sorted(l);l.reverse()"
two = "l = sorted(l, reverse=True)"
setup = "l = [1, 2, 3, 5]"
slowfast.compare(one, two, setup)

title = "sorted reverse list"
one = "l = sorted(l);l.reverse()"
two = "l = sorted(l, reverse=True)"
setup = "import random;l = range(1000);random.shuffle(l);"
slowfast.compare(one, two, setup, 100000, title)

title = "sorted reverse list"
one = "l = sorted(l, key=lambda s: len(s));l.reverse()"
two = "l = sorted(l, key=lambda s: len(s), reverse=True)"
setup = "import random;l = [[x for x in range(random.randrange(10))] for i in range(1000)];random.shuffle(l);"
slowfast.compare(one, two, setup, 100000, title)
