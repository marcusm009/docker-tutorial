# Docker Tutorial

Docker is an open-source platform that automates the deployment, scaling, and management of applications. It uses containerization to package up an application with all of its dependencies into a standardized unit for software development.

This tutorial will cover the basics of Docker including installation, Dockerfiles, Docker images, Docker containers, Docker Compose, and some useful Docker commands. By the end of this tutorial, you'll have a good grasp of Docker basics.

## Table of Contents

* [Benefits of Using Docker](#benefits-of-using-docker)
* [Docker Architecture](#docker-architecture)
* [Installing Docker](#installing-docker)
  * [Windows and macOS](#windows-and-macos)
  * [Linux (Ubuntu as an example)](#linux-ubuntu-as-an-example)
* [Docker Images](#docker-images)
  * [Pulling a Docker Image](#pulling-a-docker-image)
  * [Listing Docker Images](#listing-docker-images)
* [Docker Containers](#docker-containers)
  * [Running a Docker Container](#running-a-docker-container)
    * [Important Options With `docker run`](#important-options-with-docker-run)
  * [Listing Docker Containers](#listing-docker-containers)
* [Dockerfile](#dockerfile)
  * [Important Dockerfile Commands](#important-dockerfile-commands)
* [Docker Compose](#docker-compose)
* [Docker Command Cheat Sheet](#docker-command-cheat-sheet)
  * [Docker Images](#docker-images-1)
  * [Docker Containers](#docker-containers-1)
  * [Docker Compose](#docker-compose-1)
  * [Docker System](#docker-system)
  * [Other Commands](#other-commands)
* [Conclusion and Next Steps](#conclusion-and-next-steps)
  * [Examples](#examples)

## Benefits of Using Docker

Docker has become popular due to the many benefits it provides for both developers and system administrators. Here are a few key advantages of using Docker:

* **Portability:** Docker ensures your applications will run on any machine that Docker can be installed on, without worrying about specific system requirements.

* **Microservices Architecture:** Docker is naturally suited for microservices architecture. Each microservice can be placed into its own container, making it easy to manage individual services independently.

* **Efficient Use of System Resources:** Docker containers are lightweight as they run directly on the host machine's kernel, meaning there's no need for a hypervisor and each container does not need a full OS installed.

* **Consistency and Reproducibility:** Since Docker images are snapshots containing everything needed to run an application, you can be confident that your application will run the same way, every time, everywhere.

* **Isolation:** Docker ensures your applications are isolated and secure. They have their own set of resources and cannot interfere with each other.

* **Integration and Deployment:** Docker works well with various tools for continuous integration and continuous deployment (CI/CD), such as Jenkins, Travis CI, and many more.

## Docker Architecture

Understanding Docker's architecture helps you to know how Docker works under the hood. The Docker architecture consists of several components including:

* **Docker Engine:** This is the runtime that runs and manages the containers. It is installed on the host machine.

* **Docker Images:** These are the read-only templates used to create containers. They contain everything an application needs to run.

* **Docker Containers:** These are the running instances of Docker images. Containers can be created, started, stopped, moved, and deleted. Each container is isolated and secure.

* **Dockerfile:** These are the scripts consisting of various commands that are executed sequentially to create a Docker image.

* **Docker Compose:** This is a tool used for defining and managing multi-container Docker applications.

* **Docker Hub/Registry:** This is a registry of Docker images. You can think of it like a repository of various Docker images that can be used to create containers. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default.

The workflow in Docker involves creating a Dockerfile, building an image from it, and then running a container from that image. Docker Compose can be used to manage an application with multiple services.

Here is a visual representation of Docker's architecture:

```
[Dockerfile] --(docker build)--> [Image] --(docker run)--> [Container]
```

Each layer in an image represents a Dockerfile instruction. The layers are stacked and each one is a delta of the changes from the previous layer.

## Installing Docker

Before you can start using Docker, you need to install it on your system. Docker is available for Linux, macOS, and Windows. Here's how to install Docker on each system:

### Windows and macOS

* Visit Docker's [official website](https://www.docker.com/products/docker-desktop) and download Docker Desktop for your operating system. Follow the installation instructions.

### Linux (Ubuntu as an example)

* Update your local database of software to make sure you've got access to the latest revisions.

    ```bash
    sudo apt-get update
    ```

* Install Docker.

    ```bash
    sudo apt-get install docker.io
    ```

* Verify the installation.

    ```bash
    docker --version
    ```

## Docker Images

A Docker image is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

### Pulling a Docker Image

To download a Docker image from Docker Hub, use the `docker pull` command followed by the image name.

```bash
docker pull nginx
```

### Listing Docker Images

To list all downloaded Docker images, use the `docker images` command.

```bash
docker images
```

## Docker Containers

A Docker container is a runtime instance of a Docker image. A container is defined by its image and any configuration options you provide to it when you create or start it.

### Running a Docker Container

To run a Docker container, use the docker run command followed by the image name.

```bash
docker run nginx
```

#### Important Options With `docker run`

* `-d`, `--detach`: This option runs the container in the background and returns the container ID. If you don't use this option, your terminal will attach to the container's standard output and you won't be able to use the terminal until you stop the container.

* `-i`, `--interactive`: This option keeps STDIN open, even if not attached. This can be useful if you want to provide input to the container at some point.

* `-t`, `--tty`: This option allocates a pseudo-TTY. This is generally used in combination with -i to provide an interactive shell.

* `-p`, `--publish`: This option binds a container's port to a host port so that the application inside the container can be accessed from outside the Docker host. The syntax is -p host_port:container_port.

* `--name`: This option lets you assign a name to the container, which can be useful for identifying and managing containers.

* `-v`, `--volume`: This option lets you mount host directories or volumes into the container. This is useful for data persistence or sharing data between the host and the container.

* `-e`, `--env`: This option lets you set environment variables in the container. This can be useful for configuring the application inside the container.

* `--rm`: This option automatically removes the container when it exits. This can be useful for cleanup, especially during development when you might be creating and destroying containers frequently.

* `--restart`: This option sets a restart policy for how to handle container exits. The options are no, on-failure[:max-retries], always, unless-stopped.

* `--network`: This option connects a container to a network. You can use it to connect to the default network, a user-defined network, or even disable networking.

Here is an example of how to use some of these options together:

```bash
docker run -d --name my_container -p 8080:80 -v /host/data:/container/data -e MY_ENV_VAR=my_value --restart always my_image
```

This command will start a new container named "my_container" in detached mode. It will expose the container's port 80 on the host's port 8080. It mounts the host directory /host/data into the container at /container/data. It sets an environment variable MY_ENV_VAR with the value my_value. The container will always restart if it stops. The Docker image it's based on is my_image.

### Listing Docker Containers

To list all running Docker containers, use the docker `ps command`. To also show stopped containers, add the `-a` flag.

```bash
docker ps -a
```

## Dockerfile

A Dockerfile is a text document that contains all the commands a user could call on the command line to **assemble an image**. It's essentially the blueprint for building Docker images.

Dockerfiles generally have the filename `Dockerfile` (with no extension). Occasionally, you will see something like `Dockerfile.dev` to denote a particular enviornment. When they are named `Dockerfile`, you are able to run `docker build` within the directly, and it will automatically be detected.

Here's what Dockerfiles generally look like:

```dockerfile
FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
```

To build a Docker image from this Dockerfile, navigate to the directory containing the Dockerfile and run the docker build command.

```
docker build -t my-python-app .
```

### Important Dockerfile Commands

* `FROM` - This command sets the base image for subsequent instructions. A Dockerfile must start with a `FROM` instruction.

* `LABEL` - The `LABEL` instruction adds metadata to an image.

* `RUN` - The `RUN` command is used to run any commands in a new layer on top of the current image and commit the results.

* `CMD` - Provides defaults for an executing container. It can include an executable, or they can omit the executable, in which case you must specify an `ENTRYPOINT` command.

* `EXPOSE` - The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime.

* `ENV` - The `ENV` instruction sets the environment variable to the value.

* `ADD` - The `ADD` instruction copies new files, directories, or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.

* `COPY` - The `COPY` command copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.

* `ENTRYPOINT` - Allows you to configure a container that will run as an executable.

* `WORKDIR` - The `WORKDIR` directive is used to set where the command defined with `CMD` is to be executed.

* `VOLUME` - The `VOLUME` command is used to enable access/linked directories between the container and the host.

* `USER` - The `USER` instruction sets the user name (or UID) and optionally the user group (or GID) to use when running the image and for any `RUN`, `CMD`, and `ENTRYPOINT` instructions that follow it in the Dockerfile.

Here's a slightly more comprehensive Dockerfile that contains examples of some of these commands:

```dockerfile
# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

```

This Dockerfile will create a Docker image with Python 3.9, set the working directory, copy the requirements file, install the required Python packages, copy the rest of the code into the image, expose port 80, and set an environment variable. When the Docker container is run, it will execute the app.py script.

## Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. It uses YAML files to configure the application's services and performs the creation and start-up process of all the containers with a single command.

Here's an example `docker-compose.yml` file:

```yaml
version: "3.8"
services:
  web:
    build: .
    command: python app.py
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```

To start all services defined in the docker-compose file, navigate to the directory containing the file and run the docker-compose up command.

```
docker compose up
```

## Docker Command Cheat Sheet

### Docker Images

* `docker pull <image>`: Pulls an image from Docker Hub
* `docker images` (or `docker image ls`): Lists all Docker images
* `docker build -t <tag> .`: Builds a Docker image from a Dockerfile
* `docker rmi <image_id>`: Removes a Docker image

### Docker Containers

* `docker run <image>`: Runs a Docker container from an image
* `docker ps` (or `docker container ls`): Lists all running Docker containers (add `-a` to include stopped containers)
* `docker stop <container_id>`: Stops a running Docker container
* `docker rm <container_id>`: Removes a Docker container
* `docker exec -it <container_id> <command>`: Attaches and executes a command on a running docker container. Most of the time, this command will be `/bin/bash`, which will start an interactive bash shell.

### Docker Compose

* `docker compose up`: Starts all services defined in `docker-compose.yml`
* `docker compose up --build`: Rebuilds and starts all services defined in `docker-compose.yml`
* `docker compose --env-file <.env_file> config`: Shows you your resolved `docker-compose.yml` file using a particular config file
* `docker compose --env-file <.env_file> up`: Starts all services defined in `docker-compose.yml` using a particular environment file
* `docker compose build`: Rebuilds and all services defined in `docker-compose.yml` but does not start any containers
* `docker compose down`: Stops all services defined in `docker-compose.yml`

Note: You may also see `docker-compose` in place of `docker compose`

### Docker System

* `docker system df`: Shows Docker disk usage
* `docker system prune`: Removes unused data

### Other Commands

* `docker volume ls`: List Docker volumes
* `docker network ls`: List Docker networks

## Conclusion and Next Steps

This tutorial covered the basics of Docker, including how to install Docker, work with Docker images and containers, create a Dockerfile, use Docker Compose, and some basic Docker commands. Docker is a powerful tool for creating, deploying, and running applications, and understanding Docker is crucial for modern software development.

Remember, practice makes perfect. So, the more you play around with Docker, the more comfortable you will be using it. Check out the included examples in this repository to help reinforce some of the concepts explained in this tutorial.

### Examples

* **[simple-container-example](./simple-container-example/README.md)**: This small example project shows how you can pull an existing image from the docker registry and run it without using a Dockerfile. It also demonstrates the concepts of bind mounts and port forwarding.

* **[microservices-example](./microservices-example/README.md)**: This example project shows how to use the docker compose pattern to create a small microservices ecosystem. It provides three example Dockerfiles, shows how to explicitly specify volumes, and shows how containers can communicate with one another using a network.