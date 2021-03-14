import os 
import getpass

os.system("tput setaf 3")
print("\t\t\tWelecome to my menu !!")
os.system("tput setaf 7")
print("\t\t\t-------------------")

passwd = getpass.getpass("Enter ur password : ")

if passwd != "S":
	print("Password incorrect...")
	exit()

r = input("Where to want to run menu ? (local/remote) : ")
print(r)

while True:
	os.system("clear")
	print("""
	\n
	press 1:to run date
	press 2:to run cal
	press 3:to reboot os

            !!!!!!!!!!!!!NAMENODE SIDE CONFIGURATION OF HADOOP!!!!!!!!!!!!!!!!!

        press 4 :to install jdk software       [First Download from Internet]
        press 5:to install hadoop software     [First Download from Intrenet]
	press 6:to stop firewall of os
	press 7:to start firewall of os
	press 8:to configuration file 
	press 9:to configuaration file
	press 10:to configuaration file 
	press 11:to format namenode      
	press 12:to make directory       
	press 13:to start namenode
	press 14:to check hadoop namenode running or not    
	press 15:to check port no.       
	press 16:to format directory 
	press 17:to hadoop namenode report
	press 18:to stop namenode
	press 19:to check port no. of all protocols
	press 20:to read the packet      
	press 21:to read internal inforamtion of packet   
	press 22:to look how many files uploaded
 
		   !!!!!!!!!!!!!DATANODE SIDE CONFIGURATION OF HADOOP!!!!!!!!!!!!!!!!!
	
	press 23:to stop firewall of os
	press 24:to start firewall of os
	press 25:to configuration file 
	press 26:to configuaration file 
	press 27:to configuaration file 
	press 28:to make directory         
	press 29:to start namenode
	press 30:to check hadoop namenode running or not    
	press 31:to check port no.      
	press 32:to format directory     
	press 33:to hadoop namenode report
	press 34:to stop namenode
	press 35:to check port no. of all protocols
	press 36:to read the packet      
	press 37:to check read i/o data os   

                 
                  !!!!!!!!!!!!!CLIENT SIDE CONFIGRATION OF HADOOP!!!!!!!!!!!!!!!!!	

        press 38:to stop firewall of os
	press 39:to start firewall of os
	press 40:to look how many files uploaded   
	press 41:to put files                      
	press 42:to remove files                    
	press 43:to read file                       
	press 44:to reduce block size        
	
	          !!!!!!!!!!!!!TO SETUP HTTP SERVER!!!!!!!!!!!!!!!!!
        
        press 45:to stop firewall of os
	press 46:to start firewall of os
	press 47:to install http server
        press 48:to enable http server 
	press 49:to configure static html file
	press 50:to configure dynamic cgi-bin file
	press 51:to stop http server
	press 52:to stop selinux os

                  !!!!!!!!!!!!!TO SETUP DOCKER CONTAINER!!!!!!!!!!!!!!!!
	
	press 53:to docker software install or not
	press 54:to install docker software 
        press 55:to docker version
	press 56:to start docker
	press 57:to check docker file system 
	press 58:to check dockar images
        press 59:to install docker images
        press 60:to launch os inside docker
        press 61:to launch os inside docker using our name
	press 62:to check how many os stop in docker
        press 63:to exit docker os
        press 64:to reconnect stop os
        press 65:to attach stop os       
         
	          !!!!!!!!!!!!!CONFIGURATION ANSIBLE!!!!!!!!!!!!!!!! 
	
	press 66:to check ansible install or not
	press 67:to install ansible
        press 68:to check version of ansible
	press 69:to check how many hosts
	press 70:to make directory
	press 71:to make ansible configure file
        press 72:to make file
        press 73:to configure another os

                  !!!!!!!!!!!!!USEFULL COMMANDS!!!!!!!!!!!!!!!! 

	press 74:to launch firefox
	press 75:to launch editor
        press 76:to launch python3
        press 77:to launch editor(vim)
        
                  !!!!!!!!!!!! HARD DISK PARTITION COMMANDS!!!!!!!!!!!!!!!!

	press 78:to check list of HD to attach OS
	press 79:to check particular HD

		[step 1:physical partition__step 2:foramt__step3:mount]

        press 80:take inside HD

        [p=detail about HD__n=new partition__e=Extended__d=deleting__w=save__q=quite]

        press 81:to check list of partition with HD
	press 82:load drive for new HD
	press 83:to format
        press 84:to mount directory
        press 85:to show all the mounted directory on partition
	press 86:to unmount directory

                       !!!!!!!!!!!! LVM COMMANDS!!!!!!!!!!!!!!!!		
	
	press 87:Creating physical volume                    
	press 88:Display physical volume
	press 89:Creating volume group 
        press 90:Display volume group
        press 91:Creating logical volume   
	press 92:Show all the logical volume creation
        press 93:formating logical volume                 [path=/dev/<vgname>/<lvanme>]
	press 94:make directory to mount on partition     
	press 95:mounting Directory on logical volume    [path=/dev/<vgname>/<lvanme>]
	press 96:Increasing logical volume               [path=/dev/<vgname>/<lvanme>]
	press 97:format logical volume after increasing LV [path=/dev/<vgname>/<lvanme>]

""")
	
	ch = input("Enter ur choice : ")
	print(ch)
	
	if r =="local":
		
		if int(ch) ==1:
			os.system("date")
		elif int(ch) == 2:
			os.system("cal")
		elif int(ch) == 3:
			os.system("reboot")
		elif int(ch) == 4:
			name=input("Enter a URL")
			os.system("rpm -q {}".format())
		elif int(ch) == 5:
			name=input("Enter a URL")
			os.system("rpm -q {}".format())
		elif int(ch) == 6:
			os.system("systemctl stop firewalld")
		elif int(ch) == 7:
			os.system("systemctl start firewalld")
		elif int(ch) == 8:
			os.system("cd /etc/hadoop")
		elif int(ch) == 9:
			os.system("vim hdfs-site.xml")
		elif int(ch) == 10:
			os.system("vim core-site.xml")
		elif int(ch) == 11:
			os.system("hadoop namenode -format")
		elif int(ch) == 12:
			name=input("Enter a directory name : ")
			os.system("mkdir /{}".format(name))
		elif int(ch) == 13:
			os.system("hadoop-daemon.sh start namenode")
		elif int(ch) == 14:
			os.system("jps")
		elif int(ch) == 15:
			os.system("netstat -tnlp")
		elif int(ch) == 16:
			name=input("Enter a directory name : ")
			os.system("rm -rf /{}".format(name))
		elif int(ch) == 17:
			os.system("hadoop dfsadmin -report")
		elif int(ch) == 18:
			os.system("hadoop-daemon.sh stop namenode")
		elif int(ch) == 19:
			os.system("vim /etc/services")
		elif int(ch) == 20:
			os.system("tcpdump -i enp0s3 -n")
		elif int(ch) == 21:
			os.system("tcpdump -r enp0s3 -n -X")
		elif int(ch) == 22:
			os.system("hadoop fs -ls /")
		elif int(ch) == 23:
			os.system("systemctl stop firewalld")
		elif int(ch) == 24:
			os.system("systemctl start firewalld")
		elif int(ch) == 25:
			os.system("cd /etc/hadoop")
		elif int(ch) == 26:
			os.system("vim hdfs-site.xml")
		elif int(ch) == 27:
			os.system("vim core-site.xml")
		elif int(ch) == 28:
			name=input("enter a file name : ")
			os.system("mkdir /{}".format(name))
		elif int(ch) == 29:
			os.system("hadoop-daemon.sh start namenode")
		elif int(ch) == 30:
			os.system("jps")
		elif int(ch) == 31:
			os.system("netstat -tnlp")
		elif int(ch) == 32:
			name=input("enter a file name : ")
			os.system("rm -rf {}".format(name))
		elif int(ch) == 33:
			os.system("hadoop dfsadmin -report")
		elif int(ch) == 34:
			os.system("hadoop-daemon.sh stop namenode")
		elif int(ch) == 35:
			os.system("vim /etc/services")
		elif int(ch) == 36:
			os.system("tcpdump -i enp0s3 -n")
		elif int(ch) == 37:
			os.system("tcpdump -i enp0s3 -n -X")
		elif int(ch) == 38:
			os.system("systemctl stop firewalld")
		elif int(ch) == 39:
			os.system("systemctl stop firewalld")
		elif int(ch) == 40:
			os.system("hadoop fs -ls /")
		elif int(ch) == 41:
			name=input("enter a file name : ")
			os.system("hadoop fs -put {}.txt /".format(name))
		elif int(ch) == 42:
			name=input("enter a file name : ")
			os.system("hadoop fs -rm /{}.txt".format(name))
		elif int(ch) == 43:
			name=input("enter a file name : ")
			os.system("hadoop fs -cat /{}.txt".format(name))
		elif int(ch) == 44:
			name=input("enter a block size : ")
			nam=input("enter a file name : ")
			os.system("hadoop fs -Ddfs.block.size={} {} /".format(name,nam))
		elif int(ch) == 45:
			os.system("systemctl stop firewalld")
		elif int(ch) == 46:
			os.system("systemctl start firewalld")
		elif int(ch) == 47:
			os.system("yum install httpd")
		elif int(ch) == 48:
			os.system("systemctl enabled httpd")
		elif int(ch) == 49:
			os.system("cd /var/www/html")
		elif int(ch) == 50:
			os.system("cd /var/www/cgi-bin")
		elif int(ch) == 51:
			os.system("systemctl stop firewalld")
		elif int(ch) == 52:
			os.system("getenforce 0")
		elif int(ch) == 53:
			os.system("rpm -q docker")
		elif int(ch) == 54:
			os.system("yum install docker-ce --nobest")
		elif int(ch) == 55:
			os.system("docker --version")
		elif int(ch) == 56:
			os.system("systemctl start docker")
		elif int(ch) == 57:
			os.system("docker ps")
		elif int(ch) == 58:
			os.system("docker images")
		elif int(ch) == 59:
			name=input("enter a OS  name : ")
			os.system("docker pull {}".format(name))
		elif int(ch) == 60:
			name=input("enter a image name : ")
			os.system("docker run -it {}".format(name))
		elif int(ch) == 61:
			name=input("enter a image name : ")
			name=input("enter a OS name : ")
			os.system("docker run -it --name {0} {1}.txt".format(name,value))
		elif int(ch) == 62:
			os.system("docker ps -a")
		elif int(ch) == 63:
			os.system("exit")
		elif int(ch) == 64:
			name=input("enter a image name : ")
			os.system("docker start {}".foramt(name))
		elif int(ch) == 65:
			name=input("enter a image name : ")
			os.system("docker attach {}".format(name))
		elif int(ch) == 66:
			os.system("rpm -q ansible")
		elif int(ch) == 67:
			os.system("pip3 install ansible")
		elif int(ch) == 68:
			os.system("ansible --version")
		elif int(ch) == 69:
			os.system("ansible all -list-hosts")
		elif int(ch) == 70:
			os.system("mkdir /etc/ansible")
		elif int(ch) == 71:
			os.system("vim /etc/ansible/ansible.cfg")
		elif int(ch) == 72:
			os.system("vim")
		elif int(ch) == 73:
			name=input("enter a file name : ")
			status=input("Enter a status : ")
			os.system("ansible all -m services -a".format(name,status))
		elif int(ch) == 74:
			os.system("firefox")
		elif int(ch) == 75:
			os.system("gedit")
		elif int(ch) == 76:
			os.system("python3")
		elif int(ch) == 77:
			os.system("vim")
		elif int(ch) == 78:
			os.system("fdisk -l")		
		elif int(ch) == 79:
			name=input("enter a HD name : ")
			os.system("fdisk -l {}".format(name))
		elif int(ch) == 80:
			name=input("enter a HD name : ")
			os.system("fdisk {}".format(name))
		elif int(ch) == 81:
			os.system("lsblk")
		elif int(ch) == 82:
			os.system("udevadm settle")
		elif int(ch) == 83:
			os.system("mkfs.ext4")
		elif int(ch) == 84:
			name=input("Enter a Directory name : ")
			os.system("mount {}".format(name))
		elif int(ch) == 85:
			os.system("df -h")
		elif int(ch) == 86:
			name=input("Enter a Directory name : ")
			os.system("umount {}".format(name))
		elif int(ch) == 87:
			name=input("Enter HD name : ")
			os.system("pvcreate {}".format(name))
		elif int(ch) == 88:
			name=input("Enter HD name : ")
			os.system("pvdisplay {}".format(name))
		elif int(ch) == 89:
			name=input("Enter VG name : ")
			nam=input("Enter pv HD name : ")
			na=input("Enter pv HD name")
			os.system("vgcreate {} {} {}".format(name,nam,na))
		elif int(ch) == 90:
			name=input("Enter VG name : ")
			os.system("vgdisplay {}".format(name))
		elif int(ch) == 91:
			name=input("Enter HD size : ")
			nam=input("Enter LV name : ")
			na=input("Enter VG name : ")
			os.system("lvcreate --size {} --name {} {}".format(name,nam,na))
		elif int(ch) == 92:
			os.system("lvdisplay")
		elif int(ch) == 93:
			name=input("Enter HD path : ")
			os.system("mkfs.ext4 {}".format(name))
		elif int(ch) == 94:
			name=input("Enter Directory name : ")
			os.system("mkdir {}".format(name))
		elif int(ch) == 95:
			name=input("Enter HD path : ")
			nam=input("Enter Directory name : ")
			os.system("mount {} {}".format(name,nam))
		elif int(ch) == 96:
			name=input("Enter HD size : ")
			nam=input("Enter LV path : ")
			os.system("lvextend --size +{} {}".format(name,nam))
		elif int(ch) == 97:
			name=input("Enter LV path : ")
			os.system("resize2fs {}".format(name))
		else:
			print("not supported")

	elif r =="remote":
		ip = input("Enter a remote IP : ")
		print(ip)
		
		if int(ch) ==1:
			os.system("ssh {} date".format(ip))
		elif int(ch) == 2:
			os.system("ssh {} cal".format(ip))
		elif int(ch) == 3:
			os.system("ssh {} reboot".format(ip))
		elif int(ch) == 4:
			os.system("ssh {} rpm -q jdk-8u171-linux-x64.rpm".format(ip))
		elif int(ch) == 5:
			os.system("ssh {} rpm -q hadoop-1.2.1-1.x86_64.rpm".format(ip))
		elif int(ch) == 6:
			os.system("ssh {} systemctl stop firewalld".format(ip))
		elif int(ch) == 7:
			os.system("ssh {} systemctl start firewalld".format(ip))
		elif int(ch) == 8:
			os.system("ssh {} cd /etc/hadoop".format(ip))
		elif int(ch) == 9:
			os.system("ssh {} vim hdfs-site.xml".format(ip))
		elif int(ch) == 10:
			os.system("ssh {} vim core-site.xml".format(ip))
		elif int(ch) == 11:
			os.system("ssh {} hadoop namenode -format".format(ip))
		elif int(ch) == 12:
			name=input("enter a Directory name : ")
			os.system("ssh {} mkdir /{}".format(ip,name))
		elif int(ch) == 13:
			os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
		elif int(ch) == 14:
			os.system("ssh {} jps".format(ip))
		elif int(ch) == 15:
			os.system("ssh {} netstat -tnlp".format(ip))
		elif int(ch) == 16:
			name=input("enter a Directory name : ")
			os.system("ssh {} rm -rf /{}".format(ip,name))
		elif int(ch) == 17:
			os.system("ssh {} hadoop dfsadmin -report".format(ip))
		elif int(ch) == 18:
			os.system("ssh {} hadoop-daemon.sh stop namenode".format(ip))
		elif int(ch) == 19:
			os.system("ssh {} vim /etc/services".format(ip))
		elif int(ch) == 20:
			os.system("ssh {} tcpdump -i enp0s3 -n".format(ip))
		elif int(ch) == 21:
			os.system("ssh {} tcpdump -r enp0s3 -n -X".format(ip))
		elif int(ch) == 22:
			os.system("ssh {} hadoop fs -ls /".format(ip))
		elif int(ch) == 23:
			os.system("ssh {} systemctl stop firewalld".format(ip))
		elif int(ch) == 24:
			os.system("ssh {} systemctl start firewalld".format(ip))
		elif int(ch) == 25:
			os.system("ssh {} cd /etc/hadoop".format(ip))
		elif int(ch) == 26:
			os.system("ssh {} vim hdfs-site.xml".format(ip))
		elif int(ch) == 27:
			os.system("ssh {} vim core-site.xml".format(ip))
		elif int(ch) == 28:
			name=input("enter a Directory name : ")
			os.system("ssh {} mkdir /{}".format(ip,name))
		elif int(ch) == 29:
			os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
		elif int(ch) == 30:
			os.system("ssh {} jps".format(ip))
		elif int(ch) == 31:
			os.system("ssh {} netstat -tnlp".format(ip))
		elif int(ch) == 32:
			name=input("enter a Directory name : ")
			os.system("ssh {} rm -rf {}".format(ip,name))
		elif int(ch) == 33:
			os.system("ssh {} hadoop dfsadmin -report".format(ip))
		elif int(ch) == 34:
			os.system("ssh {} hadoop-daemon.sh stop namenode".format(ip))
		elif int(ch) == 35:
			os.system("ssh {} vim /etc/services".format(ip))
		elif int(ch) == 36:
			os.system("ssh {} tcpdump -i enp0s3 -n".format(ip))
		elif int(ch) == 37:
			os.system("ssh {} tcpdump -i enp0s3 -n -X".format(ip))
		elif int(ch) == 38:
			os.system("ssh {} systemctl stop firewalld".format(ip))
		elif int(ch) == 39:
			os.system("ssh {} systemctl stop firewalld".format(ip))
		elif int(ch) == 40:
			os.system("ssh {} hadoop fs -ls /".format(ip))
		elif int(ch) == 41:
			name=input("enter a file name : ")
			os.system("ssh {} hadoop fs -put {}.txt /".format(ip,name))
		elif int(ch) == 42:
			name=input("enter a file name : ")
			os.system("ssh {} hadoop fs -rm /{}.txt".format(ip,name))
		elif int(ch) == 43:
			name=input("enter a file name")
			os.system("ssh {} hadoop fs -cat /{}.txt".format(ip,name))
		elif int(ch) == 44:
			name=input("enter a block size : ")
			nam=input("enter a file name : ")
			os.system("ssh {}hadoop fs -Ddfs.block.size={} {} /".format(ip,name,nam))
		elif int(ch) == 45:
			os.system("ssh {} systemctl stop firewalld".format(ip))
		elif int(ch) == 46:
			os.system("ssh {} systemctl start firewalld".format(ip))
		elif int(ch) == 47:
			os.system("ssh {} yum install httpd".format(ip))
		elif int(ch) == 48:
			os.system("ssh {} systemctl enabled httpd".format(ip))
		elif int(ch) == 49:
			os.system("ssh {} cd /var/www/html".format(ip))
		elif int(ch) == 50:
			os.system("ssh {} cd /var/www/cgi-bin".format(ip))
		elif int(ch) == 51:
			os.system("ssh {} systemctl stop firewalld".format(ip))
		elif int(ch) == 52:
			os.system("ssh {} getenforce 0".format(ip))
		elif int(ch) == 53:
			os.system("ssh {} rpm -q docker".format(ip))
		elif int(ch) == 54:
			os.system("ssh {} yum install docker-ce --nobest".format(ip))
		elif int(ch) == 55:
			os.system("ssh {} docker --version".format(ip))
		elif int(ch) == 56:
			os.system("ssh {} systemctl start docker".format(ip))
		elif int(ch) == 57:
			os.system("ssh {} docker ps".format(ip))
		elif int(ch) == 58:
			os.system("ssh {} doker images".format(ip))
		elif int(ch) == 59:
			name=input("enter a os name : ")
			os.system("ssh {} docker pull {}".format(ip,name))
		elif int(ch) == 60:
			name=input("enter a HD os name : ")
			os.system("ssh {} docker run -it {}".format(ip,value))
		elif int(ch) == 61:
			name=input("enter a name : ")
			nam=input("enter a os name : ")
			os.system("ssh {} docker run -it --name {0} {1}.txt".format(ip,name,nam))
		elif int(ch) == 62:
			os.system("ssh {} docker ps -a".format(ip))
		elif int(ch) == 63:
			os.system("ssh {} exit".format(ip))
		elif int(ch) == 64:
			name=input("enter a image name : ")
			os.system("ssh {} docker start {}".foramt(ip,name))
		elif int(ch) == 65:
			name=input("enter a HD image name")
			os.system("ssh {} docker attach {}".format(ip,name))
		elif int(ch) == 66:
			os.system("ssh {} rpm -q ansible".format(ip))
		elif int(ch) == 67:
			os.system("ssh {} pip3 install ansible".format(ip))
		elif int(ch) == 68:
			os.system("ssh {} ansible --version".format(ip))
		elif int(ch) == 69:
			os.system("ssh {} ansible all -list-hosts".format(ip))
		elif int(ch) == 70:
			os.system("ssh {} mkdir /etc/ansible".format(ip))
		elif int(ch) == 71:
			os.system("ssh {} vim /etc/ansible/ansible.cfg".format(ip))
		elif int(ch) == 72:
			os.system("ssh {} vim".format(ip))
		elif int(ch) == 73:
			name=input("enter a file name : ")
			status=input("Enter a status : ")
			os.system("ssh {} ansible all -m services -a".format(ip))
		elif int(ch) == 74:
			os.system(" ssh {} firefox".format(ip))
		elif int(ch) == 75:
			os.system("ssh {} gedit".format(ip))
		elif int(ch) == 76:
			os.system("ssh {} python3".format(ip))
		elif int(ch) == 77:
			os.system("ssh {} vim".format(ip))		
		elif int(ch) == 78:
			os.system("ssh {} fdisk -l".format(ip))		
		elif int(ch) == 79:
			name=input("enter a HD name")
			os.system("ssh {} fdisk -l {}".format(ip,name))
		elif int(ch) == 80:
			name=input("enter a HD name")
			os.system("ssh {} fdisk {}".format(ip,name))
		elif int(ch) == 81:
			os.system("ssh {} lsblk".format(ip))
		elif int(ch) == 82:
			os.system("ssh {} udevadm settle".format(ip))
		elif int(ch) == 83:
			os.system("ssh {} mkfs.ext4".format(ip))
		elif int(ch) == 84:
			name=input("enter a Directory name : ")
			os.system("ssh {} mount {}".format(ip,name))
		elif int(ch) == 85:
			os.system("ssh {} df -h".format(ip))
		elif int(ch) == 86:
			name=input("enter a Directory name : ")
			os.system("ssh {} umount {}".format(ip,name))
		elif int(ch) == 87:
			name=input("Enter HD name : ")
			os.system("ssh {} pvcreate {}".format(ip,name))
		elif int(ch) == 88:
			name=input("Enter HD name : ")
			os.system("ssh {} pvdisplay {}".format(ip,name))
		elif int(ch) == 89:
			name=input("Enter VG name : ")
			nam=input("Enter pv HD name : ")
			na=input("Enter pv HD name : ")
			os.system("ssh {} vgcreate {} {} {}".format(ip,name,nam,na))
		elif int(ch) == 90:
			name=input("Enter VG name : ")
			os.system("ssh {} vgdisplay {}".format(ip,name))
		elif int(ch) == 91:
			name=input("Enter HD size : ")
			na=input("Enter LV name : ")
			n=input("Enter VG name : ")
			os.system("ssh {} lvcreate --size {} --name {} {}".format(ip,name,na,n))
		elif int(ch) == 92:
			os.system("ssh {} lvdisplay".format(ip))
		elif int(ch) == 93:
			name=input("Enter HD path : ")
			os.system("ssh {} mkfs.ext4 {}".format(ip,name))
		elif int(ch) == 94:
			name=input("Enter Directory name : ")
			os.system("ssh {} mkdir {}".format(ip,name))
		elif int(ch) == 95:
			name=input("Enter HD path : ")
			name=input("Enter Directory name : ")
			os.system("ssh {} mount {} {}".format(ip,name))
		elif int(ch) == 96:
			name=input("Enter HD size : ")
			nam=input("Enter LV path : ")
			os.system("ssh {} lvextend --size +{} {}".format(ip,name,nam))
		elif int(ch) == 97:
			name=input("Enter LV path : ")
			os.system("ssh {} resize2fs {}".format(ip,name))
		else:
			print("not supported")
	else:
		print("not supported login ...")
	input("\n plz enter to conti .....")	




































