# Microservices Example

This project shows how you can use `docker compose` to create three distinct docker containers that can communicate with one another in a local network.

## Running

To run this entire microservices stack, run the following command from the same directory as this README:

```bash
docker compose up --build
```

This will build three distinct containers, as detailed in the `docker-compose.yml` file. They are:

* **flask-app**: A simple Python Flask application to act as the main microservice that will communicate with the ASP.NET Core application and the Mongo database.
* **mongo-db**: A simple Mongo Database. This database makes use of a volume to keep its data persistant.
* **aspnet-app**: An example ASP.NET Core 7 app that is automatically generated via the `dotnet new webapi` command within the Dockerfile. `flask-app` will make a request to the `WeatherForecast` controller to show how services can communicate within a Docker network.

In addition to building those containers, Docker compose will also build a volume named `mongo-data` and a network named `microservices`.

## Testing

### Test Microservices

1. To test this newly created microservices stack, go to <http://localhost:8000/swagger> to see the Swagger page for `aspnet-app`, and then go to <http://localhost:5000/swagger> to see the Swagger page for `flask-app`.
2. Make a request to `aspnet-app` using the Swagger UI to see the weather response.
3. Make a GET request to the `/users` endpoint in `flask-app` using Swagger UI to see how the flask app is able to aggregate mongo data, as well as data from `aspnet-app`.
4. Make a POST request to the `/add` endpoint in `flask-app` using Swagger UI to add a user. Then make another GET request to `/users` to see this new data.

### Observe Data Persistence

1. Stop the three running containers and delete them.
2. Run `docker compose up --build` again to rebuild all the apps.
3. Make a GET request to `http://localhost:8000/users` to see how the data persisted due to the volume that the mongo container uses.

### Connect to Mongo

1. Run `docker ps` to see the running containers.
2. Run `docker exec -it <container_id> mongosh` to run an interactive mongo shell against the running mongo container.
3. Run `use mydatabase` to switch to the database used by `flask-app`.
4. Run `db.users.find()` to show the current state of the database.
5. Run `db.users.deleteOne({email: 'john@example.com'})` to delete one of the documents inserted via `flask-app`.
6. Make a GET request to `http://localhost:8000/users` to see how the data was deleted via the mongo shell.

## Other Considerations

To see how environments are handled in docker compose, take a look at the `.env[.ENV]` files. These files contain variables that can be substituted in the `docker-compose.yml` file.

To run the "prod" version of this microservices tutorial, you can run `docker compose --env-file .env.prod up --build`. The only difference is that the swagger page won't show up.