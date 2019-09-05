# DEXMA DevOps / System Engineer Test

## Introduction

We need to deploy a microservice (created by our developer team in python) to production that help us to monitorize the status of a new instance of RedisDB.

## Architecture
This architecture will have three components:

* RedisDB Server 
* Web Application (Code provided)
* Web proxy

## RedisDB Server
To test this new microservice, you need to install a redisDB instance with the following requirements:

* Authentication is required, so you need to configured it with password. 

## Web Application 

You already have the code of the application, the only thing you need to do is filling the redis configuration editing the file redis-monitoring.ini with the next variables: 

* host: Host to connect with redis
* port: Port where is listen the db 
* password: Password you set on redis configuration

This microservice will listen on port 8081 (by default) and will respond for the following endpoints:

* /ping
* /redis-status

Also you need to install all the dependencies, this packages are in requirements.txt file.

## Web Proxy

A reverse HTTP proxy needs to handle all the requests and send them to the backend application.

Requirements for the proxy:

* Pass `HTTP` (port 80) requests to the backend application (port 8081)

We suggest to use `Nginx` as the proxy application, but any other software will also be accepted.

**(OPTIONAL)**

* Pass `HTTPS` requests (port 443) to the backend application (port 8081) 
  * In case `HTTPS` is implemented, redirect port 80 requests to 443 and the certificate can be self-signed.

# Deployment

Using **one single command** we want to deploy all the required infrastructure for this application to work. After the application is working, we should get the following result:

```
$ curl -L http://HOST/ping
pong
$ curl -L  http://HOST/redis-status
{"redis_connectivity": "OK"}
```

The provided solution should be updated to a public GitHub, GitLab, Bitbucket repository with a proper README.MD providing:

* Instructions on how to run your solution.
* Requirements.
* The rationale explaining why you chose this solution over others.

## Additional notes
* Simplicity is valued over complexity.
* If you get stuck in any step, you can still submit your proposal and explain the challenges you faced and what you did to try to solve them.
* Commit from the very beginning and commit often. We value the possibility to review your git log.
* There are many possible solutions to this exercise. Some technologies you can use (but you're not limited to) are:
    * Docker
    * Docker Compose
    * Kubernetes
    * Vagrant
    * Puppet
    * Ansible