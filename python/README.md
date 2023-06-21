# AWS Lambda Function (Container Image of Python Handler)

The following is adapted from these docs: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html

Setup environment

```shell
cp .env_sample .env
source .env
```

which should consist of things like

```shell
# Container Image Build and Publish env
export IMAGE_NAME=
export AWS_REGION=
export AWS_ID=
export AWS_URL=${AWS_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

# Run time env
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres
export FUNCTION_URL=http://localhost:9000/2015-03-31/functions/function/invocations
```

# Build

```shell
docker build -t ${IMAGE_NAME} .
```

## Local E2E Test

Assuming you have a local postgres instance running at:

Run the lambda locally at `postgresql://postgres:postgres@localhost:5432/postgres`

```shell
docker run -p 9000:8080 -env DATABASE_URL=${DATABASE_URL} ${IMAGE_NAME}
```

Post to handler

```shell
curl -XPOST ${FUNCTION_URL} -d '{"txHash": "Hello", "solver": "World"}'
```

