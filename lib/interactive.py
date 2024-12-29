'''
based on riplpox 
'''

import sys
sys.path.append(".")

from mininet.topo import Topo
from mininet.node import Controller, RemoteController, OVSKernelSwitch, CPULimitedHost
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.util import custom
from mininet.log import setLogLevel, info, warn, error, debug
import time
from DCTopo import FatTreeTopo
from DCRouting import Routing

from subprocess import Popen, PIPE
from argparse import ArgumentParser
import multiprocessing
from time import sleep
from monitor import monitor_devs_ng
import os

import mn_ft

def topo_create(k=4, bw=10, cpu=-1, queue=100, controller='DCController'):
    info('*** Creating the topology')
    topo = FatTreeTopo(k)

    host = custom(CPULimitedHost, cpu=cpu)
    link = custom(TCLink, bw=bw, max_queue_size=queue)
    net = Mininet(topo, host=host, link=link, switch=OVSKernelSwitch,
            controller=RemoteController, autoStaticArp=True)

    return net

if __name__=="__main__":
    net = topo_create()
    net.start()
    time.sleep(1)
    CLI(net)
    net.stop()
    mn_ft.clean()
