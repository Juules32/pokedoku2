# Start from the official Python base image
FROM python:3.12-slim

# The directory to put the code in (inside the container)
WORKDIR /code

# Copy just the requirements to optimise docker cache usage
# when building the image (since the requirements don't change much)
COPY ./requirements.txt /code/requirements.txt

# Will be run during the build of the image
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy everything to the container
COPY ./*.py /code/
COPY ./*.json /code/

# Will be run once the container is started from the image
# Runs from the WORKDIR directory
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
