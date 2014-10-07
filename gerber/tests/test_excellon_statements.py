#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Hamilton Kibbe <ham@hamiltonkib.be>

from .tests import *
from ..excellon_statements import *


def test_ExcellonTool_factory():
    """ Test ExcellonTool factory method
    """
    exc_line = 'T8F00S00C0.12500'
    settings = {'format': (2, 5), 'zero_suppression': 'trailing',
                'units': 'inch', 'notation': 'absolute'}
    tool = ExcellonTool.from_excellon(exc_line, settings)
    assert_equal(tool.diameter, 0.125)
    assert_equal(tool.feed_rate, 0)
    assert_equal(tool.rpm, 0)


def test_ExcellonTool_dump():
    """ Test ExcellonTool to_gerber method
    """
    exc_lines = ['T1F00S00C0.01200', 'T2F00S00C0.01500', 'T3F00S00C0.01968',
                 'T4F00S00C0.02800', 'T5F00S00C0.03300', 'T6F00S00C0.03800',
                 'T7F00S00C0.04300', 'T8F00S00C0.12500', 'T9F00S00C0.13000', ]
    settings = {'format': (2, 5), 'zero_suppression': 'trailing',
                'units': 'inch', 'notation': 'absolute'}
    for line in exc_lines:
        tool = ExcellonTool.from_excellon(line, settings)
        assert_equal(tool.to_excellon(), line)
    