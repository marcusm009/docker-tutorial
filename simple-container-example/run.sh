docker pull nginx
docker run --name nginx -p 8080:80 -v .:/usr/share/nginx/html:ro -d nginx
xdg-open http://localhost:8080/