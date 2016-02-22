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
        group = MagicMock()
        del(group.aboutText)
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertFalse(a.hasAboutText)

    def test_has_about_blank(self):
        group = MagicMock()
        group.aboutText = ' '
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertFalse(a.hasAboutText)

    def test_has_about_set(self):
        group = MagicMock()
        group.aboutText = 'Tonight on Ethel the Frog'
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = About(group, request, view, manager)

        self.assertTrue(a.hasAboutText)
