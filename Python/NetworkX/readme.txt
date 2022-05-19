openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout notebook.pem -out notebook.pem

img="cps_py39pdjupy"
certfile=/home/jovyan/work/jupyter/notebook.pem
#docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work $img
docker run -d --rm --name abc -p 10000:8888 -v "${PWD}":/home/jovyan/work $img start-notebook.sh --NotebookApp.certfile=$certfile

##https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html#ssl-certificates
docker run -it --rm -name abc -p 10000:8888 \
    -v "${PWD}":/home/jovyan/work \
    $img \
    start-notebook.sh --NotebookApp.certfile=/home/jovyan/work/ssl/notebook.pem
    #--NotebookApp.keyfile=/etc/ssl/notebook/notebook.key \
    #--NotebookApp.certfile=/etc/ssl/notebook/notebook.crt


