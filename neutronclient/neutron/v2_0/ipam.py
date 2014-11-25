import argparse
import logging

from neutronclient.neutron.v2_0 import CreateCommand
from neutronclient.neutron.v2_0 import DeleteCommand
from neutronclient.neutron.v2_0 import ListCommand
from neutronclient.neutron.v2_0 import UpdateCommand
from neutronclient.neutron.v2_0 import ShowCommand


class ListIpam(ListCommand):
    """List IP Address Management information that belong to a given tenant."""

    resource = 'ipam'
    log = logging.getLogger(__name__ + '.ListIpam')
    _formatters = {}
    list_columns = ['id', 'name']


class ShowIpam(ShowCommand):
    """Show information of a given IPAM."""

    resource = 'ipam'
    log = logging.getLogger(__name__ + '.ShowIpam')


class CreateIpam(CreateCommand):
    """Create an IPAM for a given tenant."""

    resource = 'ipam'
    log = logging.getLogger(__name__ + '.CreateIpam')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--method',
            default='fixed',
            help='Set IP Address Management Scheme')
        parser.add_argument(
            'name', metavar='name',
            help='Name of IPAM to create')

    def args2body(self, parsed_args):
        body = {'ipam': {
            'name': parsed_args.name,
            'mgmt': {'method': parsed_args.method}, },
               }
        if parsed_args.tenant_id:
            body['ipam'].update({'tenant_id': parsed_args.tenant_id})
        return body


class DeleteIpam(DeleteCommand):
    """Delete a given IPAM."""

    log = logging.getLogger(__name__ + '.DeleteIpam')
    resource = 'ipam'


class UpdateIpam(UpdateCommand):
    """Update IPAM's information."""

    log = logging.getLogger(__name__ + '.UpdateIpam')
    resource = 'ipam'

