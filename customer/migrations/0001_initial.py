# Generated by Django 5.0.3 on 2024-04-03 09:45

import customer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BCCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.CharField(max_length=10, unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('SearchName', models.CharField(max_length=100)),
                ('Name2', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Address2', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=100)),
                ('PhoneNo', models.CharField(max_length=15)),
                ('TelexNo', models.CharField(max_length=100)),
                ('Blocked', models.CharField(max_length=100)),
                ('DocumentSendingProfile', models.CharField(max_length=100)),
                ('ShiptoCode', models.CharField(max_length=10)),
                ('OurAccountNo', models.CharField(max_length=100)),
                ('TerritoryCode', models.CharField(max_length=100)),
                ('GlobalDimension1Code', models.CharField(max_length=100)),
                ('GlobalDimension2Code', models.CharField(max_length=100)),
                ('ChainName', models.CharField(max_length=100)),
                ('BudgetedAmount', models.IntegerField(default=0)),
                ('CreditLimitLCY', models.IntegerField(default=0)),
                ('CustomerPostingGroup', models.CharField(max_length=100)),
                ('CurrencyCode', models.CharField(max_length=100)),
                ('CustomerPriceGroup', models.CharField(max_length=100)),
                ('LanguageCode', models.CharField(max_length=100)),
                ('RegistrationNumber', models.CharField(max_length=100)),
                ('StatisticsGroup', models.IntegerField(default=0)),
                ('PaymentTermsCode', models.CharField(max_length=100)),
                ('SalespersonCode', models.CharField(max_length=100)),
                ('ShipmentMethodCode', models.CharField(max_length=100)),
                ('PlaceofExport', models.CharField(max_length=100)),
                ('CustomerDiscGroup', models.CharField(max_length=100)),
                ('CountryRegionCode', models.CharField(max_length=100)),
                ('Amount', models.IntegerField(default=0)),
                ('DebitAmount', models.IntegerField(default=0)),
                ('CreditAmount', models.IntegerField(default=0)),
                ('InvoiceAmounts', models.IntegerField(default=0)),
                ('OtherAmountsLCY', models.IntegerField(default=0)),
                ('Comment', models.BooleanField(default=False)),
                ('LastStatementNo', models.IntegerField(default=0)),
                ('Prepayment', models.IntegerField(default=0)),
                ('PartnerType', models.CharField(max_length=100)),
                ('Payments', models.IntegerField(default=0)),
                ('PostCode', models.CharField(max_length=100)),
                ('PrintStatements', models.BooleanField(default=False)),
                ('PricesIncludingVAT', models.BooleanField(default=False)),
                ('ProfitLCY', models.IntegerField(default=0)),
                ('BilltoCustomerNo', models.CharField(max_length=100)),
                ('Priority', models.IntegerField(default=0)),
                ('PaymentMethodCode', models.CharField(max_length=100)),
                ('LastModifiedDateTime', models.DateTimeField()),
                ('GlobalDimension1Filter', models.CharField(max_length=100)),
                ('GlobalDimension2Filter', models.CharField(max_length=100)),
                ('Balance', models.IntegerField(default=0)),
                ('BalanceLCY', models.IntegerField(default=0)),
                ('BalanceDue', models.IntegerField(default=0)),
                ('NetChange', models.IntegerField(default=0)),
                ('NetChangeLCY', models.IntegerField(default=0)),
                ('SalesLCY', models.IntegerField(default=0)),
                ('InvAmountsLCY', models.IntegerField(default=0)),
                ('InvDiscountsLCY', models.IntegerField(default=0)),
                ('NoofInvoices', models.IntegerField(default=0)),
                ('InvoiceDiscCode', models.CharField(max_length=100)),
                ('InvoiceCopies', models.IntegerField(default=0)),
                ('PmtDiscountsLCY', models.IntegerField(default=0)),
                ('PmtToleranceLCY', models.IntegerField(default=0)),
                ('BalanceDueLCY', models.IntegerField(default=0)),
                ('PaymentsLCY', models.IntegerField(default=0)),
                ('CrMemoAmounts', models.IntegerField(default=0)),
                ('CrMemoAmountsLCY', models.IntegerField(default=0)),
                ('FinanceChargeMemoAmounts', models.IntegerField(default=0)),
                ('ShippedNotInvoiced', models.IntegerField(default=0)),
                ('ShippedNotInvoicedLCY', models.IntegerField(default=0)),
                ('ShippingAgentCode', models.CharField(max_length=100)),
                ('ApplicationMethod', models.CharField(max_length=100)),
                ('LocationCode', models.CharField(max_length=100)),
                ('FaxNo', models.CharField(max_length=100)),
                ('VATBusPostingGroup', models.CharField(max_length=100)),
                ('VATRegistrationNo', models.CharField(max_length=100)),
                ('CombineShipments', models.BooleanField(default=False)),
                ('GenBusPostingGroup', models.CharField(max_length=100)),
                ('GLN', models.CharField(max_length=100)),
                ('County', models.CharField(max_length=100)),
                ('EMail', models.EmailField(max_length=100)),
                ('EORINumber', models.CharField(max_length=100)),
                ('UseGLNinElectronicDocument', models.BooleanField(default=False)),
                ('ReminderTermsCode', models.CharField(max_length=100)),
                ('ReminderAmounts', models.IntegerField(default=0)),
                ('ReminderAmountsLCY', models.IntegerField(default=0)),
                ('TaxAreaCode', models.CharField(max_length=100)),
                ('TaxAreaID', models.CharField(max_length=100)),
                ('TaxLiable', models.BooleanField(default=False)),
                ('CurrencyFilter', models.CharField(max_length=100)),
                ('EnterpriseNo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('addressLine1', models.CharField(blank=True, max_length=200, null=True)),
                ('addressLine2', models.CharField(blank=True, max_length=200, null=True)),
                ('region_code', models.CharField(blank=True, max_length=5, null=True)),
                ('language_code', models.CharField(blank=True, max_length=5, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('enterprise_no', models.CharField(blank=True, max_length=200, null=True)),
                ('CustomerPriceGroup', models.CharField(blank=True, max_length=100, null=True)),
                ('Vat', models.CharField(blank=True, max_length=100, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=50, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_phoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_id', models.CharField(max_length=550, unique=True)),
                ('blocked', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', customer.models.CustomUserManager()),
            ],
        ),
    ]
