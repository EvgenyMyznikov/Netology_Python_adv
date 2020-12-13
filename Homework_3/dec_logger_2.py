import os
import hashlib
from datetime import datetime


def logger(path):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            logs = {
                'date_time': f'{datetime.now()}',
                'name': function.__name__,
                'arguments': path,
                'result': result
            }
            with open('new_logs.txt', 'w') as f:
                f.write(str(logs))
            return result
        return wrapper
    return decorator


@logger(os.path.abspath('logs.txt'))
def generator(path):
    with open(path, 'rb') as f:
        for string in f:
            yield hashlib.md5(string).hexdigest()


if __name__ == '__main__':
    for elem in generator(os.path.abspath('countries.txt')):
        print(elem)
