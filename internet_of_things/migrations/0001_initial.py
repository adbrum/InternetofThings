# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('dateManufacture', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('peripherals', models.CharField(max_length=50)),
                ('GPIO', models.IntegerField()),
                ('equipment', models.ForeignKey(to='internet_of_things.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hdmi', models.BooleanField(default=False)),
                ('USBPorts', models.CharField(max_length=50)),
                ('videoInput', models.CharField(max_length=50)),
                ('videoOutputs', models.CharField(max_length=50)),
                ('audioInputs', models.CharField(max_length=50)),
                ('audioOutputs', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=50)),
                ('network', models.CharField(max_length=50)),
                ('jack', models.CharField(max_length=50)),
                ('digitalIOPins', models.IntegerField()),
                ('analogInputPins', models.IntegerField()),
                ('equipment', models.ForeignKey(to='internet_of_things.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('RAM', models.IntegerField()),
                ('SRAM', models.IntegerField()),
                ('EEPROM', models.IntegerField()),
                ('flashMemory', models.IntegerField()),
                ('equipment', models.ForeignKey(to='internet_of_things.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OperationSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=50)),
                ('equipment', models.ForeignKey(to='internet_of_things.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhysicalCharacteristics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('weight', models.IntegerField()),
                ('equipment', models.ForeignKey(to='internet_of_things.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CPU', models.CharField(max_length=100)),
                ('GPU', models.CharField(max_length=100)),
                ('equipment', models.ForeignKey(to='internet_of_things.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voltage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operatingVoltage', models.IntegerField()),
                ('IOCurrentMax', models.IntegerField()),
                ('inputVoltageRecommended', models.IntegerField()),
                ('DCCurrentperIOPin', models.IntegerField()),
                ('DCCurrentfor3_3VPin', models.IntegerField()),
                ('powerRatings', models.CharField(max_length=50)),
                ('powerSource', models.CharField(max_length=50)),
                ('equipment', models.ForeignKey(to='internet_of_things.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='accessories',
            name='equipment',
            field=models.ForeignKey(to='internet_of_things.Equipment'),
            preserve_default=True,
        ),
    ]
