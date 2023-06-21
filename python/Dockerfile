FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . ${LAMBDA_TASK_ROOT}

# Project MUST have a file app.py containing funciton `handler`
CMD [ "app.handler" ] 
