# Generated by Django 4.2.23 on 2025-06-11 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0004_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantidade', models.IntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='garagem.compra')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='garagem.veiculo')),
            ],
        ),
    ]
