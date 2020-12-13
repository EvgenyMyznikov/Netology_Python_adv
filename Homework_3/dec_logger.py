import os
from datetime import datetime
from Homework_2.generator_md5 import generator


def dec_logger(function):
    def wrapper(path):
        result = function(path)
        logs = {
            'date_time': f'{datetime.now()}',
            'name': function.__name__,
            'arguments': path,
            'result': result
        }
        with open('logs.txt', 'w') as f:
            f.write(str(logs))
        return result

    return wrapper


if __name__ == '__main__':
    decorator = dec_logger(generator)(os.path.abspath('countries.txt'))
