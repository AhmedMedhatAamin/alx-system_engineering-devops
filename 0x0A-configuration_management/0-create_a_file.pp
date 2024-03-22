# Add this code to suppress the warnings
module URI
  def self.escape(*args)
    # No-op, suppress the warning
  end
end

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
