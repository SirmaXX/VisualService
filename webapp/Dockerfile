

# ==== CONFIGURE =====
# Use a Node 16 base image
FROM node:18-alpine 
# Set the working directory to /app inside the container

COPY . .
# ==== BUILD =====
# Build the app
RUN npm run build
# Expose the port on which the app will be running (3000 is the default that `serve` uses)
EXPOSE 3000
# Start the app
CMD [ "npm","start" ]