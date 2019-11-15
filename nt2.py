#! /usr/bin/env python3
from typing import NamedTuple

class StateInternal(NamedTuple):
    disk_ids: dict
    display_name: str
    ports: list
    throttling_file: str

class StateThrottling(NamedTuple):
    cpu: str
    network: str

#state = State(
#        None,           # disks
#        StateInternal(  # internal
#        False,          # failed
#        StateThrottling(# throttling
#            None,       #   cpu
#            None),      #   network
#        True,           # daemonize
#        None,           # state_file
#        None,           # v2v_log
#        None)           # machine_readable_log

#t = StateThrottling(None, None) # type error
t = StateThrottling('', '')

t.abc = 1
