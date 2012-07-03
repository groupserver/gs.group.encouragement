# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import getMultiAdapter
from Products.GSGroup.interfaces import IGSMailingListInfo
from Products.GSParticipationStats.queries import MessageQuery as \
    StatsQuery
from gs.group.member.canpost.interfaces import IGSPostingUser
from gs.group.home.simpletab import UserInfoTab

class StartTopic(UserInfoTab):

    @Lazy
    def canPost(self):
        retval = getMultiAdapter((self.groupInfo.groupObj, self.userInfo), 
                                  IGSPostingUser)
        return retval

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

    @property
    def show(self):
        retval = (self.canPost.canPost 
            and (self.statsQuery.posts_per_day(self.groupInfo.id) == []))
        assert type(retval) == bool
        return retval

