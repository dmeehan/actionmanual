# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'UserProfile.first_name'
        db.add_column('accounts_userprofile', 'first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'UserProfile.middle_name'
        db.add_column('accounts_userprofile', 'middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'UserProfile.last_name'
        db.add_column('accounts_userprofile', 'last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'UserProfile.birth_date'
        db.add_column('accounts_userprofile', 'birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'UserProfile.address_line1'
        db.add_column('accounts_userprofile', 'address_line1', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True), keep_default=False)

        # Adding field 'UserProfile.address_line2'
        db.add_column('accounts_userprofile', 'address_line2', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True), keep_default=False)

        # Adding field 'UserProfile.city'
        db.add_column('accounts_userprofile', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'UserProfile.state'
        db.add_column('accounts_userprofile', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'UserProfile.code'
        db.add_column('accounts_userprofile', 'code', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True), keep_default=False)

        # Adding field 'UserProfile.country'
        db.add_column('accounts_userprofile', 'country', self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True), keep_default=False)

        # Adding field 'UserProfile.email'
        db.add_column('accounts_userprofile', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True), keep_default=False)

        # Adding field 'UserProfile.phone'
        db.add_column('accounts_userprofile', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)

        # Adding field 'UserProfile.mobile'
        db.add_column('accounts_userprofile', 'mobile', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)

        # Adding field 'UserProfile.fax'
        db.add_column('accounts_userprofile', 'fax', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)

        # Adding field 'UserProfile.website'
        db.add_column('accounts_userprofile', 'website', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)

        # Adding field 'UserProfile.tags'
        db.add_column('accounts_userprofile', 'tags', self.gf('tagging.fields.TagField')(default=''), keep_default=False)

        # Adding field 'UserProfile.slug'
        db.add_column('accounts_userprofile', 'slug', self.gf('django.db.models.fields.SlugField')(default='', unique=True, max_length=50, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'UserProfile.first_name'
        db.delete_column('accounts_userprofile', 'first_name')

        # Deleting field 'UserProfile.middle_name'
        db.delete_column('accounts_userprofile', 'middle_name')

        # Deleting field 'UserProfile.last_name'
        db.delete_column('accounts_userprofile', 'last_name')

        # Deleting field 'UserProfile.birth_date'
        db.delete_column('accounts_userprofile', 'birth_date')

        # Deleting field 'UserProfile.address_line1'
        db.delete_column('accounts_userprofile', 'address_line1')

        # Deleting field 'UserProfile.address_line2'
        db.delete_column('accounts_userprofile', 'address_line2')

        # Deleting field 'UserProfile.city'
        db.delete_column('accounts_userprofile', 'city')

        # Deleting field 'UserProfile.state'
        db.delete_column('accounts_userprofile', 'state')

        # Deleting field 'UserProfile.code'
        db.delete_column('accounts_userprofile', 'code')

        # Deleting field 'UserProfile.country'
        db.delete_column('accounts_userprofile', 'country')

        # Deleting field 'UserProfile.email'
        db.delete_column('accounts_userprofile', 'email')

        # Deleting field 'UserProfile.phone'
        db.delete_column('accounts_userprofile', 'phone')

        # Deleting field 'UserProfile.mobile'
        db.delete_column('accounts_userprofile', 'mobile')

        # Deleting field 'UserProfile.fax'
        db.delete_column('accounts_userprofile', 'fax')

        # Deleting field 'UserProfile.website'
        db.delete_column('accounts_userprofile', 'website')

        # Deleting field 'UserProfile.tags'
        db.delete_column('accounts_userprofile', 'tags')

        # Deleting field 'UserProfile.slug'
        db.delete_column('accounts_userprofile', 'slug')


    models = {
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']
