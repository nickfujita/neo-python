from boa.interop.Neo.Runtime import Notify

# build smartContract/arrayValues1.py test 0710 05 False False ANYTHING ['register']

def Main(operation, args):

    value = args[0]

    if value == 'register':
        print('this is working')
    else:
        print('this is NOT working')

    return True
