# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import launch_testing.launch_test
import launch_testing_ros

from ros2cli.command import CommandExtension


class TestCommand(CommandExtension):
    """Run a launch test."""

    def add_arguments(self, parser, cli_name):
        """Add arguments to argparse."""
        launch_testing.launch_test.add_arguments(parser)

    def main(self, *, parser, args):
        """Entry point for CLI program."""
        return launch_testing.launch_test.main(
            parser, args, test_runner_cls=launch_testing_ros.LaunchTestRunner
        )
