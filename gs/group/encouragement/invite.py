# coding=utf-8
from zope.cachedescriptors.property import Lazy
from Products.GSGroupMember.groupMembersInfo import GSGroupMembersInfo
from starttopic import StartTopic


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
        retval = ((self.memberCount < 2)
            and (self.statsQuery.posts_per_day(self.groupInfo.id) != []))
        assert type(retval) == bool
        return retval
