#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from collections import OrderedDict
from cookiecutter.prompt import query_yes_no, prompt_for_config

try:
    input = raw_input
except NameError:
    pass


folders = OrderedDict()
folders['tasks']= {
    'question': 'It should had tasks? ',
    'hint': 'Add a tasks name i.e (Installing packages): ',
    'action': '- name: {}\n  # TODO\n\n'
}
folders['handlers'] = {
    'question': 'It should had handlers?',
    'hint': 'Add a handlers name i.e (Installing packages): ',
    'action': '- name: {}\n  # TODO\n\n'
}
folders['defaults'] = {
    'question': 'It should contain default variables?: ',
    'hint': 'Add a variable i.e (operator: User Name): ',
    'action': '{}\n\n'
}
folders['templates'] = {
    'question': 'It should had templates? ',
}
folders['files'] = {
    'question': 'It should had files? ',
}


def configure_role():
    print('\n\nROLE CONFIGURATION:\n')
    for folder_name, folder in folders.items():
        if query_yes_no(folder['question']):

            try:
                # this file has to be there, git doesn't store empty folders.
                os.remove(os.path.join(folder_name, '.empty'))
            except OSError:
                pass

            if 'hint' in folder:
                with open('{}/main.yml'.format(folder_name), 'a') as fp:
                    action_name = input(folder['hint'])
                    while action_name:
                        fp.write(folder['action'].format(action_name))
                        action_name = input(folder['hint'])

        else:
           shutil.rmtree(folder_name)
        

if __name__ == '__main__':
    configure_role()
