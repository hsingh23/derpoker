# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poke'
        db.create_table('pokeviewer_poke', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poker', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('poke_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('pokeviewer', ['Poke'])


    def backwards(self, orm):
        # Deleting model 'Poke'
        db.delete_table('pokeviewer_poke')


    models = {
        'pokeviewer.poke': {
            'Meta': {'object_name': 'Poke'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poke_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'poker': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['pokeviewer']