
source /opt/ansible/bin/activate

cwd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export ANSIBLE_CONFIG=${cwd}/config.ini
