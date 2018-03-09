from boa.interop.Neo.Runtime import Notify

# build smartContract/arrayValues.py test 0710 05 False False ANYTHING ['register']

def Main(operation, args):

    isWorking = args[0] == 'register'

    if isWorking:
        print('this is working')
    else:
        print('this is NOT working')

    return True
