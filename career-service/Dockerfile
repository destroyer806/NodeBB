# specifies the Parent Image from which you are building.
FROM python:3.9

# specify the working directory for the image
WORKDIR /code

# copy requirement.txt to working directory
COPY ./requirements.txt /code/requirements.txt

# install dependencies into the virtual environment
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the ./app directory to the /code directory
COPY ./app /code/app

# Run Uvicorn and tell it to import the app object from main
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]