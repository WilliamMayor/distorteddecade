$script = <<SCRIPT
    locale-gen en_GB.UTF-8
    echo <<EOF
        deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main
    EOF > /etc/apt/sources.list.d/pgdg.list
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
    apt-get --assume-yes update
    apt-get --assume-yes dist-upgrade
    apt-get --assume-yes install git postgresql-9.4
    wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

    wget -qO- https://get.docker.com/ | sh
    usermod -aG docker vagrant

    wget -qO- https://raw.githubusercontent.com/WilliamMayor/vantage/master/bootstrap.sh | sh
    echo "VG_APP_DIR=/vagrant" >> /etc/environment
    export VG_APP_DIR=/vagrant
    echo "VG_PLUGIN_PATH=/vagrant/vantage" >> /etc/environment
    echo "VG_DEFAULT_ENV=/vagrant/.env/default" >> /etc/environment
    chown -R vagrant:vagrant /usr/local/vantage
    vantage plugin install pg
    vantage plugin install alembic
SCRIPT

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network "private_network", ip: "192.168.33.21"
    config.vm.provision "shell", inline: $script
    config.vm.hostname = "dd.local"

    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
    end
end
