# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2014 Juniper Networks.  All rights reserved.
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
# @author:

import logging

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListIpam(neutronV20.ListCommand):
    """List IP Address Management information that belong to a given tenant."""

    resource = 'ipam'
    log = logging.getLogger(__name__ + '.ListIpam')
    _formatters = {}
    list_columns = ['id', 'name']


class ShowIpam(neutronV20.ShowCommand):
    """Show information of a given IPAM."""

    resource = 'ipam'
    log = logging.getLogger(__name__ + '.ShowIpam')


class CreateIpam(neutronV20.CreateCommand):
    """Create an IPAM for a given tenant."""

    resource = 'ipam'
    log = logging.getLogger(__name__ + '.CreateIpam')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', metavar='name',
            help=_('Name of IPAM to create'))

        parser.add_argument(
            '--dns_method',
            default='none',
            choices=['none',
                     'default-dns-server',
                     'virtual-dns-server',
                     'tenant-dns-server'],
            help=_('Set DNS Method'))

        parser.add_argument(
            '--virtual_dns_server_name',
            default=None,
            help=_('Set Virtual DNS Server Name'))

        parser.add_argument(
            '--tenant_dns_server_ip_address',
            default=[],
            action='append',
            help=_('Set Tenant DNS Server IP Address '
                   '(This option can be repeated).'))

    def args2body(self, parsed_args):
        body = {
            'ipam': {
            'name': parsed_args.name,
            'mgmt': {
                'ipam_method': None,
                'ipam_dns_method': parsed_args.dns_method,
                'ipam_dns_server': {
                'tenant_dns_server_address': {
                'ip_address': parsed_args.tenant_dns_server_ip_address, },
                'virtual_dns_server_name': parsed_args.virtual_dns_server_name},
                'dhcp_option_list': None,
                'host_routes': None,
                'cidr_block': None}, }, }
        if parsed_args.tenant_id:
            body['ipam'].update({'tenant_id': parsed_args.tenant_id})
        return body


class DeleteIpam(neutronV20.DeleteCommand):
    """Delete a given IPAM."""

    log = logging.getLogger(__name__ + '.DeleteIpam')
    resource = 'ipam'


class UpdateIpam(neutronV20.UpdateCommand):
    """Update IPAM's information."""

    log = logging.getLogger(__name__ + '.UpdateIpam')
    resource = 'ipam'
