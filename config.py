#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6742577076:AAGJS0qCRfwPioVBOSC0Y4rav-DsFz1DfVg")
    API_ID = int(os.environ.get("API_ID", "28589332"))
    API_HASH = os.environ.get("API_HASH", "e038e76d9a6226da0bb2ae6bce2bf0a0")
    AUTH_USERS = "5651100634"

