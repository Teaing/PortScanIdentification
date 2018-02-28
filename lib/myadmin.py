#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Tea

import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    print 'is administrator.'
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
