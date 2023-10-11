import datetime
from datetime import date
import random

from django.core.management import BaseCommand
from django.db import transaction

from project_management.models import Organization, Department, User, Team, Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        with transaction.atomic():
            org = Organization.objects.create(
                title="Kementerian Keuangan",
                settings=dict(),
                status=1
            )

            for i in range(10):
                dept = Department.objects.create(
                    title=f"Department {i}",
                    settings=dict(),
                    status=1,
                    organization=org
                )

                for j in range(10):
                    user = dept.user.create(
                        name=f"User {j}",
                        settings=dict(),
                        status=1,
                        organization=org,
                    )

                for k in range(5):
                    team = Team.objects.create(
                        title=f"Team {k}",
                        settings=dict(),
                        status=1,
                        department=dept
                    )

                    for l in range(5):
                        user_id = random.randint(1, 10)
                        user = User.objects.get(id=user_id)
                        team.user.add(user)

                    for m in range(5):
                        project = Project.objects.create(
                            title=f"Project {m}",
                            settings=dict(),
                            status=1,
                            team=team
                        )

                        for n in range(5):
                            user_id = random.randint(1, 10)
                            user = User.objects.get(id=user_id)
                            project.user.add(user)

                        for o in range(5):
                            task = project.task.create(
                                title=f"Task {o}",
                                description=f"Description {o}",
                                start=date.today(),
                                end=date.today() + datetime.timedelta(days=5),
                                settings=dict(),
                                status=1,
                                project=project
                            )

                            for p in range(5):
                                user_id = random.randint(1, 10)
                                user = User.objects.get(id=user_id)
                                task.user.add(user)

            print("Done")
