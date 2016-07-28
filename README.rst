Cookiecutter Ansible Role
=========================

Cookie cutter recipe to easily create `ansible roles`_. 
It infuses antigravity (or maybe not).

.. _`ansible roles`: http://docs.ansible.com/playbooks_roles.html#roles

Features
--------
  * Follows `best practices`_.
  * Only Creates the necessary files and folders.
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
    ===================

    Should it have tasks?  [Y/n] 
      Add task name i.e (Install packages) Add some task
      Add task name i.e (Install packages) another task 
      Add task name i.e (Install packages) 

    Should it have handlers? [Y/n] 
      Add handler name i.e (Restart uwsgi) restart something
      Add handler name i.e (Restart uwsgi) alert someone
      Add handler name i.e (Restart uwsgi) 

    It should contain default variables?:  [Y/n] 
      Add variable i.e (operator: : drunken_master) var: name
      Add variable i.e (operator: : drunken_master)      

    Should it have meta info?  [Y/n] 
     - Should it have dependencies?  [Y/n] 
        Add dependency i.e ({role: aptsupercow, var: 'value'}) {role: cool, version: latest}
        Add dependency i.e ({role: aptsupercow, var: 'value'}) 

    Should it have templates?  [Y/n] n

    Should it have files?  [Y/n] y

This will generate this folders (Please note the absence of templates folder)::

    .
    ├── CONTRIBUTORS.txt
    ├── defaults
    │   └── main.yml
    ├── files
    ├── handlers
    │   └── main.yml
    ├── LICENSE.rst
    ├── meta
    │   └── main.yml
    ├── README.rst
    └── tasks
        └── main.yml

Contributions
-------------

All contributions are more than welcome, please do so.


License
-------

* 3-clause BSD license.
* Copyright ©2014, Enrique Paredes
* Enjoy it!

