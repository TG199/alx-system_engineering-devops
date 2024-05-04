# A Puppet manifest that installs Python Flask using pip3

package {'flask':
  ensure   => '2.1.0'
  provider => 'gem'
}
