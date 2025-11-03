"""Management command to delete a feature after implementation."""

from __future__ import annotations

from django.core.management.base import BaseCommand, CommandError

from main.models import Feature


class Command(BaseCommand):
    """Delete a feature by ID after it has been implemented."""

    help = "Delete a feature by ID after it has been implemented"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "feature_id",
            type=int,
            help="The ID of the feature to delete",
        )

    def handle(self, *args, **options) -> None:
        feature_id = options["feature_id"]

        try:
            feature = Feature.objects.get(id=feature_id)
        except Feature.DoesNotExist:
            raise CommandError(f"Feature with ID {feature_id} does not exist")

        feature_title = feature.title
        feature.delete()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully deleted feature "{feature_title}" (ID: {feature_id})'
            )
        )
