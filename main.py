from ssh_server_ryu import *
from topology import topologyNetwork, setLogLevel



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    return 0
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''print_hi('PyCharm') '''
    configControllerMaster()
    configControllerSlave()
    setLogLevel('info')
    topologyNetwork()
    