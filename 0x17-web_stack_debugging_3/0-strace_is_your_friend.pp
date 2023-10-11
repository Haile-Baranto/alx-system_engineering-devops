#!/usr/bin/env puppet
# Ensure WordPress file wp-settings.php has correct PHP extensions
exec { 'web stack deubging':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
}
