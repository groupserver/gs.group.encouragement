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
from gs.group.encouragement.private import (Private, MAX_SECRET_MEMBERS, )


class TestPrivate(TestCase):
    'Test the ``Private`` viewlet'

    @patch.object(Private, 'memberCount', new_callable=PropertyMock)
    @patch.object(Private, 'statsQuery', new_callable=PropertyMock)
    @patch.object(Private, 'groupInfo', new_callable=PropertyMock)
    @patch.object(Private, 'isSecret', new_callable=PropertyMock)
    def test_show(self, m_iS, m_gI, m_sQ, m_mC):
        '''Ensure show is True if the group is secret, we have too many members, and posts'''
        m_iS.return_value = True
        m_gI.id = 'example_group'
        m_mC.return_value = MAX_SECRET_MEMBERS + 1
        m_sQ().posts_per_day.return_value = ['A post']

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        private = Private(group, request, view, manager)

        self.assertTrue(private.show)

    @patch.object(Private, 'memberCount', new_callable=PropertyMock)
    @patch.object(Private, 'statsQuery', new_callable=PropertyMock)
    @patch.object(Private, 'groupInfo', new_callable=PropertyMock)
    @patch.object(Private, 'isSecret', new_callable=PropertyMock)
    def test_show_not_secret(self, m_iS, m_gI, m_sQ, m_mC):
        '''Ensure show is False if the group is something other than secret'''
        m_iS.return_value = False
        m_gI.id = 'example_group'
        m_mC.return_value = MAX_SECRET_MEMBERS + 1
        m_sQ().posts_per_day.return_value = ['A post']

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        private = Private(group, request, view, manager)

        self.assertFalse(private.show)

    @patch.object(Private, 'memberCount', new_callable=PropertyMock)
    @patch.object(Private, 'statsQuery', new_callable=PropertyMock)
    @patch.object(Private, 'groupInfo', new_callable=PropertyMock)
    @patch.object(Private, 'isSecret', new_callable=PropertyMock)
    def test_show_small(self, m_iS, m_gI, m_sQ, m_mC):
        '''Ensure show is False if the secret group is small'''
        m_iS.return_value = True
        m_gI.id = 'example_group'
        m_mC.return_value = MAX_SECRET_MEMBERS
        m_sQ().posts_per_day.return_value = ['A post']

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        private = Private(group, request, view, manager)

        self.assertFalse(private.show)

    @patch.object(Private, 'memberCount', new_callable=PropertyMock)
    @patch.object(Private, 'statsQuery', new_callable=PropertyMock)
    @patch.object(Private, 'groupInfo', new_callable=PropertyMock)
    @patch.object(Private, 'isSecret', new_callable=PropertyMock)
    def test_show_inactive(self, m_iS, m_gI, m_sQ, m_mC):
        '''Ensure show is False if the secret group lacks posts'''
        m_iS.return_value = True
        m_gI.id = 'example_group'
        m_mC.return_value = MAX_SECRET_MEMBERS - 1
        m_sQ().posts_per_day.return_value = []

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        private = Private(group, request, view, manager)

        self.assertFalse(private.show)
