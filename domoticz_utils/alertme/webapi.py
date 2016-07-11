# Copyright 9 June 2008 AlertMe.com    All rights reserved

import xmlrpclib
import datetime
import logging

from errors import *

IA_STATE_HOME = "disarm"
IA_STATE_AWAY = "away"
IA_STATE_NIGHT = "night"


class WebAPIClient:
    sessionToken = ''
    xml_rpc = ''
    verbose = 0  # By default print nothing!
    trace = 0  # By default print nothing!

    # These are all of the errors that can be returned by the API. We want to raise them as exceptions
    errors = {
        "no_session": ExceptionNoSession(),
        "internal_error": ExceptionInternalError(),
        "invalid_arguments": ExceptionInvalidArguments(),
        "service_not_available_for_login_status": ExceptionServiceNotAvailableForLoginStatus(),
        "no_hub": ExceptionNoHub(),
        "invalid_hub_id": ExceptionInvalidHubId(),
        "hub_not_contactable": ExceptionHubNotContactable(),
        "unknown_device": ExceptionUnknownDevice(),
        "needs_hub_upgrade": ExceptionNeedsHubUpgrade(),
        "device_not_present": ExceptionDeviceNotPresent(),
        "invalid_method": ExceptionInvalidMethod(),
        "invalid_user_details": ExceptionInvalidUserDetails(),
        "invalid_user_identifier": ExceptionInvalidUserIdentifier(),
        "privileged_systems_only": ExceptionPrivileged(),
        "login_failed_account_locked": ExceptionAccountLocked(),
        "exists": ExceptionExists()
    }

    def __init__(self, url="https://api.alertme.com/webapi/v2"):
        """Most people will want to ignore the second parameter to this constructor. However some
        developers may be asked to use our test systems in which case an option may be provided
        to you by AlertMe engineers."""
        self.xml_rpc = xmlrpclib.ServerProxy(url, verbose=0)

    def login(self, username, password, appname):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> login( ", username, ", **********, ", appname, " )"

        self.sessionToken = self.xml_rpc.login(username, password, appname)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", self.sessionToken

        if self.sessionToken in self.errors:  # Did an error occur?
            raise self.errors[self.sessionToken]  # If so then raise an exception for it

    def logout(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> logout( ", self.sessionToken, ")"

        result = self.xml_rpc.logout(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        self.sessionToken = ''

    def get_user_info(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getUserInfo( ", self.sessionToken, ")"

        result = self.xml_rpc.getUserInfo(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getUserInfo:"
            for i in result.split(","):
                print "       ", i.split("|")[0], "=", i.split("|")[1]

        return result

    def get_all_hubs(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getAllHubs( ", self.sessionToken, ")"

        result = self.xml_rpc.getAllHubs(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getAllHubs:"
            for i in result.split(","):
                print "       ", i.split("|")[0], " (", i.split("|")[1], ")"

        return result

    def get_all_device_channel_values(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getAllDeviceChannelValues( ", self.sessionToken, ")"

        result = self.xml_rpc.getAllDeviceChannelValues(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getAllDeviceChannelValues:"
            print result;

        return result

    def set_hub(self, hubId):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> setHub( ", self.sessionToken, ",", hubId, ")"

        result = self.xml_rpc.setHub(self.sessionToken, hubId)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        return result

    def get_hub_status(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getHubStatus( ", self.sessionToken, ")"

        result = self.xml_rpc.getHubStatus(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getHubStatus:"
            for i in result.split(","):
                print "       ", i.split("|")[0], "=", i.split("|")[1]

        return result

    def get_all_behaviours(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getAllBehaviours( ", self.sessionToken, ")"

        result = self.xml_rpc.getAllBehaviours(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getAllBehaviours:"
            for i in result.split(","):
                print "       ", i

        return result

    def get_behaviour(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getBehaviour( ", self.sessionToken, ")"

        result = self.xml_rpc.getBehaviour(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getBehaviour:"
            print "       ", result

        return result

    def get_all_services(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getAllServices( ", self.sessionToken, ")"

        result = self.xml_rpc.getAllServices(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getAllServices:"
            for i in result.split(","):
                print "       ", i

        return result

    def get_all_service_states(self, service):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getAllServiceStates( ", self.sessionToken, ",", service, ")"

        result = self.xml_rpc.getAllServiceStates(self.sessionToken, service)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getAllServiceStates (", service, ")"
            for i in result.split(","):
                print "       ", i

        return result

    def get_current_service_state(self, service):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getCurrentServiceState( ", self.sessionToken, ",", service, ")"

        result = self.xml_rpc.getCurrentServiceState(self.sessionToken, service)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getCurrentServiceState (", service, ")"
            if service == "null":
                for i in result.split(","):
                    j = i.split("|")  # We are only interested in the part after the |
                    print "       ", j[1]
            else:
                print result

        return result

    def send_command(self, service, command):
        if self.trace > 0:
            print datetime.datetime.now(), "---> sendCommand ( ", self.sessionToken, ", ", service, ", ", command, ") "

        result = self.xml_rpc.sendCommand(self.sessionToken, service, command)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        return result;

    def get_all_devices(self):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getAllDevices( ", self.sessionToken, ")"

        result = self.xml_rpc.getAllDevices(self.sessionToken)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getAllDevices"
            print "      ZigbeeId\t\tType\t\tName"
            for i in result.split(","):
                j = i.split("|")
                print "       ", j[0], "\t", j[1], "\t", j[2]

        return result

    def get_device_details(self, device):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getDeviceDetails( ", self.sessionToken, ",", device, ")"

        result = self.xml_rpc.getDeviceDetails(self.sessionToken, device)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getDeviceDetails (", device, ")"
            for i in result.split(","):
                j = i.split("|")  # We are only interested in the part after the |
                print "       ", j[1]

        return result

    def get_all_device_channels(self, device):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getAllDeviceChannels( ", self.sessionToken, ",", device, ")"

        result = self.xml_rpc.getAllDeviceChannels(self.sessionToken, device)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getAllDeviceChannels (", device, ")"
            for i in result.split(","):
                print "       ", i

        return result

    def get_device_channel_value(self, device, channel=''):
        if channel == '':
            if self.trace > 0:
                print datetime.datetime.now(), " ---> getDeviceChannelValue( ", self.sessionToken, ",", device, ")"

            result = self.xml_rpc.getDeviceChannelValue(self.sessionToken, device)
        else:
            if self.trace > 0:
                print datetime.datetime.now(), " ---> getDeviceChannelValue( ", self.sessionToken, ",", device, ",", channel, ")"

            result = self.xml_rpc.getDeviceChannelValue(self.sessionToken, device, channel)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            if channel == '':
                print "   getDeviceChannelValue (", device, ")"
            else:
                print "   getDeviceChannelValue (", device, ",", channel, ")"

            print "       ", result

        return result

    def get_device_channel_log(self, device, channel, numEntries, start, end):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getDeviceChannelLog( ", self.sessionToken, ",", device, ",", channel, ",", numEntries, ",", start, ",", end, ")"

        result = self.xml_rpc.getDeviceChannelLog(self.sessionToken, device, channel, numEntries, start, end)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getDeviceChannelLog (", device, ",", channel, ",", numEntries, ",", start, ",", end, ")"
            for i in result.split(","):
                print "       ", i

        return result

    def get_event_log(self, service, numEntries, start, end, localiseTimes="false"):
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getEventLog( ", self.sessionToken, ",", service, ",", numEntries, ",", start, ",", end, ",", localiseTimes, ")"

        result = self.xml_rpc.getEventLog(self.sessionToken, service, numEntries, start, end, localiseTimes)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getEventLog (", service, ",", numEntries, ",", start, ",", end, ",", localiseTimes, ")"
            for i in result.split(","):
                print "       ", i

        return result

    def get_tracking_data(self, device, numEntries, start, end, localiseTimes="false"):
        """Note that this function is temporary and will be removed in the near future.
        It will return no data for most users."""
        if self.trace > 0:
            print datetime.datetime.now(), " ---> getTrackingData( ", self.sessionToken, ",", device, ",", numEntries, ",", start, ",", end, ",", localiseTimes, ")"

        result = self.xml_rpc.getTrackingData(self.sessionToken, device, numEntries, start, end, localiseTimes)

        if self.trace > 0:
            print datetime.datetime.now(), "Got back: ", result

        if result in self.errors:  # Did an error occur?
            raise self.errors[result]  # If so then raise an exception for it

        if self.verbose > 0:
            print "   getEventLog (", device, ",", numEntries, ",", start, ",", end, ",", localiseTimes, ")"
            for i in result.split(","):
                print "       ", i

        return result

    def set_intruder_alarm(self, new_state, skip_grace_period=False):
        logging.info("Setting IA to {state:s}".format(state=new_state))
        self.send_command("IntruderAlarm", new_state)
        if skip_grace_period:
            # Send the command again, in order to skip the grace period
            self.send_command("IntruderAlarm", new_state)
        logging.info("IA set to {state:s}".format(state=new_state))

    def disarm_intruder_alarm_home(self):
        self.set_intruder_alarm(IA_STATE_HOME)

    def arm_intruder_alarm_away(self, skip_grace_period=False):
        self.set_intruder_alarm(IA_STATE_AWAY, skip_grace_period)

    def arm_intruder_alarm_night(self, skip_grace_period=False):
        self.set_intruder_alarm(IA_STATE_NIGHT, skip_grace_period)
