import keyholder.keyholder

kh = keyholder.keyholder.keyholder("test", "zookeeper", "192.168.122.10", 2181)
if (kh.state != "CONNECTED"):
    exit(1)

print kh.exists("/etc/ceph/ceph.mon.keyring")

exit(0)
with open ("ceph.conf", "r") as myfile:
    data=myfile.read()

kh.ensure_path("/etc/ceph/ceph.conf")
if (kh.state != "CONNECTED"):
    exit(1)
kh.set_node_data("/etc/ceph/ceph.conf",data)
if (kh.state != "CONNECTED"):
    exit(1)

data,stat=kh.get_node_data("/etc/ceph/ceph.conf")
if (kh.state != "CONNECTED"):
    exit(1)
print data