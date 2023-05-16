import unittest 
from unittest.mock import Mock,patch
import datetime
from userRegistration import UserRegistrationService


class userrtests(unittest.TestCase):
    def test_when_registering_ok_email_should_be_sent(self):
        # System UNDER TEST
        sut = UserRegistrationService()
        sut.Users.clear()

        with patch('smtplib.SMTP', autospec=True) as mock_smtp:       
            sut.Register("stefan@aaa.se", "Stefan")
            # mock_smtp.assert_called()
            context = mock_smtp.return_value.__enter__.return_value
            context.server.sendmail.assert_called()
            # context.ehlo.assert_called()
            # context.starttls.assert_called()
            # context.login.assert_called()             

unittest.main()


