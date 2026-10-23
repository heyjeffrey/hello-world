import os


def set_git_env(name: str, value: str):
    env_file = os.getenv('GITHUB_ENV')
    if env_file:
        with open(env_file, 'a') as f:
            # f.write("MY_VAR=MY_VALUE")
            f.write(f"{name.upper()}={value}")
        return True
    return False


set_git_env('MY_VAR', 'Env_Value')
