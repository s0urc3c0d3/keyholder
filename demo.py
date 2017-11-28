import keyholder.keyholder

kh = keyholder.keyholder.keyholder("test", "zookeeper", "192.168.122.10", 2181)



with open ("ceph.conf", "r") as myfile:
    data=myfile.read()

kh.ensure_path("/etc/ceph/ceph.conf")
kh.set_node_data("/etc/ceph/ceph.conf",data)

data,stat=kh.get_node_data("/etc/ceph/ceph.conf")
print data