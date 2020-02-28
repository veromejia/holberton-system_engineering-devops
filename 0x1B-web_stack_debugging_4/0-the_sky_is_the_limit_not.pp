#increase the open file limit for to 4096
exec { 'change ULIMIT':
  command => "sed -i 's/15/2000/g' /etc/default/nginx ; service nginx restart",
  path    => ['/usr/local/bin/:/bin/']
}
