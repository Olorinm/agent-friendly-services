FROM node:24-bookworm-slim
ARG CODEX_VERSION=0.162.0
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates git python3 procps ripgrep curl \
    && rm -rf /var/lib/apt/lists/* \
    && npm install -g @openai/codex@${CODEX_VERSION} \
    && mkdir -p /workspace && chown node:node /workspace
USER node
WORKDIR /workspace
CMD ["sleep", "infinity"]
