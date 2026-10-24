from lib.mylib import _make_file
from lib.write_env import set_git_env, get_run_id

# rt = _make_file()


# set_git_env('MY_VAR', 'Env_Value')
set_git_env('MY_VAR', '1')


_run_id = get_run_id()
print(_run_id)
