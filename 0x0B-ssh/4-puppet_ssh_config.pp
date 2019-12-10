# Client configuration file (w/ Puppet)
file_line { 'PasswordAuthentication setting':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}

file_line { 'IdentityFile setting':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/holberton',
}
