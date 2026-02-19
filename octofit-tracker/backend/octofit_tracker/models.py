from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=200)
    total_points = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    total_points = models.IntegerField(default=0)
    member_count = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField()
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    points = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
    
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    rank = models.IntegerField()
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    points = models.IntegerField()
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']
    
    def __str__(self):
        return f"{self.rank}. {self.name}"


class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    points = models.IntegerField()
    category = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
