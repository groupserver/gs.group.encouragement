# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import getMultiAdapter
from Products.GSGroup.interfaces import IGSMailingListInfo
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

    @property
    def show(self):
        retval = self.canPost.canPost 
        assert type(retval) == bool
        return retval

