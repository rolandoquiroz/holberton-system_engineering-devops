# 0. Sky is the limit, let's bring that limit higher

exec { 'fix wp-settings.php file':
  command => "sed -i 's|15|5000|g' /etc/default/nginx",
  path    => ['/bin']
}

exec { 'nginx restart':
  command => 'service nginx restart',
  path    => ['/usr/bin']
}
