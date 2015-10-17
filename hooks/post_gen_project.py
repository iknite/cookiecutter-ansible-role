#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from collections import OrderedDict
from cookiecutter.prompt import read_user_yes_no

try:
    input = raw_input
except NameError:
    pass


folders = OrderedDict()

folders['tasks']= {
    'question': '\nShould it have tasks? ',
    'hint': '  Add task name i.e (Install packages) ',
    'action': '- name: {}\n  # TODO\n\n'
}

folders['handlers'] = {
    'question': '\nShould it have handlers?',
    'hint': '  Add handler name i.e (Restart uwsgi) ',
    'action': '- name: {}\n  # TODO\n\n'
}

folders['defaults'] = {
    'question': '\nIt should contain default variables?: ',
    'hint': '  Add variable i.e (operator: drunken_master) ',
    'action': '{}\n\n'
}

folders['meta']= {
    'question': '\nShould it have meta info? ',
    'pre_hint': ' - Should it have dependecies? ',
    'pre_action': '\ndependencies:\n',
    'hint': '    Add dependecy i.e ({role: aptsupercow, var: \'value\'}) ',
    'action': '  - {}\n'
}

folders['templates'] = {
    'question': '\nShould it have templates? ',
}

folders['files'] = {
    'question': '\nShould it have files? ',
}


def configure_role():
    print('\n\nROLE CONFIGURATION:\n===================')
    for folder_name, folder in folders.items():
        if read_user_yes_no(folder['question'], default_value=u'yes'):

            try:
                # this file has to be there, git doesn't store empty folders.
                os.remove(os.path.join(folder_name, '.empty'))
            except OSError:
                pass

            if 'hint' in folder:
                with open('{}/main.yml'.format(folder_name), 'a') as fp:

                    if 'pre_hint' in folder:
                        if read_user_yes_no(folder['pre_hint'], default_value=u'yes'):
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
