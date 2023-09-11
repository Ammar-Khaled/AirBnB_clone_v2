# sets up my web servers for the deployment of web_static

exec { 'deploy':
  provider => shell,
  command  => "sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo service nginx start ; sudo mkdir -p /data/web_static/shared/ ; sudo mkdir -p /data/web_static/releases/test/ ; sudo echo 'Holberton School' > /data/web_static/releases/test/index.html ; sudo ln -sf /data/web_static/releases/test/ /data/web_static/current ; sudo chown -R ubuntu:ubuntu /data/ ; sudo sed -i '41i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default ; sudo service nginx restart"
}
