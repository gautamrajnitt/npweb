# Generated by Django 2.2.1 on 2020-03-22 09:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('navprayas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chess',
            name='category',
            field=models.CharField(choices=[('', 'select'), ('Junior', '10th Passout'), ('Senior', '12th Passout')], max_length=12, verbose_name='Category'),
        ),
        migrations.CreateModel(
            name='cc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('category', models.CharField(choices=[('', 'select'), ('Junior', '10th Passout'), ('Senior', '12th Passout')], max_length=12, verbose_name='Category')),
                ('contact', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)], verbose_name='Contact')),
                ('addess', models.CharField(max_length=100, verbose_name='Address')),
                ('cc_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
