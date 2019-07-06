# zfs
zfs purging script

The script is intended to be run as a cron-job and output should be sent to log-file.

Create and move script to directory:
>mkdir /var/script
>mv zfs_auto-snap_purge_script.py /var/script

Edit crontab via:
>crontab -e

Add (will run script at 1am, can be changed to user preference):
0 1 * * * zfs_auto-snap_purge_script >> /var/log/zfs_purge.log
