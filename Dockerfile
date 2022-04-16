FROM ubuntu:latest

# Install everything, then clean unused things
RUN apt-get update && \
    apt-get install -y git python3 python3-pip && \
    git clone --recursive https://github.com/bryan-souza/api_fabaceae.git /api && \
    pip install --no-cache-dir -r /api/requirements.txt && \
    pip install --no-cache-dir -r /api/app/cerebrum/requirements.txt && \
    mkdir /api/app/cache && \
    apt-get purge git python3-pip -y && \
    apt-get autoremove --purge -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Mount cache as a Docker subvolume
VOLUME /api/app/cache

# Expose HTTP port
EXPOSE 80

# Finally, start the API
WORKDIR /api/app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]