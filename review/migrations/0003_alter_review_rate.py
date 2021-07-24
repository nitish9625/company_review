# Generated by Django 3.2.5 on 2021-07-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.CharField(choices=[('1', '1️⃣'), ('2', '2️⃣'), ('3', '3️⃣'), ('4', '4️⃣'), ('5', '5️⃣'), ('6', '6️⃣'), ('7', '7️⃣'), ('8', '8️⃣'), ('9', '9️⃣'), ('10', '🔟')], max_length=10),
        ),
    ]
