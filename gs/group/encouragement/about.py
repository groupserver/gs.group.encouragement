# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2013, 2014, 2015, 2016 OnlineGroups.net and
# Contributors.
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
from __future__ import absolute_import, unicode_literals, print_function
from zope.cachedescriptors.property import Lazy
from .invite import Invite


class About(Invite):
    '''The *Change about* encouragement'''
    @Lazy
    def hasAboutText(self):
        t = getattr(self.context, b'aboutText', '').strip()
        retval = bool(t)
        return retval

    @property
    def show(self):
        '''Show the *Change about* encouragement box if we lack about text, have posts, and some
members'''
        retval = (
            (not self.hasAboutText)
            and (self.statsQuery.posts_per_day(self.groupInfo.id) != [])
            and (self.memberCount > 1))
        assert type(retval) == bool
        return retval
