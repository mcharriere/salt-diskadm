# -*- coding: utf-8 -*-
'''
Multipath module
'''
from __future__ import absolute_import, print_function, unicode_literals
import os.path
import re


def list():
    '''
    Multipath list

    CLI Example:

    .. code-block:: bash

        salt '*' multipath.list
    '''
    cmd = 'multipath -l'
    return __salt__['cmd.run'](cmd).splitlines()


def flush(device):
    '''
    Multipath flush

    CLI Example:

    .. code-block:: bash

        salt '*' multipath.flush mpath1
    '''
    if not os.path.exists(device):
        return '{0} does not exist'.format(device)

    cmd = 'multipath -f {0}'.format(device)
    return __salt__['cmd.run'](cmd).splitlines()

def flush_all(device):
    '''
    Multipath flush all

    CLI Example:

    .. code-block:: bash

        salt '*' multipath.flush_all
    '''
    cmd = 'multipath -F'
    return __salt__['cmd.run'](cmd).splitlines()

def get_hcil(device):
    '''
    Get HCIL of a path

    CLI Example:

    .. code-block:: bash

        salt '*' multipath.get_hcil mpath1
    '''

    path_re = re.compile("(\w*) (\d:\d:\d:\d)")

    cmd = 'multipathd show paths format "%w %i"'
    ret = []
    
    for line in __salt__['cmd.run'](cmd).splitlines():
        path, hcil = path_re.match(line).groups()
        if device == path:
            ret.append(hcil)

    if len(ret) == 0:
        return '{0} does not exist'.format(device)

    return ret
     
