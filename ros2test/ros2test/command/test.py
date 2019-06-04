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

import logging
import os

import launch_testing.launch_test
import launch_testing_ros

from ros2cli.command import CommandExtension

from ..api.domain_coordinator import get_coordinated_domain_id

_logger_ = logging.getLogger(__name__)


class TestCommand(CommandExtension):
    """Run a ROS2 launch test."""

    def add_arguments(self, parser, cli_name):
        """Add arguments to argparse."""
        launch_testing.launch_test.add_arguments(parser)
        parser.add_argument(
            '--disable-isolation', action='store_true', default=False,
            help='Disable automatic ROS_DOMAIN_ID isolation.'
        )

    def main(self, *, parser, args):
        """Entry point for CLI program."""
        # If ROS_DOMAIN_ID is already set, launch_test will respect that domain ID and use it.
        # If ROS_DOMAIN_ID is not set, launch_test will pick a ROS_DOMAIN_ID that's not being used
        # by another launch_test process.
        # This is to allow launch_test to run in parallel and not have ROS cross-talk.
        # If the user needs to debug a test and they don't have ROS_DOMAIN_ID set in their
        # environment they can disable isolation by passing the --disable-isolation flag.
        if 'ROS_DOMAIN_ID' not in os.environ and not args.disable_isolation:
            domain_id = get_coordinated_domain_id()  # Must keep this as a local to keep it alive
            _logger_.info('Running with ROS_DOMAIN_ID {}'.format(domain_id))
            os.environ['ROS_DOMAIN_ID'] = str(domain_id)
        if 'ROS_DOMAIN_ID' in os.environ:
            print('ROS_DOMAIN_ID', os.environ['ROS_DOMAIN_ID'])
        else:
            print('No ROS_DOMAIN_ID')
        return launch_testing.launch_test.run(
            parser, args, test_runner_cls=launch_testing_ros.LaunchTestRunner
        )
