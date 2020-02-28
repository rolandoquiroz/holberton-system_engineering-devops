# 0. Sky is the limit, let's bring that limit higher

exec { 'fix wp-settings.php file':
  command => "sed -i 's|15|4096|g' /etc/default/nginx",
  path    => ['/usr/bin/env']
}

exec { 'nginx restart':
  command => 'service nginx restart',
  path    => ['/usr/bin/env']
}
