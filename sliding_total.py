class SlidingTotal(object):
    class Bucket(object):
        def __init__(self, time):
            self.start = time
            self.total = 0

        def __str__(self):
            return '[ start: %s total: %s ]' % (
                    self.start,
                    self.total)

    def __init__(self, window, num_buckets=10):
        self.window = window
        self.resolution = int(window/num_buckets)
        self.current = 0
        self.buckets = []

    def onTime(self, time):
        while self.buckets and self.buckets[0].start <= time - self.window:
            self.current -= self.buckets[0].total
            self.buckets.pop(0)
        if not self.buckets or self.buckets[-1].start + self.resolution <= time:
            self.buckets.append(SlidingTotal.Bucket(time))

    def onValue(self, time, value):
        self.onTime(time)
        self.buckets[-1].total += value
        self.current += value

    def getCurrent(self, time=None):
        if time:
            self.onTime(time)
        return self.current

    def __str__(self):
        return ' '.join([str(x) for x in self.buckets]) + (" => %s" % (self.current))

if __name__ == "__main__":
    from test import check

    s = SlidingTotal(20, num_buckets=5)

    s.onValue(100, 1)
    check(s.getCurrent(), 1)

    check(s.getCurrent(120), 0)

    s.onValue(130, 1)
    check(s.getCurrent(), 1)

    s.onValue(130, 1)
    check(s.getCurrent(), 2)

    s.onValue(131, 1)
    check(s.getCurrent(), 3)

    s.onValue(132, 2)
    check(s.getCurrent(), 5)

    s.onValue(133, 1)
    check(s.getCurrent(), 6)

    s.onValue(134, 1)
    check(s.getCurrent(), 7)

    s.onValue(149, 1)
    check(s.getCurrent(), 8)

    s.onValue(150, 1)
    check(s.getCurrent(), 3)

