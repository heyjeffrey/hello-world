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


def cancel_workflow_run(token: str, repo: str, run_id: str = ''):
    """
    repo: owner/repo
    """
    import requests

    run_id = run_id or os.getenv('GITHUB_RUN_ID', '')
    if not run_id:
        return False

    # {repo_owner}/{repo_name}
    url = f'https://api.github.com/repos/{repo}/actions/runs/{run_id}/cancel'

    if token.startswith('ghp_'):
        _auth = f"token {token}"
    else:
        _auth = f"Bearer {token}"

    headers = {
        'Authorization': _auth,
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2026-03-10'
    }

    _r = requests.post(url, headers=headers)
    return _r.status_code == 202
