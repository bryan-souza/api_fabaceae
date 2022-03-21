FROM ubuntu:latest

# Install dependencies
RUN apt update
RUN apt install -y git python3 python3-pip
RUN git clone https://github.com/bryan-souza/api_fabaceae.git

# CD into cloned directory
WORKDIR /api_fabaceae

# Mount cache as a Docker subvolume
RUN mkdir ./cache
VOLUME /api_fabaceae/cache

# Install python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose HTTP port
EXPOSE 80

# Finally, start the API
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
