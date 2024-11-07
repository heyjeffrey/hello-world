import os


fpath = os.path.join(os.path.dirname(__file__), 'out.txt')

with open(file=fpath, mode='wt') as fw:
    print('hello world', file=fw)
