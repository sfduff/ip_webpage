# ip_webpage

Docker based system to show all the ip numbers assigned by an Apple Time Capsule, and their ongoing ping status.
The exported `Time Capsule.baseconfig` file is exported into the `/app` folder.

When the server first loads, it reads the file and creates an export with just the IP registrations.
It then uses the file to build a webpage that can be updated by web sockets.

The client also uses the export file, pinging each entry in turn and posting the result to the website.

# setup

Clone the repo to your docker host
  ```
  git clone https://github.com/sfduff/ip_webpage.git
  ```
Navigate into the new folder `/ip_webpage` and build the containers
  ```
  cd ip_webpage
  ```
  ```
  docker-compose build
  ```
and launch.
```
  docker-compose up -d
```

# exporting router file

On a host Apple Mac open the AirPort Utility, and export the configuration file to the repo folder on the docker host.  AirPort will remember the files save location.

Run `router_export.workflow` using Apple Automator to automate the process.

# scheduling the export

- In Automator, create a Calendar Alarm
- Select Utilities from the library pane
- Select & drag Run AppleScript into the workflow area
- Copy/paste the AppleScript into the Run AppleScript box
- Save the newly created Calendar Alarm
- On save it will immediately be added to your calendar
- Change the schedule and recurrence as desired.
