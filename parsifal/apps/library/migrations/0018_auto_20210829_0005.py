# Generated by Django 3.2.6 on 2021-08-29 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20151009_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collaborator',
            options={'verbose_name': 'collaborator', 'verbose_name_plural': 'collaborators'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'document', 'verbose_name_plural': 'documents'},
        ),
        migrations.AlterModelOptions(
            name='documentfile',
            options={'verbose_name': 'document file', 'verbose_name_plural': 'document files'},
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'ordering': ('name',), 'verbose_name': 'folder', 'verbose_name_plural': 'folders'},
        ),
        migrations.AlterModelOptions(
            name='sharedfolder',
            options={'ordering': ('name',), 'verbose_name': 'shared folder', 'verbose_name_plural': 'shared folders'},
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='access',
            field=models.CharField(choices=[('R', 'Read'), ('W', 'Write'), ('A', 'Admin')], default='R', max_length=1),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='bibtexkey',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Bibtex key'),
        ),
        migrations.AlterField(
            model_name='document',
            name='crossref',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Cross-referenced'),
        ),
        migrations.AlterField(
            model_name='document',
            name='doi',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='DOI'),
        ),
        migrations.AlterField(
            model_name='document',
            name='entry_type',
            field=models.CharField(blank=True, choices=[('article', 'Article'), ('book', 'Book'), ('booklet', 'Booklet'), ('conference', 'Conference'), ('inbook', 'Inbook'), ('incollection', 'Incollection'), ('inproceedings', 'Inproceedings'), ('manual', 'Manual'), ('mastersthesis', "Master's Thesis"), ('misc', 'Misc'), ('phdthesis', 'Ph.D. Thesis'), ('proceedings', 'Proceedings'), ('techreport', 'Tech Report'), ('unpublished', 'Unpublished')], max_length=13, null=True, verbose_name='Document type'),
        ),
        migrations.AlterField(
            model_name='document',
            name='howpublished',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='How it was published'),
        ),
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='isbn',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='document',
            name='issn',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ISSN'),
        ),
        migrations.AlterField(
            model_name='document',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='documentfile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sharedfolder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
