# Generated by Django 4.2 on 2023-05-10 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0004_flaggedtransaction_receiver_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AddressFrequency",
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
                ("address", models.CharField(max_length=42)),
                ("times_sender", models.IntegerField(default=0)),
                ("times_receiver", models.IntegerField(default=0)),
                ("last_transaction", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "frequent_addresses",
                "ordering": ["-last_transaction"],
            },
        ),
        migrations.AddField(
            model_name="ethereumtransaction",
            name="is_update_checked",
            field=models.BooleanField(default=False),
        ),
    ]