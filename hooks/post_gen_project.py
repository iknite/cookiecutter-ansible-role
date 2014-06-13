#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from collections import OrderedDict
from cookiecutter.prompt import query_yes_no

try:
    input = raw_input
except NameError:
    pass


folders = OrderedDict()

folders['tasks']= {
    'question': '\nIt should had tasks? ',
    'hint': '  Add task name i.e (Install packages): ',
    'action': '- name: {}\n  # TODO\n\n'
}

folders['handlers'] = {
    'question': '\nIt should had handlers?',
    'hint': '  Add handler name i.e (Restart uwsgi): ',
    'action': '- name: {}\n  # TODO\n\n'
}

folders['defaults'] = {
    'question': '\nIt should contain default variables?: ',
    'hint': '  Add variable i.e (operator: : drunken_master)',
    'action': '{}\n\n'
}

folders['meta']= {
    'question': '\nIt should had meta info? ',
    'pre_hint': ' - It should had dependecies? ',
    'pre_action': '\ndependencies:\n',
    'hint': '    Add dependecy i.e ({role: aptsupercow, apt_state=present}): ',
    'action': '  - {}\n'
}

folders['templates'] = {
    'question': '\nIt should had templates? ',
}

folders['files'] = {
    'question': '\nIt should had files? ',
}


def configure_role():
    print('\n\nROLE CONFIGURATION:\n===================')
    for folder_name, folder in folders.items():
        if query_yes_no(folder['question']):

            try:
                # this file has to be there, git doesn't store empty folders.
                os.remove(os.path.join(folder_name, '.empty'))
            except OSError:
                pass

            if 'hint' in folder:
                with open('{}/main.yml'.format(folder_name), 'a') as fp:

                    if 'pre_hint' in folder:
                        if query_yes_no(folder['pre_hint']):
                            fp.write(folder['pre_action'])
                        else:
                            continue

                    action_name = input(folder['hint'])
                    while action_name:
                        fp.write(folder['action'].format(action_name))
                        action_name = input(folder['hint'])

        else:
           shutil.rmtree(folder_name)


if __name__ == '__main__':
    configure_role()
