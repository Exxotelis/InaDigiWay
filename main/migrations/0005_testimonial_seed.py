from django.db import migrations


def seed_testimonials(apps, schema_editor):
    Testimonial = apps.get_model("main", "Testimonial")
    if Testimonial.objects.exists():
        return
    Testimonial.objects.bulk_create(
        [
            Testimonial(
                name="Maria K.",
                role="Founder",
                company="Studio M",
                quote="The strategy and content were spot on. Our engagement doubled in a month.",
                sort_order=1,
            ),
            Testimonial(
                name="George P.",
                role="Marketing Manager",
                company="Aster Group",
                quote="Professional, fast, and creative. The new website converts much better.",
                sort_order=2,
            ),
            Testimonial(
                name="Elena T.",
                role="Owner",
                company="Bloom Boutique",
                quote="Beautiful visuals and clear messaging. We finally look premium online.",
                sort_order=3,
            ),
            Testimonial(
                name="Nikos L.",
                role="CEO",
                company="Northwave",
                quote="Excellent collaboration and measurable results from day one.",
                sort_order=4,
            ),
        ]
    )


def unseed_testimonials(apps, schema_editor):
    Testimonial = apps.get_model("main", "Testimonial")
    Testimonial.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_testimonial"),
    ]

    operations = [
        migrations.RunPython(seed_testimonials, unseed_testimonials),
    ]
