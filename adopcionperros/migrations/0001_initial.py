# Generated by Django 2.1.2 on 2018-10-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagen', models.ImageField(upload_to='upload')),
                ('NombreMascota', models.CharField(max_length=20)),
                ('RazaPredominante', models.CharField(max_length=15)),
                ('Descripcion', models.TextField()),
                ('ESTADO', models.CharField(choices=[('R', 'Rescatado'), ('D', 'Disponible'), ('A', 'Adoptado')], default='R', max_length=1)),
                ('FechaPublicado', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
