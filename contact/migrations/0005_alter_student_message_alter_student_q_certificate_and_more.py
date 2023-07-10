# Generated by Django 4.1.7 on 2023-07-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_rename_students_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='message',
            field=models.TextField(null=True, verbose_name='Tell us more about you, and how you want us to help you with this course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='q_certificate',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], default='Maybe', max_length=150, verbose_name='Souhaiteriez-vous obtenir un certificat?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='q_hearing_us',
            field=models.CharField(choices=[('Site Web', 'Site Web'), ('Amis', 'Amis'), ('Email', 'Email'), ('Whatsapp', 'Whatsapp'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('Television', 'Television')], default='2,500 - 3,500 HTG', max_length=150, verbose_name='Comment avez-vous entendu parler de cet événement?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='q_laptop',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], default='Yes', max_length=150, verbose_name='Avez-vous un laptop?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='q_price',
            field=models.CharField(choices=[('2,500 - 3,500 HTG', '2,500 - 3,500 HTG'), ('3,500 - 5,500 HTG', '3,500 - 5,500 HTG'), ('5,500 - 10,500 HTG', '5,500 - 10,500 HTG'), ('10,500 HTG +', '10,500 HTG +')], default='3,500 - 5,500 HTG', max_length=150, verbose_name='Combien esperez vous la participation?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='q_wish',
            field=models.CharField(choices=[('En ligne', 'En ligne'), ('En presentiel', 'En presentiel')], default='3,500 - 5,500 HTG', max_length=150, verbose_name='Comment souhaiteriez-vous participer a ce cours?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='set_schedule',
            field=models.CharField(choices=[('Samedi - 9h - 17h', 'Samedi - 9h - 17h'), ('Dimanche - 9h - 17h', 'Dimanche - 9h - 17h'), ('Samedi - 9h - 12h et Dimanche - 9h - 12h', 'Samedi - 9h - 12h et Dimanche - 9h - 12h')], default='5,500 - 10,500 HTG', max_length=150, verbose_name='Quelle horaire vous serait confortable?'),
        ),
    ]
