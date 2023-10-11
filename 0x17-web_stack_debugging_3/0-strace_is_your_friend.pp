# Ensure WordPress file wp-settings.php has correct PHP extensions

file { '/var/www/html/wp-settings.php':
  ensure => file,
}

exec { 'fix-wordpress-php-extensions':
  command     => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path        => ['/usr/local/bin', '/bin'],
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
