# Logs Analysis

A reporting tool that prints out reports (_in plain text_) based on data loaded to a **PostgreSQL** database running in an Ubuntu image via a **Virtual Machine** installed on a laptop.

The tool will connect to the data base, execute three queries and print the results.

## Questions Answered
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

If using Vagrant/VirtualBox, how to set it up.
A link to the newsdata.sql file so the user can import it into the database
How to import the data into the database.


## Dependencies

This project was done on Mac OS using the following:
- OS X Terminal
- Vagrant (v2.2.3)/VirtualBox (v5.2.4)
  - If you don't have VirtualBox, get it [here](https://www.virtualbox.org/wiki/Downloads). Install the *platform package* for your operating system. You do not need the extension pack or the SDK.
  - If you don't have Vagrant, get it [here](https://www.vagrantup.com/downloads.html). Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem; install the version for your operating system.


Use Github to clone or download this [repository](https://github.com/udacity/fullstack-nanodegree-vm).  This repository contains the Vagrantfile that provides (defines) the environment used by this project.

From a terminal, `cd` to the directory where your cloned or downloaded the Vagrantfile.  Then `cd vagrant` to change to the vagrant directory. Using `ls`, you should now see the Vagrantfile. You are now ready to launch the Ubuntu image.

#### Launch Ubuntu image
- `vagrant up`  - to download (first time only) and start the VM
- `vagrant ssh` - to access the VM
- `cd /vagrant` - to access the volume mount that is shared with the host (same host location where you executed `vagrant up`)

#### Prepare PostgreSQL
Get database, table definitions and table data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  Download to the shared directory (same host location where you executed `vagrant up`)

To load the data from within the VM, `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

Now you are ready to run the log analysis program.

## Usage

##### Command Line

```
python3 log_analysis.py
```

