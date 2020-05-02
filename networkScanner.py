from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   
   for P in [5000,3306]:
      s = socket(AF_INET, SOCK_STREAM)
      conn = s.connect_ex((t_IP, P))
      if(conn == 0) :
         print ('Port %d: OPEN' % (P,))
      s.close()
print('Time taken:', time.time() - startTime)
