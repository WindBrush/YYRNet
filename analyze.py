from configs import *
from xml.dom.minidom import parse


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


if __name__ == '__main__':
    analyze_os(NETWORK_LIST)
