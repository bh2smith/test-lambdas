# Lambdas Everywhere

Tinkering with AWS lambda functions in multiple languages.


## Node Lambda (hello world)

Instructions borrowed from: https://docs.aws.amazon.com/lambda/latest/dg/typescript-image.html

### Local Test
1. Run the "server"
```sh
cd node
export IMAGE_NAME=node-lambda
docker build -t ${IMAGE_NAME} .
docker run -p 9000:8080 ${IMAGE_NAME}
```
2. Invoke via Function URL

```sh
 export FUNCTION_URL=http://localhost:9000/2015-03-31/functions/function/invocations
curl -XPOST ${FUNCTION_URL} -d '{"x": 1, "y": 2}'
```

Note that the data passed in will be part of the `event` within the lambda function.

## Python Lambda (insert to DB)

The following is adapted from these docs: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html

In this example we demonstrate how to write to DB with data passed into the invoked function.

Assuming you have a local postgres instance of postgres running (`docker run postgres`?)

```sh
# 1. Get env vars sorted
cd python
cp .env_sample .env  <-- fill out credentials
source .env

# 2. build and run image.
docker build -t ${IMAGE_NAME} .
# Remote DB:
docker run -p 9000:8080 --env DATABASE_URL=${DATABASE_URL} ${IMAGE_NAME}
# Local (Docker) DB:
docker run -p 9000:8080 --add-host=localhost:host-gateway --env DATABASE_URL=${DATABASE_URL} ${IMAGE_NAME}

# 3. Invoke the lambda function
curl -XPOST ${FUNCTION_URL} -d '{"txHash": "0x42"}'
```
# Create & Publish to Container Registry

```sh
# Using env vars specified in .env_publish
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_URL}
aws ecr create-repository --repository-name ${IMAGE_NAME} --region ${AWS_REGION} --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
docker tag ${IMAGE_NAME}:latest ${AWS_URL}/${IMAGE_NAME}:latest
docker push ${AWS_URL}/${IMAGE_NAME}:latest 
```

## Create Lambda from Image

Via AWS Console this can now be selected. 
Set relevant environment variables. 
In the configuration settings, you can enable `functionURL`. 
Once the functionURL is acquired try to invoke it as following:

then

```shell
export LAMBDA_URL=

curl -XPOST \
      ${LAMBDA_URL} \
      -H 'content-type: application/json' \
      -d '{"txHash": "0x42"}'
```


### Notes & Issues

Some things encountered during this process:

- Had to coordinate with devops about Role & Permissions
- Test (event) input does not agree with input coming from functionURL (must append some SSL stuff).
