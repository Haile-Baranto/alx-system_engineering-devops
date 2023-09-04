# Configure Nginx to add a custom HTTP header response
exec { 'custom_http_response_header':
  command  => "bash -c 'apt-get -y update &&
                       apt-get -y install nginx &&
                       sed -i \"/listen 80 default_server;/a add_header X-Served-By \${hostname};\" /etc/nginx/sites-available/default &&
                       service nginx restart'",
  provider => shell,
  path     => ['/bin', '/usr/bin'],
  onlyif   => '/bin/grep -q "add_header X-Served-By" /etc/nginx/sites-available/default',
  require  => Package['nginx'],
}