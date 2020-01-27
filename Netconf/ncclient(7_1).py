# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:13:53 2020

@author: Umair Bin Mansoor
"""

from ncclient import manager

nexus = manager.connect(host='sbx-nxos-mgmt.cisco.com', port=10000, username='admin', password='Admin_1234!',
                        hostkey_verify=False)
for capability in nexus.server_capabilities:
    print(capability)