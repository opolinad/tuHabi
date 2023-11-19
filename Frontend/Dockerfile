# base image
FROM node:20.9.0-alpine3.17

# setup environment variable
ENV DockerHOME=/app

# set work directory
WORKDIR $DockerHOME

# Copy package.json and package-lock.json to the working directory
COPY ./package*.json ./

# install dependencies
RUN npm install

# Start the Next.js application
CMD ["npm", "run", "dev"]
