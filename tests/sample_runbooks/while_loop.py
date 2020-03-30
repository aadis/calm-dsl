"""
Calm DSL Sample Runbook with while loop task

"""

from calm.dsl.builtins import runbook
from calm.dsl.builtins import CalmTask


@runbook
def DslWhileLoopRunbook():
    "Runbook Service example"
    while(CalmTask.While(10, name="WhileTask", parallel_factor=2)):
        CalmTask.Exec.escript(name="Task1", script="print 'Inside loop1 @@{iteration}@@'")

    while(5):
        CalmTask.Exec.escript(name="Task2", script="print 'Inside loop2 @@{iteration}@@'")


def main():
    print(DslWhileLoopRunbook.runbook.json_dumps(pprint=True))


if __name__ == "__main__":
    main()
