from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='Model',
            name='tags',
        ),
        migrations.AddField(
            model_name='Model',
            name='tags',
            field=models.ManyToManyField(to='Core.tag'),
        ),
    ]
