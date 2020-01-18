[
    {
        name: configure webservers,
        hosts: webservers,
        tasks: [
    {
        name: install web pkgs,
        yum: {
            name: [httpd, php, php - mysql],
            state: present
        }
    },
    {
        name: configure web serivce,
        service: {
            name: httpd,
            state: started,
            enabled: yes
        }
    }
]

}
]