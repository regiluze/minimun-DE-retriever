# -*- coding: utf-8 -*-

from expects import *


with describe('describe'):
    with before.each:
         pass
    with context('context'):
        with it('foo'):
            pass
