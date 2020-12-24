from configs import *
from xml.dom.minidom import parse


def analyze_os(network_list):
    network = '118.229.0.0/19'
    result_path = os.path.join(NMAP_DIR, network.replace('.', '_').replace('/', '_'), 'result.xml')
    tmp = parse(result_path)
    print(tmp)


if __name__ == '__main__':
    analyze_os(NETWORK_LIST)