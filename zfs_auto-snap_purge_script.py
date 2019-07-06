#!/usr/bin/env python3

#The script is intended to be run as a cron-job 
#and output should be sent to log-file, 
#i.e. zfs_auto-snap_purge_script >> /var/log/zfs_purge.log

import os
import datetime

#Establish current time and date and print
now = datetime.datetime.now()
print(now)

#Function that fetches current snapshots into a list
def fetch(grepfor):
        fetch_list = os.popen('zfs list -t snapshot | grep ' + grepfor).read().split("\n")
        return_list = [n.split()[0] for n in fetch_list[:-1]]
        return return_list

#Function to parse strings so time can be evaluated
def time_test(passed_string, opt_val):
        join_string = " ".join(passed_string.split("-")[3:])
        string_date = datetime.datetime.strptime(join_string, '%Y %m %d %H%M')
        timediff = now - string_date
        seconds = timediff.total_seconds()
        hours = seconds/3600
        days = hours/24
        weeks = days/7

        #Test optional value to see what value to return
        if opt_val == 1:
                return hours
        elif opt_val == 2:
                return days
        elif opt_val == 3 or opt_val == 4:
                return weeks

#Function that evaluates age of snapshots and destroys snapshots that are too old
def destroy(inputlist,test_val,max_val):
        #Test to see if list are empty. Empty lists means no snapshot of that policy exists.
        if len(inputlist) != 0:
                for snap in inputlist:
                        if time_test(snap, test_val) >= max_val:
                                print("Snapshot {snap} will be destroyed".format(snap=snap))
                                #### Destroy snapshot ####
                                os.system('zfs destroy ' + snap)
                                
        else:
                if test_val == 1:
                        print("\nNo hourly snapshots found.\n")
                elif test_val == 2:
                        print("\nNo daily snapshots found.\n")
                elif test_val == 3:
                        print("\nNo weekly snapshots found.\n")
                elif test_val == 4:
                        print("\nNo monthly snapshots found.\n")

#Calls fetch-function
hourly_list = fetch("hourly")
daily_list = fetch("daily")
weekly_list = fetch("weekly")
monthly_list = fetch("monthly")

#Calls destroy-function
destroy(hourly_list, 1, 24)
destroy(daily_list, 2, 7)
destroy(weekly_list, 3, 4)
destroy(monthly_list, 4, 52)

#Print out
print("\n##### Purge complete! #####")
