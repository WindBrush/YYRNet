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


def analyze_route(network_list, color_list, default_color):
    network = '183.172.0.0/16'
    graph = nx.Graph()
    router_dict = {}
    for network in network_list:
        result_dir = os.path.join(TRACEROUTE_DIR, network.replace('.', '_').replace('/', '_'))
        if not os.path.exists(result_dir):
            continue
        result_names = os.listdir(result_dir)
        for result_name in result_names:
            result_path = os.path.join(result_dir, result_name)
            with open(result_path, 'r') as f:
                lines = f.readlines()
                ips_list = []
                for i in range(1, len(lines)):
                    ips = re.findall(r'\d+\.\d+\.\d+\.\d+', lines[i])
                    if len(ips) == 0:
                        break
                    ips_list.append(ips)
                    graph.add_nodes_from(ips, label=False)
                # print(ips_list)
                for i in range(0, len(ips_list)-1):
                    if 0 < i < len(ips_list)-1:
                        for ip in ips_list[i]:
                            router_dict[ip] = True
                    ips1 = ips_list[i]
                    ips2 = ips_list[i+1]
                    for ip1 in ips1:
                        for ip2 in ips2:
                            graph.add_edge(ip1, ip2)
        #    break
    color_map = []
    for node in graph:
        color = default_color
        for network_id in range(len(network_list)):
            if network_list[network_id][:7] == node[:7]:
                color = color_list[network_id]
        color_map.append(color)
    plt.figure()
    print(router_dict.items())
    print(len(router_dict.items()))

    # nx.draw_networkx(graph, node_color=color_map, with_labels=True)
    # plt.show()


if __name__ == '__main__':
    # analyze_os(NETWORK_LIST)
    analyze_route(NETWORK_LIST, COLOR_LIST, DEFAULT_COLOR)
