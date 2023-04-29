# export NB_USER="cbatth"; export NB_UID="1000"
# export NB_GID="100"; export HOME="/home/${NB_USER}"


useradd -m -d $HOME -u $NB_UID -G $NB_GID  $NB_USER
apt update && apt upgrade && apt -y install curl
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && chmod a+rx /usr/local/bin/yt-dlp
yt-dlp -U
USER ${NB_UID}
cd $HOME
mkdir media
cd media
