
#
# spyne - Copyright (C) Spyne contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#


class LogicError(Exception):
    pass

__version__ = '2.13.7-alpha'

from pytz import utc as LOCAL_TZ
from decimal import Decimal as D

DEFAULT_LANGUAGE = 'en'

from spyne._base import Address

from spyne.context import AuxMethodContext
from spyne.context import TransportContext
from spyne.context import ProtocolContext
from spyne.context import EventContext
from spyne.context import MethodContext

from spyne.evmgr import EventManager

from spyne.descriptor import MethodDescriptor
from spyne.descriptor import BODY_STYLE_WRAPPED
from spyne.descriptor import BODY_STYLE_BARE
from spyne.descriptor import BODY_STYLE_OUT_BARE
from spyne.descriptor import BODY_STYLE_EMPTY
from spyne.descriptor import BODY_STYLE_EMPTY_OUT_BARE

# decorator imports descriptor, so this needs to come after
from spyne.decorator import rpc
from spyne.decorator import srpc
from spyne.decorator import mrpc

from spyne.service import ServiceBase as Service
from spyne.service import ServiceBase  # DEPRECATED
from spyne.application import Application

from spyne.model import *
from spyne.model import Mandatory as M

from spyne.error import InvalidCredentialsError
from spyne.error import RequestTooLongError
from spyne.error import RequestNotAllowed
from spyne.error import ArgumentError
from spyne.error import InvalidInputError
from spyne.error import MissingFieldError
from spyne.error import ValidationError
from spyne.error import InternalError
from spyne.error import ResourceNotFoundError
from spyne.error import RespawnError
from spyne.error import ResourceAlreadyExistsError
from spyne.error import Redirect

from spyne.client import ClientBase, RemoteProcedureBase, RemoteService
from spyne.server import ServerBase, NullServer


def _vercheck():
    import sys
    if not hasattr(sys, "version_info") or sys.version_info < (2, 6):
        raise RuntimeError("Spyne requires Python 2.6 or later. Trust us.")
_vercheck()
