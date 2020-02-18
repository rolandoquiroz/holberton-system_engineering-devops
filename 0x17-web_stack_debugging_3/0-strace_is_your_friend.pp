# Strace is your friend: Fix wp-settings.php file

exec { 'fix wp-settings.php file':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin']
}
