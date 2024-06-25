## issue summary
From 10:12 PM to 10:17 PM, all attempt to test the apache2 server by running a docker container which contains the text "Hello Holberton" was not successful. The test was done using the `curl` command to curl the port mapped to the docker container and it came back with the following response `curl: (56) Recv failure: Connection reset by peer` which is not the intended response.

## Timeline (all times Pacific Time)
- 10:10 PM: Start docker container with the command `docker run -p 8080:80 -d -it holbertonschool/265-0`
- 10:12 PM: Ran the command `curl 0:8080`
- 10:12 PM: Beginning of error response from the above command `curl: (56) Recv failure: Connection reset by peer`
- 10:15 PM: Check status of the apache2 server
- 10: 17 PM: Got intended response `Hello Holberton`

## Root Cause
The root cause of the problem from the docker container was as a result of the current status of the apache2 server. The server, which is available in the system, was not running. This caused the curl command to respond with the error message mentioned earlier. I was able to detect this by running the following command `server status apache2`. To fix this issue, I wrote a script to start the apache2 server.

## Corrective and Preventative Measures
To prevent this issue from reoccuring, I wrote a bash script that checks the status of the apache2 server and start it if the service is not running
