from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Activity, Team, Workout, Leaderboard
import random

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create superhero users
        self.stdout.write('Creating superhero users...')
        marvel_heroes = ['IronMan', 'CaptainAmerica', 'Thor', 'BlackWidow', 'Hulk']
        dc_heroes = ['Batman', 'Superman', 'WonderWoman', 'Flash', 'GreenLantern']
        
        all_users = []
        for hero in marvel_heroes + dc_heroes:
            user = User.objects.create_user(
                username=hero,
                email=f'{hero.lower()}@superheroes.com',
                password='hero1234'
            )
            all_users.append(user)

        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League Members'
        )

        # Add members to teams
        for hero in marvel_heroes:
            team_marvel.members.add(User.objects.get(username=hero))
        for hero in dc_heroes:
            team_dc.members.add(User.objects.get(username=hero))

        # Create activities
        self.stdout.write('Creating activities...')
        activities = [
            Activity.objects.create(name='Super Sprint', description='High-speed running', points=10),
            Activity.objects.create(name='Power Lifting', description='Strength training', points=15),
            Activity.objects.create(name='Sky Flying', description='Aerial exercises', points=20),
            Activity.objects.create(name='Combat Training', description='Fighting practice', points=25),
            Activity.objects.create(name='Endurance Challenge', description='Long-duration training', points=30),
        ]

        # Create workouts
        self.stdout.write('Creating workouts...')
        for user in all_users:
            for _ in range(5):  # 5 workouts per user
                activity = random.choice(activities)
                duration = random.randint(15, 120)
                points = activity.points * (duration // 15)
                Workout.objects.create(
                    user=user,
                    activity=activity,
                    duration=duration,
                    points_earned=points,
                    completed_at=timezone.now()
                )

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in all_users:
            total_points = sum(w.points_earned for w in user.workouts.all())
            team = team_marvel if user.username in marvel_heroes else team_dc
            Leaderboard.objects.create(
                user=user,
                team=team,
                total_points=total_points,
                rank=0  # Will be updated later
            )

        # Update ranks
        for i, entry in enumerate(Leaderboard.objects.all().order_by('-total_points')):
            entry.rank = i + 1
            entry.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))