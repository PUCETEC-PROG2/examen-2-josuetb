from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('year', models.IntegerField(max_length=4)),
                ('director', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('synopsis', models.TextField(max_length=50)),
            ],
        ),
    ]