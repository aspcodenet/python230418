from price import calculatePrice
import unittest 
from unittest.mock import Mock,patch
import datetime
from userregistration import UserRegistrationService


class userrtests(unittest.TestCase):
    def test_sendmail_called(self):
        sut = UserRegistrationService()
        with patch('smtplib.SMTP', autospec=True) as mock_smtp:       
            sut.Register("stefan@aaa.se", "Stefan")

            mock_smtp.assert_called()

            context = mock_smtp.return_value.__enter__.return_value
            context.ehlo.assert_called()
            context.starttls.assert_called()
            context.login.assert_called()             

unittest.main()