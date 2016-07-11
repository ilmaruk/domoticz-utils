# -*- coding: utf-8 -*-
import subprocess

import pytest

from domoticz_utils.presence import DEVICE_FOUND, DEVICE_NOT_FOUND
from domoticz_utils.presence.finders import IpFinder


@pytest.fixture
def sut():
    return IpFinder()


def test_should_find_device(sut, monkeypatch):
    def mock_subprocess_call(command, **kwargs):
        return 0
    monkeypatch.setattr(subprocess, 'call', mock_subprocess_call)
    assert sut.find("0.0.0.0") == DEVICE_FOUND


def test_should_not_find_device(sut, monkeypatch):
    def mock_subprocess_call(command, **kwargs):
        return 2
    monkeypatch.setattr(subprocess, 'call', mock_subprocess_call)
    assert sut.find("0.0.0.0") == DEVICE_NOT_FOUND
