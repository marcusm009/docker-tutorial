# Simple Container Example

This project shows how you can use an nginx container and a bind mount to host local files.

To get started, simply run either `run.ps1` or `run.sh`, dependending on your platform. This script will run the following commands:

1. `docker pull nginx` - This will pull down an image called `nginx` hosted on the docker.io registry. This image contains a basic web server for hosting files.
2. `docker run --name nginx -p 8080:80 -v .:/usr/share/nginx/html:ro -d nginx` - This command will create a container from the nginx image, forward port 8080 (outside the container) to port 80 (within the container). It will also create a bind mount from the current directory (outside the container) to `/usr/share/nginx/html` (within the container). This will cause the `index.html` file to be served when you go to <http://localhost:8080> in a web browser.
3. Opens a web browser to the aforementioned link

After the container is running, try changing the text in index.html and reload the page to see the changes happening in real time.