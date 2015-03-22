import os
import shutil
import unittest
from npm.bindings import (
    npm_installed, npm_version, npm_version_raw, npm_install, npm_run, ensure_npm_installed, ensure_npm_version_gte
)
from npm.utils import six
from npm.exceptions import OutdatedDependency, MalformedVersionInput

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PATH_TO_NODE_MODULES = os.path.join(TEST_DIR, 'node_modules')
DEPENDENCY_PACKAGE = 'yargs'
PATH_TO_INSTALLED_PACKAGE = os.path.join(PATH_TO_NODE_MODULES, DEPENDENCY_PACKAGE)
PACKAGE_TO_INSTALL = 'jquery'
PATH_TO_PACKAGE_TO_INSTALL = os.path.join(PATH_TO_NODE_MODULES, PACKAGE_TO_INSTALL)
PATH_TO_PACKAGE_JSON = os.path.join(TEST_DIR, 'package.json')


class Testnpm(unittest.TestCase):
    def setUp(self):
        self.package_json_contents = self.read_package_json()

    def tearDown(self):
        if os.path.exists(PATH_TO_NODE_MODULES):
            shutil.rmtree(PATH_TO_NODE_MODULES)
        self.write_package_json(self.package_json_contents)

    def read_package_json(self):
        with open(PATH_TO_PACKAGE_JSON, 'r') as package_json_file:
            return package_json_file.read()

    def write_package_json(self, contents):
        with open(PATH_TO_PACKAGE_JSON, 'w+') as package_json_file:
            package_json_file.write(contents)

    def test_npm_is_installed(self):
        self.assertTrue(npm_installed)

    def test_npm_version_raw(self):
        self.assertTrue(isinstance(npm_version_raw, six.string_types))
        self.assertGreater(len(npm_version_raw), 0)

    def test_npm_version(self):
        self.assertTrue(isinstance(npm_version, tuple))
        self.assertGreaterEqual(len(npm_version), 3)

    def test_ensure_npm_installed(self):
        ensure_npm_installed()

    def test_ensure_npm_version_greater_than(self):
        self.assertRaises(MalformedVersionInput, ensure_npm_version_gte, 'v99999.0.0')
        self.assertRaises(MalformedVersionInput, ensure_npm_version_gte, '99999.0.0')
        self.assertRaises(MalformedVersionInput, ensure_npm_version_gte, (None,))
        self.assertRaises(MalformedVersionInput, ensure_npm_version_gte, (10,))
        self.assertRaises(MalformedVersionInput, ensure_npm_version_gte, (999999999,))
        self.assertRaises(MalformedVersionInput, ensure_npm_version_gte, (999999999, 0,))

        self.assertRaises(OutdatedDependency, ensure_npm_version_gte, (999999999, 0, 0,))

        ensure_npm_version_gte((0, 0, 0,))
        ensure_npm_version_gte((0, 9, 99999999))
        ensure_npm_version_gte((2, 1, 8,))

    def test_npm_run_returns_output(self):
        stderr, stdout = npm_run('--version',)
        stdout = stdout.strip()
        self.assertEqual(stdout, npm_version_raw)

    def test_npm_install_can_install_dependencies(self):
        npm_install(TEST_DIR)
        self.assertTrue(os.path.exists(PATH_TO_NODE_MODULES))
        self.assertTrue(os.path.exists(PATH_TO_INSTALLED_PACKAGE))