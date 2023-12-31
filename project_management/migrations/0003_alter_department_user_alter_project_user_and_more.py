# Generated by Django 4.2.6 on 2023-10-08 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0002_alter_department_user_alter_project_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='user',
            field=models.ManyToManyField(related_name='department_user', to='project_management.user'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(related_name='project_user', to='project_management.user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='project_management.project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ManyToManyField(related_name='task_user', to='project_management.user'),
        ),
        migrations.AlterField(
            model_name='team',
            name='user',
            field=models.ManyToManyField(related_name='team_user', to='project_management.user'),
        ),
    ]
