#!/usr/bin/env python

import os
import pyrax

creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cloud_servers = pyrax.cloudservers

for server in cloud_servers.servers.list():
    print "Name: %s\n    ID: %s\n    IP: %s" % \
           (server.name, server.id, server.accessIPv4)    
