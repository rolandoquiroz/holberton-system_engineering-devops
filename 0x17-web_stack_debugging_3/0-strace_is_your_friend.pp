# Strace is your friend: Fix wp-settings.php file

exec { 'fix wp-settings.php file':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin']
}
exec { 'restart apache 2 web server':
  command => '/usr/sbin/service apache2 restart'
}
