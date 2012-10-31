# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Poke.poker_profile_link'
        db.add_column('pokeviewer_poke', 'poker_profile_link',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=300),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Poke.poker_profile_link'
        db.delete_column('pokeviewer_poke', 'poker_profile_link')


    models = {
        'pokeviewer.poke': {
            'Meta': {'object_name': 'Poke'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poke_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'poker': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'poker_profile_link': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['pokeviewer']