from timeit import timeit


def _print_result(one_time, one_pystm, two_time, two_pystm):
    if one_time > two_time:
        slow_pystm = one_pystm
        slow_time = one_time
        fast_pystm = two_pystm
        fast_time = two_time
    else:
        slow_pystm = two_pystm
        slow_time = two_time
        fast_pystm = one_pystm
        fast_time = one_time
    print("(slow) %f[sec]" % slow_time)
    print("\n".join(["  " + l for l in slow_pystm.splitlines()]))
    print("(fast) %f[sec]" % fast_time)
    print("\n".join(["  " + l for l in fast_pystm.splitlines()]))
    print("%.2f times faster" % (slow_time/fast_time))


def compare(one, two, setup='pass', number=10000, title=''):
    print("===== %s =====" % title)
    while True:
        _one = timeit(one, setup=setup, number=number)
        _two = timeit(two, setup=setup, number=number)
        if _one == _two:
            continue
        _print_result(_one, one, _two, two)
        print("")
        break


if __name__ == '__main__':
    #compare(
    #    "print(1)",
    #    "print 1",
    #    title="print",
    #)
    NUM = 500000
    compare(
        """\
s = "Hello, {} {}".format(first, second)""",
        """\
s = "Hello, {first} {second}".format(first=first, second=second)""",
        setup="""first = 'jim';second = 'hope'""",
        number=NUM,
        title="format string 1",
    )

    compare(
        """\
s = "Hello, %s %s" % (first, second)""",
        """\
s = "Hello, {} {}".format(first, second)""",
        setup="""first = 'jim';second = 'hope'""",
        number=NUM,
        title="format string 2",
    )

    compare(
        "[str(i) for i in range(10)]",
        "map(str, [i for i in range(10)])",
        number=NUM,
        title="to string",
    )

    compare(
        """\
s.find('c') != -1""",
        """\
'c' in s""",
        setup="s = 'abcde'",
        number=NUM,
        title="find string",
    )

    compare(
        """\
l.reverse()""",
        """\
l = [i for i in reversed(l)]""",
        setup="l = [1, 2, 3, 5]",
        number=NUM,
        title="reverse list",
    )

    compare(
        """\
l = sorted(l)
l.reverse()""",
        """\
l = sorted(l, reverse=True)""",
        setup="""l = [1, 2, 3, 5]""",
        number=NUM,
        title="sorted reverse list",
    )

    compare(
        """\
d = {}""",
        """\
d = dict()""",
        number=NUM,
        title="dict",
    )

    compare(
        """\
t = ()""",
        """\
t = tuple()""",
        number=NUM,
        title="tuple",
    )

    compare(
        """\
l = []""",
        """\
l = list()""",
        number=NUM,
        title="list",
    )
