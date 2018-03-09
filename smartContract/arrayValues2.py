from boa.interop.Neo.Runtime import Notify

# build smartContract/arrayValues2.py test 0710 05 False False ANYTHING ['register']

def Main(operation, args):

    if args[0] == 'register':
        print('this is working')
    else:
        print('this is NOT working')

    return True
