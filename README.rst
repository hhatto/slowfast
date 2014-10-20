slowfast
========
Two Python code compare using timeit module.


Usage
-----
module::

    # rev.py
    import slowfast

    title = "sorted reverse list"
    one = "l = sorted(l);l.reverse()"
    two = "l = sorted(l, reverse=True)"
    setup = "l = [1, 2, 3, 5]"
    slowfast.compare(title, one, two, setup)

    $ python rev.py
    ===== sorted reverse list =====
    (slow) 0.063604[sec]
      l = sorted(l, reverse=True)
    (fast) 0.035824[sec]
      l = sorted(l);l.reverse()
    1.78 times faster
    $


LICENSE
-------
MIT
