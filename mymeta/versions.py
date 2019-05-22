#!/usr/bin/env python3

import rose.upgrade


class Migration_001(rose.upgrade.MacroUpgrade):
    """migration_001"""

    BEFORE_TAG = 'myapp1.0'
    AFTER_TAG = 'myapp2.0'

    def upgrade(self, config, meta_config=None):
        self.add_setting(config, ['namelist:foo'])
        self.add_setting(config, ['namelist:foo', 'foo'], '.false.')

        derived_value = self.get_setting_value(config, ['env', 'a'])

        self.add_setting(config, ['namelist:bar'])
        self.add_setting(config, ['namelist:bar', 'bar'], derived_value)

        return config, self.reports
