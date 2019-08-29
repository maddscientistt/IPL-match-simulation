import os
from kazoo.client import KazooClient
import time
import subprocess

print("My PID",os.getpid())
def handler(event):
        ID=[]
       
        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
        for pid in pids:
                s=open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                s=str(s)
                if(s[2:11]=="python3.6"):
                    ID.append(pid)
        
        if(os.getpid()==int(min(ID))):
	        print(os.getpid(),' is creating the new process')
	        subprocess.call(['gnome-terminal -e \"python3.6 1.py"'],shell=True)
	        time.sleep(2)
	        child=zk.get_children(path="/my/zoo")
	        print(child)
	        for i in child:       
                        zk.get(path="/my/zoo/"+i,watch=handler)  
	
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
zk.ensure_path("/my/zoo")
zk.create(path="/my/zoo/"+str(os.getpid()),value=b"value ---  ",acl=None,ephemeral=True,sequence=True)
time.sleep(1)
child=zk.get_children(path="/my/zoo")
print("children= ",child)



for i in child:       
        zk.get(path="/my/zoo/"+i,watch=handler)  
        
while(1):      
        time.sleep(20)
