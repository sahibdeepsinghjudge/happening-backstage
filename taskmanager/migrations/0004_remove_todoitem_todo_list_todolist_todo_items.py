# Generated by Django 4.2 on 2024-09-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskmanager", "0003_task_end_date_task_priority_task_start_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todoitem",
            name="todo_list",
        ),
        migrations.AddField(
            model_name="todolist",
            name="todo_items",
            field=models.ManyToManyField(
                related_name="todo_list", to="taskmanager.todoitem"
            ),
        ),
    ]
