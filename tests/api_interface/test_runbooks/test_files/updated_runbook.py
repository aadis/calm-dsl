"""
Calm DSL Sample Runbook used for testing runbook update

"""

from calm.dsl.builtins import runbook
from calm.dsl.builtins import CalmTask
from calm.dsl.builtins import read_local_file, basic_cred


code = '''print "Start"
sleep(20)
print "End"'''

CRED_USERNAME = read_local_file(".tests/runbook_tests/username")
CRED_PASSWORD = read_local_file(".tests/runbook_tests/password")

LinuxCred = basic_cred(CRED_USERNAME, CRED_PASSWORD, name="linux_cred")


@runbook
def DslUpdatedRunbook(credentials=[LinuxCred]):
    "Runbook Service example"
    CalmTask.Exec.escript(name="Task2", script=code)
    CalmTask.Exec.escript(name="Task3", script=code)
    CalmTask.Exec.escript(name="Task4", script=code)
    CalmTask.Exec.escript(name="Task5", script=code)
