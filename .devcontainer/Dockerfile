FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
       python3 python3-fitz python3-pil make latexmk \
       texlive-latex-base texlive-latex-recommended texlive-latex-extra \
       texlive-pictures texlive-fonts-recommended texlive-lang-french \
       lmodern poppler-utils \
    && rm -rf /var/lib/apt/lists/*
USER vscode
