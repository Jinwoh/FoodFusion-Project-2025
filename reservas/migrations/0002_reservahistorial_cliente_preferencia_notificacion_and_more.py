# Generated by Django 5.2 on 2025-06-18 19:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaHistorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('eliminado_en', models.DateTimeField()),
                ('creada_en', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'reserva_historial',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='preferencia_notificacion',
            field=models.CharField(choices=[('email', 'Correo'), ('whatsapp', 'WhatsApp'), ('ambos', 'Ambos')], default='email', max_length=10),
        ),
        migrations.AddField(
            model_name='reserva',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
