##############################################################################
#
# Copyright (C) Zenoss, Inc. 2016, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

import common
import unittest


class test_changeMemcachedStartup(unittest.TestCase, common.ServiceMigrationTestCase):
    """
    Test that setting for memcached was changed
    """
    initial_servicedef = 'zenoss-resmgr-lite-5.1.0.json'
    expected_servicedef = 'zenoss-resmgr-lite-5.1.0-changeMemcachedStartup.json'
    migration_module_name = 'changeMemcachedStartup'
    migration_class_name = 'ChangeMemcachedStartup'
