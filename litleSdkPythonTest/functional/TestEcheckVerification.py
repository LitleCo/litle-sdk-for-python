#Copyright (c) 2011-2012 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

from litleSdkPythonTest.all.SetupTest import *
import unittest

class TestEcheckVerification(unittest.TestCase):
    
    def test_simpleEcheckVerification(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456L
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeckverification.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echeckverification.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckverification)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

    
    def test_echeckVerificationWithEcheckToken(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456L
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'
        
        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum = "123455"
        echeckverification.echeckOrEcheckToken = token
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echeckverification.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckverification)
        self.assertEquals(response.message, "Valid Format")
        self.assertEquals("Approved",response.transactionResponse.message)

        
    def test_MissingBillingField(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123L
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeckverification.echeckOrEcheckToken = echeck
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echeckverification)
        self.assert_(response.message.count("Error validating xml data against the schema"))

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEcheckVerification)
    return suite