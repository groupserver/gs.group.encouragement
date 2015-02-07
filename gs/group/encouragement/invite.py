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
from Products.GSGroupMember.groupMembersInfo import GSGroupMembersInfo
from .starttopic import StartTopic


class Invite(StartTopic):
    # See the "show" property for why "Invite" inherits from
    #   "StartTopic"
    @Lazy
    def membersInfo(self):
        retval = GSGroupMembersInfo(self.context)
        assert retval
        return retval

    @Lazy
    def memberCount(self):
        retval = self.membersInfo.fullMemberCount
        return retval

    @property
    def show(self):
        # Only show the Invite encouragement when the Topic
        #   encouragement is not shown.
        retval = (
            (self.memberCount < 2)
            and (self.statsQuery.posts_per_day(self.groupInfo.id) != []))
        assert type(retval) == bool
        return retval
