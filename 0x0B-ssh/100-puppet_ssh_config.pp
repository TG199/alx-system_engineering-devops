# Modifies SSH Config fil
exec {'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "  IdentityFile ~/.ssh/school\n   Password Authentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
