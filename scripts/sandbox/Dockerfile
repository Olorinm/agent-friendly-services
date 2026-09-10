FROM node:22-bookworm-slim

# Shared tools only. Service-specific packages belong to the individual trial.
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl git python3 python3-venv procps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /workspace \
    && chown node:node /workspace
RUN printf '%s\n' 'export PATH="/home/node/venv/bin:$PATH"' > /etc/profile.d/afs-python.sh
USER node
RUN python3 -m venv /home/node/venv
ENV PATH="/home/node/venv/bin:${PATH}"
WORKDIR /workspace
CMD ["sleep", "infinity"]
