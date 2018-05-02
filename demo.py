import handlers
from keyholder import *

kh = keyholder("test", "zookeeper", "192.168.122.10", 2181)
if (kh.state != "CONNECTED"):
    exit(1)

print kh.exists("/etc/ceph/ceph.conf")

with open ("ceph.conf", "r") as myfile:
    data=myfile.read()
print "Making sure that node exists\n"

kh.ensure_path("/etc/ceph/ceph.conf")
if (kh.state != "CONNECTED"):
    exit(1)
print kh.exists("/etc/ceph/ceph.conf")

print "Sending to zookeeper:\n",data
kh.set_node_data("/etc/ceph/ceph.conf",data)
if (kh.state != "CONNECTED"):
    exit(1)

data,stat=kh.get_node_data("/etc/ceph/ceph.conf")
if (kh.state != "CONNECTED"):
    exit(1)
print "Receiving from Zookeeper:\n",data

print "Removing node from ZK\n"
kh.delete_node("/etc/ceph/ceph.conf", True)
if (kh.state != "CONNECTED"):
    exit(1)
print "Done"