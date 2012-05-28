# coding=utf-8
from zope.cachedescriptors.property import Lazy
from Products.GSGroupMember.groupMembersInfo import GSGroupMembersInfo
from starttopic import StartTopic

class Invite(StartTopic):
    # See the "show" property for why "Invite" inherits from
    #   "StartTopic"
    @Lazy
    def membersInfo(self):
        retval = GSGroupMembersInfo(self.group)
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
        ppd = self.statsQuery.posts_per_day(self.groupInfo.id)
        retval = (ppd != []) and self.memberCount < 2
        assert type(retval) == bool
        return retval

