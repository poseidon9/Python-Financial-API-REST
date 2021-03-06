# Generated by Django 4.0 on 2022-04-13 07:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Company',
			fields=[
				('UIID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
				('name', models.CharField(max_length=50)),
				('symbol', models.CharField(max_length=50)),
				('market_values', models.TextField()),
				('last_modified', models.DateTimeField(auto_now_add=True)),
				('img', models.ImageField(null=True, upload_to='images/')),
			],
		),
	]
