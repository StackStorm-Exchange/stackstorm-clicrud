# encoding: utf-8

"""
Copyright 2017 Brocade Communications Systems, Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from st2actions.runners.pythonrunner import Action

CONFIG_ITEMS = ['username', 'method']


class BaseConfig(Action):
    """This class loads the correct config environment for the run."""

    def __init__(self, config):
        """Constructor for  checking the environment."""
        super(BaseConfig, self).__init__(config)
        if config is None:
            raise ValueError("No connection configuration details found")
        if "environment" in config:
            if config['environment'] is None:
                raise ValueError("'environment' config defined but empty.")
            else:
                pass
        else:
            for item in CONFIG_ITEMS:
                if item in config:
                    pass
                else:
                    raise KeyError("Config.yaml Mising: %s" % (item))

    def _set_config(self, environment):
        if environment and environment in self.config['environment']:
            group_config = self.config['environment'].get(environment)

            for item in CONFIG_ITEMS:
                if item in group_config:
                    pass
                else:
                    raise KeyError("Config.yaml Mising: environment key:%s:%s"
                                   % (environment, item))
        else:
            group_config = self.config['environment'].get('default')

        try:
            self.method = group_config['method']
            self.method = self.method.encode('utf-8', 'ignore')

            self.username = group_config['username']
            self.username = self.username.encode('utf-8', 'ignore')

            if 'password' in group_config:
                self.password = group_config['password']
                self.password = self.password.encode('utf-8', 'ignore')
            else:
                self.password = ""

            if 'enable' in group_config:
                self.enable = group_config['enable']
                self.enable = self.enable.encode('utf-8', 'ignore')
            else:
                self.enable = ""

            if 'b64password' in group_config:
                if group_config['b64password'] is not None:
                    self.b64password = group_config['b64password']
                    self.b64password = self.b64password.encode('utf-8',
                                                               'ignore')
                else:
                    self.b64password = ""
            else:
                self.b64password = ""

            if 'b64enable' in group_config:
                if group_config['b64enable'] is not None:
                    self.b64enable = group_config['b64enable']
                    self.b64enable = self.b64enable.encode('utf-8', 'ignore')
                else:
                    self.b64enable = ""
            else:
                self.b64enable = ""

        except Exception as e:
            raise Exception(e)
