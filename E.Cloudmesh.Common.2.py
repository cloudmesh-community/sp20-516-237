from cloudmesh.common.dotdict import dotdict


data = {
    'fname': 'Jonathan',
    'lname': 'Beckford',
    'Company': 'Verizon'
}

person = dotdict(data)

print("Person from dict: ", person.fname, person.lname)