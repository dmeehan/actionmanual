# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Article'
        db.create_table('posts_article', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('excerpt_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Person'], null=True, blank=True)),
            ('excerpt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('body_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('posts', ['Article'])

        # Adding model 'Link'
        db.create_table('posts_link', (
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, unique=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('via_name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('via_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('posts', ['Link'])

        # Adding model 'Image'
        db.create_table('posts_image', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('crop_vert', self.gf('django.db.models.fields.IntegerField')(default=1, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('crop_horiz', self.gf('django.db.models.fields.IntegerField')(default=1, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_image_user', blank=True, null=True, to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_image_contenttype', to=orm['contenttypes.ContentType'])),
            ('image_size', self.gf('django.db.models.fields.CharField')(default=1, max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_location', self.gf('django.db.models.fields.CharField')(default=0, max_length=50)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('posts', ['Image'])

        # Adding model 'Video'
        db.create_table('posts_video', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_video_user', blank=True, null=True, to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_video_contenttype', to=orm['contenttypes.ContentType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('posts', ['Video'])

        # Adding model 'Flash'
        db.create_table('posts_flash', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('swf', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_flash_user', blank=True, null=True, to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_flash_contenttype', to=orm['contenttypes.ContentType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('posts', ['Flash'])

        # Adding model 'Audio'
        db.create_table('portfolio_audio', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_audio_user', blank=True, null=True, to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_audio_contenttype', to=orm['contenttypes.ContentType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('posts', ['Audio'])

        # Adding model 'Document'
        db.create_table('posts_document', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_document_user', blank=True, null=True, to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts_document_contenttype', to=orm['contenttypes.ContentType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('posts', ['Document'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Article'
        db.delete_table('posts_article')

        # Deleting model 'Link'
        db.delete_table('posts_link')

        # Deleting model 'Image'
        db.delete_table('posts_image')

        # Deleting model 'Video'
        db.delete_table('posts_video')

        # Deleting model 'Flash'
        db.delete_table('posts_flash')

        # Deleting model 'Audio'
        db.delete_table('portfolio_audio')

        # Deleting model 'Document'
        db.delete_table('posts_document')
    
    
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
        'contacts.person': {
            'Meta': {'object_name': 'Person', 'db_table': "'contacts_people'"},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
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
        'posts.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Person']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'excerpt_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'posts.audio': {
            'Meta': {'object_name': 'Audio', 'db_table': "'portfolio_audio'"},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_audio_contenttype'", 'to': "orm['contenttypes.ContentType']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_audio_user'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'posts.document': {
            'Meta': {'object_name': 'Document'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_document_contenttype'", 'to': "orm['contenttypes.ContentType']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_document_user'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'posts.flash': {
            'Meta': {'object_name': 'Flash'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_flash_contenttype'", 'to': "orm['contenttypes.ContentType']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'swf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_flash_user'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"})
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'posts.video': {
            'Meta': {'object_name': 'Video'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_video_contenttype'", 'to': "orm['contenttypes.ContentType']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts_video_user'", 'blank': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['posts']
