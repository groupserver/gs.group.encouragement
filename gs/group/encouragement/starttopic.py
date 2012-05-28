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
        da = self.context.zsqlalchemy
        retval = StatsQuery(self.context, da)
        assert retval
        return retval

    @property
    def show(self):
        ppd = self.statsQuery.posts_per_day(self.groupInfo.id)
        retval = self.canPost.canPost and (ppd == [])
        assert type(retval) == bool
        return retval

