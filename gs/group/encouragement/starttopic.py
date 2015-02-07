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
from zope.component import getMultiAdapter
from Products.GSGroup.interfaces import IGSMailingListInfo
from gs.group.stats import MessageQuery as StatsQuery
from gs.group.member.canpost.interfaces import IGSPostingUser
from gs.group.member.viewlet import SiteAdminViewlet


class StartTopic(SiteAdminViewlet):
    def __init__(self, group, request, view, manager):
        super(StartTopic, self).__init__(group, request, view, manager)

    @Lazy
    def email(self):
        l = IGSMailingListInfo(self.groupInfo.groupObj)
        retval = l.get_property('mailto')
        return retval

    @Lazy
    def statsQuery(self):
        retval = StatsQuery(self.context)
        assert retval
        return retval

    @Lazy
    def canPost(self):
        retval = getMultiAdapter(
            (self.groupInfo.groupObj, self.loggedInUser), IGSPostingUser)
        return retval

    @property
    def show(self):
        retval = (
            super(StartTopic, self).show and self.canPost.canPost
            and (self.statsQuery.posts_per_day(self.groupInfo.id) == []))
        assert type(retval) == bool
        return retval
