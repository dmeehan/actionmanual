# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Essay'
        db.create_table('resources_essay', (
            ('article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['posts.Article'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('resources', ['Essay'])

        # Adding M2M table for field ideas on 'Essay'
        db.create_table('resources_essay_ideas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('essay', models.ForeignKey(orm['resources.essay'], null=False)),
            ('idea', models.ForeignKey(orm['portfolio.idea'], null=False))
        ))
        db.create_unique('resources_essay_ideas', ['essay_id', 'idea_id'])

        # Adding M2M table for field precedents on 'Essay'
        db.create_table('resources_essay_precedents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('essay', models.ForeignKey(orm['resources.essay'], null=False)),
            ('precedent', models.ForeignKey(orm['portfolio.precedent'], null=False))
        ))
        db.create_unique('resources_essay_precedents', ['essay_id', 'precedent_id'])

        # Adding model 'Web'
        db.create_table('resources_web', (
            ('link_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['posts.Link'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('resources', ['Web'])

        # Adding M2M table for field ideas on 'Web'
        db.create_table('resources_web_ideas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('web', models.ForeignKey(orm['resources.web'], null=False)),
            ('idea', models.ForeignKey(orm['portfolio.idea'], null=False))
        ))
        db.create_unique('resources_web_ideas', ['web_id', 'idea_id'])

        # Adding M2M table for field precedents on 'Web'
        db.create_table('resources_web_precedents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('web', models.ForeignKey(orm['resources.web'], null=False)),
            ('precedent', models.ForeignKey(orm['portfolio.precedent'], null=False))
        ))
        db.create_unique('resources_web_precedents', ['web_id', 'precedent_id'])

        # Adding model 'ResourceOrganization'
        db.create_table('resources_resourceorganization', (
            ('organization_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Organization'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('resources', ['ResourceOrganization'])

        # Adding M2M table for field ideas on 'ResourceOrganization'
        db.create_table('resources_resourceorganization_ideas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resourceorganization', models.ForeignKey(orm['resources.resourceorganization'], null=False)),
            ('idea', models.ForeignKey(orm['portfolio.idea'], null=False))
        ))
        db.create_unique('resources_resourceorganization_ideas', ['resourceorganization_id', 'idea_id'])

        # Adding M2M table for field precedents on 'ResourceOrganization'
        db.create_table('resources_resourceorganization_precedents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resourceorganization', models.ForeignKey(orm['resources.resourceorganization'], null=False)),
            ('precedent', models.ForeignKey(orm['portfolio.precedent'], null=False))
        ))
        db.create_unique('resources_resourceorganization_precedents', ['resourceorganization_id', 'precedent_id'])

        # Adding model 'ResourcePerson'
        db.create_table('resources_resourceperson', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Person'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('resources', ['ResourcePerson'])

        # Adding M2M table for field ideas on 'ResourcePerson'
        db.create_table('resources_resourceperson_ideas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resourceperson', models.ForeignKey(orm['resources.resourceperson'], null=False)),
            ('idea', models.ForeignKey(orm['portfolio.idea'], null=False))
        ))
        db.create_unique('resources_resourceperson_ideas', ['resourceperson_id', 'idea_id'])

        # Adding M2M table for field precedents on 'ResourcePerson'
        db.create_table('resources_resourceperson_precedents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resourceperson', models.ForeignKey(orm['resources.resourceperson'], null=False)),
            ('precedent', models.ForeignKey(orm['portfolio.precedent'], null=False))
        ))
        db.create_unique('resources_resourceperson_precedents', ['resourceperson_id', 'precedent_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Essay'
        db.delete_table('resources_essay')

        # Removing M2M table for field ideas on 'Essay'
        db.delete_table('resources_essay_ideas')

        # Removing M2M table for field precedents on 'Essay'
        db.delete_table('resources_essay_precedents')

        # Deleting model 'Web'
        db.delete_table('resources_web')

        # Removing M2M table for field ideas on 'Web'
        db.delete_table('resources_web_ideas')

        # Removing M2M table for field precedents on 'Web'
        db.delete_table('resources_web_precedents')

        # Deleting model 'ResourceOrganization'
        db.delete_table('resources_resourceorganization')

        # Removing M2M table for field ideas on 'ResourceOrganization'
        db.delete_table('resources_resourceorganization_ideas')

        # Removing M2M table for field precedents on 'ResourceOrganization'
        db.delete_table('resources_resourceorganization_precedents')

        # Deleting model 'ResourcePerson'
        db.delete_table('resources_resourceperson')

        # Removing M2M table for field ideas on 'ResourcePerson'
        db.delete_table('resources_resourceperson_ideas')

        # Removing M2M table for field precedents on 'ResourcePerson'
        db.delete_table('resources_resourceperson_precedents')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.CategoryGroup']"}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'})
        },
        'categories.categorygroup': {
            'Meta': {'object_name': 'CategoryGroup'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'})
        },
        'contacts.organization': {
            'Meta': {'object_name': 'Organization'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'org_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contacts.person': {
            'Meta': {'object_name': 'Person', 'db_table': "'contacts_people'"},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portfolio.designer': {
            'Meta': {'object_name': 'Designer'},
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'blurb_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Person']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'portfolio.firm': {
            'Meta': {'object_name': 'Firm'},
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'blurb_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Organization']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'portfolio.idea': {
            'Meta': {'object_name': 'Idea'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['categories.Category']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.License']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'moderate_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Person']", 'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'copyright': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.License']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'crop_horiz': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'crop_vert': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'lead': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'portfolio.license': {
            'Meta': {'object_name': 'License'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'portfolio.precedent': {
            'Meta': {'object_name': 'Precedent'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['categories.Category']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.License']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'moderate_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'posts.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Person']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'excerpt_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'posts.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_image_contenttype'", 'to': "orm['contenttypes.ContentType']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'crop_horiz': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'crop_vert': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_location': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '50'}),
            'image_size': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_image_user'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'posts.link': {
            'Meta': {'object_name': 'Link'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'via_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'via_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'})
        },
        'resources.essay': {
            'Meta': {'object_name': 'Essay', '_ormbases': ['posts.Article']},
            'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['posts.Article']", 'unique': 'True', 'primary_key': 'True'}),
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Idea']", 'null': 'True', 'blank': 'True'}),
            'precedents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Precedent']", 'null': 'True', 'blank': 'True'})
        },
        'resources.resourceorganization': {
            'Meta': {'object_name': 'ResourceOrganization', '_ormbases': ['contacts.Organization']},
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Idea']", 'null': 'True', 'blank': 'True'}),
            'organization_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Organization']", 'unique': 'True', 'primary_key': 'True'}),
            'precedents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Precedent']", 'null': 'True', 'blank': 'True'})
        },
        'resources.resourceperson': {
            'Meta': {'object_name': 'ResourcePerson', '_ormbases': ['contacts.Person']},
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Idea']", 'null': 'True', 'blank': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'precedents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Precedent']", 'null': 'True', 'blank': 'True'})
        },
        'resources.web': {
            'Meta': {'object_name': 'Web', '_ormbases': ['posts.Link']},
            'ideas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Idea']", 'null': 'True', 'blank': 'True'}),
            'link_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['posts.Link']", 'unique': 'True', 'primary_key': 'True'}),
            'precedents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Precedent']", 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['resources']
