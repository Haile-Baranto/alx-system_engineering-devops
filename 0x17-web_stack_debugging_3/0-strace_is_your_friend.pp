# 0-strace_is_your_friend.pp

# Define a file resource to manage the Apache configuration file
file { '/etc/apache2/sites-available/my-site.conf':
  ensure  => present,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => template('apache/my-site.conf.erb'),
  require => Package['apache2'],  # Ensure Apache is installed before managing the config
}

# Define an Apache vhost resource to enable the site
apache::vhost { 'my-site':
  vhost_name    => 'my-site',
  docroot       => '/var/www/html',
  vhost_aliases => '*',
  require       => File['/etc/apache2/sites-available/my-site.conf'],
  notify        => Service['apache2'],
}

# Ensure Apache service is running
service { 'apache2':
  ensure => 'running',
  enable => true,
}
