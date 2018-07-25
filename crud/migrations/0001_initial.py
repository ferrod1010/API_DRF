# Generated by Django 2.0.6 on 2018-07-19 19:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField(default=django.utils.timezone.now, null=True)),
                ('autor', models.CharField(blank=True, max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paginas', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]