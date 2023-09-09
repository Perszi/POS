from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_remove_movie_tags_movie_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
