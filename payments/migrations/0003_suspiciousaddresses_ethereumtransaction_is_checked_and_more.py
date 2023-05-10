# Generated by Django 4.2 on 2023-05-10 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0002_alter_ethereumtransaction_eth_timestamp"),
    ]

    operations = [
        migrations.CreateModel(
            name="SuspiciousAddresses",
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
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("1", "Suspicious Amount"),
                            ("2", "Suspicious Receiver"),
                            ("3", "Suspicious Sender"),
                            ("4", "Suspicious Gas Price"),
                            ("5", "Suspicious Gas Used"),
                            ("6", "Suspicious Transaction Fee"),
                            ("7", "Suspicious Timestamp"),
                            ("8", "Suspicious Block Number"),
                            ("9", "Multiple Transactions"),
                            ("10", "Suspicious Contract Creation"),
                            ("11", "Suspicious Transaction Hash"),
                            ("12", "Suspicious Transaction Index"),
                            ("13", "Suspicious Nonce"),
                            ("14", "Suspicious Input"),
                        ],
                        max_length=50,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "suspicious_addresses",
                "ordering": ["-timestamp"],
            },
        ),
        migrations.AddField(
            model_name="ethereumtransaction",
            name="is_checked",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="FlaggedTransaction",
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
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("1", "Suspicious Amount"),
                            ("2", "Suspicious Receiver"),
                            ("3", "Suspicious Sender"),
                            ("4", "Suspicious Gas Price"),
                            ("5", "Suspicious Gas Used"),
                            ("6", "Suspicious Transaction Fee"),
                            ("7", "Suspicious Timestamp"),
                            ("8", "Suspicious Block Number"),
                            ("9", "Multiple Transactions"),
                            ("10", "Suspicious Contract Creation"),
                            ("11", "Suspicious Transaction Hash"),
                            ("12", "Suspicious Transaction Index"),
                            ("13", "Suspicious Nonce"),
                            ("14", "Suspicious Input"),
                        ],
                        max_length=50,
                    ),
                ),
                ("is_flagged", models.BooleanField(default=False)),
                ("is_checked", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "transaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payments.ethereumtransaction",
                    ),
                ),
            ],
            options={
                "db_table": "flagged_transactions",
                "ordering": ["-timestamp"],
            },
        ),
    ]