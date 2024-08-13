# 0-strace_is_your_friend.pp
#
# Puppet manifest to fix Apache 500 error by ensuring the correct configuration for WordPress.

# Ensure that the wp-config.php file exists with the correct ownership and permissions
file { '/var/www/html/wp-config.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  source  => 'puppet:///modules/wordpress/wp-config.php', # Replace with your source
}

# Ensure that the WordPress directory has the correct ownership and permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  recurse => true,
  mode    => '0755',
}

# Restart Apache if the configuration file changes
exec { 'restart-apache':
  command     => '/etc/init.d/apache2 restart',
  refreshonly => true,
  subscribes  => File['/var/www/html/wp-config.php'],
}
