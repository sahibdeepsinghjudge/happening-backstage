# Generated by Django 4.2 on 2024-09-07 21:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_teammember_email_alter_teammember_user"),
        ("createevent", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eventdetails",
            old_name="guests",
            new_name="event_cateogry",
        ),
        migrations.RemoveField(
            model_name="eventdetails",
            name="price",
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2024, 9, 7, 21, 44, 27, 847323, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.businessaccount",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="event_date",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="event_time",
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="events"),
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="location",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.teammanager",
            ),
        ),
        migrations.AlterField(
            model_name="eventdetails",
            name="details",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="eventdetails",
            name="name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name="EventTickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("is_sold_out", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="createevent.eventdetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EventGuests",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=30)),
                ("description", models.CharField(blank=True, max_length=2000)),
                ("image", models.ImageField(blank=True, null=True, upload_to="events")),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="createevent.eventdetails",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="eventdetails",
            name="tickets",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="createevent.eventtickets",
            ),
        ),
    ]
