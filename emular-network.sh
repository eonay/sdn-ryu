#!/bin/bash
#         h1
#       /
# c0 - s1 - h2
#       \
#         h3
sudo mn --topo single,3 --mac --controller remote --switch ovsk
