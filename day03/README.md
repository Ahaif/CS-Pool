
- The goal of this project is to create a web page and make it accessible from the Tor network by creating a hidden service.
  
- Tor hidden service **allows users to publish their service without revealing their identity (IP address**
- Setup Tor hidden service with nginx
  - install Tor : sudo apt install tor 
    - modify torrc config file in /etc/tor/torrc
      - uncomment hidden service directory and port /var/lib/tor/hidden_service/
      - restart tor
      - sudo cat /var/lib/tor/hidden_service/hostname to show your .onion URL**
  - install nginx
    - modify .conf file in /etc/nginx/ 
    - add site.onion.conf to sites-available directory in nginx, make sure .conf file is linked with sites enabled
- restart services and you can access to default nginx page in [localhost:80](http://localhost:80) or
- custom web page when searching from tor browser

- this Project is for Educational Purpose
