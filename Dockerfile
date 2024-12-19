FROM docker.io/python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_ROOT_USER_ACTION=ignore

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends --no-install-suggests build-essential && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt && \
    apt-get purge -y build-essential && apt-get autoremove -y && \
    apt-get install -y --no-install-recommends --no-install-suggests libstdc++6 libx11-6 && apt-get clean all && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt

CMD ["bash", "-c", "python -O src/main.py"]
