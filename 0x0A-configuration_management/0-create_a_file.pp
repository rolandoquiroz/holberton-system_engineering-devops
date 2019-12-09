# Using Puppet, install puppet-lint.
file { '/tmp/holberton':
      ensure  => 'file'
      content => 'I love Puppet',
      group   => 'www-data',
      owner   => 'www-data',
      mode    => '0744',
}
