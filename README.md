# ip_webpage

Docker based system to show all the ip numbers assigned by an Apple Time Capsule, and their ongoing ping status.
The exported `Time Capsule.baseconfig` file is exported into the `/app` folder.

When the server first loads, it reads the file and creates an export with just the IP registrations.
It then uses the file to build a webpage that can be updated by web sockets.

The client also uses the export file, pinging each entry in turn and posting the resolt to the website.

# setup

Clone the repo to your docker host

  `git clone https://github.com/sfduff/ip_webpage.git'`

Navigate into the new folder `/ip_webpage` and build the containers


  `cd ip_webpage
  docker-compose build`
  
and launch.

  `docker-compose up -d`
