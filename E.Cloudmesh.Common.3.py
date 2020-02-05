from cloudmesh.common.FlatDict import FlatDict

data = {
    'name': {
        'fname': 'Jonathan',
        'lname': 'Beckford'
    },
    'address': {
        'location': {
            'city': 'Atlanta',
            'zip': '30041'
        },
        'state': 'GA'
    },

}

flat = FlatDict(data, sep='.')

print(flat)