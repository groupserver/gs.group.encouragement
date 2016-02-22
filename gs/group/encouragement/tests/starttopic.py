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
from gs.group.encouragement.starttopic import (StartTopic, )


class TestStartTopic(TestCase):
    'Test the ``StartTopic`` viewlet'

    @patch.object(StartTopic, 'statsQuery', new_callable=PropertyMock)
    @patch.object(StartTopic, 'groupInfo', new_callable=PropertyMock)
    @patch.object(StartTopic, 'canPost', new_callable=PropertyMock)
    @patch('gs.group.encouragement.starttopic.SiteAdminViewlet.show', new_callable=PropertyMock)
    def test_show(self, m_SAVs, m_cP, m_gI, m_sQ):
        '''Ensure show is True if the member can post, and the group lacks posts'''
        m_SAVs.return_value = True
        m_cP().canPost = True
        m_gI.id = 'example_group'
        m_sQ().posts_per_day.return_value = []

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        s = StartTopic(group, request, view, manager)

        self.assertTrue(s.show)

    @patch.object(StartTopic, 'statsQuery', new_callable=PropertyMock)
    @patch.object(StartTopic, 'groupInfo', new_callable=PropertyMock)
    @patch.object(StartTopic, 'canPost', new_callable=PropertyMock)
    @patch('gs.group.encouragement.starttopic.SiteAdminViewlet.show', new_callable=PropertyMock)
    def test_show_cannot_post(self, m_SAVs, m_cP, m_gI, m_sQ):
        '''Ensure show is False if the member is prevented from posting'''
        m_SAVs.return_value = True
        m_cP().canPost = False
        m_gI.id = 'example_group'
        m_sQ().posts_per_day.return_value = []

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        s = StartTopic(group, request, view, manager)

        self.assertFalse(s.show)

    @patch.object(StartTopic, 'statsQuery', new_callable=PropertyMock)
    @patch.object(StartTopic, 'groupInfo', new_callable=PropertyMock)
    @patch.object(StartTopic, 'canPost', new_callable=PropertyMock)
    @patch('gs.group.encouragement.starttopic.SiteAdminViewlet.show', new_callable=PropertyMock)
    def test_show_posts(self, m_SAVs, m_cP, m_gI, m_sQ):
        '''Ensure show is False if there are posts'''
        m_SAVs.return_value = True
        m_cP().canPost = True
        m_gI.id = 'example_group'
        m_sQ().posts_per_day.return_value = ['A post']

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        s = StartTopic(group, request, view, manager)

        self.assertFalse(s.show)
