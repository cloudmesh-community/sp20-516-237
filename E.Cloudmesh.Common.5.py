from cloudmesh.common.StopWatch import StopWatch
from time import sleep


StopWatch.start('test1')
y = []
for i in range(1000000):
    y.append(i+1)
print(len(y))
StopWatch.stop('test1')
print(StopWatch.get('test1', digits=4))

StopWatch.start('test2')
x = [i+1 for i in range(1000000)]
print(len(x))
StopWatch.stop('test2')
print(StopWatch.get('test2', digits=4))


StopWatch.benchmark()


