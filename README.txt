==========================
``gs.group.encouragement``
==========================
A System to Encourage Group Administrators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-04
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

Setting up a group can be challenging, as it is hard to know what to do
first. This product assists with this by providing some encouragement to
the group administrator. `The encouragement`_ takes the form of some
help-text for the administrator, which is automatically displayed by some
JavaScript_.

The Encouragement
=================

The encouragement is a viewlet_, which appears in the JavaScript_ area of
the Group page (see below for the reason why). Within the viewlet is a
viewlet manager, that shows one of four items of encouragement:

#.  `Start a topic`_,
#.  `Invite a new member`_,
#.  `Write an About`_,
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

Write an About
--------------

To normal members the *About* tab just shows some text that the 
administrator. Once the group has really started this encouragement
asks the administrator to write some metadata about the group.

Make a Group Private
---------------------

The final encouragement is to make a group private, rather than secret.  At
`OnlineGroups.Net`_ we have noticed that people start *secret* groups as a
matter of course (the default is *public*).  However, once a group gets to
around a dozen members the boundaries of the group becomes loose, and its
existence stops being secret. In addition, people have difficulty finding
the group if they are not logged in.

To alleviate this problem encouragement is given to the *site*
administrator to change the privacy of the group from secret to public
when more than eleven people are members of the secret group.

JavaScript
==========

The encouragement is not shown by default (it is hidden by the
CSS). Instead it provides the source-data for a Bootstrap_ Popover_ . The
popover will be automatically shown, pointing at the related button or
link, if the encouragement viewlet exists. The popover is almost standard:
the only difference is that there is a close-button (which is necessary as
the popovers are opened automatically).

The JavaScript `browser resource`_ ``gs-group-encouragement-20130304.js``
contains the code for controlling the encouragement. 


Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.encouragement/
- Questions and comments to http://groupserver.org/groups/development/
- Report bugs at https://redmine.iopen.net/projects/groupserver/

.. _onlinegroups.net: http://onlinegroups.net/
.. _GroupServer.org: http://groupserver.org/
.. _GroupServer: http://groupserver.org/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
.. _viewlet: http://docs.zope.org/zope.viewlet/
.. _browser resource: http://docs.zope.org/zope.browserresource/
.. _Bootstrap: http://twitter.github.com/bootstrap/
.. _Popover: http://twitter.github.com/bootstrap/javascript.html#popovers
