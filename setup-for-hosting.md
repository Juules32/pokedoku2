# General
These are just notes for myself if I ever want to host the application.

## Secret Values
[The repository](https://github.com/Juules32/pokedoku2) uses github secrets for sensitive data:
- BACKEND_HOST: The ip address of the hosted backend container.
- FRONTEND_HOST: The ip address of the hosted frontend container.
- DOCKER_USERNAME: The username of the user whose repository will be accessed.
- DOCKER_TOKEN: Is used to allow the workflow to push new images to repositories.
- SSH_USERNAME: The ssh username of the hosted environments. Used by the workflows to login to the terminal and start the latest image from the docker repository.
- SSH_PASSWORD: The ssh password of the hosted environments.

The workflows use local environment variables for readability. These are:
- DOCKER_REPOSITORY: The name of the docker repository that should be pushed to.
- IMAGE_NAME: The name of the image that will be pushed to the docker repository.

## Using Docker Hub for storing images
Follow these steps to setup the two repositories:
- Create an account/login to your account.
- Create a docker token [here](https://hub.docker.com/settings/security).
- Create two repositories for frontend and backend, respectively.
- Change the github secrets DOCKER_USERNAME and DOCKER_TOKEN to their corresponding values.
- In the workflows, change the DOCKER_REPOSITORY environment variable to the name of the corresponding repository.

## Using DigitalOcean for hosting
I have used DigitalOcean to host the app (frontend and backend) successfully.
Follow these steps to host the app in the future:
- Create two droplets running ubuntu. They should be located in the same country. They should use SSH to login.
- Install docker on them by following [this guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
- Change the github secrets BACKEND_HOST, FRONTEND_HOST, SSH_PASSWORD, and SSH_USERNAME in accordance with the new droplets.
- Run the workflows (either from github or by pushing a tag)

## Pushing tags:
- git tag -a v0.0.0 -m "Tag message"
- git push origin v0.0.0
