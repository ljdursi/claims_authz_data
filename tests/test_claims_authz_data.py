#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for `python_model_service` package."""

import subprocess


def test_dredd():
    """
    Launch the dredd process (which in turn launches the server; see dredd.yml)
    """
    subprocess.check_call(['dredd', '--language=python',
                           '--hookfiles=./dreddhooks.py'],
                          cwd='./tests')
