#!/usr/bin/python
# -*- coding: utf-8-*-
import os
import platform
import glob
import re
from collections import OrderedDict
from collections import namedtuple
import pwd
import argparse
import socket
import fcntl
import struct
import getpass
import string


def netdevs():
    ''' RX and TX bytes for each of the network devices '''

    with open('/proc/net/dev') as f:
        net_dump = f.readlines()

    device_data = {}
    data = namedtuple('data', ['rx', 'tx'])
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = data(float(line[1].split()[0]) / (1024.0 * 1024.0),
                                                float(line[1].split()[8]) / (1024.0 * 1024.0))

    return device_data


dev_pattern = ['sd.*', 'mmcblk*']


def size(device):
    ''' Size of the available hard drives '''

    nr_sectors = open(device + '/size').read().rstrip('\n')
    sect_size = open(device + '/queue/hw_sector_size').read().rstrip('\n')

    # The sect_size is in bytes, so we convert it to GiB and then send it back
    return (float(nr_sectors) * float(sect_size)) / (1024.0 * 1024.0 * 1024.0)


def detect_devs():
    ''' All Infos from sys/block/ that is matches out pattern and prints out the GB of each hard drive '''
    c = 0
    for device in glob.glob('/sys/block/*'):

        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                c = c + 1
                print('DEV:') + (str(c)) + (' {0}, Size: {1} GiB'.format(device, size(device)))




def cpuinf():
    ''' Return the information in /proc/cpuinfo
    as a dictionary and turns the model infos of the CPU
    also we can check the number of the available CPUs '''

    c = 0
    with open('/proc/cpuinfo') as f:
        for line in f:

            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    c = c + 1
                    model_name = line.rstrip('\n').split(':')[1]
                    print "CPU_" + (str(c)) + "   " + model_name


def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo= OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo





def get_ip_address(ifname):
    ''' Return the IP address  '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def get_hw_address(ifname):
    ''' Return the MAC address  '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]


def get_GPUinfo():
    ''' Return temperature, model etc infos for the GPU'''
    infgpu = os.system("nvidia-smi")
    return infgpu


def get_Ethinfo():
    ''' Return the speed of the ehternet port '''
    infeth = os.system("ethtool eth0 | grep -i speed")
    return infeth


def main():

    print('------------------------------------------------------------------------------+')
    print ("OS: ") + platform.uname()[0] + " " + platform.architecture()[0] + " " + platform.linux_distribution()[
        0] + " " + \
          platform.linux_distribution()[1]



    print('------------------------------------------------------------------------------+')

    detect_devs()

    print('+-----------------------------------------------------------------------------+')
    meminfo2 = meminfo()
    print('Total memory: {0}'.format(meminfo2['MemTotal']))
    print('Free memory: {0}'.format(meminfo2['MemFree']))

    print('------------------------------------------------------------------------------+')
    cpuinf()

    print('------------------------------------------------------------------------------+')

    print 'IP: ' + get_ip_address('eth0')

    print('------------------------------------------------------------------------------+')

    print 'MAC ADDRESS: ' + get_hw_address("eth0")

    print('------------------------------------------------------------------------------+')

    print 'Username: ' + getpass.getuser()

    print('------------------------------------------------------------------------------+')
    get_GPUinfo()

    print('------------------------------------------------------------------------------+')
    get_Ethinfo()


if __name__ == '__main__':

    main()




