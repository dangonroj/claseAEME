# Generated by Django 3.1.6 on 2021-02-19 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('creditos', models.IntegerField()),
                ('curso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('presentado', models.BooleanField(default=False)),
                ('fecha', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.alumno')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.asignatura')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesores',
            field=models.ManyToManyField(to='master.Profesor'),
        ),
    ]