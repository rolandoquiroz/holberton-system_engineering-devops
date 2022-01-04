# Using Puppet, create a file in /tmp.
file { 'holberton':
  ensure  => file,
  path    => '/tmp/holberton',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
