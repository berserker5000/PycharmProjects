def hello():
    print('Hello from reactor')
    print('WTF is that?')

from twisted.internet import reactor
reactor.callWhenRunning(hello)

print('Starting reactor')
reactor.run()
