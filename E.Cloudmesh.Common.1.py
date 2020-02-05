from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables
import memory_profiler as mem_profile
import random
import time

names = ['John', 'Jack', 'Adam', 'Steve', 'Rick']
majors = ['Math',
          'CompScience',
          'Arts',
          'Business',
          'Economics']

# prints the memory before we run the function
memory = mem_profile.memory_usage(-1)
banner(f'Memory (Before): {memory}Mb')


def people_generator(people):
    HEADING()
    for i in range(people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.process_time()

people = people_generator(10000000)
t2 = time.process_time()

# prints the memory after we run the function
memory = mem_profile.memory_usage(-1)
banner(f'Memory (After): {memory}Mb')
banner('Took {time} seconds'.format(time=t2-t1))

test_individual = next(people)
VERBOSE(test_individual)