# coding=utf-8
from zope.cachedescriptors.property import Lazy
from invite import Invite

class Private(Invite):
    @property
    def show(self):
        ppd = self.statsQuery.posts_per_day(self.groupInfo.id)
        retval = (ppd != []) and (self.memberCount > 11) # And secret
        assert type(retval) == bool
        return retval

