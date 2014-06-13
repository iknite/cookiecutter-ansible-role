Cookiecutter Ansible Role
=========================

Cookie cutter recipe to easily create `ansible roles`_. 
It infuses antigravity (or maybe not).

.. _`ansible roles`: http://docs.ansible.com/playbooks_roles.html#roles

Features
--------
  * follow `best practices`_.
  * create only the needed files and folders.
  * Blazing fast creation, forget about file creation and focus in actions.

.. _`best practices`: http://docs.ansible.com/playbooks_best_practices.html

Usage
-----

    cookiecutter https://github.com/iknite/cookiecutter-ansible-role.git

It begin to ask you configuration variables then you can enter tasks names,
handlers names, and default variables. 

Inside a `Add <some> name i.e (<example>)` you can go to next section by entering
an empty string.


Example::

    ROLE CONFIGURATION:

    It should had tasks?  [Y/n] y
    Add task name i.e (Install packages): fist task
    Add task name i.e (Install packages): next task
    Add task name i.e (Install packages): the next one will cut the cycle
    Add task name i.e (Install packages): 
    It should had handlers? [Y/n] 
    Add handler name i.e (Restart uwsgi): restart something
    Add handler name i.e (Restart uwsgi): alert someone
    Add handler name i.e (Restart uwsgi): 
    It should had default variables?:  [Y/n] 
    Add variable i.e (operator: User Name): variable_name: value
    Add variable i.e (operator: User Name): 
    It should had templates?  [Y/n] y
    It should had files?  [Y/n] n

This will generate this folders (Please note the absence of files folder)::

    .
    ├── CONTRIBUTORS.txt
    ├── defaults
    │   └── main.yml
    ├── handlers
    │   └── main.yml
    ├── LICENSE.rst
    ├── meta
    │   └── main.yml
    ├── README.rst
    ├── tasks
    │   └── main.yml
    └── templates

Contributings
-------------

All contributings are more than welcome, please do so.


License
-------

3-clause BSD license.
Copyright ©2013, Enrique Paredes



Enjoy it! 

