# Use an official Python runtime as a parent image
FROM python:3.13-alpine
# Set the working directory in the container
COPY requirements.txt /tmp
# Install any needed packages specified in requirements.txt
RUN pip install -r /tmp/requirements.txt
# Copy the current src directory contents into the container at /src
COPY ./src /src
# run the app.py when the container launches
#EXPOSE 5000
CMD python /src/app.py