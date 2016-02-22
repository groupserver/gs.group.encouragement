# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals, print_function
from mock import (MagicMock, patch, PropertyMock)
from unittest import TestCase
from gs.group.encouragement.invite import (Invite, )


class TestInvite(TestCase):
    'Test the ``Invite`` viewlet'

    @patch.object(Invite, 'memberCount', new_callable=PropertyMock)
    @patch.object(Invite, 'statsQuery', new_callable=PropertyMock)
    @patch.object(Invite, 'groupInfo', new_callable=PropertyMock)
    def test_show(self, m_gI, m_sQ, m_mC):
        '''Ensure show is True if have one member, and posts'''
        m_gI.id = 'example_group'
        m_mC.return_value = 1
        m_sQ().posts_per_day.return_value = ['A post']

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        invite = Invite(group, request, view, manager)

        self.assertTrue(invite.show)

    @patch.object(Invite, 'memberCount', new_callable=PropertyMock)
    @patch.object(Invite, 'statsQuery', new_callable=PropertyMock)
    @patch.object(Invite, 'groupInfo', new_callable=PropertyMock)
    def test_show_no_post(self, m_gI, m_sQ, m_mC):
        '''Ensure show is false if lack posts'''
        m_gI.id = 'example_group'
        m_mC.return_value = 1
        m_sQ().posts_per_day.return_value = []

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        invite = Invite(group, request, view, manager)

        self.assertFalse(invite.show)

    @patch.object(Invite, 'memberCount', new_callable=PropertyMock)
    @patch.object(Invite, 'statsQuery', new_callable=PropertyMock)
    @patch.object(Invite, 'groupInfo', new_callable=PropertyMock)
    def test_show_people(self, m_gI, m_sQ, m_mC):
        '''Ensure show is False if have more than one member'''
        m_gI.id = 'example_group'
        m_mC.return_value = 2
        m_sQ().posts_per_day.return_value = []

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        invite = Invite(group, request, view, manager)

        self.assertFalse(invite.show)
