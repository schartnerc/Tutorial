from django.db import models


class CheckQuestion(models.Model):
    check_id = models.IntegerField(primary_key=True)
    equip_id = models.IntegerField(blank=True, null=True)
    check_type = models.TextField(blank=True, null=True)
    check_text = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'check_question'


class CheckClassroom(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_short_name = models.CharField(max_length=64, blank=True, null=True)
    room_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'check_classroom'
