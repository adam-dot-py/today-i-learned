# Key Linux Commands

Here is a selection of key command-line actions under Linux that can help you manage files, directories, processes, and system information effectively

## File and Directory Management

1. List all files and directories

```
ls -l
```

2. Change directory

```
cd /path/to/directory
```

3. Create a directory

```
mkdir new_directory
```

4. Remove a directory

This will only work if the directory is empty

```
rmdir directory_name
```

To remove a directory containing files

```
rm -r path/to/directory
```

5. Copy a file

```
cp source_file destination_file
```

6. Move or rename a file

```
mv old_name new_name
```

7. Delete a file

```
rm filename
```

8. View file contents

```
cat filename
```

9. Edit a file with `nano`

```
nano filename
```

10. Find files and directories

```
find /path -name filename
```

## System Information

1. Display current directory

```
pwd
```

2. Display disk usage

```
df -h
```

3. Display free and used memory

```
free -h
```

4. Display system information

```
uname -a
```

5. Show running processes

```
ps aux
```

6. Show system uptime and load

```
uptime
```

7. Display network configuration

```
ifconfig
```

## Process Management

1. Kill a process by PID

```
kill PID
```

2. Kill a process by name

```
kill process_name
```

3. Monitor live system processes

```
top
```

## File Permissions and Ownership

1. Change file permissions

```
chmod 755 filename
```

2. Change file ownership 

```
chown user:group filename
```

## Networking

1. Check connectivity to host

```
ping hostname
```

2. Download files from the internet

```
wget URL
```

3. Securely transfer files to a remote host

```
scp local_file user@remote_host:/path/to/destination
```

4. Secure shell into a remote host

```
ssh user@remote_host
```

## Package Management (Debian-based systems)

1. Update package list:

```
sudo apt update
```

2. Upgrade all packages

```
sudo apt upgrade
```

3. Install a package


```
sudo apt install package_name
```

4. Remove a package

```
sudo apt remove package_name
```

## System Monitoring and Logs

1. View system logs

```
tail -f /var/log/syslog
```




