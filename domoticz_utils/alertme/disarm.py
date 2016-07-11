#!/usr/bin/python
import sys
import time
from webapi import *

# Usage is: <username> <password>

# Copyright 9 June 2008 AlertMe.com    All rights reserved


# Note that in most of this code the values are not displayed herein but we instead rely upon the 
# WebAPIClient classes built-in debugging to tell us what is going on.



# This is where the code starts executing. 
if __name__=="__main__":
	try:
		if ( len(sys.argv) != 3 ):
			print "usage: " , sys.argv[0], " <username> <password>"
			sys.exit (-1);


		# Most people will not want to pass any arguments to this constructor as by default
		# the web api talks to AlertMe's live servers anyway.
		webapi = WebAPIClient()

		webapi.verbose = 1      # 0 = print no result details
					# 1 = print results in a formatted fashion

		webapi.trace =   0      # 0 = print no tracing details
					# 1 = print details of each call and response

		username = sys.argv[1]        # The arguments specified on the command line!
		password = sys.argv[2]
		appname = "python_api_test"   # Note that only alphabetic characters and _ are permitted here.
	
		webapi.login( username, password, appname )

		# Send a disarm command
		webapi.send_command("IntruderAlarm", "disarm")
		
		# Note that this is not guaranteed to work and it is advisable to poll the behaviour at this point
		# to check that the command was acted upon by the hub. (Eg. if the hub is not connected to the Internet.)

	except WebAPIClient.ExceptionProtocolError:
		print "The API server could not be contacted correctly"

	except WebAPIClient.ExceptionNoSession:
		print "A valid session must be established with login prior to making this call"

	except WebAPIClient.ExceptionInternalError:
		print "An internal error occured on the API server"

	except WebAPIClient.ExceptionInvalidArguments:
		print "Invalid arguments were provided to a call"

	except WebAPIClient.ExceptionServiceNotAvailableForLoginStatus:
		print "Service cannot be used without a sucessfull login first"

	except WebAPIClient.ExceptionNoHub:
		print "The logged in user doesn't have a hub installed"

	except WebAPIClient.ExceptionInvalidHubId:
		print "The Hub ID specified is not owned by this user"

	except WebAPIClient.ExceptionHubNotContactable:
		print "The hub is not currently attached to the AlertMe system"

	except WebAPIClient.ExceptionUnknownDevice:
		print "The deviceId provided is not known to this hub"

	except WebAPIClient.ExceptionNeedsHubUpgrade:
		print "The hub requires upgrading if you wish to use this functionality"

	except WebAPIClient.ExceptionDeviceNotPresent:
		print "The device specified is not currently attached to the hub"

	except WebAPIClient.ExceptionInvalidMethod:
		print "The method specified does not exist"

	except WebAPIClient.ExceptionInvalidUserDetails:
		print "The login details provided are incorrect"

	except WebAPIClient.ExceptionAccountLocked:
		print "This account has been locked due to too many failed login attempts"
