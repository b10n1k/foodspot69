# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Offer.foodspot_offer_description'
        db.add_column(u'foodspot_offer', 'foodspot_offer_description',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Offer.foodspot_offer_description'
        db.delete_column(u'foodspot_offer', 'foodspot_offer_description')


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
            'foodspot_offer_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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