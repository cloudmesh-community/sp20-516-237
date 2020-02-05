##Testing Datetime and parser modules

from datetime import datetime
from dateutil.parser import parse

class_dates = [
    '8/25/2017',
    '9/1/2017',
    '9/8/2017',
    '9/15/2017',
    '9/22/2017',
    '9/29/2017']

a = [datetime.strptime(x, '%m/%d/%Y') for x in class_dates]
b = [parse(x) for x in class_dates]

print(a)
print(b)

## Testing sets vs lists
import sys, random, timeit
nums_set = set([random.randint(0, sys.maxsize) for _ in range(10**5)])
nums_list = list(nums_set)
print(len(nums_set))
print(timeit.timeit('random.randint(0, sys.maxsize) in nums',
            setup='import random; nums=%s' % str(nums_set), number=100))

print(timeit.timeit('random.randint(0, sys.maxsize) in nums',
              setup='import random; nums=%s' % str(nums_list), number=100))

## dicts

computer = {
  'name': 'mycomputer',
  'memory': 16,
  'kind': 'Laptop'
  }

print('{name} {memory}'.format(**computer))

## Counting using dicts

import random
die_rolls = [
  random.choice(['heads', 'tails']) for _ in range(10)
]
print(die_rolls)

counts = {'heads': 0, 'tails': 0}
for outcome in die_rolls:
   assert outcome in counts
   counts[outcome] += 1
print('Probability of heads: %.2f' % (counts['heads'] / len(die_rolls)))
print('Probability of tails: %.2f' % (counts['tails'] / sum(counts.values())))