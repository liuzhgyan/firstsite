echo "shutdown uwsgi"
ps -ef|grep uwsgi|grep emperor|grep -v grep|awk '{print $2}'|xargs kill -9

