import os


def _make_file() -> bool:
    fpath = os.path.join(os.path.dirname(__file__),
                         os.pardir,  'out', 'out.txt')

    with open(file=fpath, mode='wt') as fw:
        print('hello world', file=fw)
        return True
    return False
