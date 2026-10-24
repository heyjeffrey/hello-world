import os

from lib.mylib import _make_file
from lib.write_env import set_git_env, get_run_id

# rt = _make_file()


# set_git_env('MY_VAR', 'Env_Value')
# set_git_env('MY_VAR', '1')


_run_id = get_run_id()
print('GITHUB_RUN_ID:', _run_id)


ENV_VAR = os.getenv('ENV_VAR')
print('read from git', ENV_VAR)


def get_args() -> int:
    import sys
    try:
        if len(sys.argv) > 1:
            return int(sys.argv[1])
        return 0
    except Exception as e:
        print('Error')
    return 0


_arg_v = get_args()
print(_arg_v)
