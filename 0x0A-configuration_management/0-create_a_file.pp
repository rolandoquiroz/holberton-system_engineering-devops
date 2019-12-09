# Using Puppet, install puppet-lint.
file { '/tmp/holberton':
  owner   => 'www-data',
  group    => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
