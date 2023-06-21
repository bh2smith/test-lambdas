# Lambdas Everywhere

Tinkering with AWS lambda functions in multiple languages.


## Node Lambda

Instructions borrowed from: https://docs.aws.amazon.com/lambda/latest/dg/typescript-image.html

### Local Test

```shell
cd node
export IMAGE_NAME=node-lambda
docker build -t ${IMAGE_NAME} .
docker run -p 9000:8080 ${IMAGE_NAME}
 export FUNCTION_URL=http://localhost:9000/2015-03-31/functions/function/invocations
curl -XPOST ${FUNCTION_URL} -d '{}'
```

