from datetime import datetime
import os


def _make_file() -> bool:
    fpath = os.path.join(os.path.dirname(__file__),
                         os.pardir,  'out', 'out.txt')

    _dt = datetime.strftime(datetime.now(), "%d/%m/%Y, %H:%M:%S")

    with open(file=fpath, mode='wt') as fw:
        print(f'hello world!\n{_dt}', file=fw)
        return True
    return False
