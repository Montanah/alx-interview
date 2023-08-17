#!/usr/bin/python3
"""module with log parsing function"""

import sys


def main():
    """prints stats every 10 lines"""
    l_count = 0
    f_size = 0
    status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
              '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            input_list = line.split()
            if len(input_list) < 2:
                continue
            l_count += 1
            f_size += int(input_list[-1])
            if input_list[-2] not in status:
                continue
            status[input_list[-2]] += 1
            if l_count == 10:
                l_count = 0
                print('File size: {}'.format(f_size))
                for key in ['200', '301', '400', '401', '403', '404',
                            '405', '500']:

                    if status[key] != 0:
                        print('{}: {}'.format(key, status[key]))
    except KeyboardInterrupt:
        pass
    except Exception:
        return
    print('File size: {}'.format(f_size))
    for key in ['200', '301', '400', '401', '403', '404', '405', '500']:
        if status[key] != 0:
            print('{}: {}'.format(key, status[key]))
