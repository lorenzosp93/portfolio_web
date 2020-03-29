"Define models for the resume app"
from django.db import models
from .base_models import (
    TimeStampable,
    Datable,
    Localizable,
    Attachable,
    Described,
    Named
)

class Company(Named):
    "Model for Company, to be referenced by Education and Experience instances"
    logo = models.ImageField(upload_to='logos/', blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

class Project(Named, Described, Attachable, TimeStampable):
    "Model to define projects during Education"

class CVEntry(Named, Datable, TimeStampable,
              Localizable, Described, Attachable):
    "Abstract model for CV entries"

    company = models.ManyToManyField(
        Company,
    )

    project = models.ManyToManyField(
        Project,
    )

    class Meta:
        abstract = True

class Education(CVEntry):
    "Model for Education entries"

class Experience(CVEntry):
    "Model for Experience entries"
    department = models.CharField(max_length=100, blank=True)
    key_achievements = models.TextField(blank=True)


class SkillCategory(Named, Described):
    "Model to capture categories for skills"

class Skill(Named, TimeStampable):
    "Model for individual skills instances"
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
    )
    url = models.URLField()
    level = models.IntegerField(choices=(
        (1, 'basic'),
        (2, 'advanced'),
        (3, 'expert'),
        (4, 'professional')
    ))