#!/bin/bash
#
echo "setando variaveis..." 
LOGIN="eonay"


echo "[OK]" 


#sudo apt -y update && sudo apt -y upgrade && sudo shutdown -r now
sudo apt -y install openssh-server git libncurses-dev libssl-dev

sudo apt -y install build-essential mtr tcpdump lynx iperf tshark fping wireshark net-tools curl openvswitch-switch python3-pip python3-scapy

sudo usermod -a -G wireshark "$LOGIN"

echo "install Mininet..."
sudo apt -y install mininet
sudo mn --version
echo "Mininet [OK]" 
echo ""
echo "" 
echo "install ryu controller..." 
sudo apt -y install python3-ryu 
sudo ryu --version
echo "ControllerSDN [OK]"
echo ""
echo "" 
