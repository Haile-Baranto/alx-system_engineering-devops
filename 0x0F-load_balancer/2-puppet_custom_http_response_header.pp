# Configure Nginx to add a custom HTTP response header
exec { 'custom_http_response_header':
  command  => "/bin/bash -c 'apt-get -y update &&
                          apt-get -y install nginx &&
                          sed -i \'/listen 80 default_server;/a add_header X-Served-By ${hostname};\' /etc/nginx/sites-available/default &&
                          service nginx restart'",
  path     => ['/bin', '/usr/bin'],
  provider => shell,
  onlyif   => '/bin/grep -q "add_header X-Served-By" /etc/nginx/sites-available/default',
  require  => Package['nginx'],
}