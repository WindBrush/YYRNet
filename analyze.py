from configs import *
import os
import re
import networkx as nx
from xml.dom.minidom import parse
from matplotlib import pyplot as plt


def analyze_os(network_list):
    network = '118.229.0.0/19'
    result_path = os.path.join(NMAP_DIR, network.replace('.', '_').replace('/', '_'), 'result.xml')
    tree = parse(result_path)
    nmaprun = tree.getElementsByTagName("nmaprun")[0]
    hosts = nmaprun.getElementsByTagName("host")
    up_cnt = 0
    os_cnt = 0
    for host in hosts:
        status = host.getElementsByTagName("status")[0]
        address = host.getElementsByTagName("address")[0]
        if status.getAttribute('state') == 'down':
            continue
        up_cnt += 1
        print(address.getAttribute('addr'))
        if len(host.getElementsByTagName('os')) > 0:
            print('lalala')
            os_cnt += 1
            osmatches = host.getElementsByTagName('os')[0]\
                .getElementsByTagName('osmatch')
            print(osmatches)
    print(up_cnt)
    print(os_cnt)


def analyze_route(network_list):
    network = '118.229.0.0/19'
    result_dir = os.path.join(TRACEROUTE_DIR, network.replace('.', '_').replace('/', '_'))
    result_names = os.listdir(result_dir)
    graph = nx.Graph()
    start_node_color = '#ffff00'
    start_node_name = 'me'
    graph.add_node(start_node_name, node_color=start_node_color)
    for result_name in result_names:
        result_path = os.path.join(result_dir, result_name)
        with open(result_path, 'r') as f:
            lines = f.readlines()
            ips_list = [[start_node_name]]
            for i in range(1, len(lines)):
                ips = re.findall(r'\d+\.\d+\.\d+\.\d+', lines[i])
                if len(ips) == 0:
                    break
                ips_list.append(ips)
                graph.add_nodes_from(ips, label=False)
            # print(ips_list)
            for i in range(0, len(ips_list)-1):
                ips1 = ips_list[i]
                ips2 = ips_list[i+1]
                for ip1 in ips1:
                    for ip2 in ips2:
                        graph.add_edge(ip1, ip2)
    #    break
    plt.figure()
    nx.draw_networkx(graph, with_labels=True)
    plt.show()


if __name__ == '__main__':
    # analyze_os(NETWORK_LIST)
    analyze_route(NETWORK_LIST)
