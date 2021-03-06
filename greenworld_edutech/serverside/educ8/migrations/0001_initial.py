
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScholasticDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_to_school', models.BooleanField()),
                ('current_class', models.IntegerField()),
                ('class_last_year', models.IntegerField()),
                ('years_in_current_school', models.IntegerField()),
                ('current_school_shift', models.IntegerField()),
                ('is_english_subject', models.BooleanField()),
                ('break_more_than_three_weeks', models.BooleanField()),
                ('last_grade_dropout', models.IntegerField()),
                ('is_private_tuition', models.BooleanField()),
                ('tuition_fees', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=20)),
                ('school_type', models.CharField(max_length=20)),
                ('study_medium', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('student_img', models.CharField(max_length=1000)),
                ('registration_date', models.DateField()),
                ('year_of_birth', models.IntegerField()),
                ('birth_date', models.DateField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('aadhar', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator('^\\d{12}$', 'Number must be 12 digits', 'Invalid aadhaar')])),
            ],
        ),
        migrations.AddField(
            model_name='scholasticdetail',
            name='current_school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educ8.School'),
        ),
        migrations.AddField(
            model_name='scholasticdetail',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educ8.Student'),
        ),
    ]
