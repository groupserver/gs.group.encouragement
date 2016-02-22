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
from gs.group.encouragement.about import (About, )


class TestAbout(TestCase):
    'Test the ``About`` viewlet'

    def test_has_about_missing(self):
        '''Ensure hasAboutText is False if the aboutText property is missing'''
        group = MagicMock()
        del(group.aboutText)
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertFalse(a.hasAboutText)

    def test_has_about_blank(self):
        '''Ensure hasAboutText is False if the aboutText property is set to " "'''
        group = MagicMock()
        group.aboutText = ' '
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertFalse(a.hasAboutText)

    def test_has_about_set(self):
        '''Ensure hasAboutText is True if the about test is set to something sane'''
        group = MagicMock()
        group.aboutText = 'Tonight on Ethel the Frog'
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertTrue(a.hasAboutText)

    @patch.object(About, 'memberCount', new_callable=PropertyMock)
    @patch.object(About, 'hasAboutText', new_callable=PropertyMock)
    @patch.object(About, 'statsQuery', new_callable=PropertyMock)
    @patch.object(About, 'groupInfo', new_callable=PropertyMock)
    def test_show(self, m_gI, m_sQ, m_hAT, m_mC):
        '''Ensure show is True if we lack about text, have members, and have a post'''
        m_gI.id = 'example_group'
        m_hAT.return_value = False
        m_mC.return_value = 2
        m_sQ().posts_per_day.return_value = ['A post', ]

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertTrue(a.show)

    @patch.object(About, 'memberCount', new_callable=PropertyMock)
    @patch.object(About, 'hasAboutText', new_callable=PropertyMock)
    @patch.object(About, 'statsQuery', new_callable=PropertyMock)
    @patch.object(About, 'groupInfo', new_callable=PropertyMock)
    def test_show_one_member(self, m_gI, m_sQ, m_hAT, m_mC):
        '''Ensure show is False if we lack about text, have only one member, and have a post'''
        m_gI.id = 'example_group'
        m_hAT.return_value = False
        m_mC.return_value = 1
        m_sQ().posts_per_day.return_value = ['A post', ]

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertFalse(a.show)

    @patch.object(About, 'memberCount', new_callable=PropertyMock)
    @patch.object(About, 'hasAboutText', new_callable=PropertyMock)
    @patch.object(About, 'statsQuery', new_callable=PropertyMock)
    @patch.object(About, 'groupInfo', new_callable=PropertyMock)
    def test_show_no_post(self, m_gI, m_sQ, m_hAT, m_mC):
        '''Ensure show is False if we lack about text, have members, and but lack a post'''
        m_gI.id = 'example_group'
        m_hAT.return_value = False
        m_mC.return_value = 2
        m_sQ().posts_per_day.return_value = []

        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertFalse(a.show)
