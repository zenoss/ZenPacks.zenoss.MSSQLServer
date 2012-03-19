######################################################################
#
# Copyright 2007, 2009 Zenoss, Inc.  All Rights Reserved.
#
######################################################################
import Globals
from Products.ZenModel.migrate.Migrate import Version
from ZenPacks.zenoss.MSSQLServer import ZenPack
import logging

class BaseClass:
    version = Version(2, 0, 1)

    def migrate(self, pack):
        if pack.__class__ != ZenPack:
            pack.__class__ = ZenPack
