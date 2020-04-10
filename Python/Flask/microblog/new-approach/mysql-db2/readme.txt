https://docs.sqlalchemy.org/en/13/dialects/mysql.html
https://gist.github.com/macloo/35bdd1648cadf1ca6e910d5fbf8fa754  #Test SQLDB
https://hub.docker.com/_/mysql?tab=description

# docker pull mysql:5.7.29
# pip install pymysql
#run
mysqlimage=mysql:5.7.29
docker run --name mysql -e MYSQL_ROOT_PASSWORD=test --rm -d ${mysqlimage}
#Connect
docker run -it --rm ${mysqlimage} mysql -h172.20.0.3 -uroot -p


