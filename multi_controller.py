#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call


def topologyNetwork():
    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.1.1.1/24')

    info('*** Adding controller\n')
    c1 = net.addController(name='c1',
                           controller=RemoteController,
                           ip='192.168.88.111',
                           protocol='tcp',
                           port=6633)
                           
    c2 = net.addController(name='c2',
                           controller=RemoteController,
                           ip='192.168.88.222',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')

    info('***** Add switch core\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info('***** Add switch distribution\n')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info('***** Add switch access\n')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)

    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.1.1.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.1.1.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.1.1.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.1.1.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.1.1.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.1.1.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.1.1.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.1.1.8', defaultRoute=None)

    info('*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s1, s3)

    net.addLink(s2, s4)
    net.addLink(s2, s5)

    net.addLink(s3, s6)
    net.addLink(s3, s7)

    net.addLink(s4, h1)
    net.addLink(s4, h2)

    net.addLink(s5, h3)
    net.addLink(s5, h4)

    net.addLink(s6, h5)
    net.addLink(s6, h6)

    net.addLink(s7, h7)
    net.addLink(s7, h8)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c1, c2])
    net.get('s2').start([c1, c2])
    net.get('s3').start([c1, c2])
    net.get('s4').start([c1 ,c2])
    net.get('s5').start([c1, c2])
    net.get('s6').start([c1, c2])
    net.get('s7').start([c1, c2])

    info('*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topologyNetwork()
