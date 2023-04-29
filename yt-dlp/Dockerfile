FROM python:3.9-slim
LABEL maintainer="Chander Batth"
#
ARG NB_USER="cbatth"
ARG NB_UID="1000"
ARG NB_GID="100"
ARG HOME="/home/${NB_USER}"
#
#https://hub.docker.com/r/jupyter/base-notebook/dockerfile
#SHELL ["/bin/bash", "-o", "pipefail", "-c"]
USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    curl \
    #bzip2 \
    #ca-certificates \
    #sudo \
    #locales \
    #fonts-liberation \
    #run-one \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
#
# Configure environment
ENV CONDA_DIR=/media \
    SHELL=/bin/bash \
    NB_USER=$NB_USER \
    NB_UID=$NB_UID \
    NB_GID=$NB_GID \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
#
#
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER
#
#RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
#
# Create NB_USER wtih name jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
#RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    #sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers && \
    #sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers 
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $CONDA_DIR && \
    chown $NB_USER:$NB_GID $CONDA_DIR && \
    chmod g+w /etc/passwd 
RUN  curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && chmod a+rx /usr/local/bin/yt-dlp  # Make executable

#USER $NB_UID
#WORKDIR $HOME
#ARG PYTHON_VERSION=default

COPY . ${HOME}
CMD ["python3"]
ENTRYPOINT  ["yt-dlp"]
USER $NB_UID
WORKDIR $HOME
WORKDIR $CONDA_DIR

#
#CMD  ${HOME}/install_yt-dlp.bash
#COPY Dockerfile ${HOME}
#COPY requirements.txt ${HOME}
#COPY requirements.txt /tmp
#RUN  apt update && apt upgrade && apt -y install curl 
#RUN  curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && chmod a+rx /usr/local/bin/yt-dlp  # Make executable
# Configure container startup
#CMD ["python3"]
# Switch back to jovyan to avoid accidental container runs as root
#WORKDIR "${HOME}"
##
##  docker run -it --rm  -v /tmp:/media:z   yt-dlp:latest   https://youtu.be/n8t_hbchQcc
