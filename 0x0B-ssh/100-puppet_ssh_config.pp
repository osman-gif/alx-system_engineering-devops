#configuration
file_line{ 'config':
  path  => '/home/ajang/config',
  line  => "\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school",
  match => '^\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school$',
  append_on_no_match => false,
}

