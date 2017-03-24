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

import sys
from clicrud.device.generic import generic
from base.actions import BaseConfig


class OPSCommand(BaseConfig):
    """OpsCommand is the ST2 way of running op commands via CLICRUD."""

    def run(self, environment, host, command):
        """Run() is called for the action to be executed."""
        self._set_config(environment)

        utf8_command = command.encode('utf-8', 'ignore')
        utf8_host = host.encode('utf-8', 'ignore')

        transport = None

        try:
            if self.b64password != "" and self.b64enable != "":
                transport = generic(host=utf8_host,
                                    username=self.username,
                                    method=self.method,
                                    b64password=self.b64password,
                                    b64enable=self.b64enable)

            if self.b64enable != "":
                transport = generic(host=utf8_host,
                                    username=self.username,
                                    method=self.method,
                                    password=self.password,
                                    b64enable=self.b64enable)

            if self.b64password != "":
                transport = generic(host=utf8_host,
                                    username=self.username,
                                    method=self.method,
                                    enable=self.enable,
                                    b64password=self.b64password)

            if self.b64enable == "" and self.b64password == "":
                transport = generic(host=utf8_host,
                                    username=self.username,
                                    method=self.method,
                                    password=self.password,
                                    enable=self.enable)

            return_value = transport.read(utf8_command, return_type="string")
            return_value = unicode(return_value, "utf-8")

            if transport:
                transport.close()

            return return_value

        except Exception, err:
            self.logger.info('OPSCommand threw an exception')
            self.logger.info(err)
            sys.exit(2)
