from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('✓ Existing data cleared'))
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Assemble! The mightiest heroes of Earth united for fitness',
            total_points=0,
            member_count=0
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League: Fighting for fitness and justice',
            total_points=0,
            member_count=0
        )
        
        self.stdout.write(self.style.SUCCESS('✓ Teams created'))
        
        # Create Users (Superheroes)
        self.stdout.write('Creating superhero users...')
        
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'tony.stark@marvel.com', 'points': 850},
            {'name': 'Captain America', 'email': 'steve.rogers@marvel.com', 'points': 920},
            {'name': 'Thor', 'email': 'thor.odinson@marvel.com', 'points': 880},
            {'name': 'Black Widow', 'email': 'natasha.romanoff@marvel.com', 'points': 795},
            {'name': 'Hulk', 'email': 'bruce.banner@marvel.com', 'points': 760},
            {'name': 'Spider-Man', 'email': 'peter.parker@marvel.com', 'points': 845},
            {'name': 'Doctor Strange', 'email': 'stephen.strange@marvel.com', 'points': 720},
            {'name': 'Black Panther', 'email': 'tchalla@marvel.com', 'points': 890},
        ]
        
        dc_heroes = [
            {'name': 'Superman', 'email': 'clark.kent@dc.com', 'points': 950},
            {'name': 'Batman', 'email': 'bruce.wayne@dc.com', 'points': 930},
            {'name': 'Wonder Woman', 'email': 'diana.prince@dc.com', 'points': 910},
            {'name': 'The Flash', 'email': 'barry.allen@dc.com', 'points': 870},
            {'name': 'Aquaman', 'email': 'arthur.curry@dc.com', 'points': 810},
            {'name': 'Green Lantern', 'email': 'hal.jordan@dc.com', 'points': 785},
            {'name': 'Cyborg', 'email': 'victor.stone@dc.com', 'points': 740},
            {'name': 'Shazam', 'email': 'billy.batson@dc.com', 'points': 820},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team Marvel',
                total_points=hero['points']
            )
            marvel_users.append(user)
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team DC',
                total_points=hero['points']
            )
            dc_users.append(user)
        
        all_users = marvel_users + dc_users
        
        # Update team statistics
        team_marvel.member_count = len(marvel_users)
        team_marvel.total_points = sum(u.total_points for u in marvel_users)
        team_marvel.save()
        
        team_dc.member_count = len(dc_users)
        team_dc.total_points = sum(u.total_points for u in dc_users)
        team_dc.save()
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(all_users)} superhero users'))
        
        # Create Activities
        self.stdout.write('Creating activities...')
        
        activity_types = [
            {'type': 'Running', 'points_per_min': 2},
            {'type': 'Swimming', 'points_per_min': 3},
            {'type': 'Cycling', 'points_per_min': 2},
            {'type': 'Weight Training', 'points_per_min': 4},
            {'type': 'Yoga', 'points_per_min': 2},
            {'type': 'Boxing', 'points_per_min': 5},
            {'type': 'Martial Arts', 'points_per_min': 4},
            {'type': 'HIIT', 'points_per_min': 5},
        ]
        
        activities_created = 0
        for user in all_users:
            # Create 3-5 activities per user
            num_activities = random.randint(3, 5)
            for i in range(num_activities):
                activity_data = random.choice(activity_types)
                duration = random.randint(20, 90)
                points = duration * activity_data['points_per_min']
                
                # Create activity with date in the past week
                days_ago = random.randint(0, 7)
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_data['type'],
                    duration=duration,
                    points=points,
                )
                activities_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {activities_created} activities'))
        
        # Create Leaderboard
        self.stdout.write('Creating leaderboard...')
        
        # Sort users by points
        sorted_users = sorted(all_users, key=lambda u: u.total_points, reverse=True)
        
        for rank, user in enumerate(sorted_users, start=1):
            Leaderboard.objects.create(
                rank=rank,
                name=user.name,
                team=user.team,
                points=user.total_points
            )
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created leaderboard with {len(sorted_users)} entries'))
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        
        workouts_data = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity workout combining strength and endurance. Perfect for building peak human performance.',
                'difficulty': 'Advanced',
                'duration': 60,
                'points': 300,
                'category': 'Strength & Conditioning'
            },
            {
                'name': 'Web-Slinger Agility',
                'description': 'Improve flexibility and agility with dynamic movements and bodyweight exercises.',
                'difficulty': 'Intermediate',
                'duration': 45,
                'points': 225,
                'category': 'Agility'
            },
            {
                'name': 'Speedster Sprint Training',
                'description': 'Explosive speed and cardiovascular endurance training for maximum velocity.',
                'difficulty': 'Advanced',
                'duration': 40,
                'points': 280,
                'category': 'Cardio'
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Build strength, power, and combat readiness with this warrior-inspired routine.',
                'difficulty': 'Advanced',
                'duration': 55,
                'points': 320,
                'category': 'Strength'
            },
            {
                'name': 'Mystic Arts Meditation',
                'description': 'Focus your mind and body through guided meditation and yoga practices.',
                'difficulty': 'Beginner',
                'duration': 30,
                'points': 150,
                'category': 'Mindfulness'
            },
            {
                'name': 'Atlantean Swim Session',
                'description': 'Master the waters with this intense swimming and aquatic training program.',
                'difficulty': 'Intermediate',
                'duration': 50,
                'points': 250,
                'category': 'Swimming'
            },
            {
                'name': 'Dark Knight Combat Training',
                'description': 'Master martial arts and tactical combat skills with this comprehensive training.',
                'difficulty': 'Advanced',
                'duration': 70,
                'points': 350,
                'category': 'Martial Arts'
            },
            {
                'name': 'Gamma Strength Protocol',
                'description': 'Heavy lifting and power training to maximize strength gains.',
                'difficulty': 'Advanced',
                'duration': 65,
                'points': 340,
                'category': 'Powerlifting'
            },
            {
                'name': 'Asgardian Endurance Challenge',
                'description': 'Build godlike endurance with this grueling stamina-focused workout.',
                'difficulty': 'Expert',
                'duration': 90,
                'points': 450,
                'category': 'Endurance'
            },
            {
                'name': 'Stark Industries HIIT',
                'description': 'High-tech, high-intensity interval training for maximum efficiency.',
                'difficulty': 'Intermediate',
                'duration': 35,
                'points': 200,
                'category': 'HIIT'
            },
            {
                'name': 'Kryptonian Core Power',
                'description': 'Build a super-strong core with this focused abdominal training routine.',
                'difficulty': 'Intermediate',
                'duration': 30,
                'points': 180,
                'category': 'Core'
            },
            {
                'name': 'Wakandan Recovery Flow',
                'description': 'Gentle stretching and mobility work for active recovery and injury prevention.',
                'difficulty': 'Beginner',
                'duration': 25,
                'points': 125,
                'category': 'Recovery'
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(workouts_data)} workout suggestions'))
        
        # Summary
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard Entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write('')
        self.stdout.write(f'Team Marvel: {team_marvel.member_count} members, {team_marvel.total_points} points')
        self.stdout.write(f'Team DC: {team_dc.member_count} members, {team_dc.total_points} points')
        self.stdout.write(self.style.SUCCESS('=' * 60))
