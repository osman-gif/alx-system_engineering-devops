package{ 'nginx':
	ensure	=> installed,
}

file{ '/var/www/html/index.html':
	owner	=> 'ajang',
		mode	=> '0644',
		content	=> "Hello World!",
}


file_line { 'add X-Served-By: hostname':
	path	=> '/etc/nginx/sites-available/default',
	ensure	=> present,
	after	=> "server {",
	line	=> "	X-Served-By: $hostname",
}
