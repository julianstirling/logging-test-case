"""
MIT License

Copyright (c) 2016 Chad Rosenquist

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Created on Dec 23, 2016

@author: Chad Rosenquist
"""
import unittest
import logging

import loggingtestcase


class LoggingTestCaseExample(loggingtestcase.LoggingTestCase):
    """Example on how to use LoggingTestCase."""

    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        """
        To change the logger or log level, override __init__.
        By default, the root logger is used and the log level is logging.INFO.
        """
        # testlevel = logging.ERROR
        super().__init__(methodName, testlogger, testlevel)

    def setUp(self):
        self.logger = logging.getLogger(__name__)

    def test_pass(self):
        """
        Run a test that logs an info message and
        verify the info is correctly logged.

        Notice that the info message is not logged to the console.
        When all your tests pass, your console output is nice and clean.
        """
        self.logger.info("Starting request...")
        self.logger.info("Done with request.")
        self.assertListEqual(self.captured_logs.output,
                             ['INFO:examples.loggingtestcase_example:Starting request...',
                              'INFO:examples.loggingtestcase_example:Done with request.'])

    def test_fail(self):
        """
        Run a test that fails.

        Notice that the error message is logged to the console.
        This allows for easier debugging.

        Here is the output:
        ======================================================================
        ERROR: test_fail (examples.example1.Example1)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "D:\Git\logging-test-case\examples\loggingtestcase_example.py.py", line 61,
          in test_fail raise FileNotFoundError("Failed to open file.")
        FileNotFoundError: Failed to open file.

        ERROR:examples.example1:Failed to open file.
        ----------------------------------------------------------------------
        """
        self.logger.error("Failed to open file.")
        raise FileNotFoundError("Failed to open file.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
