from SetupTest import *
import unittest
from mock import *

class TestLitleOnline(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_auth(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'
        authorization.card = card

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authorization)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authorization.*?<card>.*?<number>4100000000000000</number>.*?</card>.*?</authorization>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)


    def test_authreversal(self):
        authreversal = litleXmlFields.authReversal()
        authreversal.litleTxnId = 12345678000
        authreversal.amount = 106
        authreversal.payPalNotes = "Notes"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(authreversal)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<authReversal.*?<litleTxnId>12345678000</litleTxnId>.*?</authReversal>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_capture(self):
        capture = litleXmlFields.capture()
        capture.litleTxnId = 123456000
        capture.amount = 106
        capture.payPalNotes = "Notes"

        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(capture)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<capture.*?<litleTxnId>123456000</litleTxnId>.*?</capture>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_capturegivenauth(self):
        capturegivenauth = litleXmlFields.captureGivenAuth()
        capturegivenauth.amount = 106
        capturegivenauth.orderId = "12344"
        
        authinfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        authinfo.authDate = date
        authinfo.authCode = "543216"
        authinfo.authAmount =12345
        capturegivenauth.authInformation = authinfo
        
        capturegivenauth.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        capturegivenauth.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(capturegivenauth)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<captureGivenAuth.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</captureGivenAuth>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_credit(self):
        credit = litleXmlFields.credit()
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(credit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<credit.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</credit>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_echeckcredit(self):
        echeckcredit = litleXmlFields.echeckCredit()
        echeckcredit.amount = 12
        echeckcredit.litleTxnId = 123456789101112
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckcredit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckCredit.*?<litleTxnId>123456789101112</litleTxnId>.*?</echeckCredit>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_echeckredeposit(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckredeposit)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckRedeposit.*?<litleTxnId>123456</litleTxnId>.*?</echeckRedeposit>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_echecksale(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "12345657890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echecksale.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echecksale)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckSale.*?<echeck>.*?<accNum>12345657890</accNum>.*?</echeck>.*?</echeckSale>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_echeckvoid(self):
        echeckvoid = litleXmlFields.echeckVoid()
        echeckvoid.litleTxnId = 12345
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckvoid)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckVoid.*?<litleTxnId>12345</litleTxnId>.*?</echeckVoid>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_echeckverification(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456
        echeckverification.orderId = "12345"
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
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(echeckverification)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<echeckVerification.*?<echeck>.*?<accNum>12345657890</accNum>.*?</echeck>.*?</echeckVerification>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_forcecapture(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.orderId = "12344"
        forcecapture.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        forcecapture.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(forcecapture)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<forceCapture.*?<card>.*?<number>4100000000000001</number>.*?</card>.*?</forceCapture>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_sale(self):
        sale = litleXmlFields.sale()
        sale.amount = 106
        sale.litleTxnId = 123456
        sale.orderId = "12344"
        sale.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000002"
        card.expDate = "1210"
        sale.card = card
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(sale)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<sale.*?<card>.*?<number>4100000000000002</number>.*?</card>.*?</sale>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

    def test_token(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = "12344"
        token.accountNumber = "1233456789103801"
        
        comm = Communications(config)
        comm.http_post = MagicMock()

        litle = litleOnlineRequest(config)
        litle.setCommunications(comm)
        litle._processResponse = MagicMock(return_value=None)
        litle.sendRequest(token)
        
        comm.http_post.assert_called_once()
        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<registerTokenRequest.*?<accountNumber>1233456789103801</accountNumber>.*?</registerTokenRequest>.*?")
        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

#    def test_pyxbexception(self):
#        auth = litleXmlFields.authorization()
#        auth.reportGroup = "Planets"
#        auth.orderId = "12344"
#        auth.amount = 106
#        auth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000002"
#        card.expDate = "1210"
#        auth.card = card
#        
#        comm = Communications(config)
#        comm.http_post = MagicMock()
#
#        litle = litleOnlineRequest(config)
#        litle.setCommunications(comm)
#        litle._processResponse = MagicMock(return_value=None)
#        litle.sendRequest(token)
#        
#        comm.http_post.assert_called_once()
#        match_re = RegexMatcher(".*?<litleOnlineRequest.*?<registerTokenRequest.*?<accountNumber>1233456789103801</accountNumber>.*?</registerTokenRequest>.*?")
#        comm.http_post.assert_called_with(match_re,url=ANY,proxy=ANY,timeout=ANY)

#    def test_defaultreportgroup(self):
#        auth = litleXmlFields.authorization()
#        auth.orderId = "12344"
#        auth.amount = 106
#        auth.orderSource = 'ecommerce'
#        
#        card = litleXmlFields.cardType()
#        card.type = 'VI'
#        card.number = "4100000000000002"
#        card.expDate = "1210"
#        auth.card = card
#        
#        # create mock communication
#        # set the communication to the mocked communication
#        
#        # get an auth  response from sending auth
#        litleXml =  litleOnlineRequest(config)
#        
#        authResponse = litleXml.sendRequest(auth)
#        assertEquals("Default Report Group", authResponse.transactionResponse.reportGroup)
