# -*- coding: utf-8 -*-
if __name__ == "__main__":
    import __init__

import unittest
import inputNotBlocked

import sys,time

class inputNotBlockedTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _try_inputNotBlocked(self,testStr):
        inputStr = -1
        start = time.time()
        while True:
            inputStr = inputNotBlocked.Input('')

            if inputStr != None:
                print("Read: {}".format(inputStr))
                self.assertEqual(inputStr, testStr)
                break

            if time.time() - start >= 5:
                inputStr = inputNotBlocked.interruptInput()
                break

        return inputStr

    def _try_input(self,testStr):
        inputStr = -1
        start = time.time()
        while True:
            inputStr = input('')
            print("Read: {}".format(inputStr))

            if inputStr != None:
                self.assertEqual(inputStr, testStr)
                break

            if time.time() - start >= 5:
                inputStr = inputNotBlocked.interruptInput()
                break

        return inputStr

    #=====================================================
    def test_01_one_Input(self):
        fd = open('test.tst', 'w')
        fd.write('ceci est un test\n')
        fd.close()

        oldstdin = sys.stdin
        sys.stdin = open('test.tst')

        self._try_inputNotBlocked('ceci est un test\n')

        sys.stdin.close()
        sys.stdin = oldstdin

    #=====================================================
    def test_02_two_Input(self):

        fd = open('test.tst', 'w')
        fd.write('ceci est un test\n')
        fd.write('ca aussi\n')
        fd.close()

        oldstdin = sys.stdin
        sys.stdin = open('test.tst')

        self._try_inputNotBlocked('ceci est un test\n')

        self._try_inputNotBlocked('ca aussi\n')

        sys.stdin.close()
        sys.stdin = oldstdin


    # =====================================================
    def test_03_first_Input_interrupted_second_not(self):
        fd = open('test.tst', 'w')
        #fd.write('ceci est un test\n')
        fd.write('ca aussi\n')
        fd.close()

        self._try_inputNotBlocked('ceci est un test\n')

        oldstdin = sys.stdin
        sys.stdin = open('test.tst')

        self._try_inputNotBlocked('ca aussi\n')

        sys.stdin.close()
        sys.stdin = oldstdin


    # =====================================================
    def test_04_first_Input_not_interrupted_second_yes(self):
        fd = open('test.tst', 'w')
        fd.write('ceci est un test\n')
        #fd.write('ca aussi\n')
        fd.close()

        oldstdin = sys.stdin
        sys.stdin = open('test.tst')

        self._try_inputNotBlocked('ceci est un test\n')

        sys.stdin.close()
        sys.stdin = oldstdin

        self._try_inputNotBlocked('ca aussi\n')

    # =====================================================
    def test_05_security(self):
        fd = open('test.tst', 'w')
        fd.write('__import__(\'os\').system(\'ls\')\n')
        fd.close()

        oldstdin = sys.stdin
        sys.stdin = open('test.tst')

        self._try_inputNotBlocked('__import__(\'os\').system(\'ls\')\n')

        sys.stdin.close()
        sys.stdin = oldstdin

        oldstdin = sys.stdin
        sys.stdin = open('test.tst')

        self._try_input('__import__(\'os\').system(\'ls\')\n')

        sys.stdin.close()
        sys.stdin = oldstdin




if __name__ == "__main__":
    unittest.main()
