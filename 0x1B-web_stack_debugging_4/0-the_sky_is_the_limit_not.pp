# 0. Sky is the limit, let's bring that limit higher

exec { 'fix wp-settings.php file':
  command => "/bin/echo ULIMIT='-n 32768' | sudo tee /etc/default/nginx",
}

exec { 'restart nginx':
  command => '/usr/bin/service nginx restart',
}
