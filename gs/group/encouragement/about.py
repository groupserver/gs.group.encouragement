# coding=utf-8
from zope.cachedescriptors.property import Lazy
from invite import Invite


class About(Invite):
    @Lazy
    def hasAboutText(self):
        t = getattr(self.context, 'aboutText', '').strip()
        retval = bool(t)
        return retval

    @property
    def show(self):
        retval = ((not self.hasAboutText)
            and (self.statsQuery.posts_per_day(self.groupInfo.id) != [])
            and (self.memberCount > 1))
        assert type(retval) == bool
        return retval

