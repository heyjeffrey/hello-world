import os


def set_git_env(name: str, value: str):
    """
    Note that this solution works for outputs 
    by using GITHUB_OUTPUT instead of GITHUB_ENV.

    # client_id = os.getenv('CLIENT_ID')
    # client_secret = os.getenv('CLIENT_SECRET')
    """

    env_file = os.getenv('GITHUB_ENV')
    if env_file:
        with open(env_file, 'a') as f:
            # f.write("MY_VAR=MY_VALUE")
            f.write(f"{name.upper()}={value}")
        return True
    return False


def get_run_id():
    _id = os.getenv('GITHUB_RUN_ID')
    return _id


# set_git_env('MY_VAR', 'Env_Value')
"""
# GITHUB_RUN_ID
echo GITHUB_RUN_ID >> $GITHUB_ENV

API_KEY = os.getenv('MY_API_KEY')
"""
