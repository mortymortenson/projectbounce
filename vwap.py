class TrailingVWAP(object):
    class Bucket(object):
        def __init__(self, time):
            self.start = time
            self.volume = 0
            self.notional = 0

        def __str__(self):
            return '[ start: %s volume: %s notional: %s ]' % (
                    self.start,
                    self.volume,
                    self.notional)

    def __init__(self, window, num_buckets=10):
        self.window = window
        self.resolution = int(window/num_buckets)
        self.volume = 0
        self.notional = 0
        self.buckets = []

    def onTime(self, time):
        while self.buckets and self.buckets[0].start <= time - self.window:
            self.volume -= self.buckets[0].volume
            self.notional -= self.buckets[0].notional
            self.buckets.pop(0)
        if not self.buckets or self.buckets[-1].start + self.resolution <= time:
            self.buckets.append(TrailingVWAP.Bucket(time))

    def onValue(self, time, price, size):
        self.onTime(time)
        self.buckets[-1].volume += size
        self.buckets[-1].notional += size * price

        self.volume += size
        self.notional += size * price

    def getVWAP(self, time=None):
        if time:
            self.onTime(time)
        if self.volume:
            return self.notional/self.volume
        else:
            return None

    def getVolume(self, time=None):
        if time:
            self.onTime(time)
        return self.volume

    def __str__(self):
        return ' '.join([str(x) for x in self.buckets]) + (" => %s" % (self.getVWAP()))

if __name__ == "__main__":
    from test import check

    s = TrailingVWAP(20, num_buckets=5)

    s.onValue(100, 5.00, 1)
    check(s.getVWAP(), 5.00)
    check(s.getVolume(), 1)

    check(s.getVolume(120), 0)
    check(s.getVWAP(120), None)

    s.onValue(130, 1.00, 1)
    check(s.getVWAP(), 1)
    check(s.getVolume(), 1)

    s.onValue(130, 1.00, 1)
    check(s.getVWAP(), 1.00)
    check(s.getVolume(), 2)

    s.onValue(131, 1.00, 1)
    check(s.getVWAP(), 1.00)
    check(s.getVolume(), 3)

    s.onValue(132, 1.00, 2)
    check(s.getVWAP(), 1.00)
    check(s.getVolume(), 5)

    s.onValue(133, 1.00, 1)
    check(s.getVWAP(), 1.00)
    check(s.getVolume(), 6)

    s.onValue(134, 1.00, 1)
    check(s.getVWAP(), 1.00)
    check(s.getVolume(), 7)

    s.onValue(149, 1.00, 1)
    check(s.getVWAP(), 1.00)
    check(s.getVolume(), 8)

    s.onValue(150, 1.00, 1)
    check(s.getVWAP(), 1.00)
    check(s.getVolume(), 3)

    s.onValue(170, 3.00, 2)
    s.onValue(171, 2.00, 2)
    check(s.getVWAP(), 2.50)
    check(s.getVolume(), 4)


