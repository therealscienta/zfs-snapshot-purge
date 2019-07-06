# zfs
zfs purging script

Syncing ZFS snapshots with Syncoid creates endless snapshots on target system and the 
purpose of this script is to purge old snapshots. The script is intended to be run as 
a cron-job and output should be sent to log-file.

Create and move script to directory:
>mkdir /var/script

>mv zfs_auto-snap_purge_script.py /var/script

>chmod +x zfs_auto-snap_purge_script.py

Edit crontab via:
>crontab -e

Add (will run script at 1am, can be changed to user preference):
>0 1 * * * /var/script/zfs_auto-snap_purge_script.py >> /var/log/zfs_purge.log
