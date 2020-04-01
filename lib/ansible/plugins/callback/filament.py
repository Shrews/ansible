from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
from os.path import basename


class CallbackModule(CallbackBase):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'filament'

    def __init__(self):
        super(CallbackModule, self).__init__()

    def v2_runner_on_start(self, host, task):
        self._display.display(" [started %s on %s]" % (task, host))

    def v2_playbook_on_start(self, playbook):
        self._display.banner("PLAYBOOK: %s" % basename(playbook._file_name))

    def v2_playbook_on_play_start(self, play):
        self._display.banner("PLAY: %s" % play.get_name())

    def v2_playbook_on_task_start(self, task, is_conditional):
        self._display.banner("TASK: %s" % task.get_name())

    def v2_runner_on_ok(self, result):
        self._display.banner("RESULTS: %s" % result._result)
