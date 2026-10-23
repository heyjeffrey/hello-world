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


def set_git_env(name: str, value: str):
    env_file = os.getenv('GITHUB_ENV')
    if env_file:
        with open(env_file, 'a') as f:
            # f.write("MY_VAR=MY_VALUE")
            f.write(f"{name.upper()}={value}")
        return True
    return False
