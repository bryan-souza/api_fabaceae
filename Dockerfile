FROM ubuntu:latest

# Install dependencies
RUN apt update
RUN apt install -y git python3 python3-pip
RUN git clone --recursive https://github.com/bryan-souza/api_fabaceae.git /api


# Mount cache as a Docker subvolume
RUN mkdir /api/app/cache
VOLUME /api/app/cache

# Install python dependencies
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /api/app/cerebrum/requirements.txt

# Expose HTTP port
EXPOSE 80

# Finally, start the API
WORKDIR /api/app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
