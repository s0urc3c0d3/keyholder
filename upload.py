#!/usr/bin/python2.7
import keyholder.keyholder
import argparse
import logging
from re import match

parser = argparse.ArgumentParser(description='Upload ceph.conf to key-value database')
parser.add_argument('TYPE', metavar='TYPE', type=str, help='zookeeper for Zookeeper, etcd for ETCD')
parser.add_argument('HOST', metavar='HOST', type=str, help='key-value IP address')
parser.add_argument('PORT', metavar='PORT', type=int, help='key-value port number')

args = parser.parse_args()

logging.basicConfig()

if (args.TYPE == "zookeeper" and match(
        "^[012]{0,1}[0-9]{0,1}[0-9]{1}\.[012]{0,1}[0-9]{0,1}[0-9]{1}\.[012]{0,1}[0-9]{0,1}[0-9]{1}\.[012]{0,1}[0-9]{0,1}[0-9]{1}",
        args.HOST) and args.PORT < 65535 and args.PORT > 0):

    conn = keyholder.keyholder.keyholder("ceph", args.TYPE, args.HOST, args.PORT)

    with open("/opt/ceph/ceph/ceph.conf", "rw") as myfile:
        data = myfile.read()

    conn.ensure_path("/etc/ceph/ceph.conf")
    conn.set_node_data("/etc/ceph/ceph.conf", data)

else:
    print "not matched!"