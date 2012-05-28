# coding=utf-8
from zope.cachedescriptors.property import Lazy
from gs.group.privacy.visibility import GroupVisibility
from invite import Invite

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
        retval = (self.isSecret
            and (self.memberCount > MAX_SECRET_MEMBERS)
            and (self.statsQuery.posts_per_day(self.groupInfo.id) != []))
        assert type(retval) == bool
        return retval

