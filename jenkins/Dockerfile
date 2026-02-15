FROM python:3.12-slim AS python-build

FROM jenkins/jenkins:lts-jdk17

USER root

COPY --from=python-build /usr/local/bin/python3.12 /usr/local/bin/python3.12
COPY --from=python-build /usr/local/lib/ /usr/local/lib/
COPY --from=python-build /usr/local/include/ /usr/local/include/
COPY --from=python-build /usr/local/bin/pip3.12 /usr/local/bin/pip3.12

RUN ln -s /usr/local/bin/python3.12 /usr/local/bin/python3 && \
    ln -s /usr/local/bin/pip3.12 /usr/local/bin/pip

RUN apt-get update && apt-get install -y \
    libsqlite3-0 \
    libexpat1 \
    libbz2-1.0 \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && apt-get install -y docker-ce-cli && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN jenkins-plugin-cli --plugins git workflow-aggregator junit coverage dark-theme 

USER jenkins