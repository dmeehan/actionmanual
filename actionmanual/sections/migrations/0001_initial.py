# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Section'
        db.create_table('sections_section', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sections.Section'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('sections', ['Section'])

        # Adding unique constraint on 'Section', fields ['parent', 'name']
        db.create_unique('sections_section', ['parent_id', 'name'])

        # Adding model 'SectionItem'
        db.create_table('sections_sectionitem', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_section', to=orm['sections.Section'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('sections', ['SectionItem'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Section'
        db.delete_table('sections_section')

        # Removing unique constraint on 'Section', fields ['parent', 'name']
        db.delete_unique('sections_section', ['parent_id', 'name'])

        # Deleting model 'SectionItem'
        db.delete_table('sections_sectionitem')
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sections.section': {
            'Meta': {'unique_together': "(('parent', 'name'),)", 'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sections.Section']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'})
        },
        'sections.sectionitem': {
            'Meta': {'object_name': 'SectionItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_section'", 'to': "orm['sections.Section']"})
        }
    }
    
    complete_apps = ['sections']
