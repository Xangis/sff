server {
	listen 80;
	server_name www.sffdb.com;
	rewrite ^/(.*) http://sffdb.com/$1 permanent;
	}

server {
	listen 80;
	server_name sffdb.com;
    root /var/django/sff;
	access_log off;
	error_log off;

        location ~ ^/admin/static/ {
            root /home/xangis/.virtualenvs/sffdb/lib/python2.7/site-packages/django/contrib/;
        }

        location ~* ^.+\.(jpg|jpeg|gif|css|png|js|ico|pdf|zip|exe|wav|gz|bmp|tgz|gz|rar|txt|tar|rtf)$ {
            root /var/django/sff/templates/;
            access_log off;
            expires 30d;
        }

        location / {
                include /etc/nginx/uwsgi_params;
                uwsgi_pass 127.0.0.1:9110;
        }

}
