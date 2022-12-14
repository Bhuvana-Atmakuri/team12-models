# Generated by Django 4.1.1 on 2022-12-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hositality', '0015_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('On The Way', 'On The Way')], default='Pending', max_length=50),
        ),
    ]
