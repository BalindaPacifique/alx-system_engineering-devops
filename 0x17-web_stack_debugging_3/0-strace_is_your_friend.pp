# Puppet manifest to fix Apache 500 Internal Server Error

# Execute the fix command to resolve the issue
exec { 'fix_apache_error':
  command => '/bin/sed -i "s/memory_limit = 128M/memory_limit = 256M/" /etc/php/7.2/apache2/php.ini',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/bin/grep -q "memory_limit = 128M" /etc/php/7.2/apache2/php.ini',
}

# Restart Apache after fixing the issue
service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => Exec['fix_apache_error'],
}
