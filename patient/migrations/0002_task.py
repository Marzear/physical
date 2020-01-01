# Generated by Django 2.2.3 on 2020-01-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patinet', models.CharField(help_text='病人ID', max_length=20)),
                ('kind', models.CharField(help_text='種類 ex. 抽血', max_length=20)),
                ('start_time', models.DateTimeField(help_text='起始時間')),
                ('doctor', models.CharField(help_text='醫生ID', max_length=20)),
            ],
        ),
    ]
