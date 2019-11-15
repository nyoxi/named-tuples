#! /usr/bin/env python3
from collections import namedtuple

# self._state = {
#         'disks': [],
#         'internal': {
#             'disk_ids': {},
#             'display_name': None,
#             'ports': [],
#             'throttling_file': None,
#             },
#         'failed': False,
#         'throttling': {
#             'cpu': None,
#             'network': None,
#             }
#         }
# self.daemonize = True
# self.state_file = None
# self.v2v_log = None
# self.machine_readable_log = None

State = namedtuple('State', ['disks', 'internal', 'failed', 'throttling', 'daemonize', 'state_file', 'v2v_log', 'machine_readable_log'])
StateInternal = namedtuple('StateInternal', ['disk_ids', 'display_name', 'ports', 'throttling_file'])
StateThrottling = namedtuple('StateThrottling', ['cpu', 'network'])

state = State(
        None,           # disks
        StateInternal(  # internal
            {},         #   disk_ids
            None,       #   display_name
            [],         #   ports
            None),      #   throttling_file
        False,          # failed
        StateThrottling(# throttling
            None,       #   cpu
            None),      #   network
        True,           # daemonize
        None,           # state_file
        None,           # v2v_log
        None)           # machine_readable_log

print(state.disks)
print(state.internal.ports)
state.abc = 1
print(state.abc)
