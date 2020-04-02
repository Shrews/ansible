from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.connection.local import Connection as LocalConnection
from ansible.utils.display import Display

display = Display()


class Connection(LocalConnection):

    transport = 'filament'

    def exec_command(self, cmd, in_data=None, sudoable=True):
        display.debug("***** DWS: here")
        return super(Connection, self).exec_command(cmd, in_data=in_data, sudoable=sudoable)
