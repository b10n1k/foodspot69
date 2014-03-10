# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'foodspot_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_home', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'foodspot', ['Profile'])

        # Adding model 'Favorites'
        db.create_table(u'foodspot_favorites', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'foodspot', ['Favorites'])

        # Adding model 'Category'
        db.create_table(u'foodspot_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_title', self.gf('django.db.models.fields.CharField')(default='Crepe', unique=True, max_length=35)),
        ))
        db.send_create_signal(u'foodspot', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'foodspot_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foodspot.Category'])),
            ('sub_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'foodspot', ['SubCategory'])

        # Adding model 'Food'
        db.create_table(u'foodspot_food', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foodspot.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'foodspot', ['Food'])

        # Adding model 'Topping'
        db.create_table(u'foodspot_topping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topping_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('topping_description', self.gf('django.db.models.fields.TextField')()),
            ('topping_price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'foodspot', ['Topping'])

        # Adding model 'Offer'
        db.create_table(u'foodspot_offer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foodspot_offer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foodspot_offer_price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'foodspot', ['Offer'])

        # Adding model 'Photo'
        db.create_table(u'foodspot_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'foodspot', ['Photo'])

        # Adding model 'Menu'
        db.create_table(u'foodspot_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'foodspot', ['Menu'])

        # Adding model 'Choise'
        db.create_table(u'foodspot_choise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foodspot.Menu'])),
        ))
        db.send_create_signal(u'foodspot', ['Choise'])

        # Adding model 'Order'
        db.create_table(u'foodspot_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foodspot.Profile'])),
            ('order_choises', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foodspot.Choise'])),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'foodspot', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'foodspot_profile')

        # Deleting model 'Favorites'
        db.delete_table(u'foodspot_favorites')

        # Deleting model 'Category'
        db.delete_table(u'foodspot_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'foodspot_subcategory')

        # Deleting model 'Food'
        db.delete_table(u'foodspot_food')

        # Deleting model 'Topping'
        db.delete_table(u'foodspot_topping')

        # Deleting model 'Offer'
        db.delete_table(u'foodspot_offer')

        # Deleting model 'Photo'
        db.delete_table(u'foodspot_photo')

        # Deleting model 'Menu'
        db.delete_table(u'foodspot_menu')

        # Deleting model 'Choise'
        db.delete_table(u'foodspot_choise')

        # Deleting model 'Order'
        db.delete_table(u'foodspot_order')


    models = {
        u'foodspot.category': {
            'Meta': {'ordering': "['category_title']", 'object_name': 'Category'},
            'category_title': ('django.db.models.fields.CharField', [], {'default': "'Crepe'", 'unique': 'True', 'max_length': '35'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'foodspot.choise': {
            'Meta': {'object_name': 'Choise'},
            'choise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foodspot.Menu']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'foodspot.favorites': {
            'Meta': {'object_name': 'Favorites'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'foodspot.food': {
            'Meta': {'ordering': "['category']", 'object_name': 'Food'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foodspot.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'foodspot.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'foodspot.offer': {
            'Meta': {'object_name': 'Offer'},
            'foodspot_offer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'foodspot_offer_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'foodspot.order': {
            'Meta': {'ordering': "['order_date']", 'object_name': 'Order'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_choises': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foodspot.Choise']"}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'order_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foodspot.Profile']"}),
            'order_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'foodspot.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'foodspot.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'foodspot.subcategory': {
            'Meta': {'ordering': "['sub_title']", 'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foodspot.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'foodspot.topping': {
            'Meta': {'object_name': 'Topping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topping_description': ('django.db.models.fields.TextField', [], {}),
            'topping_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'topping_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['foodspot']