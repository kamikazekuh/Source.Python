# ../listeners/__init__.py

"""Provides listener based functionality."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
#   Core
from core import AutoUnload
#   Loggers
from loggers import _sp_logger


# =============================================================================
# >> FORWARD IMPORTS
# =============================================================================
# Source.Python Imports
#   Listeners
from _listeners import client_active_listener_manager
from _listeners import client_connect_listener_manager
from _listeners import client_disconnect_listener_manager
from _listeners import client_fully_connect_listener_manager
from _listeners import client_put_in_server_listener_manager
from _listeners import client_settings_changed_listener_manager
from _listeners import level_init_listener_manager
from _listeners import level_shutdown_listener_manager
from _listeners import network_id_validated_listener_manager
from _listeners import on_edict_allocated_listener_manager
from _listeners import on_edict_free_listener_manager
from _listeners import on_query_cvar_value_finished_listener_manager
from _listeners import server_activate_listener_manager
from _listeners import tick_listener_manager


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = ('ClientActive',
           'client_active_listener_manager',
           'ClientConnect',
           'client_connect_listener_manager',
           'ClientDisconnect',
           'client_disconnect_listener_manager',
           'ClientFullyConnect',
           'client_fully_connect_listener_manager',
           'ClientPutInServer',
           'client_put_in_server_listener_manager',
           'ClientSettingsChanged',
           'client_settings_changed_listener_manager',
           'LevelInit',
           'level_init_listener_manager',
           'LevelShutdown',
           'level_shutdown_listener_manager',
           'NetworkidValidated',
           'network_id_validated_listener_manager',
           'OnEdictAllocated',
           'on_edict_allocated_listener_manager',
           'OnEdictFreed',
           'on_edict_free_listener_manager',
           'OnQueryCvarValueFinished',
           'on_query_cvar_value_finished_listener_manager',
           'ServerActivate',
           'server_activate_listener_manager',
           'Tick',
           'tick_listener_manager',
           )


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the sp.listeners logger
listeners_logger = _sp_logger.listeners


# =============================================================================
# >> CLASSES
# =============================================================================
class _ListenerManager(AutoUnload):

    """Base decorator class used to register/unregister a listener."""

    def __init__(self, callback):
        """Store the callback and register the listener."""
        # Log the <instance>.__init__ message
        listeners_logger.log_info(
            '{0}.__init__<{1}>'.format(self.name, callback))

        # Is the callback callable?
        if not callable(callback):

            # Raise an error
            raise TypeError(
                "'" + type(callback).__name__ + "'object is not callable")

        # Log the registering message
        listeners_logger.log_info(
            '{0}.__init__ - Registering'.format(self.name))

        # Store the callback
        self.callback = callback

        # Register the listener
        self.manager.register_listener(self.callback)

    def __call__(self, *args):
        """Call the listener."""
        # Log the calling
        listeners_logger.log_info(
            '{0}.__call__<{1}>'.format(self.name, args))

        # Call the listener
        return self.callback(*args)

    @property
    def name(self):
        """Return the class name of the instance."""
        return self.__class__.__name__

    def _unload_instance(self):
        """Unregister the listener."""
        # Log the unregistering
        listeners_logger.log_info(
            '{0}._unload_instance - Unregistering <{1}>'.format(
                self.name, self.callback))

        # Unregister the listener
        self.manager.unregister_listener(self.callback)


class ClientActive(_ListenerManager):

    """Register/unregister a ClientActive listener."""

    manager = client_active_listener_manager


class ClientConnect(_ListenerManager):

    """Register/unregister a ClientConnect listener."""

    manager = client_connect_listener_manager


class ClientDisconnect(_ListenerManager):

    """Register/unregister a ClientDisconnect listener."""

    manager = client_disconnect_listener_manager


class ClientFullyConnect(_ListenerManager):

    """Register/unregister a ClientFullyConnect listener."""

    manager = client_fully_connect_listener_manager


class ClientPutInServer(_ListenerManager):

    """Register/unregister a ClientPutInServer listener."""

    manager = client_put_in_server_listener_manager


class ClientSettingsChanged(_ListenerManager):

    """Register/unregister a ClientSettingsChanged listener."""

    manager = client_settings_changed_listener_manager


class LevelInit(_ListenerManager):

    """Register/unregister a LevelInit listener."""

    manager = level_init_listener_manager


class LevelShutdown(_ListenerManager):

    """Register/unregister a LevelShutdown listener."""

    manager = level_shutdown_listener_manager


class NetworkidValidated(_ListenerManager):

    """Register/unregister a NetworkidValidated listener."""

    manager = network_id_validated_listener_manager


class OnEdictAllocated(_ListenerManager):

    """Register/unregister an OnEdictAllocated listener."""

    manager = on_edict_allocated_listener_manager


class OnEdictFreed(_ListenerManager):

    """Register/unregister an OnEdictFreed listener."""

    manager = on_edict_free_listener_manager


class OnQueryCvarValueFinished(_ListenerManager):

    """Register/unregister an OnQueryCvarValueFinished listener."""

    manager = on_query_cvar_value_finished_listener_manager


class ServerActivate(_ListenerManager):

    """Register/unregister a ServerActivate listener."""

    manager = server_activate_listener_manager


class Tick(_ListenerManager):

    """Register/unregister a Tick listener."""

    manager = tick_listener_manager