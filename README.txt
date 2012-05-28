Introduction
============

Setting up a group can be challenging, as it is hard to know what to do
first. This product assists with this by providing some encouragement
to the group administrator. `The encouragement`_ takes the form of some
help-text for the administrator.

The Encouragement
=================

The encouragement is a viewlet, which appears at the top of the About 
area (supplied by the ``gs.group.about.interfaces.IGroupAboutInfo`` 
manager). Within the viewlet is a viewlet manager, that shows one of
three items of encouragement:

#.  `Start a topic`_,
#.  `Invite a new member`_, or
#.  `Make a group private`_ rather than secret.

Unlike most viewlets the ``show`` property of each encouragement is
written it is mutually exclusive with the others.

Start a Topic
-------------

The *Start a Topic* encouragement is given to the group administrator
just after the group has been started. If the group has no topics it
encourages the administrator to start one.

Invite a New Member
-------------------

Once the group has a topic the *Invite a New Member* encouragement is
shown. It encourages the administrator to invite someone else to join 
the group. Once that person has accepted an invitation then the
encouragement is hidden.

Make a Group Private
---------------------

The final encouragement is to make a group private, rather than secret.
With the running of `OnlineGroups.Net`_ we have noticed that people 
start *secret* groups as a matter of course (the default is *public*).
However, once a group gets to around a dozen members the boundaries of
the group becomes loose, and its existence stops being secret. In 
addition, people have difficulty finding the group if they are not 
logged in.

To alleviate this problem encouragement is given to the *site*
administrator to change the privacy of the group from secret to public
when more than eleven people are members of the secret group group.

..  _OnlineGroups.Net: http://onlinegroups.net/

