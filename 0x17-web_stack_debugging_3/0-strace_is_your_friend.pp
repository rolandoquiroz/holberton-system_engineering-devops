# Strace is your friend: Fix wp-settings.php file
exec { 'stop apache 2 web server':
  command => '/usr/sbin/service apache2 stop'
}
exec { 'fix wp-settings.php file':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
exec { 'start apache 2 web server':
  command => '/usr/sbin/service apache2 start'
}
