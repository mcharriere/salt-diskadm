# -*- coding: utf-8 -*-
'''
FiberChannel module
'''
from __future__ import absolute_import, print_function, unicode_literals
import os.path, os.listdir
import re


def rescan(host):
    '''
    Rescan FC host

    CLI Example:

    .. code-block:: bash

        salt '*' fiberchannel.rescan 0
    '''
    if os.path.isdir('/sys/class/fc_host/host{0}'.format(host)):
        cmd = 'echo "1" > /sys/class/fc_host/host{0}/issue_lip'.format(host)
    else:
        return 'Host {0} does not exist'.format(host)
    return __salt__['cmd.run'](cmd).splitlines()

def rescan_all():
    '''
    Rescan FC hosts

    CLI Example:

    .. code-block:: bash

        salt '*' fiberchannel.rescan_all
    '''

    dir_base = '/sys/class/fc_host'

    for host in os.listdir(dir_base):
        cmd = 'echo "1" > {0}/{1}/issue_lip'.format(dir_base, host)
        __salt__['cmd.run'](cmd)

    return True
