# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:33:30 2023

@author: willy
"""

import re

def check_password(password):
    if len(password) < 8 or len(password) > 20:
        return '密碼長度必須8-20位之間'
    if not re.search(r'\d', password):
        return '密碼必須包含數字'
    if not re.search(r'[a-z]', password):
        return '密碼必須包含英文字母'
    return None
