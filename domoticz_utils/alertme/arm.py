#!/usr/bin/python
import sys

import time

from webapi import *
from errors import AlertMeException

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

    try:
        if len(sys.argv) != 3:
            print "usage: ", sys.argv[0], " <username> <password>"
            sys.exit(-1)

        # Most people will not want to pass any arguments to this constructor as by default
        # the web api talks to AlertMe's live servers anyway.
        web_api = WebAPIClient()

        web_api.verbose = 1  # 0 = print no result details
        # 1 = print results in a formatted fashion

        web_api.trace = 0  # 0 = print no tracing details
        # 1 = print details of each call and response

        username = sys.argv[1]  # The arguments specified on the command line!
        password = sys.argv[2]
        appname = "python_api_test"  # Note that only alphabetic characters and _ are permitted here.

        web_api.login(username, password, appname)
        web_api.disarm_intruder_alarm_home()
        time.sleep(30)
        web_api.arm_intruder_alarm_away()

        # Send an arm command
        web_api.send_command("IntruderAlarm", "arm")

    except AlertMeException as error:
        print error

    # except WebAPIClient.ExceptionProtocolError:
    #     print "The API server could not be contacted correctly"
    #
    # except WebAPIClient.ExceptionNoSession:
    #     print "A valid session must be established with login prior to making this call"
    #
    # except WebAPIClient.ExceptionInternalError:
    #     print "An internal error occured on the API server"
    #
    # except WebAPIClient.ExceptionInvalidArguments:
    #     print "Invalid arguments were provided to a call"
    #
    # except WebAPIClient.ExceptionServiceNotAvailableForLoginStatus:
    #     print "Service cannot be used without a sucessfull login first"
    #
    # except WebAPIClient.ExceptionNoHub:
    #     print "The logged in user doesn't have a hub installed"
    #
    # except WebAPIClient.ExceptionInvalidHubId:
    #     print "The Hub ID specified is not owned by this user"
    #
    # except WebAPIClient.ExceptionHubNotContactable:
    #     print "The hub is not currently attached to the AlertMe system"
    #
    # except WebAPIClient.ExceptionUnknownDevice:
    #     print "The deviceId provided is not known to this hub"
    #
    # except WebAPIClient.ExceptionNeedsHubUpgrade:
    #     print "The hub requires upgrading if you wish to use this functionality"
    #
    # except WebAPIClient.ExceptionDeviceNotPresent:
    #     print "The device specified is not currently attached to the hub"
    #
    # except WebAPIClient.ExceptionInvalidMethod:
    #     print "The method specified does not exist"
    #
    # except WebAPIClient.ExceptionInvalidUserDetails:
    #     print "The login details provided are incorrect"
    #
    # except WebAPIClient.ExceptionAccountLocked:
    #     print "This account has been locked due to too many failed login attempts"
