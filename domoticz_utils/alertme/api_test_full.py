#!/usr/bin/python
import sys
import time
from webapi import *

# Usage is: <username> <password>

# Copyright 9 June 2008 AlertMe.com    All rights reserved


# Note that in most of this code the values are not displayed herein but we instead rely upon the 
# WebAPIClient class's built-in debugging to tell us what is going on.



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

		# Fetch the main event log
		webapi.get_event_log("null", 4, "null", "null")
		
		webapi.get_user_info()
	
		hubIds = webapi.get_all_hubs()
	 	
		# Lets just operate on the first hub returned by getAllHubs.
		hubId = hubIds.split(",")[0].split("|")[1] 

		webapi.set_hub(hubId)
	
		webapi.get_hub_status()

		webapi.get_all_behaviours()

		webapi.get_behaviour()
	
		services = webapi.get_all_services()

		for service in services.split(","):
			webapi.get_all_service_states(service)

		for service in services.split(","):
			webapi.get_current_service_state(service)

		devices = webapi.get_all_devices()

		for device in devices.split(","):
			zigbeeId = device.split("|")[1]	
			try:
				webapi.get_device_details(zigbeeId)
			# In this situation this is an anticiapted error so don't exit if we get it!
			except WebAPIClient.ExceptionNeedsHubUpgrade: 
					print "   webapi.getDeviceDetails(" , zigbeeId, ")"
					print "      needs_hub_upgrade"		
			
		for device in devices.split(","):
			channels = webapi.get_all_device_channels(zigbeeId)
			for channel in channels.split(","):
				try:
					webapi.get_device_channel_value(zigbeeId, channel)
				# In this situation this is an anticiapted error so don't exit if we get it!
				except WebAPIClient.ExceptionDeviceNotPresent: 
					print "   webapi.getDeviceChannelValue(" , zigbeeId, "," , channel , ")"
					print "      device_not_present"		

			# Also test fetching all of the details at once (this is faster if more than one item is needed
			# and it will not return a device_not_present exception). Although all fields may be returned
			# for all devices you should only rely upon those detailed in getAllDeviceChannels for the 
			# device concerned as some hardware cannot reliably return certain values. Eg. The lamp 
			# temerature is excessively affected by the lamp's brightness.
			webapi.get_device_channel_value(zigbeeId)

		# Fetch logs for each device's channels
		for device in devices.split(","):
			channels = webapi.get_all_device_channels(zigbeeId)
			for channel in channels.split(","):
				webapi.get_device_channel_log(zigbeeId, channel, 4, "null", "null")

		# Fetch the main event log
		webapi.get_event_log("null", 4, "null", "null")
		
		webapi.logout()
	
		# Send an arm command
		webapi.send_command("IntruderAlarm", "arm")
	
		# Don't do anything for 60 seconds
		time.sleep (60)
		
		# Send an arm command
		webapi.send_command("IntruderAlarm", "disarm")

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

	except WebAPIClient.ExceptionInvalidUserDetails:
		print "The login details provided are incorrect"

	except WebAPIClient.ExceptionAccountLocked:
		print "This account has been locked due to too many failed login attempts"
