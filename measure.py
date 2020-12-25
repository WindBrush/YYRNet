from configs import *
import os
from multiprocessing import Pool
from IPy import IP


def single_traceroute(ip, save_path):
    """ 执行单条 traceroute 指令 """
    order = 'traceroute -I -m 7 -n -w 1 %s > %s' % (ip, save_path)
    if os.path.exists(save_path):
        print('Pass: ', order)
    else:
        print('Executing: ', order)
        os.system(order)


def traceroute(network_list):
    for network in network_list:
        result_dir = os.path.join(TRACEROUTE_DIR, network.replace('.', '_').replace('/', '_'))
        os.makedirs(result_dir, exist_ok=True)
        ips = IP(network)
        pool = Pool(processes=16)
        for ip in ips:
            save_path = os.path.join(result_dir, str(ip).replace('.', '_') + '.log')
            pool.apply_async(single_traceroute, args=(ip, save_path))
        pool.close()
        pool.join()


if __name__ == '__main__':
    traceroute(NETWORK_LIST)
