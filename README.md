# Lambdas Everywhere

Tinkering with AWS lambda functions in multiple languages.


## Node Lambda

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
