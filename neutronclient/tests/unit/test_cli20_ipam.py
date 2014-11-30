# Copyright 2012 OpenStack Foundation.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Saju Madhavan.
#

import sys

from neutronclient.neutron.v2_0 import ipam
from neutronclient.tests.unit import test_cli20


class CLITestV20Ipam(test_cli20.CLITestV20Base):

    def test_create_ipam(self):
        """Create ipam: myid."""
        resource = 'ipam'
        cmd = ipam.CreateIpam(test_cli20.MyApp(sys.stdout), None)
        name = 'myname'
        mgmt = {'ipam_method': None,
                'ipam_dns_method': "none",
                'ipam_dns_server': {
                                   'tenant_dns_server_address': {
                                   'ip_address': []},
                'virtual_dns_server_name': None},
                'dhcp_option_list': None,
                'host_routes': None,
                'cidr_block': None}
        myid = 'myid'
        args = [name]
        position_names = ['name', 'mgmt']
        position_values = [name, mgmt]
        self._test_create_resource(resource, cmd, name, myid, args,
                                   position_names, position_values)

    def test_list_ipams_detail(self):
        """List ipams: -D."""
        resources = 'ipams'
        cmd = ipam.ListIpam(test_cli20.MyApp(sys.stdout), None)
        contents = [{'id': 'name'}]
        self._test_list_resources(resources, cmd, True,
                                  response_contents=contents)

    def test_show_ipam(self):
        """Show ipam: --fields id --fields name myid."""
        resource = 'ipam'
        cmd = ipam.ShowIpam(test_cli20.MyApp(sys.stdout), None)
        args = ['--fields', 'id', '--fields', 'name', self.test_id]
        self._test_show_resource(resource, cmd, self.test_id, args,
                                 ['id', 'name'])

    def test_delete_ipam(self):
        """Delete ipam: myid."""
        resource = 'ipam'
        cmd = ipam.DeleteIpam(test_cli20.MyApp(sys.stdout), None)
        myid = 'myid'
        args = [myid]
        self._test_delete_resource(resource, cmd, myid, args)

    def test_update_ipam(self):
        """Update ipam: myid --name myname --tags a b."""
        resource = 'ipam'
        cmd = ipam.UpdateIpam(test_cli20.MyApp(sys.stdout), None)
        self._test_update_resource(resource, cmd, 'myid',
                                   ['myid', '--name', 'myname'],
                                   {'name': 'myname'})
