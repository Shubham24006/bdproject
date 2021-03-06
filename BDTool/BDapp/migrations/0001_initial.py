# Generated by Django 2.0.7 on 2018-07-26 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('skype_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('url_name', models.CharField(max_length=100)),
                ('domain_name', models.CharField(max_length=100)),
                ('project_desrciption', models.CharField(max_length=1000)),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ('project_name',),
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.ManyToManyField(related_name='technology', to='BDapp.Technology'),
        ),
        migrations.AddField(
            model_name='client',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='BDapp.Project'),
        ),
    ]
