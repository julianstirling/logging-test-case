'''
This module is for manually testing class LoggingTestCase.

Created on Dec 23, 2016

@author: Chad Rosenquist
'''
import unittest


from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class LoggingTestCaseTest(LoggingTestCase):
    '''
    This class is for manually testing LoggingTestCase.
    By default, all the tests are disabled.
    Enable them, one by one.
    '''
    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        '''
        To change log level, override __init__.
        TO DO: There has go to be a better way!!!!!!!!!!
        '''
        #import logging; testlevel = logging.ERROR
        super().__init__(methodName, testlogger, testlevel)
    
    
    def setUp(self):
        self.simple_logging = SimpleLogging()
        pass


    def tearDown(self):
        pass


    @unittest.skip("manual test")
    def test_success(self):
        '''
        No logs should be written to the console.
        The test passed, so the logs are discarded.
        '''
        self.simple_logging.all()
        self.assertTrue(True)
    
    @unittest.skip("manual test")
    def test_failure(self):
        '''
        This test fails.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        '''
        self.simple_logging.all()
        self.assertTrue(False)
    
    @unittest.skip("manual test")
    def test_error(self):
        '''
        This test errors.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        '''
        self.simple_logging.all()
        raise Exception("test exception")
    
    @unittest.skip("manual test")
    def test_success_no_logs(self):
        '''
        Tests success with no logs written out.
        
        By default, assertLogs() throws an exception if no logs are written.
        So this test case verifies that exception is correctly handled.
        '''
        self.assertTrue(True)

    @unittest.skip("manual test")
    def test_failure_no_logs(self):
        '''
        This test fails with no logs.
        '''
        self.assertTrue(False)

    @unittest.skip("manual test")
    def test_error_no_logs(self):
        '''
        This test errors with no logs.
        '''
        raise Exception("test exception")
    
    @unittest.skip("manual test")
    def test_captured_logs(self):
        '''
        Tests accessing the captured log files.
        '''
        self.simple_logging.warning()
        self.assertEqual(self.captured_logs.output, ['WARNING:tests.simplelogging:SimpleLogging Warning'])
    
    @unittest.skip("manual test")
    def test_failure_error_and_critical(self):
        '''
        This test fails.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        
        Only the critical and error message should be written out.
        In __init__(), uncomment out the line:
            import logging; testlevel = logging.ERROR
        '''
        self.simple_logging.all()
        self.assertTrue(False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()