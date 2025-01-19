#!/usr/bin/env python3
import angr
project = angr.Project('./vuln', load_options={'auto_load_libs': False})
def print_flag(state):
    print("FLAG SHOULD BE:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()