# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /mylove

# Copy the requirements.txt file into the container
COPY requirments.txt .

# Install the dependencies
RUN pip install -r requirments.txt

# Copy the rest of the application code into the container
COPY . .

RUN apk update


RUN apk add nano


# Set build-time variables as environment variables
ARG SECRECT_KEY
ARG ALGORITHEM
ARG TOKEN_EXPIRY_TIME_NEW
ARG MONGO_URL
ARG DATABASE
ARG USERCOLLECTION
ARG ADMINCOLLECTION
ARG REDIS_URL
ARG ADMIN
ARG TRAINER
ARG USER
ARG AWS_ACCESS_KEY
ARG AWS_SECRET_KEY
ARG AWS_REGION
ARG AWS_S3_BUCKET

ENV SECRECT_KEY=${SECRECT_KEY}
ENV ALGORITHEM=${ALGORITHEM}
ENV TOKEN_EXPIRY_TIME_NEW=${TOKEN_EXPIRY_TIME_NEW}
ENV MONGO_URL=${MONGO_URL}
ENV DATABASE=${DATABASE}
ENV USERCOLLECTION=${USERCOLLECTION}
ENV ADMINCOLLECTION=${ADMINCOLLECTION}
ENV REDIS_URL=${REDIS_URL}
ENV ADMIN=${ADMIN}
ENV TRAINER=${TRAINER}
ENV USER=${USER}
ENV AWS_ACCESS_KEY=${AWS_ACCESS_KEY}
ENV AWS_SECRET_KEY=${AWS_SECRET_KEY}
ENV AWS_REGION=${AWS_REGION}
ENV AWS_S3_BUCKET=${AWS_S3_BUCKET}

EXPOSE 4522
# Command to run the application
CMD ["python", "main.py"]
