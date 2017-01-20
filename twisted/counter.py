__author__ = 'kud'
from twisted.internet import reactor


class Coutndown(object):
    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)

class Coutndown2(object):
    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)


class Coutndown3(object):
    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)


reactor.callWhenRunning(Coutndown().count)
reactor.callWhenRunning(Coutndown2().count)
reactor.callWhenRunning(Coutndown3().count)



print("Start")
reactor.run()
