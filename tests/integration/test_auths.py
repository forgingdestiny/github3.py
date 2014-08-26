"""Integration tests for the github3.auths module."""
import github3

from .helper import IntegrationHelper


class TestAuthorization(IntegrationHelper):

    """Integration tests for the Authorization class."""

    def test_add_scopes(self):
        """Test the ability to add scopes to an authorization."""
        self.basic_login()
        cassette_name = self.cassette_name('add_scopes')
        with self.recorder.use_cassette(cassette_name):
            auth = self.gh.authorization(10716101)
            assert isinstance(auth, github3.auths.Authorization)
            assert auth.add_scopes(['user']) is True