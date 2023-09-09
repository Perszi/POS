from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_movie_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
