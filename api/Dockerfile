# FROM node:17-alpine

# WORKDIR /app

# COPY . .

# RUN npm install

# EXPOSE 4000
# # required for docker desktop port mapping

# CMD ["node", "app.js"]

# base image first layer, parent image
FROM node:17-alpine 


# set the working directory in the container
WORKDIR /app

# copy all files from current directory to /app in the container
COPY . .


# install all dependencies
RUN npm install

# run the app
CMD ["node", "app.js"]

# The EXPOSE instruction in a Dockerfile is used to inform Docker that the container listens on the specified network ports at runtime. 
# This is primarily for documentation purposes and does not actually publish the port.
EXPOSE 4000



