#configuration
augeas{ 'configure the .ssh/config'
  context => '.ssh/config',
  changes => [
     'insert after /.ssh/config/*[contains(text(), "Host *")] "PasswordAuthentication no"',  
  ],
  onlyif => 'match /.ssh/config/*[contains(text(), "PasswordAuthentication no")] size == 0',
}

