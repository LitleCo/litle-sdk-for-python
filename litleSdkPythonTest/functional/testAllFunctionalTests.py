import unittest
import TestAuth, TestAuthReversal, TestCapture, TestCaptureGivenAuth, TestCredit
import TestEcheckCredit, TestEcheckRedeposit, TestEcheckSale, TestEcheckVerification
import TestEcheckVoid, TestForceCapture, TestSale, TestToken

testauth = TestAuth.suite()
testauthreverasal = TestAuthReversal.suite()
testcapture = TestCapture.suite()
testcapturegivenauth = TestCaptureGivenAuth.suite()
testcredit = TestCredit.suite()

testecheckcredit = TestEcheckCredit.suite()
testecheckredeposit = TestEcheckRedeposit.suite()
testechecksale = TestEcheckSale.suite()
testecheckverfication = TestEcheckVerification.suite()

testecheckvoid = TestEcheckVoid.suite()
testforcecapture = TestForceCapture.suite()
testsale = TestSale.suite()
testtoken = TestToken.suite()

unittest.TextTestRunner().run(testauth)
unittest.TextTestRunner().run(testauthreverasal)
unittest.TextTestRunner().run(testcapture)
unittest.TextTestRunner().run(testcapturegivenauth)
unittest.TextTestRunner().run(testcredit)

unittest.TextTestRunner().run(testecheckcredit)
unittest.TextTestRunner().run(testecheckredeposit)
unittest.TextTestRunner().run(testechecksale)
unittest.TextTestRunner().run(testecheckverfication)

unittest.TextTestRunner().run(testecheckvoid)
unittest.TextTestRunner().run(testforcecapture)
unittest.TextTestRunner().run(testsale)
unittest.TextTestRunner().run(testtoken)