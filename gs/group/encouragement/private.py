# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2013, 2014, 2015 OnlineGroups.net and Contributors.
#
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from gs.group.privacy.visibility import GroupVisibility
from .invite import Invite

# TODO: change to an option.
MAX_SECRET_MEMBERS = 11
# --=mpj17=--
# The number of secret members was set to 11 by dvr and mpj17. It seemed
#   a good idea at the time.


class Private(Invite):
    @Lazy
    def isSecret(self):
        gv = GroupVisibility(self.groupInfo)
        return gv.isSecret

    @property
    def show(self):
        retval = (
            self.isSecret
            and (self.memberCount > MAX_SECRET_MEMBERS)
            and (self.statsQuery.posts_per_day(self.groupInfo.id) != []))
        assert type(retval) == bool
        return retval
