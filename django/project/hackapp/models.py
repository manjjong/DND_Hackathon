from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('user_id',)
        db_table = 'User'

class Follow(models.Model):
    num = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id', related_name='OneSelf')
    target_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='target_id', related_name='Opponent')

    class Meta:
        ordering = ('num', 'user_id', 'target_id',)
        db_table = 'Follow'

class Challenge(models.Model):
    challenge_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.CharField(max_length=100, blank=True)
    contents = models.CharField(max_length=100)
    creator_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='creator_id')

    class Meta:
        ordering = ('challenge_id', 'name', 'start_date', 'end_date', 'image', 'contents', 'creator_id')
        db_table = 'Challenge'

class Challenge_User(models.Model):
    challenge_id = models.ForeignKey('Challenge', on_delete=models.CASCADE, db_column='challenge_id')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    start_date = models.DateField()
    num = models.AutoField(primary_key=True)

    class Meta:
        ordering = ('challenge_id', 'user_id', 'start_date', 'num')
        db_table = 'Challenge_User'

class Challenge_Check(models.Model):
    num = models.AutoField(primary_key=True)
    challenge_id = models.ForeignKey('Challenge', on_delete=models.CASCADE, db_column='challenge_id')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    check_date = models.DateField()    

    class Meta:
        ordering = ('num', 'challenge_id', 'user_id', 'check_date')
        db_table = 'Challenge_Check'