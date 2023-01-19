#9.4

class OopsException(Exception):
    pass

try:
    raise OopsException()
except OopsException as err:
    print(f'Caught an oops.')