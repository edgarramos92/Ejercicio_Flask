from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

def sideBarpages(server_id, site_id):
        pages = [{"name": "Instalacion y mantemiento preventivo", "url": url_for("sites.show", server_id=server_id, site_id=site_id) },
        {"name": "Desarrollo de Software/Electronica", "url": url_for("sites.environment_page", server_id=server_id, site_id=site_id)},
        {"name": "Proximamente", "url": url_for("sites.ssl_page", server_id=server_id,site_id=site_id)}]
        return pages

