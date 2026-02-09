from django.db import migrations


def copy_quote_to_en(apps, schema_editor):
    Testimonial = apps.get_model("main", "Testimonial")
    for item in Testimonial.objects.all():
        if not item.quote_en and item.quote:
            item.quote_en = item.quote
            item.save(update_fields=["quote_en"])


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_testimonial_quote_el_testimonial_quote_en_and_more"),
    ]

    operations = [
        migrations.RunPython(copy_quote_to_en, noop_reverse),
    ]
