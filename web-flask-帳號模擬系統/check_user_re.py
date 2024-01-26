# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:20:34 2024

@author: willy
"""

import re

def check_user(user):
    if len(user) < 8 or len(user) > 20:
        return '帳號長度必須8-20位之間'
    if not re.search(r'\d', user):
        return '帳號必須包含數字'
    if not re.search(r'[a-z]', user):
        return '帳號必須包含英文字母'
    return None