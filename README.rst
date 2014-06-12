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

It begin to ask you configuration variables then you can enter tasks names, handlers names, and default variables
Example::

    ROLE CONFIGURATION:

    It should had tasks?  [Y/n] y
    Add a tasks name i.e (Installing packages): fist task
    Add a tasks name i.e (Installing packages): next task
    Add a tasks name i.e (Installing packages): tasks will appear until a empty task names appears
    Add a tasks name i.e (Installing packages): 
    It should had handlers? [Y/n] 
    Add a handlers name i.e (Installing packages): restart something
    Add a handlers name i.e (Installing packages): alert someone
    Add a handlers name i.e (Installing packages): 
    It should contain default variables?:  [Y/n] 
    Add a variable i.e (operator: User Name): variable_name: value
    Add a variable i.e (operator: User Name): 
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

