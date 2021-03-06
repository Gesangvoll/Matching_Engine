import socket
import threading
import random
from concurrent.futures import ThreadPoolExecutor
import time


if __name__ == '__main__':
    start_total = time.time()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vcm-8940.vm.duke.edu', 12345))

    for i in range(2):
        set_up_user = '173\r\n' \
                      '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                      '<create>\r\n' \
                      '  <account id=\''+str(i)+'\' balance=\'1000000\'/>\r\n' \
                      '  <symbol sym=\'SPY\'>\r\n' \
                      '    <account id=\''+str(i)+'\'>100000</account>\r\n' \
                      '  </symbol>\r\n' \
                      '  <symbol sym=\'XYZ\'>\r\n' \
                      '    <account id=\'' + str(i) + '\'>100000</account>\r\n' \
                      '  </symbol>\r\n' \
                      '  <symbol sym=\'ABC\'>\r\n' \
                      '    <account id=\'' + str(i) + '\'>100000</account>\r\n' \
                      '  </symbol>\r\n' \
                      '</create>\r\n\r\n'
        s.sendall(str.encode(set_up_user, 'utf-8'))

        recv_message = s.recv(4096)

    # user 0 sell, user 1 buy

    user0_sell = '173\r\n' \
               '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
               '<transactions account = \'0\'>\r\n' \
               '<order sym =\'SPY\' amount=\'-100\' limit=\'123.45\'/>\r\n' \
               '</transactions>\r\n\r\n'
    s.sendall(str.encode(user0_sell, 'utf-8'))
    recv_message = s.recv(4096)


    user1_buy = '173\r\n' \
               '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
               '<transactions account = \'1\'>\r\n' \
               '<order sym =\'SPY\' amount=\'100\' limit=\'150\'/>\r\n' \
               '</transactions>\r\n\r\n'
    s.sendall(str.encode(user1_buy, 'utf-8'))
    recv_message = s.recv(4096)

    query_trade = '173\r\n' \
                   '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                   '<transactions account = \'1\'>\r\n' \
                   '<query id=\'1\'/>\r\n' \
                  '<query id=\'2\'/>\r\n' \
                  '</transactions>\r\n\r\n'
    s.sendall(str.encode(query_trade, 'utf-8'))
    recv_message = s.recv(4096)

    print(recv_message.decode())
    #print ('total time:', end_total - start_total)
