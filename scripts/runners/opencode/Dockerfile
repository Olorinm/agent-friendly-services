FROM node:24-bookworm-slim
ARG OPENCODE_VERSION=1.18.29
ARG DEBIAN_MIRROR=http://deb.debian.org
RUN sed -i "s|http://deb.debian.org|${DEBIAN_MIRROR}|g" /etc/apt/sources.list.d/debian.sources
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl git python3 python3-venv procps \
    && rm -rf /var/lib/apt/lists/* \
    && npm install -g opencode-ai@${OPENCODE_VERSION} \
    && mkdir -p /workspace /home/node/service-tools \
    && chown -R node:node /workspace /home/node/service-tools
RUN apt-get update && apt-get install -y --no-install-recommends ripgrep && rm -rf /var/lib/apt/lists/*
ENV OPENCODE_DISABLE_AUTOUPDATE=true
ENV OPENCODE_DISABLE_TERMINAL_TITLE=true
USER node
WORKDIR /workspace
CMD ["sleep", "infinity"]
