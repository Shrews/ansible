from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.strategy.linear import StrategyModule as LinearStrategy
from ansible.utils.display import Display
import time

display = Display()


class StrategyModule(LinearStrategy):

    def _queue_task(self, host, task, task_vars, play_context):
        display.debug("Sleeping 1 second for task %s" % task)
        time.sleep(1)
        super()._queue_task(host, task, task_vars, play_context)
