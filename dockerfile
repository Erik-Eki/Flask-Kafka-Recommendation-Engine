# start by pulling the python image
FROM python:3.10
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
#Server will reload itself on file changes if in dev mode
ENV FLASK_ENV=development 

# install the dependencies and packages in the requirements file
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY ./app /app

# configure the container to run in an executed manner
# ENTRYPOINT [ "python" ]
EXPOSE 5000:5000

# CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]
# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["flask", "run", "--host", "0.0.0.0"]