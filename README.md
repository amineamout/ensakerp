ensakerp
========

Exemple très basic d'un module sur openERP - démonstration ENSAK
====

Étapes pré-installation + installation OpenERP & PostgreSQL

adduser --system --quiet --shell=/bin/bash --home=/opt/openerp --gecos 'OpenERP' --group openerp
passwd [sasir un mot de passe]

apt-get install postgresql

su - postgres -c "createuser -s openerp"

apt-get install python-dateutil python-feedparser python-gdata python-ldap \
    python-libxslt1 python-lxml python-mako python-openid python-psycopg2 \
    python-pybabel python-pychart python-pydot python-pyparsing python-reportlab \
    python-simplejson python-tz python-vatnumber python-vobject python-webdav \
    python-werkzeug python-xlwt python-yaml python-zsi python-docutils \
    python-psutil bzr wget python-unittest2 python-mock python-jinja2


wget http://gdata-python-client.googlecode.com/files/gdata-2.0.17.tar.gz
tar zxvf gdata-2.0.17.tar.gz
cd gdata-2.0.17/
python setup.py install


su - openerp
cd /opt/openerp
bzr branch lp:openobject-server/7.0 server
bzr branch lp:openobject-addons/7.0 addons
bzr branch lp:openerp-web/7.0 web

vi start

\#!/bin/bash
./server/openerp-server --xmlrpc-port=38550 --netrpc-port=40070 --addons-path=/opt/openerp/addons,/opt/openerp/web/addons $1 $2 $3 $4 $5 &

./server/openerp-server -h

chmod +x start
./start

OpenERP est accessible maintenant à partir du lien : localhost:38550
