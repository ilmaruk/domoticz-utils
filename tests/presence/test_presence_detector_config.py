# -*- coding: utf-8 -*-
import __builtin__
import pytest
import yaml

from domoticz_utils.presence.detector import InvalidConfigFileError, PresenceDetectorConfig, DeviceConfig


@pytest.fixture
def config():
    return {
        'finders': {
            'ip_finder': {
                'class': 'IpFinder'
            }
        },
        'devices': {
            '192.168.0.83': {
                'finder': 'ip_finder',
                'polling_interval': '5',
                'missing_threshold': '20',
                'domoticz_idx': '24'
            }
        }
    }


@pytest.fixture
def sut(monkeypatch, config):
    def patched_read_from_yaml(self, path):
        return config
    monkeypatch.setattr(PresenceDetectorConfig, 'read_from_yaml', patched_read_from_yaml)
    return PresenceDetectorConfig('foo.yaml')


def test_should_raise_error_for_unsupported_config_types():
    with pytest.raises(InvalidConfigFileError):
        PresenceDetectorConfig('invalid.config')


def test_should_return_finders(sut):
    finders = sut.get_finders()
    assert len(finders.keys()) == 1
    assert finders.keys()[0] == 'ip_finder'


def test_should_return_device_configs(sut):
    device_configs = sut.get_devices()
    assert len(device_configs.keys()) == 1
    assert isinstance(device_configs.values()[0], DeviceConfig)
