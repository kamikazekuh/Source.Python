# ../auth/base.py

"""Provides a base Authorization class."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
#   Auth
from auth import AuthLogger
from auth import _auth_strings


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = ('AuthBase',
           )


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get sp.auth.base logger
AuthBaseLogger = AuthLogger.base


# =============================================================================
# >> CLASSES
# =============================================================================
class AuthBase(object):

    """A basic Auth Service class to be inherited by other Auth services."""

    def load(self):
        """Base implementation of load that if called will print an error."""
        AuthBaseLogger.log_warning(
            '[SP Auth] ' + _auth_strings['Not Implemented'].get_string(
                classname=self.__class__.__name__, method='load'))

    def unload(self):
        """Base implementation of unload that if called will print an error."""
        AuthBaseLogger.log_warning(
            '[SP Auth] ' + _auth_strings['Not Implemented'].get_string(
                classname=self.__class__.__name__, method='unload'))

    def is_player_authorized(self, *args):
        """Base implementation of is_player_authorized.

        If base method is called, it will print an error.
        """
        AuthBaseLogger.log_warning(
            '[SP Auth] ' + _auth_strings['Not Implemented'].get_string(
                classname=self.__class__.__name__,
                method='is_player_authorized'))
