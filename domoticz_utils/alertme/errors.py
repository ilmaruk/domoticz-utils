# -*- coding: utf-8 -*-


class AlertMeException(Exception):
    """Base class for exceptions in this module."""
    pass


class ExceptionProtocolError(AlertMeException):
    """The API server could not be contacted correctly"""
    pass


class ExceptionNoSession(AlertMeException):
    """A valid session must be established with login prior to making this call"""
    pass


class ExceptionInternalError(AlertMeException):
    """An internal error occured on the API server"""
    pass


class ExceptionInvalidArguments(AlertMeException):
    """Invalid arguments were provided to a call"""
    pass


class ExceptionServiceNotAvailableForLoginStatus(AlertMeException):
    """Service cannot be used without a sucessfull login first"""
    pass


class ExceptionNoHub(AlertMeException):
    """The logged in user doesn't have a hub installed"""
    pass


class ExceptionInvalidHubId(AlertMeException):
    """The Hub ID specified is not owned by this user"""
    pass


class ExceptionHubNotContactable(AlertMeException):
    """The hub is not currently attached to the AlertMe system"""
    pass


class ExceptionUnknownDevice(AlertMeException):
    """The deviceId provided is not known to this hub"""
    pass


class ExceptionNeedsHubUpgrade(AlertMeException):
    """The hub requires upgrading if you wish to use this functionality"""
    pass


class ExceptionDeviceNotPresent(AlertMeException):
    """The device specified is not currently attached to the hub"""
    pass


class ExceptionInvalidMethod(AlertMeException):
    """The method specified does not exist"""
    pass


class ExceptionInvalidUserDetails(AlertMeException):
    """The login details provided are incorrect"""
    pass


class ExceptionInvalidUserIdentifier(AlertMeException):
    """The user specified does not exist"""
    pass


class ExceptionPrivileged(AlertMeException):
    """This function may only be called by privilidged systems"""
    pass


class ExceptionAccountLocked(AlertMeException):
    """This account has been locked due to too many failed login attempts"""
    pass


class ExceptionProtocolError(AlertMeException):
    """We didn't understand what we got back!"""
    pass


class ExceptionUnknownError(AlertMeException):
    """An unknown error has occured"""
    pass


class ExceptionExists(AlertMeException):
    """The specified item already exists"""
    pass
