from timeit import timeit

NUM = 50000


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


def compare(title, one, two, setup='pass'):
    print("===== %s =====" % title)
    while True:
        _one = timeit(one, setup=setup, number=NUM)
        _two = timeit(two, setup=setup, number=NUM)
        if _one == _two:
            continue
        _print_result(_one, one, _two, two)
        print("")
        break


if __name__ == '__main__':
    #compare(
    #    "print",
    #    "print(1)",
    #    "print 1",
    #)

    compare(
        "to string",
        "[str(i) for i in range(100)]",
        "map(str, [i for i in range(100)])",
    )

    compare(
        "find string",
        """\
s.find('c') != -1""",
        """\
'c' in s""",
        setup="s = 'abcde'",
    )

    compare(
        "reverse list",
        """\
l.reverse()""",
        """\
l = [i for i in reversed(l)]""",
        setup="l = [1, 2, 3, 5]",
    )

    compare(
        "sorted reverse list",
        """\
l = sorted(l)
l.reverse()""",
        """\
l = sorted(l, reverse=True)""",
        setup="""l = [1, 2, 3, 5]""",
    )
