#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

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
            if 'hint' in folder:
                with open('{}/main.yml'.format(folder_name), 'a') as fp:
                    action_name = True
                    while action_name:
                        action_name = input(folder['hint'])
                        fp.write(folder['action'].format(action_name))
        else:
           shutil.rmtree(folder_name)


if __name__ == '__main__':
    configure_role()
