# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AccAddDetail(models.Model):
    account = models.ForeignKey('Guide', primary_key=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    date5 = models.DateField(blank=True, null=True)
    date6 = models.DateField(blank=True, null=True)
    date7 = models.DateField(blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    name5 = models.CharField(max_length=100, blank=True, null=True)
    name6 = models.CharField(max_length=100, blank=True, null=True)
    name7 = models.CharField(max_length=100, blank=True, null=True)
    num1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    l_var_char = models.TextField(blank=True, null=True)
    name8 = models.CharField(max_length=100, blank=True, null=True)
    jop = models.CharField(max_length=30, blank=True, null=True)
    national = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    shoon = models.CharField(max_length=12, blank=True, null=True)
    tarkhes = models.CharField(max_length=12, blank=True, null=True)
    op_balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    credit_days_flage = models.IntegerField(blank=True, null=True)
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    date_flage = models.IntegerField(blank=True, null=True)
    discount_ratio = models.IntegerField(blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    sector = models.CharField(max_length=20, blank=True, null=True)
    gada = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    flat = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    supno = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    descreption1 = models.CharField(max_length=150, blank=True, null=True)
    desc2 = models.CharField(max_length=100, blank=True, null=True)
    desc3 = models.CharField(max_length=100, blank=True, null=True)
    desc4 = models.CharField(max_length=150, blank=True, null=True)
    amount1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    currancy = models.IntegerField(blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    taamen_co = models.CharField(max_length=100, blank=True, null=True)
    datofcredit = models.DateField(blank=True, null=True)
    bolesa = models.CharField(max_length=30, blank=True, null=True)
    policydate = models.DateField(blank=True, null=True)
    tagded1 = models.DateField(blank=True, null=True)
    tagded2 = models.DateField(blank=True, null=True)
    tagded3 = models.DateField(blank=True, null=True)
    ex_rate = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    v1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v8 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v9 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v10 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v11 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v12 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    vc9 = models.CharField(max_length=100, blank=True, null=True)
    vc10 = models.CharField(max_length=100, blank=True, null=True)
    vc11 = models.CharField(max_length=100, blank=True, null=True)
    vc12 = models.CharField(max_length=100, blank=True, null=True)
    lc_notes = models.TextField(blank=True, null=True)
    conditions = models.CharField(max_length=30, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    v13 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    per = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    invoice_no = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    lc_status = models.IntegerField(blank=True, null=True)
    itmarrvdate = models.DateField(blank=True, null=True)
    lc_accno = models.BigIntegerField(blank=True, null=True)
    reset = models.IntegerField(blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    costcenter_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cash_exp = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    check_exp = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    inst_acceptlessthanminval = models.NullBooleanField()
    balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    isbranch = models.NullBooleanField()
    luv = models.IntegerField(blank=True, null=True)
    pcenter = models.NullBooleanField()
    ob_balance_f = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    ob_balance_curr = models.IntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    test = models.CharField(max_length=500, blank=True, null=True)
    route = models.IntegerField(blank=True, null=True)
    vendor_priority = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_add_detail'


class AccBudgEstAccAnn(models.Model):
    budget = models.ForeignKey('AccBudget')
    account_id = models.BigIntegerField()
    financial_year_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budg_est_acc_ann'
        unique_together = (('budget_id', 'account_id', 'financial_year_id'),)


class AccBudgEstAccCostAnn(models.Model):
    budget = models.ForeignKey('AccBudget')
    account_id = models.BigIntegerField()
    costcenter = models.ForeignKey('Cost2')
    financial_year_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budg_est_acc_cost_ann'
        unique_together = (('budget_id', 'account_id', 'costcenter_id', 'financial_year_id'),)


class AccBudgEstAccCostMonth(models.Model):
    year_no = models.IntegerField()
    month_no = models.IntegerField()
    account_id = models.BigIntegerField()
    costcenter = models.ForeignKey('Cost2')
    budget = models.ForeignKey('AccBudget')
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budg_est_acc_cost_month'
        unique_together = (('year_no', 'month_no', 'account_id', 'costcenter_id', 'budget_id'),)


class AccBudgEstAccMonth(models.Model):
    year_no = models.IntegerField()
    month_no = models.IntegerField()
    account_id = models.FloatField()
    budget = models.ForeignKey('AccBudget')
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budg_est_acc_month'
        unique_together = (('year_no', 'month_no', 'account_id', 'budget_id'),)


class AccBudgEstCostcntrAnn(models.Model):
    budget = models.ForeignKey('AccBudget')
    costcenter = models.ForeignKey('Cost2')
    financial_year_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budg_est_costcntr_ann'
        unique_together = (('budget_id', 'costcenter_id', 'financial_year_id'),)


class AccBudgEstCostcntrMonth(models.Model):
    year_no = models.IntegerField()
    month_no = models.IntegerField()
    costcenter = models.ForeignKey('Cost2')
    budget = models.ForeignKey('AccBudget')
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budg_est_costcntr_month'
        unique_together = (('year_no', 'month_no', 'costcenter_id', 'budget_id'),)


class AccBudget(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    name_e = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'acc_budget'


class AccBudgetEstimateAccountAn(models.Model):
    budget_id = models.IntegerField()
    account_id = models.BigIntegerField()
    financial_year_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budget_estimate_account_an'
        unique_together = (('budget_id', 'account_id', 'financial_year_id'),)


class AccBudgetEstimateAccountC2(models.Model):
    year_no = models.IntegerField()
    month_no = models.IntegerField()
    account_id = models.BigIntegerField()
    costcenter_id = models.DecimalField(max_digits=20, decimal_places=5)
    budget_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budget_estimate_account_c2'
        unique_together = (('year_no', 'month_no', 'account_id', 'costcenter_id', 'budget_id'),)


class AccBudgetEstimateAccountCo(models.Model):
    budget_id = models.IntegerField()
    account_id = models.BigIntegerField()
    costcenter_id = models.DecimalField(max_digits=20, decimal_places=5)
    financial_year_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budget_estimate_account_co'
        unique_together = (('budget_id', 'account_id', 'costcenter_id', 'financial_year_id'),)


class AccBudgetEstimateAccountMo(models.Model):
    year_no = models.IntegerField()
    month_no = models.IntegerField()
    account_id = models.BigIntegerField()
    budget_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budget_estimate_account_mo'
        unique_together = (('year_no', 'month_no', 'account_id', 'budget_id'),)


class AccBudgetEstimateCostcente2(models.Model):
    year_no = models.IntegerField()
    month_no = models.IntegerField()
    costcenter = models.ForeignKey('Cost2')
    budget = models.ForeignKey(AccBudget)
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budget_estimate_costcente2'
        unique_together = (('year_no', 'month_no', 'costcenter_id', 'budget_id'),)


class AccBudgetEstimateCostcenter(models.Model):
    budget = models.ForeignKey(AccBudget)
    costcenter = models.ForeignKey('Cost2')
    financial_year_id = models.IntegerField()
    debit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budget_estimate_costcenter'
        unique_together = (('budget_id', 'costcenter_id', 'financial_year_id'),)


class AccBudgetMonthly(models.Model):
    bud_id = models.CharField(max_length=15)
    bud_type = models.NullBooleanField()
    amount1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    accno = models.BigIntegerField()
    finan_year = models.IntegerField()
    acc_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_budget_monthly'
        unique_together = (('bud_id', 'accno', 'finan_year'),)


class AccCheckDesign(models.Model):
    account_no = models.BigIntegerField(primary_key=True)
    check_design = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_check_design'


class AccCostcenterAccount(models.Model):
    costcenter_no = models.ForeignKey('Cost2', db_column='costcenter_no')
    account_no = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'acc_costcenter_account'
        unique_together = (('costcenter_no', 'account_no'),)


class AccCostcenterDistribution(models.Model):
    from_costcenter_no = models.ForeignKey('Cost2', db_column='from_costcenter_no')
    to_costcenter_no = models.ForeignKey('Cost2', db_column='to_costcenter_no')
    percentage = models.DecimalField(max_digits=18, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'acc_costcenter_distribution'
        unique_together = (('from_costcenter_no', 'to_costcenter_no'),)


class AccGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    description = models.CharField(max_length=100)
    notes = models.CharField(max_length=200, blank=True, null=True)
    description_e = models.CharField(max_length=100)
    rep_syntax = models.TextField(blank=True, null=True)
    sort_id = models.FloatField(blank=True, null=True)
    typ = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_groups'


class AccInvoicepay(models.Model):
    id = models.DecimalField(max_digits=20, decimal_places=5)
    reset = models.IntegerField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    branch = models.IntegerField()
    serial = models.IntegerField()
    payed = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    payed_reset = models.IntegerField(blank=True, null=True)
    payed_reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    payed_branch = models.IntegerField(blank=True, null=True)
    payed_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    payed_f = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_invoicepay'
        unique_together = (('id', 'reset', 'reset_id', 'branch', 'serial'),)


class AccKafalatType(models.Model):
    code = models.IntegerField(primary_key=True)
    namear = models.CharField(max_length=30, blank=True, null=True)
    nameen = models.CharField(max_length=30, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_kafalat_type'


class AccLcAmount(models.Model):
    accno = models.BigIntegerField()
    id = models.IntegerField()
    modify_date = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=3)
    branch = models.IntegerField(blank=True, null=True)
    reset = models.IntegerField(blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_lc_amount'
        unique_together = (('accno', 'id'),)


class AccLoanDetail(models.Model):
    accno = models.BigIntegerField()
    id = models.IntegerField()
    date_crd = models.DateField(blank=True, null=True)
    value_crd = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    crd_flag = models.CharField(max_length=1, blank=True, null=True)
    rest_amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    profit_amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    deserved_amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_loan_detail'
        unique_together = (('accno', 'id'),)


class AccMasterDepositType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    name_e = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_master_deposit_type'


class AccMasterDocument(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=150)
    name_e = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'acc_master_document'


class AccMasterSalesrepExpenses(models.Model):
    accno = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'acc_master_salesrep_expenses'


class AccNotesLabels(models.Model):
    c1_label = models.CharField(primary_key=True, max_length=20)
    c2_label = models.CharField(max_length=20, blank=True, null=True)
    c3_label = models.CharField(max_length=20, blank=True, null=True)
    c4_label = models.CharField(max_length=20, blank=True, null=True)
    c5_label = models.CharField(max_length=20, blank=True, null=True)
    c6_label = models.CharField(max_length=20, blank=True, null=True)
    c7_label = models.CharField(max_length=20, blank=True, null=True)
    n1_label = models.CharField(max_length=20, blank=True, null=True)
    n2_label = models.CharField(max_length=20, blank=True, null=True)
    n3_label = models.CharField(max_length=20, blank=True, null=True)
    n4_label = models.CharField(max_length=20, blank=True, null=True)
    n5_label = models.CharField(max_length=20, blank=True, null=True)
    n6_label = models.CharField(max_length=20, blank=True, null=True)
    n7_label = models.CharField(max_length=20, blank=True, null=True)
    l1_label = models.CharField(max_length=20, blank=True, null=True)
    l2_label = models.CharField(max_length=20, blank=True, null=True)
    l3_label = models.CharField(max_length=20, blank=True, null=True)
    l4_label = models.CharField(max_length=20, blank=True, null=True)
    l5_label = models.CharField(max_length=20, blank=True, null=True)
    l6_label = models.CharField(max_length=20, blank=True, null=True)
    l7_label = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_notes_labels'


class AccPaymentCategory(models.Model):
    category = models.ForeignKey(AccGroups, primary_key=True)
    allow = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'acc_payment_category'


class AccSalesrepExpensesCustome2(models.Model):
    no = models.BigIntegerField(primary_key=True)
    order_date = models.DateField()
    operation_no = models.ForeignKey('Cost2', db_column='operation_no')
    customer_accno = models.CharField(max_length=40)
    notes = models.CharField(max_length=250, blank=True, null=True)
    reset = models.IntegerField(blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    salesrep_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_custome2'


class AccSalesrepExpensesCustomer(models.Model):
    header_no = models.ForeignKey(AccSalesrepExpensesCustome2, db_column='header_no')
    invoice_no = models.BigIntegerField()
    notes = models.CharField(max_length=250, blank=True, null=True)
    id = models.IntegerField()
    expensis_type = models.CharField(max_length=14, blank=True, null=True)
    add_expensis = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    add_expensis_accno = models.CharField(max_length=34, blank=True, null=True)
    expensis_amt = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_customer'
        unique_together = (('header_no', 'id'),)


class AccSalesrepExpensesDetail(models.Model):
    header_no = models.ForeignKey('AccSalesrepExpensesHeader', db_column='header_no')
    no = models.IntegerField()
    expense_type = models.CharField(max_length=32, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=5)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_detail'
        unique_together = (('header_no', 'no'),)


class AccSalesrepExpensesHeader(models.Model):
    no = models.BigIntegerField(primary_key=True)
    invoice_date = models.DateField()
    customer_accno = models.CharField(max_length=32)
    notes = models.CharField(max_length=250, blank=True, null=True)
    salesrep_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    operation_no = models.ForeignKey('Cost2', db_column='operation_no')

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_header'


class AccSalesrepExpensesOrdDet(models.Model):
    header_no = models.BigIntegerField()
    invoice_no = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_ord_det'
        unique_together = (('header_no', 'invoice_no'),)


class AccSalesrepExpensesOrdHdr(models.Model):
    no = models.BigIntegerField(primary_key=True)
    order_date = models.DateField()
    notes = models.CharField(max_length=250, blank=True, null=True)
    salesrep_id = models.DecimalField(max_digits=20, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_ord_hdr'


class AccSalesrepExpensesOrderDe(models.Model):
    header_no = models.ForeignKey('AccSalesrepExpensesOrderHe', db_column='header_no')
    invoice_no = models.ForeignKey(AccSalesrepExpensesHeader, db_column='invoice_no')

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_order_de'
        unique_together = (('header_no', 'invoice_no'),)


class AccSalesrepExpensesOrderHe(models.Model):
    no = models.BigIntegerField(primary_key=True)
    order_date = models.DateField()
    notes = models.CharField(max_length=250, blank=True, null=True)
    salesrep = models.ForeignKey('SalesMen')

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_order_he'


class AccSalesrepExpensesOrderP2(models.Model):
    no = models.BigIntegerField(primary_key=True)
    order_date = models.DateField()
    notes = models.CharField(max_length=250, blank=True, null=True)
    reset = models.IntegerField(blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_order_p2'


class AccSalesrepExpensesOrderPa(models.Model):
    header_no = models.ForeignKey(AccSalesrepExpensesOrderP2, db_column='header_no')
    order_no = models.ForeignKey(AccSalesrepExpensesHeader, db_column='order_no')

    class Meta:
        managed = False
        db_table = 'acc_salesrep_expenses_order_pa'
        unique_together = (('header_no', 'order_no'),)


class AccSlsrepExpnsCustHdr(models.Model):
    no = models.BigIntegerField(primary_key=True)
    order_date = models.DateField()
    operation_no = models.DecimalField(max_digits=20, decimal_places=5)
    customer_accno = models.CharField(max_length=14)
    notes = models.CharField(max_length=250, blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    salesrep_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_slsrep_expns_cust_hdr'


class AccSlsrepExpnsCustInvdet(models.Model):
    header_no = models.BigIntegerField()
    invoice_no = models.BigIntegerField()
    notes = models.CharField(max_length=250, blank=True, null=True)
    id = models.IntegerField()
    order_no = models.BigIntegerField(blank=True, null=True)
    expensis_type = models.CharField(max_length=14, blank=True, null=True)
    add_expensis = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    add_expensis_accno = models.CharField(max_length=34, blank=True, null=True)
    expensis_amt = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_slsrep_expns_cust_invdet'
        unique_together = (('header_no', 'invoice_no', 'id'),)


class AccSlsrepExpnsOrdPmtDet(models.Model):
    header_no = models.BigIntegerField()
    order_no = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'acc_slsrep_expns_ord_pmt_det'
        unique_together = (('header_no', 'order_no'),)


class AccSlsrepExpnsOrdPmtHdr(models.Model):
    no = models.BigIntegerField(primary_key=True)
    order_date = models.DateField()
    notes = models.CharField(max_length=250, blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_slsrep_expns_ord_pmt_hdr'


class AccVoucherDocument(models.Model):
    branch = models.ForeignKey('Move', db_column='branch')
    reset = models.ForeignKey('Move', db_column='reset')
    reset_0 = models.ForeignKey('Move', db_column='reset_id')  # Field renamed because of name conflict.
    document_id = models.IntegerField()
    document_type = models.ForeignKey(AccMasterDocument, db_column='document_type')
    document_number = models.CharField(max_length=20)
    document_date = models.DateField(blank=True, null=True)
    document_image = models.BinaryField(blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    id = models.ForeignKey('Move', db_column='id')
    doc_ext = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_voucher_document'
        unique_together = (('branch', 'reset', 'reset_id', 'document_id', 'id'),)


class AccVoucherDocumentTemp(models.Model):
    branch = models.IntegerField()
    reset = models.IntegerField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    document_id = models.IntegerField()
    document_type = models.IntegerField()
    document_number = models.CharField(max_length=20)
    document_date = models.DateField(blank=True, null=True)
    document_image = models.BinaryField(blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    id = models.DecimalField(max_digits=20, decimal_places=5)
    doc_ext = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_voucher_document_temp'
        unique_together = (('branch', 'reset', 'reset_id', 'document_id', 'id'),)


class AccYears(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_years'


class AccnoNotes(models.Model):
    c1 = models.CharField(max_length=100, blank=True, null=True)
    c2 = models.CharField(max_length=100, blank=True, null=True)
    c3 = models.CharField(max_length=100, blank=True, null=True)
    c4 = models.CharField(max_length=100, blank=True, null=True)
    c5 = models.CharField(max_length=100, blank=True, null=True)
    c6 = models.CharField(max_length=100, blank=True, null=True)
    c7 = models.CharField(max_length=100, blank=True, null=True)
    n1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    n2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    n3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    n4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    n5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    n6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    n7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    l1 = models.TextField(blank=True, null=True)
    l2 = models.TextField(blank=True, null=True)
    l3 = models.TextField(blank=True, null=True)
    l4 = models.TextField(blank=True, null=True)
    l5 = models.TextField(blank=True, null=True)
    l6 = models.TextField(blank=True, null=True)
    l7 = models.TextField(blank=True, null=True)
    accno = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'accno_notes'


class AcsUsers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    time1 = models.DateField(blank=True, null=True)
    time2 = models.DateField(blank=True, null=True)
    falge = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acs_users'


class AddCostcenters(models.Model):
    no = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    p1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    omit = models.NullBooleanField()
    name_e = models.CharField(max_length=50)
    notes = models.CharField(max_length=100, blank=True, null=True)
    notes_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_costcenters'


class Ages(models.Model):
    ag_id = models.IntegerField(primary_key=True)
    ag_name = models.CharField(max_length=100, blank=True, null=True)
    ag_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ages'


class AlterationType(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alteration_type'


class AnnualCostBudget(models.Model):
    bud_id = models.CharField(max_length=15)
    cost_id = models.DecimalField(max_digits=20, decimal_places=5)
    finan_year = models.IntegerField()
    type = models.NullBooleanField()
    debit_val = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit_val = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annual_cost_budget'
        unique_together = (('bud_id', 'cost_id', 'finan_year'),)


class AquaCheckDate(models.Model):
    id = models.BigIntegerField()
    ser = models.BigIntegerField()
    transferdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aqua_check_date'
        unique_together = (('id', 'ser'),)


class AquaContract(models.Model):
    id = models.BigIntegerField(primary_key=True)
    customers_id = models.BigIntegerField(blank=True, null=True)
    status = models.NullBooleanField()
    vdate = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    val = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    payment_method = models.NullBooleanField()
    tanks = models.IntegerField(blank=True, null=True)
    cup_carriers = models.IntegerField(blank=True, null=True)
    rent_tanks = models.IntegerField(blank=True, null=True)
    tot_bottles = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    hot_cold_tanks = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    bottel_value = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    tank_value = models.DecimalField(max_digits=23, decimal_places=2, blank=True, null=True)
    period_payment_credit = models.BigIntegerField(blank=True, null=True)
    hot_cold_val = models.BigIntegerField(blank=True, null=True)
    hot_cold_rentval = models.BigIntegerField(blank=True, null=True)
    cold_val = models.BigIntegerField(blank=True, null=True)
    cold_rentval = models.BigIntegerField(blank=True, null=True)
    cold_tanks = models.BigIntegerField(blank=True, null=True)
    cold_renttanka = models.BigIntegerField(blank=True, null=True)
    cust_manid = models.CharField(max_length=20, blank=True, null=True)
    renewal_count = models.BigIntegerField(blank=True, null=True)
    comm_domestic = models.BigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    original_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aqua_contract'


class AquaContractDetails(models.Model):
    id = models.BigIntegerField()
    ser = models.BigIntegerField()
    area_code = models.BigIntegerField()
    sector = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    gada = models.CharField(max_length=20, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)
    flat = models.CharField(max_length=20, blank=True, null=True)
    delivery_date = models.NullBooleanField()
    period = models.NullBooleanField()
    cup_carriers = models.IntegerField(blank=True, null=True)
    driver_code = models.BigIntegerField(blank=True, null=True)
    last_transdate = models.DateField(blank=True, null=True)
    route = models.CharField(max_length=30, blank=True, null=True)
    full_address = models.TextField(blank=True, null=True)
    cust_manid = models.CharField(max_length=20, blank=True, null=True)
    cust_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aqua_contract_details'
        unique_together = (('id', 'ser'),)


class AssCenterMove(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    ass = models.ForeignKey('Assets')
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    c_date = models.DateField(blank=True, null=True)
    accno_ass = models.CharField(max_length=34, blank=True, null=True)
    accno_des = models.CharField(max_length=34, blank=True, null=True)
    accno_ex = models.CharField(max_length=34, blank=True, null=True)
    c_date_end = models.DateField(blank=True, null=True)
    c_date1 = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_center_move'


class AssContact(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_contact'


class AssDestruction(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    ass = models.ForeignKey('Assets', blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    reset = models.IntegerField(blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dmonth = models.IntegerField(blank=True, null=True)
    dyear = models.IntegerField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    dmonth_2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_destruction'


class AssMUser(models.Model):
    user_name = models.CharField(primary_key=True, max_length=16)
    password = models.CharField(max_length=16)
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    default_language = models.IntegerField(blank=True, null=True)
    blocked = models.CharField(max_length=1, blank=True, null=True)
    salary_view = models.CharField(max_length=1, blank=True, null=True)
    modify_equip_code_till = models.CharField(max_length=10, blank=True, null=True)
    appear_zeros = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ass_m_user'


class AssPlaces(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_places'


class AssSettings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assets_acc_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_settings'


class AssSyApplication(models.Model):
    app_cd = models.CharField(primary_key=True, max_length=20)
    app_name_a = models.CharField(max_length=100, blank=True, null=True)
    app_name_e = models.CharField(max_length=100, blank=True, null=True)
    opt_cnt = models.IntegerField(blank=True, null=True)
    opt1_label = models.CharField(max_length=100, blank=True, null=True)
    opt2_label = models.CharField(max_length=100, blank=True, null=True)
    opt3_label = models.CharField(max_length=100, blank=True, null=True)
    opt4_label = models.CharField(max_length=100, blank=True, null=True)
    opt5_label = models.CharField(max_length=100, blank=True, null=True)
    opt6_label = models.CharField(max_length=100, blank=True, null=True)
    opt7_label = models.CharField(max_length=100, blank=True, null=True)
    opt8_label = models.CharField(max_length=100, blank=True, null=True)
    opt9_label = models.CharField(max_length=100, blank=True, null=True)
    opt10_label = models.CharField(max_length=100, blank=True, null=True)
    opt11_label = models.CharField(max_length=100, blank=True, null=True)
    opt12_label = models.CharField(max_length=100, blank=True, null=True)
    app_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_sy_application'


class AssSyMenu(models.Model):
    app_cd = models.CharField(max_length=20)
    m_code = models.IntegerField()
    m_name_a = models.CharField(max_length=100, blank=True, null=True)
    m_name_e = models.CharField(max_length=100, blank=True, null=True)
    link_name = models.CharField(max_length=100, blank=True, null=True)
    m_type = models.CharField(max_length=1, blank=True, null=True)
    item_level = models.IntegerField(blank=True, null=True)
    item_sort = models.CharField(max_length=100, blank=True, null=True)
    window_name_a = models.CharField(max_length=100, blank=True, null=True)
    window_name_e = models.CharField(max_length=100, blank=True, null=True)
    ret_win_a = models.CharField(max_length=100, blank=True, null=True)
    ret_win_e = models.CharField(max_length=100, blank=True, null=True)
    sel_opt1 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt2 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt3 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt4 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt5 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt6 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt7 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt8 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt9 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt10 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt11 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt12 = models.CharField(max_length=1, blank=True, null=True)
    opt1 = models.CharField(max_length=100, blank=True, null=True)
    opt2 = models.CharField(max_length=100, blank=True, null=True)
    opt3 = models.CharField(max_length=100, blank=True, null=True)
    opt4 = models.CharField(max_length=100, blank=True, null=True)
    opt5 = models.CharField(max_length=100, blank=True, null=True)
    opt6 = models.CharField(max_length=100, blank=True, null=True)
    opt7 = models.CharField(max_length=100, blank=True, null=True)
    opt8 = models.CharField(max_length=100, blank=True, null=True)
    opt9 = models.CharField(max_length=100, blank=True, null=True)
    opt10 = models.CharField(max_length=100, blank=True, null=True)
    opt11 = models.CharField(max_length=100, blank=True, null=True)
    opt12 = models.CharField(max_length=100, blank=True, null=True)
    parent_m_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_sy_menu'
        unique_together = (('app_cd', 'm_code'),)


class AssSyUserrights(models.Model):
    user_name = models.CharField(max_length=50)
    app_cd = models.CharField(max_length=20)
    m_code = models.IntegerField()
    ret = models.CharField(max_length=1, blank=True, null=True)
    addition = models.CharField(max_length=1, blank=True, null=True)
    saving = models.CharField(max_length=1, blank=True, null=True)
    deletion = models.CharField(max_length=1, blank=True, null=True)
    printing = models.CharField(max_length=1, blank=True, null=True)
    posting = models.CharField(max_length=1, blank=True, null=True)
    unposting = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_sy_userrights'
        unique_together = (('user_name', 'app_cd', 'm_code'),)


class AssTakeStock(models.Model):
    asset_id = models.CharField(max_length=10)
    act_qty = models.DecimalField(max_digits=20, decimal_places=6)
    qty = models.DecimalField(max_digits=20, decimal_places=6)
    vdate = models.DateField()
    notes = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_take_stock'
        unique_together = (('asset_id', 'vdate'),)


class AssType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50, blank=True, null=True)
    is_equipment = models.NullBooleanField()
    ass_syntax = models.TextField(blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    serial = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_type'


class AssUserCat1Rights(models.Model):
    user_name = models.CharField(max_length=16)
    cat1_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ass_user_cat1_rights'
        unique_together = (('user_name', 'cat1_id'),)


class AssValue(models.Model):
    ass = models.ForeignKey('Assets')
    serial = models.IntegerField()
    vdate = models.DateField(blank=True, null=True)
    move_type = models.CharField(max_length=1, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    jv_no = models.CharField(max_length=30, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ass_value'
        unique_together = (('ass_id', 'serial'),)


class Assets(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)
    vendor = models.CharField(max_length=50, blank=True, null=True)
    pur_date = models.DateField(blank=True, null=True)
    per = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    depresion = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    c_date = models.DateField(blank=True, null=True)
    sal = models.NullBooleanField()
    sal_date = models.DateField(blank=True, null=True)
    sal_price = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sal_man = models.CharField(max_length=50, blank=True, null=True)
    sal_notes = models.TextField(blank=True, null=True)
    depresion1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ass_ucost = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ass_type = models.ForeignKey(AssType, db_column='ass_type', blank=True, null=True)
    pur_invoice = models.CharField(max_length=20, blank=True, null=True)
    jv_no = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    ass_cnt = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    temp_depresion = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    location = models.IntegerField(blank=True, null=True)
    depresion_method = models.NullBooleanField()
    amount_changed = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    shaseno = models.CharField(max_length=30, blank=True, null=True)
    carno = models.CharField(max_length=30, blank=True, null=True)
    accno1 = models.CharField(max_length=32, blank=True, null=True)
    accno2 = models.CharField(max_length=32, blank=True, null=True)
    accno3 = models.CharField(max_length=32, blank=True, null=True)
    stop_ass = models.NullBooleanField()
    attached_to_assey = models.CharField(max_length=10, blank=True, null=True)
    location_detail_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    contact_per = models.IntegerField(blank=True, null=True)
    depr_date_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'assets'


class AssetsAccno(models.Model):
    cost_center_id = models.DecimalField(max_digits=20, decimal_places=5)
    type_id = models.IntegerField()
    accno1 = models.CharField(max_length=32)
    accno2 = models.CharField(max_length=32)
    accno3 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'assets_accno'
        unique_together = (('cost_center_id', 'type_id'),)


class AssettypeAdded(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    added = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assettype_added'


class AssettypeDesign(models.Model):
    num3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    l_var_char = models.TextField(blank=True, null=True)
    accno = models.CharField(primary_key=True, max_length=10)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    date5 = models.DateField(blank=True, null=True)
    date6 = models.DateField(blank=True, null=True)
    date7 = models.DateField(blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    name5 = models.CharField(max_length=100, blank=True, null=True)
    name6 = models.CharField(max_length=100, blank=True, null=True)
    name7 = models.CharField(max_length=100, blank=True, null=True)
    num1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ass_type = models.BigIntegerField(blank=True, null=True)
    assets_id = models.CharField(max_length=10, blank=True, null=True)
    num8 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num9 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num10 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num11 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num12 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    name8 = models.CharField(max_length=100, blank=True, null=True)
    name9 = models.CharField(max_length=100, blank=True, null=True)
    name10 = models.CharField(max_length=100, blank=True, null=True)
    name11 = models.CharField(max_length=100, blank=True, null=True)
    name12 = models.CharField(max_length=100, blank=True, null=True)
    date8 = models.DateField(blank=True, null=True)
    date9 = models.DateField(blank=True, null=True)
    date10 = models.DateField(blank=True, null=True)
    date11 = models.DateField(blank=True, null=True)
    date12 = models.DateField(blank=True, null=True)
    string1 = models.CharField(max_length=100, blank=True, null=True)
    string2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assettype_design'


class AutDate(models.Model):
    id = models.DecimalField(max_digits=20, decimal_places=5)
    vdate = models.DateField(blank=True, null=True)
    flage = models.NullBooleanField()
    notes = models.CharField(max_length=100, blank=True, null=True)
    move_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.DecimalField(max_digits=20, decimal_places=5)
    reset = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aut_date'
        unique_together = (('id', 'branch'),)


class Authorty(models.Model):
    no = models.IntegerField(primary_key=True)
    pass_field = models.CharField(db_column='pass', max_length=10)  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=50)
    us_guide = models.NullBooleanField()
    us_cost = models.NullBooleanField()
    us_m1 = models.NullBooleanField()
    us_m2 = models.NullBooleanField()
    us_m3 = models.NullBooleanField()
    us_m4 = models.NullBooleanField()
    us_m5 = models.NullBooleanField()
    us_m6 = models.NullBooleanField()
    us_m7 = models.NullBooleanField()
    us_m8 = models.NullBooleanField()
    us_r_guide = models.NullBooleanField()
    us_r_mezan = models.NullBooleanField()
    us_r_statment = models.NullBooleanField()
    us_r_arbah = models.NullBooleanField()
    us_r_sanad = models.NullBooleanField()
    us_mod1 = models.NullBooleanField()
    us_mod2 = models.NullBooleanField()
    us_mod3 = models.NullBooleanField()
    us_mod4 = models.NullBooleanField()
    us_mod5 = models.NullBooleanField()
    us_mod6 = models.NullBooleanField()
    us_mod7 = models.NullBooleanField()
    us_mod8 = models.NullBooleanField()
    us_mezania = models.NullBooleanField()
    us_x1 = models.NullBooleanField()
    us_x2 = models.NullBooleanField()
    us_x3 = models.NullBooleanField()
    us_x4 = models.NullBooleanField()
    us_x5 = models.NullBooleanField()
    us_x6 = models.NullBooleanField()
    us_x7 = models.NullBooleanField()
    us_x8 = models.NullBooleanField()
    us_x9 = models.NullBooleanField()
    us_x10 = models.NullBooleanField()
    us_files = models.NullBooleanField()
    us_super = models.NullBooleanField()
    us_settings = models.NullBooleanField()
    print_jv = models.IntegerField(blank=True, null=True)
    print_rv = models.IntegerField(blank=True, null=True)
    print_pv = models.IntegerField(blank=True, null=True)
    print_cv = models.IntegerField(blank=True, null=True)
    print_bv = models.IntegerField(blank=True, null=True)
    print_csinv = models.IntegerField(blank=True, null=True)
    print_crinv = models.IntegerField(blank=True, null=True)
    print_otv = models.IntegerField(blank=True, null=True)
    ovprtdel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authorty'


class AverageLog(models.Model):
    prods = models.FloatField()
    prodn = models.CharField(max_length=30)
    vdate = models.DateField(blank=True, null=True)
    msg = models.CharField(max_length=500, blank=True, null=True)
    msg_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'average_log'


class AverageQueue(models.Model):
    prods = models.ForeignKey('Store', db_column='prods')
    prodn = models.CharField(max_length=30)
    vdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'average_queue'
        unique_together = (('prods', 'prodn'),)


class AverageQueueBuffer(models.Model):
    prods = models.IntegerField()
    prodn = models.CharField(max_length=30)
    vdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'average_queue_buffer'
        unique_together = (('prods', 'prodn'),)


class AverageSession(models.Model):
    sid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'average_session'


class Banks(models.Model):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    name_e = models.CharField(max_length=150, blank=True, null=True)
    accno = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banks'


class Batche(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    naotes = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'batche'


class Beneficary(models.Model):
    id = models.BigIntegerField(primary_key=True)
    details = models.TextField()
    details_e = models.TextField()

    class Meta:
        managed = False
        db_table = 'beneficary'


class BillCurrencies(models.Model):
    id = models.ForeignKey('Currancy', db_column='id')
    code = models.ForeignKey('Issue1', db_column='code')
    pcenter = models.ForeignKey('Issue1', db_column='pcenter')
    bilno = models.ForeignKey('Issue1', db_column='bilno')
    bill_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    paied = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    change = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    exchange_rate = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    change_local = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_currencies'
        unique_together = (('id', 'code', 'pcenter', 'bilno'),)


class Branches(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    name_e = models.CharField(max_length=50)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'


class Brands(models.Model):
    br_id = models.IntegerField(primary_key=True)
    br_name = models.CharField(max_length=100, blank=True, null=True)
    br_name_e = models.CharField(max_length=100, blank=True, null=True)
    ss_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    response_man = models.CharField(max_length=150, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    e_mail = models.CharField(max_length=100, blank=True, null=True)
    web_site = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'


class Budget(models.Model):
    bud_id = models.CharField(max_length=15)
    bud_type = models.NullBooleanField()
    include = models.NullBooleanField()
    amount1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    accno = models.CharField(max_length=32)
    credit1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    depit_val = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit_val = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    finan_year = models.IntegerField()
    acc_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget'
        unique_together = (('bud_id', 'accno', 'finan_year'),)


class BudgetMonthlyAccCost(models.Model):
    bud_id = models.CharField(max_length=15)
    bud_type = models.NullBooleanField()
    amount1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    accno = models.CharField(max_length=32)
    cost_id = models.DecimalField(max_digits=20, decimal_places=5)
    finan_year = models.IntegerField()
    acc_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_monthly_acc_cost'
        unique_together = (('bud_id', 'accno', 'cost_id', 'finan_year'),)


class BudjetCostAcc(models.Model):
    bud_id = models.CharField(max_length=15)
    cost_id = models.DecimalField(max_digits=20, decimal_places=5)
    accno = models.CharField(max_length=32)
    debit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    finan_year = models.IntegerField()
    acc_level = models.IntegerField(blank=True, null=True)
    bud_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'budjet_cost_acc'
        unique_together = (('bud_id', 'cost_id', 'accno', 'finan_year'),)


class CAcceditreports(models.Model):
    code = models.IntegerField(primary_key=True)
    nameen = models.CharField(max_length=250, blank=True, null=True)
    window_name = models.CharField(max_length=250, blank=True, null=True)
    dwo_name = models.CharField(max_length=250, blank=True, null=True)
    rep_syntax = models.BinaryField(blank=True, null=True)
    enable_header = models.CharField(max_length=1)
    name2 = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True)
    moudle = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_acceditreports'


class CCustcat1(models.Model):
    code = models.IntegerField(primary_key=True)
    namear = models.CharField(max_length=40)
    nameen = models.CharField(max_length=40, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_custcat1'


class CCustcat2(models.Model):
    code = models.IntegerField(primary_key=True)
    namear = models.CharField(max_length=40)
    nameen = models.CharField(max_length=40, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_custcat2'


class CEditreports(models.Model):
    code = models.IntegerField(primary_key=True)
    nameen = models.CharField(max_length=100, blank=True, null=True)
    window_name = models.CharField(max_length=100, blank=True, null=True)
    dwo_name = models.CharField(max_length=100, blank=True, null=True)
    rep_syntax = models.BinaryField(blank=True, null=True)
    enable_header = models.CharField(max_length=1, blank=True, null=True)
    repname_e = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    moudle = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_editreports'


class CProfitperson(models.Model):
    code = models.IntegerField(primary_key=True)
    namear = models.CharField(max_length=100)
    nameen = models.CharField(max_length=100, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_profitperson'


class CVendorcat1(models.Model):
    code = models.IntegerField(primary_key=True)
    namear = models.CharField(max_length=40)
    nameen = models.CharField(max_length=40, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_vendorcat1'


class CVendorcat2(models.Model):
    code = models.IntegerField(primary_key=True)
    namear = models.CharField(max_length=40)
    nameen = models.CharField(max_length=40, blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_vendorcat2'


class Calendar(models.Model):
    yr = models.IntegerField()
    mon = models.IntegerField()
    dy = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calendar'
        unique_together = (('yr', 'mon', 'dy'),)


class CarType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    name_e = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_type'


class Cards(models.Model):
    card_id = models.BigIntegerField(primary_key=True)
    card_st = models.IntegerField(blank=True, null=True)
    card_tp = models.IntegerField(blank=True, null=True)
    card_cat = models.IntegerField(blank=True, null=True)
    card_no = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'cards'


class Cars(models.Model):
    no = models.CharField(max_length=15)
    typ_id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    model = models.IntegerField(blank=True, null=True)
    gover = models.NullBooleanField()
    shassy = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.BigIntegerField()
    color = models.CharField(max_length=20, blank=True, null=True)
    siz = models.CharField(max_length=25, blank=True, null=True)
    engine_no = models.CharField(max_length=25, blank=True, null=True)
    top_no = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'
        unique_together = (('no', 'customer_id'),)


class CashArea(models.Model):
    area_code = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_area'


class CashCustomers(models.Model):
    cust_no = models.BigIntegerField(primary_key=True)
    cust_tel = models.CharField(max_length=20, blank=True, null=True)
    cust_name = models.CharField(max_length=60, blank=True, null=True)
    area_code = models.ForeignKey(CashArea, db_column='area_code', blank=True, null=True)
    sector = models.CharField(max_length=20, blank=True, null=True)
    gada = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    flat = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)
    beside = models.CharField(max_length=50, blank=True, null=True)
    cust_tel2 = models.CharField(max_length=20, blank=True, null=True)
    cust_tel3 = models.CharField(max_length=20, blank=True, null=True)
    cust_tel4 = models.CharField(max_length=20, blank=True, null=True)
    cust_tel5 = models.CharField(max_length=20, blank=True, null=True)
    cust_name_e = models.CharField(max_length=255, blank=True, null=True)
    cardid = models.BigIntegerField(blank=True, null=True)
    nat_no = models.BigIntegerField(blank=True, null=True)
    has_card = models.NullBooleanField()
    area_code2 = models.BigIntegerField(blank=True, null=True)
    sector2 = models.CharField(max_length=20, blank=True, null=True)
    gada2 = models.CharField(max_length=20, blank=True, null=True)
    street2 = models.CharField(max_length=50, blank=True, null=True)
    house2 = models.CharField(max_length=50, blank=True, null=True)
    flat2 = models.CharField(max_length=50, blank=True, null=True)
    floor2 = models.CharField(max_length=50, blank=True, null=True)
    beside2 = models.CharField(max_length=50, blank=True, null=True)
    area_code3 = models.BigIntegerField(blank=True, null=True)
    sector3 = models.CharField(max_length=20, blank=True, null=True)
    gada3 = models.CharField(max_length=20, blank=True, null=True)
    street3 = models.CharField(max_length=50, blank=True, null=True)
    house3 = models.CharField(max_length=50, blank=True, null=True)
    flat3 = models.CharField(max_length=50, blank=True, null=True)
    floor3 = models.CharField(max_length=50, blank=True, null=True)
    beside3 = models.CharField(max_length=50, blank=True, null=True)
    area_code4 = models.BigIntegerField(blank=True, null=True)
    sector4 = models.CharField(max_length=20, blank=True, null=True)
    gada4 = models.CharField(max_length=20, blank=True, null=True)
    street4 = models.CharField(max_length=50, blank=True, null=True)
    house4 = models.CharField(max_length=50, blank=True, null=True)
    flat4 = models.CharField(max_length=50, blank=True, null=True)
    floor4 = models.CharField(max_length=50, blank=True, null=True)
    beside4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_customers'


class CashCustomersAddress(models.Model):
    cust_no = models.BigIntegerField()
    area_code = models.BigIntegerField(blank=True, null=True)
    sector = models.CharField(max_length=20, blank=True, null=True)
    gada = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    flat = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)
    beside = models.CharField(max_length=50, blank=True, null=True)
    id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cash_customers_address'
        unique_together = (('id', 'cust_no'),)


class CashDelivary(models.Model):
    id = models.BigIntegerField()
    total = models.BigIntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    user_no = models.BigIntegerField(blank=True, null=True)
    from_casher = models.CharField(max_length=100, blank=True, null=True)
    to_cahser = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)
    pcenter = models.ForeignKey('Centers', db_column='pcenter')
    from_invoice = models.BigIntegerField(blank=True, null=True)
    to_invoice = models.BigIntegerField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    to_time = models.DateField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    from_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_delivary'
        unique_together = (('id', 'pcenter'),)


class CashMachines(models.Model):
    id = models.BigIntegerField(primary_key=True)
    machine_id = models.CharField(max_length=50)
    center_id = models.BigIntegerField(blank=True, null=True)
    floor_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_machines'


class CashPayments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=150, blank=True, null=True)
    accno = models.CharField(max_length=14, blank=True, null=True)
    name_e = models.CharField(max_length=150, blank=True, null=True)
    bnk_commp = models.FloatField(blank=True, null=True)
    sort_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_payments'


class Categorysetting(models.Model):
    catid = models.FloatField()
    catlevel = models.FloatField()
    centerid = models.FloatField()
    printerpath = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorysetting'
        unique_together = (('catid', 'catlevel', 'centerid'),)


class Cattypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    naotes = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50)
    sort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cattypes'


class Centers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    prods = models.BigIntegerField(blank=True, null=True)
    sman = models.ForeignKey('SalesMen', db_column='sman', blank=True, null=True)
    cost_center = models.BigIntegerField(blank=True, null=True)
    acc_branch = models.BigIntegerField(blank=True, null=True)
    phone1 = models.CharField(max_length=10, blank=True, null=True)
    phone2 = models.CharField(max_length=10, blank=True, null=True)
    vaddress = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    bnkcommaccno = models.BigIntegerField(blank=True, null=True)
    cntr_salesqtycash = models.NullBooleanField()
    cntr_salesqtycredit = models.NullBooleanField()
    cntr_salesrqtycash = models.NullBooleanField()
    cntr_salesrqtycredit = models.NullBooleanField()
    cntr_sysdate = models.DateField(blank=True, null=True)
    cntr_creditcustomer = models.BigIntegerField(blank=True, null=True)
    cashsales_credit_acc = models.BigIntegerField(blank=True, null=True)
    printer_nm = models.CharField(max_length=200, blank=True, null=True)
    cntr_creditnoteacc = models.BigIntegerField(blank=True, null=True)
    region = models.CharField(max_length=150, blank=True, null=True)
    center_type = models.IntegerField(blank=True, null=True)
    default_curr = models.IntegerField(blank=True, null=True)
    logo_path = models.CharField(max_length=100, blank=True, null=True)
    logo_blob = models.BinaryField(blank=True, null=True)
    site_name = models.CharField(max_length=200, blank=True, null=True)
    bnkcommaccno_old = models.CharField(max_length=40, blank=True, null=True)
    cashsales_credit_acc_old = models.CharField(max_length=40, blank=True, null=True)
    cntr_creditnoteacc_old = models.CharField(max_length=40, blank=True, null=True)
    mgento_order = models.NullBooleanField()
    fromcategory = models.FloatField(blank=True, null=True)
    tocategory = models.FloatField(blank=True, null=True)
    tablescreenwidth = models.FloatField(blank=True, null=True)
    tablescreenheight = models.FloatField(blank=True, null=True)
    loadandprintassemitem = models.BigIntegerField(blank=True, null=True)
    logo2_path = models.CharField(max_length=100, blank=True, null=True)
    logo3_path = models.CharField(max_length=100, blank=True, null=True)
    logo2_blob = models.BinaryField(blank=True, null=True)
    logo3_blob = models.BinaryField(blank=True, null=True)
    closeorderprint = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centers'


class Centersection(models.Model):
    sec_id = models.IntegerField()
    sec_center = models.ForeignKey(Centers, db_column='sec_center')
    sec_ardesc = models.CharField(max_length=100, blank=True, null=True)
    sec_latindesc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centersection'
        unique_together = (('sec_id', 'sec_center'),)


class Centersprinters(models.Model):
    centerid = models.FloatField()
    printerid = models.FloatField()
    printerpath = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centersprinters'
        unique_together = (('centerid', 'printerid'),)


class Charges(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charges'


class Checks(models.Model):
    check_id = models.CharField(primary_key=True, max_length=35)
    description = models.CharField(max_length=50)
    currency = models.ForeignKey('Currancy', db_column='currency')
    gl_account = models.CharField(max_length=32, blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    check_status = models.CharField(max_length=1, blank=True, null=True)
    frist_check_no = models.IntegerField(blank=True, null=True)
    last_check_no = models.IntegerField(blank=True, null=True)
    description_e = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'checks'


class ChkRec(models.Model):
    prods = models.BigIntegerField()
    prodn = models.CharField(max_length=30)
    rec = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chk_rec'


class ChkTrackcost(models.Model):
    prods = models.BigIntegerField()
    prodn = models.CharField(max_length=30)
    ob = models.FloatField(blank=True, null=True)
    rec = models.FloatField(blank=True, null=True)
    issue = models.FloatField(blank=True, null=True)
    endbal = models.FloatField(blank=True, null=True)
    ob_date = models.DateField(blank=True, null=True)
    endbal_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chk_trackcost'


class Class(models.Model):
    code = models.FloatField(primary_key=True)
    class_name = models.CharField(max_length=20)
    percent = models.FloatField()
    class_name_e = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Class1(models.Model):
    cl_1_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_name = models.CharField(max_length=100, blank=True, null=True)
    cl_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_1'


class Class10(models.Model):
    cl_10_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_10_name = models.CharField(max_length=100, blank=True, null=True)
    cl_10_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_10'


class Class2(models.Model):
    cl_2_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_2_name = models.CharField(max_length=100, blank=True, null=True)
    cl_2_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_2'


class Class3(models.Model):
    cl_3_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_3_name = models.CharField(max_length=100, blank=True, null=True)
    cl_3_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_3'


class Class4(models.Model):
    cl_4_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_4_name = models.CharField(max_length=100, blank=True, null=True)
    cl_4_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_4'


class Class5(models.Model):
    cl_5_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_5_name = models.CharField(max_length=100, blank=True, null=True)
    cl_5_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_5'


class Class6(models.Model):
    cl_6_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_6_name = models.CharField(max_length=100, blank=True, null=True)
    cl_6_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_6'


class Class7(models.Model):
    cl_7_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_7_name = models.CharField(max_length=100, blank=True, null=True)
    cl_7_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_7'


class Class8(models.Model):
    cl_8_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_8_name = models.CharField(max_length=100, blank=True, null=True)
    cl_8_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_8'


class Class9(models.Model):
    cl_9_id = models.IntegerField(primary_key=True)
    cl_type = models.IntegerField()
    cl_9_name = models.CharField(max_length=100, blank=True, null=True)
    cl_9_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_9'


class ClassDesc(models.Model):
    cl_des_id = models.IntegerField(primary_key=True)
    cl_name = models.CharField(max_length=100, blank=True, null=True)
    cl_name_e = models.CharField(max_length=100, blank=True, null=True)
    cl_type = models.IntegerField(blank=True, null=True)
    cl_note = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_desc'


class Codes(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    items = models.IntegerField(blank=True, null=True)
    cust = models.IntegerField(blank=True, null=True)
    name_e = models.CharField(max_length=250, blank=True, null=True)
    accno = models.CharField(max_length=14, blank=True, null=True)
    payment = models.BigIntegerField(blank=True, null=True)
    reset_type = models.BigIntegerField(blank=True, null=True)
    trans_collection = models.NullBooleanField()
    autopost = models.NullBooleanField()
    partialpayment_reset_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codes'


class CodesTaxes(models.Model):
    id = models.ForeignKey('Taxes', db_column='id')
    code = models.ForeignKey(Codes, db_column='code')
    move = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'codes_taxes'
        unique_together = (('id', 'code'),)


class CodesmithExtendedProperties(models.Model):
    container_object_owner = models.CharField(max_length=50)
    object_name = models.CharField(max_length=61)
    codesmith_schema_type = models.CharField(max_length=200)
    property_name = models.CharField(max_length=75)
    property_value = models.CharField(max_length=4000, blank=True, null=True)
    clr_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'codesmith_extended_properties'
        unique_together = (('container_object_owner', 'object_name', 'codesmith_schema_type', 'property_name'),)


class Coloor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    name_e = models.CharField(max_length=50)
    sort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coloor'


class Color(models.Model):
    clr_id = models.IntegerField(primary_key=True)
    clr_ardesc = models.CharField(max_length=50, blank=True, null=True)
    clr_latindesc = models.CharField(max_length=50, blank=True, null=True)
    clr_useddesc = models.NullBooleanField()
    clr_code = models.CharField(max_length=20, blank=True, null=True)
    color_cat = models.BigIntegerField(blank=True, null=True)
    reqsort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color'


class ColorCat(models.Model):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_e = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color_cat'


class Colors(models.Model):
    clr_id = models.IntegerField(primary_key=True)
    clr_name = models.CharField(max_length=20, blank=True, null=True)
    clr_name_e = models.CharField(max_length=20, blank=True, null=True)
    clr_code = models.CharField(max_length=150, blank=True, null=True)
    clr_cat = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colors'


class CommCat(models.Model):
    sman = models.ForeignKey('SalesMen')
    cat_id = models.BigIntegerField()
    comm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_cat'
        unique_together = (('sman_id', 'cat_id'),)


class CommCatLevels(models.Model):
    sman = models.ForeignKey('SalesMen')
    cat_id = models.BigIntegerField()
    level_max = models.FloatField()
    comm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_cat_levels'
        unique_together = (('sman_id', 'cat_id', 'level_max'),)


class CommLevels(models.Model):
    sman = models.ForeignKey('SalesMen')
    level_max = models.FloatField()
    comm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_levels'
        unique_together = (('sman_id', 'level_max'),)


class CommiosnPeriods(models.Model):
    id_h = models.BigIntegerField(primary_key=True)
    sections_id = models.IntegerField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    target_amt = models.FloatField(blank=True, null=True)
    actualsalesinperiod = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    actualunprofitsales = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commiosn_periods'


class CommiosnTargetCalc(models.Model):
    id = models.BigIntegerField()
    id_h = models.BigIntegerField()
    commission_type = models.NullBooleanField()
    amount = models.FloatField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    sales_amt = models.FloatField(blank=True, null=True)
    target_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commiosn_target_calc'
        unique_together = (('id', 'id_h'),)


class CommisionTargets(models.Model):
    id = models.BigIntegerField()
    id_h = models.BigIntegerField()
    commission_type = models.NullBooleanField()
    from_amount = models.FloatField(blank=True, null=True)
    to_amount = models.FloatField(blank=True, null=True)
    from_commission = models.FloatField(blank=True, null=True)
    to_commission = models.FloatField(blank=True, null=True)
    commission_percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commision_targets'
        unique_together = (('id', 'id_h'),)


class CompanyAccounts(models.Model):
    company_code = models.FloatField()
    local_account = models.ForeignKey('Guide')
    relative_account_id = models.FloatField()
    relative_accno = models.CharField(max_length=40, blank=True, null=True)
    relative_accname = models.CharField(max_length=150, blank=True, null=True)
    relative_accname_e = models.CharField(max_length=150, blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    relative_reset = models.BigIntegerField(blank=True, null=True)
    relative_branch = models.BigIntegerField(blank=True, null=True)
    relative_user = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_accounts'
        unique_together = (('company_code', 'local_account_id', 'relative_account_id'),)


class Complains(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    name_e = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complains'


class Contract(models.Model):
    id = models.BigIntegerField(primary_key=True)
    file_no = models.BigIntegerField(blank=True, null=True)
    custno = models.BigIntegerField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    visit_type = models.NullBooleanField()
    amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    machine_type = models.IntegerField(blank=True, null=True)
    machine_kind = models.BigIntegerField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    machine_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract'


class ContractType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50, blank=True, null=True)
    spare_parts = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'contract_type'


class Copy(models.Model):
    prods = models.BigIntegerField()
    prodn = models.CharField(max_length=25)
    prodname = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copy'


class Cost(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    name = models.CharField(max_length=10, blank=True, null=True)
    p1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    p2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    p3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost'


class Cost1(models.Model):
    no = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    rep_syntax = models.TextField(blank=True, null=True)
    name_e = models.CharField(max_length=50)
    id = models.CharField(unique=True, max_length=60)
    cc_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost1'


class Cost2(models.Model):
    no = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    p1 = models.BigIntegerField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    date5 = models.DateField(blank=True, null=True)
    date6 = models.DateField(blank=True, null=True)
    date7 = models.DateField(blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    name5 = models.CharField(max_length=100, blank=True, null=True)
    name6 = models.CharField(max_length=100, blank=True, null=True)
    name7 = models.CharField(max_length=100, blank=True, null=True)
    num1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    l_var_char = models.TextField(blank=True, null=True)
    name8 = models.CharField(max_length=100, blank=True, null=True)
    omit = models.NullBooleanField()
    a_name1 = models.CharField(max_length=50, blank=True, null=True)
    a_name2 = models.CharField(max_length=50, blank=True, null=True)
    a_name3 = models.CharField(max_length=50, blank=True, null=True)
    a_name4 = models.CharField(max_length=50, blank=True, null=True)
    a_name5 = models.CharField(max_length=50, blank=True, null=True)
    a_name6 = models.CharField(max_length=50, blank=True, null=True)
    a_name7 = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50)
    num12 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    num13 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    num14 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    num15 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    num16 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    num17 = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    name9 = models.CharField(max_length=100, blank=True, null=True)
    name10 = models.CharField(max_length=100, blank=True, null=True)
    name11 = models.CharField(max_length=100, blank=True, null=True)
    name12 = models.CharField(max_length=100, blank=True, null=True)
    name13 = models.CharField(max_length=100, blank=True, null=True)
    date8 = models.DateField(blank=True, null=True)
    date9 = models.DateField(blank=True, null=True)
    date10 = models.DateField(blank=True, null=True)
    date11 = models.DateField(blank=True, null=True)
    date12 = models.DateField(blank=True, null=True)
    cc_level = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=250, blank=True, null=True)
    parent_child = models.NullBooleanField()
    cost_addition = models.NullBooleanField()
    rep_syntax = models.TextField(blank=True, null=True)
    close_type = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost2'


class Cost3(models.Model):
    no = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost3'


class CostBudget(models.Model):
    bud_id = models.CharField(max_length=15)
    bud_type = models.NullBooleanField()
    amount1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit5 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit6 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit7 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit8 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit9 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit10 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit11 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit12 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost_id = models.DecimalField(max_digits=20, decimal_places=5)
    finan_year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cost_budget'
        unique_together = (('cost_id', 'finan_year'),)


class Country(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    name_e = models.CharField(max_length=40, blank=True, null=True)
    items_code = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Coupon(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    name_e = models.CharField(max_length=200, blank=True, null=True)
    isdefault = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon'


class Couponcenters(models.Model):
    couponid = models.FloatField()
    centerid = models.FloatField()
    checked = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'couponcenters'
        unique_together = (('couponid', 'centerid'),)


class Coupontypes(models.Model):
    type_id = models.FloatField(blank=True, null=True)
    coupon_id = models.FloatField(primary_key=True)
    from_no = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    to_no = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    isactive = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupontypes'


class CportInvoice(models.Model):
    inv_no = models.BigIntegerField(primary_key=True)
    inv_date = models.DateField()
    job_no = models.CharField(max_length=30, blank=True, null=True)
    bayan = models.CharField(max_length=200, blank=True, null=True)
    accno_debit = models.BigIntegerField(blank=True, null=True)
    flight = models.CharField(max_length=30, blank=True, null=True)
    awb = models.CharField(max_length=30, blank=True, null=True)
    loading_airport = models.CharField(max_length=50, blank=True, null=True)
    discharge_airport = models.CharField(max_length=50, blank=True, null=True)
    shipper = models.CharField(max_length=100, blank=True, null=True)
    commodity = models.CharField(max_length=30, blank=True, null=True)
    chargeable_weight = models.CharField(max_length=30, blank=True, null=True)
    accno_credit = models.BigIntegerField(blank=True, null=True)
    accname_debit = models.CharField(max_length=100, blank=True, null=True)
    advance = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    branch = models.BigIntegerField(blank=True, null=True)
    job_type = models.CharField(max_length=200, blank=True, null=True)
    jop_type = models.CharField(max_length=200, blank=True, null=True)
    vessel_nm = models.CharField(max_length=30, blank=True, null=True)
    cosignee = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    no_packages = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    total_weight = models.CharField(max_length=50, blank=True, null=True)
    job_date = models.DateField(blank=True, null=True)
    deliv_date = models.DateField(blank=True, null=True)
    doc_no = models.CharField(max_length=30, blank=True, null=True)
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cport_invoice'


class CportInvoicedet(models.Model):
    inv_no = models.ForeignKey(CportInvoice, db_column='inv_no')
    serial = models.IntegerField()
    charge = models.ForeignKey(Charges)
    curr1 = models.CharField(max_length=20, blank=True, null=True)
    rate = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    per = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    curr2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    totals = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.BigIntegerField(blank=True, null=True)
    refrenc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cport_invoicedet'
        unique_together = (('inv_no', 'serial', 'charge_id'),)


class CsqlHist(models.Model):
    file_name = models.CharField(primary_key=True, max_length=255)
    lastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csql_hist'


class Currancy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    name_e = models.CharField(max_length=25, blank=True, null=True)
    ex_rate = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    acc_currency = models.BigIntegerField(blank=True, null=True)
    localcurr = models.NullBooleanField()
    sub_unit = models.CharField(max_length=30, blank=True, null=True)
    sub_unit_e = models.CharField(max_length=30, blank=True, null=True)
    have_tax = models.BigIntegerField(blank=True, null=True)
    tax_ratio = models.BigIntegerField(blank=True, null=True)
    tax_accounnt = models.BigIntegerField(blank=True, null=True)
    cash_round_way = models.IntegerField(blank=True, null=True)
    credit_round_way = models.IntegerField(blank=True, null=True)
    cash_round_way_typ = models.NullBooleanField()
    credit_round_way_typ = models.NullBooleanField()
    digits = models.NullBooleanField()
    cash_cost_way = models.NullBooleanField()
    creidt_cost_way = models.NullBooleanField()
    cash_cost_fraction = models.IntegerField(blank=True, null=True)
    creidt_cost_fraction = models.IntegerField(blank=True, null=True)
    creidt_dis_way = models.NullBooleanField()
    cash_dis_way = models.NullBooleanField()
    creidt_dis_fraction = models.IntegerField(blank=True, null=True)
    cash_dis_fraction = models.IntegerField(blank=True, null=True)
    currency_unit = models.CharField(max_length=20, blank=True, null=True)
    currency_unit_e = models.CharField(max_length=20, blank=True, null=True)
    tax_accounnt_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currancy'


class CustCat1(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    name = models.CharField(max_length=40, blank=True, null=True)
    name_e = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_cat1'


class CustCat2(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    name = models.CharField(max_length=40, blank=True, null=True)
    name_e = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_cat2'


class CustTaxes(models.Model):
    id = models.ForeignKey('Taxes', db_column='id')
    cus_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cust_taxes'
        unique_together = (('id', 'cus_id'),)


class Custfinandata(models.Model):
    cfd_branchid = models.BigIntegerField()
    cfd_custid = models.BigIntegerField()
    cfd_creditlimit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    cfd_opbalance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    cfd_balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    cfd_complementbranchid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custfinandata'
        unique_together = (('cfd_branchid', 'cfd_custid'),)


class Custfinanlimit(models.Model):
    cfl_frombranchid = models.BigIntegerField()
    cfl_tobranchid = models.BigIntegerField()
    cfl_custid = models.BigIntegerField()
    cfl_creditlimit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custfinanlimit'
        unique_together = (('cfl_frombranchid', 'cfl_tobranchid', 'cfl_custid'),)


class CustitemPrice(models.Model):
    prodn = models.CharField(max_length=30)
    custno = models.BigIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    conv = models.BigIntegerField(blank=True, null=True)
    target_qty = models.BigIntegerField(blank=True, null=True)
    customer_barcode = models.CharField(max_length=30, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    discount_ratio = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custitem_price'
        unique_together = (('prodn', 'custno'),)


class CustomerBranches(models.Model):
    customer_code = models.BigIntegerField()
    branch = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_branches'
        unique_together = (('customer_code', 'branch'),)


class CustomerLastPrice(models.Model):
    custno = models.BigIntegerField()
    prodn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    conv = models.BigIntegerField(blank=True, null=True)
    prodname = models.CharField(max_length=60, blank=True, null=True)
    p_disc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_last_price'
        unique_together = (('custno', 'prodn'),)


class CustomerPointsBalance(models.Model):
    code = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    cust_no = models.BigIntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    cardid = models.BigIntegerField(blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    is_payment = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'customer_points_balance'
        unique_together = (('code', 'pcenter', 'bilno', 'is_payment'),)


class Customers(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    cat1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    cat2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    caddress = models.CharField(max_length=400, blank=True, null=True)
    tel1 = models.CharField(max_length=100, blank=True, null=True)
    tel2 = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    credit_limit_flage = models.FloatField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    credit_days = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sales_man = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    accno = models.BigIntegerField(blank=True, null=True)
    discount_code = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    name_e = models.CharField(max_length=150, blank=True, null=True)
    tel4 = models.CharField(max_length=100, blank=True, null=True)
    jop = models.CharField(max_length=30, blank=True, null=True)
    national = models.CharField(max_length=30, blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=4000, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    shoon = models.CharField(max_length=12, blank=True, null=True)
    tarkhes = models.CharField(max_length=12, blank=True, null=True)
    op_balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp1 = models.FloatField(blank=True, null=True)
    temp2 = models.FloatField(blank=True, null=True)
    temp3 = models.FloatField(blank=True, null=True)
    temp4 = models.FloatField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    web_page = models.CharField(max_length=100, blank=True, null=True)
    temp_date = models.DateField(blank=True, null=True)
    temp_date2 = models.DateField(blank=True, null=True)
    credit_days_flage = models.IntegerField(blank=True, null=True)
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    to_dt = models.DateField(blank=True, null=True)
    date_flage = models.IntegerField(blank=True, null=True)
    discount_ratio = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    sector = models.CharField(max_length=20, blank=True, null=True)
    gada = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    flat = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)
    isbranch = models.NullBooleanField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter', blank=True, null=True)
    inst_acceptlessthanminval = models.NullBooleanField()
    ob_balance_f = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    ob_balance_curr = models.IntegerField(blank=True, null=True)
    cust_manid = models.CharField(max_length=20, blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    is_stop = models.BigIntegerField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    stop_reason = models.CharField(max_length=150, blank=True, null=True)
    stop_user = models.CharField(max_length=100, blank=True, null=True)
    route = models.IntegerField(blank=True, null=True)
    account_id = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)
    caddress2 = models.CharField(max_length=400, blank=True, null=True)
    caddress3 = models.CharField(max_length=400, blank=True, null=True)
    caddress4 = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class CutType(models.Model):
    cut_id = models.IntegerField(primary_key=True)
    cut_name = models.CharField(max_length=50, blank=True, null=True)
    cut_name_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cut_type'


class DbErrors(models.Model):
    error_code = models.BigIntegerField(primary_key=True)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    eng_message = models.CharField(max_length=255, blank=True, null=True)
    arabic_message = models.CharField(max_length=500, blank=True, null=True)
    sql_syntax = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_errors'


class DbVersion(models.Model):
    version = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'db_version'


class DbVersionCustomer(models.Model):
    version = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'db_version_customer'


class DelivaryMethod(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    name_e = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivary_method'


class Descriptions(models.Model):
    des_id = models.FloatField(primary_key=True)
    des_name = models.CharField(max_length=100, blank=True, null=True)
    des_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descriptions'


class Dictionary(models.Model):
    id = models.CharField(max_length=100)
    app_id = models.CharField(max_length=20)
    arabic = models.CharField(max_length=300, blank=True, null=True)
    english = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dictionary'
        unique_together = (('id', 'app_id'),)


class DiscountCodes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    value = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_codes'


class DiscountPolicy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    comments_a = models.CharField(max_length=250, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    discount_p = models.FloatField(blank=True, null=True)
    round_way = models.BigIntegerField(blank=True, null=True)
    no = models.BigIntegerField(blank=True, null=True)
    cri_items = models.CharField(max_length=1, blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    season = models.CharField(max_length=10, blank=True, null=True)
    like_col = models.CharField(max_length=1, blank=True, null=True)
    like_val = models.CharField(max_length=50, blank=True, null=True)
    app_branch = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_policy'


class DiscountPolicydet(models.Model):
    id = models.ForeignKey(DiscountPolicy, db_column='id')
    prodn = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'discount_policydet'
        unique_together = (('id', 'prodn'),)


class DocSerial(models.Model):
    code = models.IntegerField()
    doc_serl = models.BigIntegerField(blank=True, null=True)
    doc_year = models.IntegerField(blank=True, null=True)
    pcenter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'doc_serial'
        unique_together = (('code', 'pcenter'),)


class DriverArea(models.Model):
    driver_code = models.BigIntegerField()
    area_code = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'driver_area'
        unique_together = (('driver_code', 'area_code'),)


class DriverRoutes(models.Model):
    driver_code = models.IntegerField()
    routes_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'driver_routes'
        unique_together = (('driver_code', 'routes_code'),)


class Drivers(models.Model):
    drv_code = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_e = models.CharField(max_length=80, blank=True, null=True)
    store_id = models.BigIntegerField(blank=True, null=True)
    pcenter = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drivers'


class EmpCommisions(models.Model):
    id_h = models.BigIntegerField()
    emp_cd = models.IntegerField()
    points = models.IntegerField(blank=True, null=True)
    commision_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_commisions'
        unique_together = (('id_h', 'emp_cd'),)


class EmpFile(models.Model):
    emp_cd = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    job_name = models.CharField(max_length=100, blank=True, null=True)
    section_code = models.IntegerField(blank=True, null=True)
    point = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    job_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_file'


class Engineers(models.Model):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_e = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineers'


class EquHandoverDetail(models.Model):
    id = models.BigIntegerField(primary_key=True)
    header_id = models.BigIntegerField()
    equipment_id = models.BigIntegerField()
    kilos = models.BigIntegerField()
    status = models.CharField(max_length=50, blank=True, null=True)
    rent_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'equ_handover_detail'


class EquHandoverHeader(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=25)
    costcenter_id = models.BigIntegerField()
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equ_handover_header'


class EquLoadworksDetail(models.Model):
    id = models.BigIntegerField(primary_key=True)
    header_id = models.BigIntegerField()
    workstype_id = models.BigIntegerField()
    notes = models.CharField(max_length=100, blank=True, null=True)
    status = models.BigIntegerField()
    trans_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'equ_loadworks_detail'


class EquLoadworksHeader(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=25)
    equ_id = models.BigIntegerField()
    tran_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'equ_loadworks_header'


class EquMaint(models.Model):
    id = models.BigIntegerField(primary_key=True)
    equipment_id = models.BigIntegerField()
    maint_date = models.DateField()
    workstype = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'equ_maint'


class EquMaintFollow(models.Model):
    id = models.BigIntegerField(primary_key=True)
    equipment_id = models.BigIntegerField()
    maint_kilo = models.BigIntegerField()
    workstype = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'equ_maint_follow'


class EquRentDetail(models.Model):
    id = models.BigIntegerField(primary_key=True)
    header_id = models.BigIntegerField()
    equipment_id = models.BigIntegerField()
    datefrom = models.DateField()
    dateto = models.DateField()
    notes = models.CharField(max_length=100, blank=True, null=True)
    daily = models.DecimalField(max_digits=18, decimal_places=3)
    monthly = models.DecimalField(max_digits=18, decimal_places=3)
    exceptio_days = models.IntegerField(blank=True, null=True)
    with_driver = models.NullBooleanField()
    with_engine = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'equ_rent_detail'


class EquRentHeader(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=25)
    costcenter_id = models.BigIntegerField()
    request_id = models.BigIntegerField(blank=True, null=True)
    deduct_fridays = models.NullBooleanField()
    inv_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'equ_rent_header'


class EquRequestDetail(models.Model):
    id = models.BigIntegerField(primary_key=True)
    header_id = models.BigIntegerField()
    equipment_id = models.BigIntegerField()
    datefrom = models.DateField()
    dateto = models.DateField()
    monthly = models.DecimalField(max_digits=18, decimal_places=3)
    daily = models.DecimalField(max_digits=18, decimal_places=3)
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equ_request_detail'


class EquRequestHeader(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=25)
    costcenter = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'equ_request_header'


class EquWorkstype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=25)
    name_1 = models.CharField(max_length=50)
    name_2 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'equ_workstype'


class ErrorMsg(models.Model):
    error_id = models.IntegerField()
    error_txt = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'error_msg'
        unique_together = (('error_id', 'lang'),)


class ExchangeRate(models.Model):
    currency_code = models.ForeignKey(Currancy, db_column='currency_code')
    transaction_date = models.DateField(primary_key=True)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'exchange_rate'


class ExpensesTypes(models.Model):
    code = models.BigIntegerField(primary_key=True)
    namear = models.CharField(max_length=100)
    nameen = models.CharField(max_length=100, blank=True, null=True)
    supno = models.ForeignKey('Suppliers', db_column='supno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expenses_types'


class FacilityTab(models.Model):
    facility_id = models.IntegerField(primary_key=True)
    facility_desc = models.CharField(max_length=50)
    facility_desc_e = models.CharField(max_length=50)
    luv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_tab'


class FieldNameDescription(models.Model):
    field_name = models.CharField(primary_key=True, max_length=20)
    field_des = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_name_description'


class FinYears(models.Model):
    year_id = models.IntegerField(primary_key=True)
    year_start_date = models.DateField()
    year_end_date = models.DateField()
    year_descr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_years'


class FixedAllocationAccounts(models.Model):
    account_id = models.BigIntegerField()
    all_account_id = models.BigIntegerField()
    ratio = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'fixed_allocation_accounts'
        unique_together = (('account_id', 'all_account_id'),)


class Floors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    pcenter = models.BigIntegerField(blank=True, null=True)
    f_order = models.BigIntegerField()
    description = models.CharField(max_length=50, blank=True, null=True)
    centerid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'floors'


class GlGroups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_ar_name = models.CharField(max_length=100, blank=True, null=True)
    group_en_name = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_groups'


class GlSettings(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    companyname = models.CharField(max_length=250, blank=True, null=True)
    address_e = models.TextField(blank=True, null=True)
    statment_footer = models.TextField(blank=True, null=True)
    alarm = models.NullBooleanField()
    tel1 = models.CharField(max_length=20, blank=True, null=True)
    tel2 = models.CharField(max_length=20, blank=True, null=True)
    address_a = models.TextField(blank=True, null=True)
    serial = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    n1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    n2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    companyname_e = models.CharField(max_length=250, blank=True, null=True)
    jv_type = models.IntegerField(blank=True, null=True)
    jv_other = models.CharField(max_length=64, blank=True, null=True)
    rcv_type = models.IntegerField(blank=True, null=True)
    rcv_other = models.CharField(max_length=64, blank=True, null=True)
    csv_type = models.IntegerField(blank=True, null=True)
    csv_other = models.CharField(max_length=64, blank=True, null=True)
    ckv_type = models.IntegerField(blank=True, null=True)
    ckv_other = models.CharField(max_length=64, blank=True, null=True)
    bkv_type = models.IntegerField(blank=True, null=True)
    bkv_other = models.CharField(max_length=64, blank=True, null=True)
    csinv_type = models.IntegerField(blank=True, null=True)
    csinv_other = models.CharField(max_length=64, blank=True, null=True)
    crinv_type = models.IntegerField(blank=True, null=True)
    crinv_other = models.CharField(max_length=64, blank=True, null=True)
    ot_type = models.IntegerField(blank=True, null=True)
    ot_other = models.CharField(max_length=64, blank=True, null=True)
    multi_curr_jv = models.IntegerField(blank=True, null=True)
    showinvsman = models.IntegerField(blank=True, null=True)
    brna_ar = models.CharField(max_length=100, blank=True, null=True)
    brna_en = models.CharField(max_length=100, blank=True, null=True)
    assets_acc_type = models.IntegerField(blank=True, null=True)
    payinv_insarfcash = models.NullBooleanField()
    allow_unbalanced_voucher = models.IntegerField(blank=True, null=True)
    allow_document_print = models.IntegerField(blank=True, null=True)
    currency_in_reports = models.IntegerField(blank=True, null=True)
    payinv_insanadat = models.IntegerField(blank=True, null=True)
    auto_acc_currency = models.IntegerField(blank=True, null=True)
    invoice_pay = models.NullBooleanField()
    mandatory_costcenter = models.IntegerField(blank=True, null=True)
    allow_unbalanced_voucher_fcc = models.IntegerField(blank=True, null=True)
    foreign_currency_only = models.CharField(max_length=1, blank=True, null=True)
    payinv_inreceipt = models.NullBooleanField()
    store_dsn_name = models.CharField(max_length=50, blank=True, null=True)
    allow_unbalanced_voucher_forei = models.IntegerField(blank=True, null=True)
    auto_lc_voucher = models.IntegerField(blank=True, null=True)
    personel_dsn_name = models.CharField(max_length=50, blank=True, null=True)
    personel_dsn_name2 = models.CharField(max_length=50, blank=True, null=True)
    akarat_dsn_name = models.CharField(max_length=50, blank=True, null=True)
    neglect_check_gabs = models.NullBooleanField()
    check_is_list = models.NullBooleanField()
    statment_with_costcenter = models.NullBooleanField()
    pay_invoices_fromalltrans = models.NullBooleanField()
    pay_show_debit_and_credit = models.BooleanField()
    breakpoint_mng_expenses_accno = models.FloatField(blank=True, null=True)
    breakpoint_mng_expenses_amount = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    breakpoint_profit_percentage = models.CharField(max_length=255, blank=True, null=True)
    show_compare_with_budget = models.NullBooleanField()
    inv_form = models.NullBooleanField()
    show_nameto_gen_voucher = models.NullBooleanField()
    mandatory_add_cc = models.NullBooleanField()
    show_simpol_for_attach = models.NullBooleanField()
    date_default = models.NullBooleanField()
    duplicate_ref_no = models.NullBooleanField()
    start_w_tasks = models.NullBooleanField()
    web_site = models.CharField(max_length=255, blank=True, null=True)
    e_mail = models.CharField(max_length=255, blank=True, null=True)
    header_footer = models.FloatField(blank=True, null=True)
    global_user = models.CharField(max_length=100, blank=True, null=True)
    cash_bill_detail_show = models.FloatField(blank=True, null=True)
    keep_date_seq = models.NullBooleanField()
    mandatory_payment = models.NullBooleanField()
    location_name_1 = models.CharField(max_length=100, blank=True, null=True)
    location_name_2 = models.CharField(max_length=100, blank=True, null=True)
    location_detail_name_1 = models.CharField(max_length=100, blank=True, null=True)
    location_detail_name_2 = models.CharField(max_length=100, blank=True, null=True)
    budject_id = models.IntegerField(blank=True, null=True)
    txt_1 = models.CharField(max_length=50, blank=True, null=True)
    txt_2 = models.CharField(max_length=50, blank=True, null=True)
    show_justify = models.NullBooleanField()
    mandatory_cc = models.FloatField(blank=True, null=True)
    no_cost = models.FloatField(blank=True, null=True)
    cc_no = models.FloatField(blank=True, null=True)
    guide_costs = models.FloatField(blank=True, null=True)
    guide_revenus = models.FloatField(blank=True, null=True)
    guide_rights = models.FloatField(blank=True, null=True)
    change_accno = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_settings'


class GlUserGroups(models.Model):
    group_id = models.IntegerField()
    user_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gl_user_groups'
        unique_together = (('group_id', 'user_no'),)


class Group1(models.Model):
    no = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group1'


class GudieTemp(models.Model):
    accname = models.CharField(max_length=150, blank=True, null=True)
    accname_e = models.CharField(max_length=150, blank=True, null=True)
    omit = models.NullBooleanField()
    cash = models.NullBooleanField()
    accno = models.CharField(primary_key=True, max_length=37)
    p_m = models.CharField(max_length=1, blank=True, null=True)
    typ_balance = models.CharField(max_length=1, blank=True, null=True)
    accno_5 = models.CharField(max_length=3, blank=True, null=True)
    accno_1 = models.CharField(max_length=2, blank=True, null=True)
    accno_2 = models.CharField(max_length=2, blank=True, null=True)
    accno_3 = models.CharField(max_length=3, blank=True, null=True)
    accno_4 = models.CharField(max_length=3, blank=True, null=True)
    bank = models.NullBooleanField()
    g = models.NullBooleanField()
    g1 = models.NullBooleanField()
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    custno = models.CharField(max_length=20, blank=True, null=True)
    no_2 = models.CharField(max_length=5, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    acc_category = models.IntegerField(blank=True, null=True)
    acc_inv = models.NullBooleanField()
    acc_sales = models.NullBooleanField()
    acc_purchase = models.NullBooleanField()
    acc_personal = models.NullBooleanField()
    acc_assest = models.NullBooleanField()
    acc_currency = models.IntegerField(blank=True, null=True)
    is_gl = models.NullBooleanField()
    alias = models.CharField(max_length=20, blank=True, null=True)
    mask_code = models.CharField(max_length=47, blank=True, null=True)
    account_level = models.IntegerField(blank=True, null=True)
    accno_full = models.CharField(max_length=37, blank=True, null=True)
    isbreakpointevent = models.CharField(max_length=1)
    accno_6 = models.CharField(max_length=3, blank=True, null=True)
    accno_7 = models.CharField(max_length=3, blank=True, null=True)
    accno_8 = models.CharField(max_length=3, blank=True, null=True)
    accno_9 = models.CharField(max_length=3, blank=True, null=True)
    accno_10 = models.IntegerField(blank=True, null=True)
    header_detail = models.CharField(max_length=1, blank=True, null=True)
    balance_control = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    dr_cr_prop = models.CharField(max_length=1, blank=True, null=True)
    parent_acc = models.CharField(max_length=37, blank=True, null=True)
    acc_nature = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gudie_temp'


class Guide(models.Model):
    account_id = models.BigIntegerField(primary_key=True)
    accno_1 = models.CharField(max_length=1, blank=True, null=True)
    accno_2 = models.CharField(max_length=8, blank=True, null=True)
    accno_3 = models.CharField(max_length=8, blank=True, null=True)
    accno_4 = models.CharField(max_length=8, blank=True, null=True)
    accno_5 = models.CharField(max_length=8, blank=True, null=True)
    accno_6 = models.CharField(max_length=8, blank=True, null=True)
    accno_7 = models.CharField(max_length=8, blank=True, null=True)
    accno_8 = models.CharField(max_length=8, blank=True, null=True)
    accno_9 = models.CharField(max_length=8, blank=True, null=True)
    accno_10 = models.CharField(max_length=8, blank=True, null=True)
    accno = models.CharField(unique=True, max_length=40, blank=True, null=True)
    accname = models.CharField(max_length=150, blank=True, null=True)
    accname_e = models.CharField(max_length=150, blank=True, null=True)
    omit = models.BigIntegerField(blank=True, null=True)
    cash = models.BigIntegerField(blank=True, null=True)
    p_m = models.CharField(max_length=1, blank=True, null=True)
    typ_balance = models.CharField(max_length=1, blank=True, null=True)
    bank = models.BigIntegerField(blank=True, null=True)
    g = models.BigIntegerField(blank=True, null=True)
    g1 = models.BigIntegerField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    sort = models.BigIntegerField(blank=True, null=True)
    custno = models.CharField(max_length=20, blank=True, null=True)
    no_2 = models.CharField(max_length=5, blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    acc_category = models.ForeignKey(AccGroups, db_column='acc_category', blank=True, null=True)
    acc_inv = models.BigIntegerField(blank=True, null=True)
    acc_sales = models.BigIntegerField(blank=True, null=True)
    acc_purchase = models.BigIntegerField(blank=True, null=True)
    acc_personal = models.BigIntegerField(blank=True, null=True)
    acc_assest = models.BigIntegerField(blank=True, null=True)
    acc_currency = models.BigIntegerField(blank=True, null=True)
    is_gl = models.BigIntegerField(blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    mask_code = models.CharField(max_length=37, blank=True, null=True)
    account_level = models.BigIntegerField(blank=True, null=True)
    accno_full = models.CharField(max_length=40, blank=True, null=True)
    isbreakpointevent = models.CharField(max_length=1, blank=True, null=True)
    balance_control = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    dr_cr_prop = models.CharField(max_length=1, blank=True, null=True)
    acc_nature = models.CharField(max_length=1, blank=True, null=True)
    old_acc = models.CharField(max_length=14, blank=True, null=True)
    old_acc_full = models.CharField(max_length=14, blank=True, null=True)
    old_mask_acc = models.CharField(max_length=14, blank=True, null=True)
    acc_typ_bal = models.CharField(max_length=1, blank=True, null=True)
    acc_perc = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    parent_child = models.NullBooleanField()
    levels_no = models.IntegerField(blank=True, null=True)
    level_2_length = models.IntegerField(blank=True, null=True)
    level_3_length = models.IntegerField(blank=True, null=True)
    level_4_length = models.IntegerField(blank=True, null=True)
    level_5_length = models.IntegerField(blank=True, null=True)
    level_6_length = models.IntegerField(blank=True, null=True)
    level_7_length = models.IntegerField(blank=True, null=True)
    level_8_length = models.IntegerField(blank=True, null=True)
    level_9_length = models.IntegerField(blank=True, null=True)
    level_10_length = models.IntegerField(blank=True, null=True)
    direct_cash_flow = models.FloatField(blank=True, null=True)
    cattypes_id = models.FloatField(blank=True, null=True)
    cattypes_sort = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guide'


class GuideTrans(models.Model):
    accname = models.CharField(max_length=50, blank=True, null=True)
    accname_e = models.CharField(max_length=50, blank=True, null=True)
    omit = models.NullBooleanField()
    cash = models.NullBooleanField()
    accno = models.BigIntegerField(primary_key=True)
    p_m = models.CharField(max_length=1, blank=True, null=True)
    typ_balance = models.CharField(max_length=1, blank=True, null=True)
    accno_5 = models.IntegerField(blank=True, null=True)
    accno_1 = models.CharField(max_length=1, blank=True, null=True)
    accno_2 = models.CharField(max_length=1, blank=True, null=True)
    accno_3 = models.CharField(max_length=2, blank=True, null=True)
    accno_4 = models.CharField(max_length=2, blank=True, null=True)
    bank = models.NullBooleanField()
    g = models.NullBooleanField()
    g1 = models.NullBooleanField()
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guide_trans'


class HcAccAddDetail(models.Model):
    account = models.ForeignKey('HcGuide', primary_key=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    date5 = models.DateField(blank=True, null=True)
    date6 = models.DateField(blank=True, null=True)
    date7 = models.DateField(blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    name4 = models.CharField(max_length=100, blank=True, null=True)
    name5 = models.CharField(max_length=100, blank=True, null=True)
    name6 = models.CharField(max_length=100, blank=True, null=True)
    name7 = models.CharField(max_length=100, blank=True, null=True)
    num1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    num7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    l_var_char = models.TextField(blank=True, null=True)
    name8 = models.CharField(max_length=100, blank=True, null=True)
    jop = models.CharField(max_length=30, blank=True, null=True)
    national = models.CharField(max_length=30, blank=True, null=True)
    cid = models.CharField(max_length=12, blank=True, null=True)
    shoon = models.CharField(max_length=12, blank=True, null=True)
    tarkhes = models.CharField(max_length=12, blank=True, null=True)
    op_balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    credit_days_flage = models.IntegerField(blank=True, null=True)
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    date_flage = models.IntegerField(blank=True, null=True)
    discount_ratio = models.IntegerField(blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    sector = models.CharField(max_length=20, blank=True, null=True)
    gada = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50, blank=True, null=True)
    flat = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    supno = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    descreption1 = models.CharField(max_length=150, blank=True, null=True)
    desc2 = models.CharField(max_length=100, blank=True, null=True)
    desc3 = models.CharField(max_length=100, blank=True, null=True)
    desc4 = models.CharField(max_length=150, blank=True, null=True)
    amount1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    currancy = models.IntegerField(blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    taamen_co = models.CharField(max_length=100, blank=True, null=True)
    datofcredit = models.DateField(blank=True, null=True)
    bolesa = models.CharField(max_length=30, blank=True, null=True)
    policydate = models.DateField(blank=True, null=True)
    tagded1 = models.DateField(blank=True, null=True)
    tagded2 = models.DateField(blank=True, null=True)
    tagded3 = models.DateField(blank=True, null=True)
    ex_rate = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    v1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v8 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v9 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v10 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v11 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v12 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    vc9 = models.CharField(max_length=100, blank=True, null=True)
    vc10 = models.CharField(max_length=100, blank=True, null=True)
    vc11 = models.CharField(max_length=100, blank=True, null=True)
    vc12 = models.CharField(max_length=100, blank=True, null=True)
    lc_notes = models.TextField(blank=True, null=True)
    conditions = models.CharField(max_length=30, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    v13 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    per = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    invoice_no = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    lc_status = models.IntegerField(blank=True, null=True)
    itmarrvdate = models.DateField(blank=True, null=True)
    lc_accno = models.BigIntegerField(blank=True, null=True)
    reset = models.IntegerField(blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    costcenter_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cash_exp = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    check_exp = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    inst_acceptlessthanminval = models.NullBooleanField()
    balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    isbranch = models.NullBooleanField()
    luv = models.IntegerField(blank=True, null=True)
    pcenter = models.NullBooleanField()
    ob_balance_f = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    ob_balance_curr = models.IntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    test = models.CharField(max_length=500, blank=True, null=True)
    old_accno = models.CharField(max_length=14, blank=True, null=True)
    old_lc_accno = models.CharField(max_length=14, blank=True, null=True)
    new_accno = models.CharField(max_length=14, blank=True, null=True)
    route = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_acc_add_detail'


class HcAccGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    description = models.CharField(max_length=100)
    notes = models.CharField(max_length=200, blank=True, null=True)
    description_e = models.CharField(max_length=100)
    rep_syntax = models.TextField(blank=True, null=True)
    sort_id = models.FloatField(blank=True, null=True)
    typ = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_acc_groups'


class HcAccounts(models.Model):
    company_cd = models.ForeignKey('HcCompanies', db_column='company_cd')
    account = models.ForeignKey('HcGuide')
    related_account_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'hc_accounts'
        unique_together = (('company_cd', 'account_id', 'related_account_id'),)


class HcAsaGuide(models.Model):
    companycd = models.IntegerField()
    account_id = models.BigIntegerField()
    accno_1 = models.CharField(max_length=1, blank=True, null=True)
    accno_2 = models.CharField(max_length=8, blank=True, null=True)
    accno_3 = models.CharField(max_length=8, blank=True, null=True)
    accno_4 = models.CharField(max_length=8, blank=True, null=True)
    accno_5 = models.CharField(max_length=8, blank=True, null=True)
    accno_6 = models.CharField(max_length=8, blank=True, null=True)
    accno_7 = models.CharField(max_length=8, blank=True, null=True)
    accno_8 = models.CharField(max_length=8, blank=True, null=True)
    accno_9 = models.CharField(max_length=8, blank=True, null=True)
    accno_10 = models.CharField(max_length=8, blank=True, null=True)
    accno = models.CharField(max_length=40, blank=True, null=True)
    accname = models.CharField(max_length=150, blank=True, null=True)
    accname_e = models.CharField(max_length=150, blank=True, null=True)
    omit = models.BigIntegerField(blank=True, null=True)
    cash = models.BigIntegerField(blank=True, null=True)
    p_m = models.CharField(max_length=1, blank=True, null=True)
    typ_balance = models.CharField(max_length=1, blank=True, null=True)
    bank = models.BigIntegerField(blank=True, null=True)
    g = models.BigIntegerField(blank=True, null=True)
    g1 = models.BigIntegerField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    sort = models.BigIntegerField(blank=True, null=True)
    custno = models.CharField(max_length=20, blank=True, null=True)
    no_2 = models.CharField(max_length=5, blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    acc_category = models.BigIntegerField(blank=True, null=True)
    acc_inv = models.BigIntegerField(blank=True, null=True)
    acc_sales = models.BigIntegerField(blank=True, null=True)
    acc_purchase = models.BigIntegerField(blank=True, null=True)
    acc_personal = models.BigIntegerField(blank=True, null=True)
    acc_assest = models.BigIntegerField(blank=True, null=True)
    acc_currency = models.BigIntegerField(blank=True, null=True)
    is_gl = models.BigIntegerField(blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    mask_code = models.CharField(max_length=37, blank=True, null=True)
    account_level = models.BigIntegerField(blank=True, null=True)
    accno_full = models.CharField(max_length=40, blank=True, null=True)
    isbreakpointevent = models.CharField(max_length=1, blank=True, null=True)
    balance_control = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    dr_cr_prop = models.CharField(max_length=1, blank=True, null=True)
    acc_nature = models.CharField(max_length=1, blank=True, null=True)
    old_acc = models.CharField(max_length=14, blank=True, null=True)
    old_acc_full = models.CharField(max_length=14, blank=True, null=True)
    old_mask_acc = models.CharField(max_length=14, blank=True, null=True)
    acc_typ_bal = models.CharField(max_length=1, blank=True, null=True)
    acc_perc = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    parent_child = models.NullBooleanField()
    levels_no = models.IntegerField(blank=True, null=True)
    level_2_length = models.IntegerField(blank=True, null=True)
    level_3_length = models.IntegerField(blank=True, null=True)
    level_4_length = models.IntegerField(blank=True, null=True)
    level_5_length = models.IntegerField(blank=True, null=True)
    level_6_length = models.IntegerField(blank=True, null=True)
    level_7_length = models.IntegerField(blank=True, null=True)
    level_8_length = models.IntegerField(blank=True, null=True)
    level_9_length = models.IntegerField(blank=True, null=True)
    level_10_length = models.IntegerField(blank=True, null=True)
    old_accno = models.CharField(max_length=14, blank=True, null=True)
    old_accno_5 = models.FloatField(blank=True, null=True)
    direct_cash_flow = models.FloatField(blank=True, null=True)
    cattypes_id = models.FloatField(blank=True, null=True)
    cattypes_sort = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_asa_guide'
        unique_together = (('companycd', 'accno'), ('companycd', 'account_id'),)


class HcAsaMove(models.Model):
    companycd = models.ForeignKey('HcAsaMove1', db_column='companycd')
    id = models.BigIntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    cost1 = models.BigIntegerField(blank=True, null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=3)
    credit = models.DecimalField(max_digits=20, decimal_places=3)
    details = models.CharField(max_length=500, blank=True, null=True)
    reset = models.ForeignKey('HcAsaMove1', db_column='reset')
    reset_0 = models.ForeignKey('HcAsaMove1', db_column='reset_id')  # Field renamed because of name conflict.
    cost2 = models.BigIntegerField(blank=True, null=True)
    cost3 = models.BigIntegerField(blank=True, null=True)
    cost4 = models.BigIntegerField(blank=True, null=True)
    chek = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.ForeignKey('HcAsaMove1', db_column='branch')
    flage = models.NullBooleanField()
    payed = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit1 = models.DecimalField(max_digits=20, decimal_places=4)
    debit1 = models.DecimalField(max_digits=20, decimal_places=4)
    currency = models.IntegerField(blank=True, null=True)
    curr_rate = models.DecimalField(max_digits=20, decimal_places=5)
    invno_e = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    sman_e = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    flage_checked = models.NullBooleanField()
    invoice_checked = models.NullBooleanField()
    bank_flag = models.IntegerField(blank=True, null=True)
    check_book = models.CharField(max_length=35, blank=True, null=True)
    payed_reset = models.IntegerField(blank=True, null=True)
    payed_reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    payed_branch = models.IntegerField(blank=True, null=True)
    ser = models.IntegerField(blank=True, null=True)
    return_no = models.CharField(max_length=30, blank=True, null=True)
    deposit_type_id = models.IntegerField(blank=True, null=True)
    deposit_bank = models.CharField(max_length=100, blank=True, null=True)
    deposit_cheque = models.CharField(max_length=100, blank=True, null=True)
    deposit_date = models.DateField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    company_code = models.FloatField(blank=True, null=True)
    accname = models.CharField(max_length=250, blank=True, null=True)
    accname_e = models.CharField(max_length=250, blank=True, null=True)
    original_id = models.FloatField(blank=True, null=True)
    old_accno = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_asa_move'
        unique_together = (('companycd', 'id', 'reset', 'reset_id', 'branch'),)


class HcAsaMove1(models.Model):
    companycd = models.IntegerField()
    batch = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    reset = models.IntegerField()
    sr = models.NullBooleanField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    name_to = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=500, blank=True, null=True)
    chek = models.BigIntegerField(blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.IntegerField()
    user_no = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    chek_flage = models.NullBooleanField()
    bank = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    details_1 = models.CharField(max_length=500, blank=True, null=True)
    currency_type = models.IntegerField(blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    post_flage = models.NullBooleanField()
    print_usr = models.IntegerField(blank=True, null=True)
    print_dtm = models.DateField(blank=True, null=True)
    print_no = models.IntegerField(blank=True, null=True)
    check_book = models.CharField(max_length=50, blank=True, null=True)
    paid = models.NullBooleanField()
    site_requisition = models.CharField(max_length=20, blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    approved = models.NullBooleanField()
    typ = models.NullBooleanField()
    inter_company = models.NullBooleanField()
    post_date = models.DateField(blank=True, null=True)
    post_user = models.CharField(max_length=16, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_user = models.CharField(max_length=16, blank=True, null=True)
    posted = models.NullBooleanField()
    is_close_voucher = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_asa_move1'
        unique_together = (('companycd', 'reset', 'reset_id', 'branch'),)


class HcCattypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    naotes = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50)
    sort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_cattypes'


class HcCompanies(models.Model):
    cd = models.IntegerField(primary_key=True)
    type_cd = models.ForeignKey('HcType', db_column='type_cd', blank=True, null=True)
    parent_cd = models.ForeignKey('self', db_column='parent__cd', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    name = models.CharField(max_length=150, blank=True, null=True)
    name_e = models.CharField(max_length=150, blank=True, null=True)
    item_level = models.IntegerField(blank=True, null=True)
    item_sort = models.CharField(max_length=300, blank=True, null=True)
    isgroup = models.CharField(max_length=1, blank=True, null=True)
    server = models.CharField(max_length=300, blank=True, null=True)
    service_name = models.CharField(max_length=300, blank=True, null=True)
    logid = models.CharField(max_length=300, blank=True, null=True)
    logpassword = models.CharField(max_length=300, blank=True, null=True)
    dbtype = models.IntegerField(blank=True, null=True)
    db_global_name = models.CharField(max_length=250, blank=True, null=True)
    sysdbauser = models.CharField(max_length=50, blank=True, null=True)
    sysdbapwd = models.CharField(max_length=50, blank=True, null=True)
    repadminpwd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_companies'


class HcGuide(models.Model):
    account_id = models.BigIntegerField(primary_key=True)
    accno_1 = models.CharField(max_length=1, blank=True, null=True)
    accno_2 = models.CharField(max_length=8, blank=True, null=True)
    accno_3 = models.CharField(max_length=8, blank=True, null=True)
    accno_4 = models.CharField(max_length=8, blank=True, null=True)
    accno_5 = models.CharField(max_length=8, blank=True, null=True)
    accno_6 = models.CharField(max_length=8, blank=True, null=True)
    accno_7 = models.CharField(max_length=8, blank=True, null=True)
    accno_8 = models.CharField(max_length=8, blank=True, null=True)
    accno_9 = models.CharField(max_length=8, blank=True, null=True)
    accno_10 = models.CharField(max_length=8, blank=True, null=True)
    accno = models.CharField(unique=True, max_length=40, blank=True, null=True)
    accname = models.CharField(max_length=150, blank=True, null=True)
    accname_e = models.CharField(max_length=150, blank=True, null=True)
    omit = models.BigIntegerField(blank=True, null=True)
    cash = models.BigIntegerField(blank=True, null=True)
    p_m = models.CharField(max_length=1, blank=True, null=True)
    typ_balance = models.CharField(max_length=1, blank=True, null=True)
    bank = models.BigIntegerField(blank=True, null=True)
    g = models.BigIntegerField(blank=True, null=True)
    g1 = models.BigIntegerField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    sort = models.BigIntegerField(blank=True, null=True)
    custno = models.CharField(max_length=20, blank=True, null=True)
    no_2 = models.CharField(max_length=5, blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    acc_category = models.ForeignKey(HcAccGroups, db_column='acc_category', blank=True, null=True)
    acc_inv = models.BigIntegerField(blank=True, null=True)
    acc_sales = models.BigIntegerField(blank=True, null=True)
    acc_purchase = models.BigIntegerField(blank=True, null=True)
    acc_personal = models.BigIntegerField(blank=True, null=True)
    acc_assest = models.BigIntegerField(blank=True, null=True)
    acc_currency = models.BigIntegerField(blank=True, null=True)
    is_gl = models.BigIntegerField(blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    mask_code = models.CharField(max_length=37, blank=True, null=True)
    account_level = models.BigIntegerField(blank=True, null=True)
    accno_full = models.CharField(max_length=40, blank=True, null=True)
    isbreakpointevent = models.CharField(max_length=1, blank=True, null=True)
    balance_control = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    dr_cr_prop = models.CharField(max_length=1, blank=True, null=True)
    acc_nature = models.CharField(max_length=1, blank=True, null=True)
    old_acc = models.CharField(max_length=14, blank=True, null=True)
    old_acc_full = models.CharField(max_length=14, blank=True, null=True)
    old_mask_acc = models.CharField(max_length=14, blank=True, null=True)
    acc_typ_bal = models.CharField(max_length=1, blank=True, null=True)
    acc_perc = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    parent_child = models.NullBooleanField()
    levels_no = models.IntegerField(blank=True, null=True)
    level_2_length = models.IntegerField(blank=True, null=True)
    level_3_length = models.IntegerField(blank=True, null=True)
    level_4_length = models.IntegerField(blank=True, null=True)
    level_5_length = models.IntegerField(blank=True, null=True)
    level_6_length = models.IntegerField(blank=True, null=True)
    level_7_length = models.IntegerField(blank=True, null=True)
    level_8_length = models.IntegerField(blank=True, null=True)
    level_9_length = models.IntegerField(blank=True, null=True)
    level_10_length = models.IntegerField(blank=True, null=True)
    old_accno = models.CharField(max_length=14, blank=True, null=True)
    old_accno_5 = models.FloatField(blank=True, null=True)
    cattypes_id = models.FloatField(blank=True, null=True)
    cattypes_sort = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_guide'


class HcType(models.Model):
    cd = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150, blank=True, null=True)
    name_e = models.CharField(max_length=150, blank=True, null=True)
    icon = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hc_type'


class HcUserAccounts(models.Model):
    user_no = models.IntegerField()
    account_no = models.BigIntegerField()
    acc_tp = models.CharField(max_length=1, blank=True, null=True)
    acc_lvl = models.IntegerField(blank=True, null=True)
    view_acc = models.NullBooleanField()
    trans_acc = models.NullBooleanField()
    print_acc = models.NullBooleanField()
    edit_acc = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'hc_user_accounts'
        unique_together = (('user_no', 'account_no'),)


class HstItembalancepost(models.Model):
    table_name = models.CharField(primary_key=True, max_length=80)
    install_date = models.DateField(blank=True, null=True)
    table_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hst_itembalancepost'


class InstalmentInvoiceSetup(models.Model):
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    first_payment_value = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    instalment_count = models.IntegerField(blank=True, null=True)
    first_instalment_date = models.DateField(blank=True, null=True)
    instalment_interval = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instalment_invoice_setup'
        unique_together = (('code', 'pcenter', 'bilno'),)


class InvItems(models.Model):
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    reset = models.IntegerField()
    branch = models.IntegerField()
    qty = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    item_desc = models.CharField(max_length=250, blank=True, null=True)
    ser = models.IntegerField()
    item_unit = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    media = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    siz = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    u_gross = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    disc = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    u_net = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    t_freq = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    tg_cost = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    tn_cost = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    vdate = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_items'
        unique_together = (('reset_id', 'reset', 'branch', 'ser'),)


class InvItemsHeader(models.Model):
    reset = models.IntegerField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    branch = models.IntegerField()
    column1 = models.CharField(max_length=100, blank=True, null=True)
    column2 = models.CharField(max_length=100, blank=True, null=True)
    column3 = models.CharField(max_length=100, blank=True, null=True)
    column4 = models.CharField(max_length=100, blank=True, null=True)
    column5 = models.CharField(max_length=100, blank=True, null=True)
    column6 = models.CharField(max_length=14, blank=True, null=True)
    deliv_fees = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    disc_value = models.FloatField(blank=True, null=True)
    cost1_no = models.FloatField(blank=True, null=True)
    cost1_name = models.CharField(max_length=250, blank=True, null=True)
    cost2_no = models.FloatField(blank=True, null=True)
    cost2_name = models.CharField(max_length=250, blank=True, null=True)
    sal_cost1_no = models.FloatField(blank=True, null=True)
    sal_cost1_name = models.CharField(max_length=250, blank=True, null=True)
    sal_cost2_no = models.FloatField(blank=True, null=True)
    sal_cost2_name = models.CharField(max_length=250, blank=True, null=True)
    sales_acc = models.CharField(max_length=14, blank=True, null=True)
    user_billno = models.FloatField(blank=True, null=True)
    sales_acc_name = models.CharField(max_length=100, blank=True, null=True)
    direct_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_items_header'
        unique_together = (('reset', 'reset_id', 'branch'),)


class InvPurimpfile(models.Model):
    code = models.BigIntegerField(primary_key=True)
    item_code = models.BigIntegerField()
    item_name = models.CharField(max_length=50, blank=True, null=True)
    ar_displayname = models.CharField(max_length=50, blank=True, null=True)
    en_displayname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_purimpfile'


class InvVartable(models.Model):
    prodn = models.CharField(primary_key=True, max_length=30)
    company = models.CharField(max_length=10, blank=True, null=True)
    season = models.CharField(max_length=10, blank=True, null=True)
    family = models.CharField(max_length=30, blank=True, null=True)
    style = models.CharField(max_length=30, blank=True, null=True)
    fabric_no = models.CharField(max_length=30, blank=True, null=True)
    trend = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    pvp_europ = models.CharField(max_length=30, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    article = models.CharField(max_length=40, blank=True, null=True)
    size_group = models.CharField(max_length=40, blank=True, null=True)
    size_code = models.CharField(max_length=40, blank=True, null=True)
    siz = models.CharField(max_length=40, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    origin = models.CharField(max_length=50, blank=True, null=True)
    qty = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    cost = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)
    sal_price = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    firstcat = models.BigIntegerField(blank=True, null=True)
    secondcat = models.BigIntegerField(blank=True, null=True)
    thirdcat = models.BigIntegerField(blank=True, null=True)
    fourthcat = models.BigIntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=50, blank=True, null=True)
    country_ar = models.CharField(max_length=50, blank=True, null=True)
    curr1 = models.BigIntegerField(blank=True, null=True)
    price_curr1 = models.BigIntegerField(blank=True, null=True)
    curr2 = models.BigIntegerField(blank=True, null=True)
    price_curr2 = models.BigIntegerField(blank=True, null=True)
    vendor_item_no = models.CharField(max_length=40, blank=True, null=True)
    item_waight = models.CharField(max_length=15, blank=True, null=True)
    item_volume = models.CharField(max_length=15, blank=True, null=True)
    item_thickness = models.CharField(max_length=15, blank=True, null=True)
    item_diameter = models.CharField(max_length=15, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_vartable'


class Invoice(models.Model):
    branch = models.IntegerField()
    reset = models.IntegerField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    head_descr = models.CharField(max_length=500, blank=True, null=True)
    sub_descr = models.CharField(max_length=200, blank=True, null=True)
    descr_1 = models.CharField(max_length=100, blank=True, null=True)
    descr_2 = models.CharField(max_length=100, blank=True, null=True)
    descr_3 = models.CharField(max_length=100, blank=True, null=True)
    descr_4 = models.CharField(max_length=100, blank=True, null=True)
    descr_5 = models.CharField(max_length=100, blank=True, null=True)
    descr_6 = models.CharField(max_length=100, blank=True, null=True)
    descr_7 = models.CharField(max_length=100, blank=True, null=True)
    descr_8 = models.CharField(max_length=100, blank=True, null=True)
    descr_9 = models.CharField(max_length=100, blank=True, null=True)
    descr_10 = models.CharField(max_length=100, blank=True, null=True)
    amt1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt3 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt4 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt5 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt6 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt7 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt8 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt9 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt10 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    sub_1 = models.CharField(max_length=200, blank=True, null=True)
    sub_2 = models.CharField(max_length=200, blank=True, null=True)
    sub_3 = models.CharField(max_length=200, blank=True, null=True)
    sub_4 = models.CharField(max_length=200, blank=True, null=True)
    bank_details = models.CharField(max_length=500, blank=True, null=True)
    qty_1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_3 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_4 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_5 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_6 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_7 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_8 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_9 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty_10 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price3 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price4 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price5 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price6 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price7 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price8 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price9 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price10 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    amt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt11 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt12 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amt13 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    descr11 = models.CharField(max_length=100, blank=True, null=True)
    descr12 = models.CharField(max_length=100, blank=True, null=True)
    descr13 = models.CharField(max_length=100, blank=True, null=True)
    qty11 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty12 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty13 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price11 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price12 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit_price13 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'
        unique_together = (('branch', 'reset', 'reset_id'),)


class Invoice1(models.Model):
    id = models.BigIntegerField()
    ser = models.BigIntegerField()
    vdate = models.DateField(blank=True, null=True)
    billto = models.CharField(max_length=50, blank=True, null=True)
    ponumber = models.CharField(max_length=20, blank=True, null=True)
    terms = models.CharField(max_length=50, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    comission = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    projects = models.CharField(max_length=50, blank=True, null=True)
    currency = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice1'
        unique_together = (('id', 'ser'),)


class InvoiceSerial(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    name_e = models.CharField(max_length=30)
    n1 = models.BigIntegerField()
    flage = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_serial'







class Issue1(models.Model):
    class Meta:
        managed = False
        db_table = 'issue_1'
        unique_together = (('code', 'pcenter', 'bilno'),)
    code = models.IntegerField(primary_key=True)
    vdate = models.DateField(blank=True, null=True)
    sman = models.ForeignKey('SalesMen', db_column='sman', blank=True, null=True)
    pur_order = models.CharField(max_length=30, blank=True, null=True)
    qutaion = models.BigIntegerField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    customer_data = models.CharField(max_length=100, blank=True, null=True)
    customer_name = models.CharField(max_length=800, blank=True, null=True)
    user_no = models.BigIntegerField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    notes_print_falge = models.NullBooleanField()
    bilno = models.BigIntegerField()
    custno = models.ForeignKey(Customers, db_column='custno', blank=True, null=True)
    templet = models.NullBooleanField()
    rev_ok = models.NullBooleanField()
    layaway = models.NullBooleanField()
    deli_date = models.DateField(blank=True, null=True)
    terms = models.ForeignKey('PaymentTerms', db_column='terms', blank=True, null=True)
    payed = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    payed1 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    payed2 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    pay_ok = models.NullBooleanField()
    reset_bilno = models.BigIntegerField(blank=True, null=True)
    step1 = models.NullBooleanField()
    step2 = models.NullBooleanField()
    step3 = models.NullBooleanField()
    step4 = models.NullBooleanField()
    from_type = models.IntegerField(blank=True, null=True)
    note6 = models.CharField(max_length=100, blank=True, null=True)
    note7 = models.CharField(max_length=100, blank=True, null=True)
    driver_name = models.CharField(max_length=60, blank=True, null=True)
    car_no = models.CharField(max_length=20, blank=True, null=True)
    leave_time = models.DateField(blank=True, null=True)
    note1 = models.CharField(max_length=40, blank=True, null=True)
    note2 = models.CharField(max_length=40, blank=True, null=True)
    note3 = models.CharField(max_length=40, blank=True, null=True)
    note4 = models.CharField(max_length=40, blank=True, null=True)
    note5 = models.CharField(max_length=40, blank=True, null=True)
    vtime = models.DateField(blank=True, null=True)
    hand_time = models.DateField(blank=True, null=True)
    drv_code = models.ForeignKey(Drivers, db_column='drv_code', blank=True, null=True)
    cust_no = models.ForeignKey(CashCustomers, db_column='cust_no', blank=True, null=True)
    return_time = models.DateField(blank=True, null=True)
    step5 = models.NullBooleanField()
    cash_delivary = models.ForeignKey(CashDelivary, blank=True, null=True)
    recieved_flage = models.NullBooleanField()
    area_code = models.CharField(max_length=20, blank=True, null=True)
    sector = models.CharField(max_length=30, blank=True, null=True)
    gada = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    house = models.CharField(max_length=30, blank=True, null=True)
    flat = models.CharField(max_length=30, blank=True, null=True)
    floor = models.CharField(max_length=30, blank=True, null=True)
    cust_tel = models.CharField(max_length=20, blank=True, null=True)
    bnkcomm = models.FloatField(blank=True, null=True)
    payment2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    payment3 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    p_date1 = models.DateField(blank=True, null=True)
    p_date2 = models.DateField(blank=True, null=True)
    p_date3 = models.DateField(blank=True, null=True)
    visit_no = models.CharField(max_length=10, blank=True, null=True)
    temp_date = models.DateField(blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    prod_id = models.BigIntegerField(blank=True, null=True)
    equipment_code = models.CharField(max_length=10, blank=True, null=True)
    f11_payed = models.FloatField(blank=True, null=True)
    costcenter_id = models.BigIntegerField(blank=True, null=True)
    xcode = models.IntegerField(blank=True, null=True)
    curr_id = models.BigIntegerField(blank=True, null=True)
    curr_rate = models.DecimalField(max_digits=15, decimal_places=7, blank=True, null=True)
    cont_equipment_code = models.CharField(max_length=10, blank=True, null=True)
    sec_id = models.IntegerField(blank=True, null=True)
    sec_center = models.BigIntegerField(blank=True, null=True)
    km_count = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    jop_no = models.CharField(max_length=30, blank=True, null=True)
    cust_phone1 = models.CharField(max_length=20, blank=True, null=True)
    cust_phone2 = models.CharField(max_length=20, blank=True, null=True)
    cust_add = models.CharField(max_length=200, blank=True, null=True)
    cust_ref = models.CharField(max_length=200, blank=True, null=True)
    cust_resp = models.CharField(max_length=100, blank=True, null=True)
    printingtimes = models.IntegerField(blank=True, null=True)
    total_act_catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    inv_type = models.NullBooleanField()
    shift_id = models.BigIntegerField(blank=True, null=True)
    inv1 = models.BigIntegerField(blank=True, null=True)
    inv2 = models.BigIntegerField(blank=True, null=True)
    engineer_commission = models.FloatField(blank=True, null=True)
    engineer_id = models.BigIntegerField(blank=True, null=True)
    manager_commission = models.FloatField(blank=True, null=True)
    manager_id = models.BigIntegerField(blank=True, null=True)
    salesman_commission = models.FloatField(blank=True, null=True)
    salesman = models.ForeignKey('SalesMen', blank=True, null=True)
    delivary_method_id = models.BigIntegerField(blank=True, null=True)
    form_no = models.BigIntegerField(blank=True, null=True)
    print_ok = models.BigIntegerField(blank=True, null=True)
    sales_commm = models.FloatField(blank=True, null=True)
    accept_user = models.CharField(max_length=16, blank=True, null=True)
    account_item_code = models.BigIntegerField(blank=True, null=True)
    purchase_order_no = models.BigIntegerField(blank=True, null=True)
    purchase_order_date = models.DateField(blank=True, null=True)
    auto_issue = models.NullBooleanField()
    round_figure = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=4000, blank=True, null=True)
    order_stat = models.CharField(max_length=255, blank=True, null=True)
    machine_no = models.FloatField(blank=True, null=True)
    insur_remaining_amt = models.DecimalField(max_digits=22, decimal_places=6, blank=True, null=True)
    insur_rem = models.DecimalField(max_digits=22, decimal_places=6, blank=True, null=True)
    price_type = models.NullBooleanField()
    price_code = models.BigIntegerField(blank=True, null=True)
    depr_accno = models.CharField(max_length=14, blank=True, null=True)
    cashcredit_type = models.CharField(max_length=25, blank=True, null=True)
    total_cur = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    total = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    discount = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    discount_cur = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    performa_bilno = models.BigIntegerField(blank=True, null=True)
    performa_pcenter = models.BigIntegerField(blank=True, null=True)
    cardid = models.BigIntegerField(blank=True, null=True)
    isrestaurant = models.FloatField(blank=True, null=True)
    rst_paid = models.FloatField(blank=True, null=True)
    rst_remain = models.FloatField(blank=True, null=True)
    order_type = models.NullBooleanField()
    rst_shift_id = models.BigIntegerField(blank=True, null=True)
    tableid = models.FloatField(blank=True, null=True)
    iscocked = models.NullBooleanField()
    floorid = models.FloatField(blank=True, null=True)
    sectionid = models.FloatField(blank=True, null=True)
    addressid = models.BigIntegerField(blank=True, null=True)
    driver_name_e = models.CharField(max_length=60, blank=True, null=True)
    orderstateno = models.FloatField(blank=True, null=True)
    latereasoncode = models.BigIntegerField(blank=True, null=True)
    discountpercentage = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    orderid = models.BigIntegerField(blank=True, null=True)
    discount_1 = models.FloatField(blank=True, null=True)
    discount_c = models.FloatField(blank=True, null=True)
    coupontypes_no = models.FloatField(blank=True, null=True)
    coupontypes_id = models.FloatField(blank=True, null=True)
    discount_v = models.FloatField(blank=True, null=True)
    void = models.FloatField(blank=True, null=True)
    void_items_balance = models.FloatField(blank=True, null=True)



class Issue1BillnoRes(models.Model):
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    bilno1 = models.BigIntegerField(blank=True, null=True)
    code1 = models.IntegerField(blank=True, null=True)
    pcenter1 = models.ForeignKey(Centers, db_column='pcenter1', blank=True, null=True)
    id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'issue_1_billno_res'
        unique_together = (('code', 'pcenter', 'bilno', 'id'),)


class Issue1Costlist(models.Model):
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    vdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_1_costlist'


class Issue1Credtnotes(models.Model):
    code = models.ForeignKey(Issue1, db_column='code')
    pcenter = models.ForeignKey(Issue1, db_column='pcenter')
    bilno = models.ForeignKey(Issue1, db_column='bilno')
    id = models.BigIntegerField()
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'issue_1_credtnotes'
        unique_together = (('code', 'pcenter', 'bilno', 'id'),)


class Issue1Hist(models.Model):
    trn_id = models.BigIntegerField()
    code = models.IntegerField()
    vdate = models.DateField(blank=True, null=True)
    sman = models.ForeignKey('SalesMen', db_column='sman', blank=True, null=True)
    pur_order = models.CharField(max_length=30, blank=True, null=True)
    qutaion = models.CharField(max_length=30, blank=True, null=True)
    payment = models.NullBooleanField()
    discount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    customer_data = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    user_no = models.BigIntegerField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    notes = models.TextField(blank=True, null=True)
    notes_print_falge = models.NullBooleanField()
    bilno = models.BigIntegerField()
    custno = models.BigIntegerField(blank=True, null=True)
    templet = models.NullBooleanField()
    rev_ok = models.NullBooleanField()
    layaway = models.NullBooleanField()
    deli_date = models.DateField(blank=True, null=True)
    terms = models.BigIntegerField(blank=True, null=True)
    step1 = models.NullBooleanField()
    step2 = models.NullBooleanField()
    step3 = models.NullBooleanField()
    step4 = models.NullBooleanField()
    payed1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    payed2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    reset_bilno = models.BigIntegerField(blank=True, null=True)
    from_type = models.NullBooleanField()
    vtime = models.DateField(blank=True, null=True)
    hand_time = models.DateField(blank=True, null=True)
    drv_code = models.BigIntegerField(blank=True, null=True)
    cust_no = models.BigIntegerField(blank=True, null=True)
    return_time = models.DateField(blank=True, null=True)
    step5 = models.NullBooleanField()
    cash_delivary_id = models.BigIntegerField(blank=True, null=True)
    trn_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_1_hist'
        unique_together = (('trn_id', 'code', 'pcenter', 'bilno'),)


class Issue1Payterms(models.Model):
    code = models.BigIntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    id = models.ForeignKey('PaymentTerms', db_column='id')
    amount = models.FloatField()
    bnkcomm = models.FloatField(blank=True, null=True)
    credtnotes_id = models.BigIntegerField(blank=True, null=True)
    trn_id = models.FloatField(blank=True, null=True)
    pay_id = models.BigIntegerField()
    main_paid_cash = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_1_payterms'
        unique_together = (('code', 'pcenter', 'bilno', 'id', 'pay_id'),)


class Issue1PaytermsHist(models.Model):
    trn_id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    id = models.ForeignKey('PaymentTerms', db_column='id')
    amount = models.FloatField()
    bnkcomm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_1_payterms_hist'
        unique_together = (('trn_id', 'code', 'pcenter', 'bilno', 'id'),)


class Issue1PaytermsP(models.Model):
    code = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    id = models.BigIntegerField()
    amount = models.FloatField()
    bnkcomm = models.FloatField(blank=True, null=True)
    credtnotes_id = models.BigIntegerField(blank=True, null=True)
    trn_id = models.FloatField(blank=True, null=True)
    pay_id = models.BigIntegerField()
    main_paid_cash = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_1_payterms_p'
        unique_together = (('code', 'pcenter', 'bilno', 'id', 'pay_id'),)


class Issue1Temp(models.Model):
    code = models.IntegerField()
    total = models.FloatField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    rst_shift_id = models.BigIntegerField(blank=True, null=True)
    table_id = models.IntegerField(blank=True, null=True)
    order_stat = models.CharField(max_length=10, blank=True, null=True)
    order_type = models.NullBooleanField()
    iscocked = models.NullBooleanField()
    floorid = models.FloatField(blank=True, null=True)
    sectionid = models.FloatField(blank=True, null=True)
    tableid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_1_temp'
        unique_together = (('code', 'pcenter', 'bilno'),)


class Issue2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    price = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    udisc_p = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    udisc = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    item_cost = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    temp1 = models.DecimalField(max_digits=22, decimal_places=6, blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    non_invent = models.NullBooleanField()
    total = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    bilno = models.BigIntegerField()
    warenty = models.NullBooleanField()
    warenty_date = models.DateField(blank=True, null=True)
    line_notes = models.TextField(blank=True, null=True)
    disc2 = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    iss_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    kit_no = models.BigIntegerField(blank=True, null=True)
    kit_qty = models.FloatField(blank=True, null=True)
    di1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp_qty = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    iss_prodname = models.CharField(max_length=200, blank=True, null=True)
    unit_name = models.CharField(max_length=25, blank=True, null=True)
    prod_id = models.BigIntegerField(blank=True, null=True)
    conv2 = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    free_class = models.BigIntegerField(blank=True, null=True)
    temp_price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    price1 = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    udisc1 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    total1 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    disc21 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    sman = models.ForeignKey('SalesMen', db_column='sman', blank=True, null=True)
    itemsort = models.BigIntegerField(blank=True, null=True)
    comppricemanualmod = models.NullBooleanField()
    marblelinenotes = models.TextField(blank=True, null=True)
    di_flage = models.BigIntegerField(blank=True, null=True)
    layaway = models.NullBooleanField()
    cont_equipment_code = models.CharField(max_length=10, blank=True, null=True)
    related_branch = models.BigIntegerField(blank=True, null=True)
    related_code = models.IntegerField(blank=True, null=True)
    related_billno = models.BigIntegerField(blank=True, null=True)
    related_id = models.BigIntegerField(blank=True, null=True)
    originparentid = models.BigIntegerField(blank=True, null=True)
    catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    act_catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    calc_again = models.NullBooleanField()
    batchno = models.CharField(max_length=20, blank=True, null=True)
    alteration_type = models.IntegerField(blank=True, null=True)
    deliver_date = models.DateField(blank=True, null=True)
    deliverd = models.NullBooleanField()
    check_takeaway_dinning = models.CharField(max_length=1, blank=True, null=True)
    achieve_ratio1 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    achieve_ratio2 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    achieve_ratio3 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    pkt_no = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qty1 = models.FloatField(blank=True, null=True)
    start_from = models.BigIntegerField(blank=True, null=True)
    end_to = models.BigIntegerField(blank=True, null=True)
    start_group = models.BigIntegerField(blank=True, null=True)
    end_group = models.BigIntegerField(blank=True, null=True)
    ser_qty = models.FloatField(blank=True, null=True)
    prod_typ = models.BigIntegerField(blank=True, null=True)
    warenty_type = models.BigIntegerField(blank=True, null=True)
    customer_barcode = models.CharField(max_length=30, blank=True, null=True)
    inv1 = models.BigIntegerField(blank=True, null=True)
    inv2 = models.BigIntegerField(blank=True, null=True)
    typ = models.NullBooleanField()
    adjust_move = models.IntegerField(blank=True, null=True)
    shipment_no = models.IntegerField(blank=True, null=True)
    item_level = models.IntegerField(blank=True, null=True)
    disc2_tmp = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    avg_cost = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    item_add_assem = models.NullBooleanField()
    discount_is2_1 = models.FloatField(blank=True, null=True)
    discount_is2_c = models.FloatField(blank=True, null=True)
    discount_is2_v = models.FloatField(blank=True, null=True)
    iscocked = models.NullBooleanField()
    paid = models.NullBooleanField()
    printed = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'issue_2'
        unique_together = (('id', 'code', 'pcenter', 'bilno'),)


class Issue2Expire(models.Model):
    id = models.ForeignKey(Issue2, db_column='id')
    code = models.ForeignKey(Issue2, db_column='code')
    pcenter = models.ForeignKey(Issue2, db_column='pcenter')
    bilno = models.ForeignKey(Issue2, db_column='bilno')
    exp_date = models.DateField()
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    batchno = models.CharField(max_length=20, blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_2_expire'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'exp_date'),)


class Issue2ExpireHist(models.Model):
    trn_id = models.BigIntegerField()
    id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    exp_date = models.DateField()
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_2_expire_hist'
        unique_together = (('trn_id', 'id', 'code', 'pcenter', 'bilno', 'exp_date'),)


class Issue2Hist(models.Model):
    trn_id = models.BigIntegerField()
    id = models.BigIntegerField()
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    udisc_p = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    udisc = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    item_cost = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    non_invent = models.NullBooleanField()
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    bilno = models.BigIntegerField()
    warenty = models.NullBooleanField()
    warenty_date = models.DateField(blank=True, null=True)
    line_notes = models.CharField(max_length=200, blank=True, null=True)
    disc2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    iss_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    kit_no = models.BigIntegerField(blank=True, null=True)
    kit_qty = models.BigIntegerField(blank=True, null=True)
    di1 = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    di2 = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    di3 = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    temp_qty = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    free_class = models.BigIntegerField(blank=True, null=True)
    temp_price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    prod_id = models.BigIntegerField(blank=True, null=True)
    conv2 = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_2_hist'
        unique_together = (('trn_id', 'id', 'code', 'pcenter', 'bilno'),)


class Issue2Temp(models.Model):
    id = models.BigIntegerField()
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    conv2 = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    productname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_2_temp'


class Issue3(models.Model):
    id = models.BigIntegerField()
    id_1 = models.BigIntegerField()
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    origin_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    udisc_p = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)
    udisc = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    bilno = models.CharField(max_length=30, blank=True, null=True)
    item_cost = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    unit_text = models.BigIntegerField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    table_id = models.BigIntegerField(unique=True)
    kit_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_3'
        unique_together = (('id', 'id_1', 'table_id'),)


class IssueLaboures(models.Model):
    id = models.ForeignKey(Issue2, db_column='id')
    code = models.ForeignKey(Issue2, db_column='code')
    pcenter = models.ForeignKey(Issue2, db_column='pcenter')
    bilno = models.ForeignKey(Issue2, db_column='bilno')
    labour_id = models.IntegerField()
    rate = models.FloatField(blank=True, null=True)
    houres = models.FloatField(blank=True, null=True)
    over_hours = models.FloatField(blank=True, null=True)
    we_hours = models.FloatField(blank=True, null=True)
    ov_hours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue_laboures'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'labour_id'),)


class IssueTaxes(models.Model):
    id = models.ForeignKey(Issue2, db_column='id')
    code = models.ForeignKey(Issue2, db_column='code')
    pcenter = models.ForeignKey(Issue2, db_column='pcenter')
    bilno = models.ForeignKey(Issue2, db_column='bilno')
    tax = models.ForeignKey('Taxes')
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'issue_taxes'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'tax_id'),)


class IssuedCredtnotes(models.Model):
    code = models.ForeignKey(Issue1, db_column='code')
    pcenter = models.ForeignKey(Issue1, db_column='pcenter')
    bilno = models.ForeignKey(Issue1, db_column='bilno')
    id = models.BigIntegerField()
    amount = models.FloatField()
    using_status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'issued_credtnotes'
        unique_together = (('code', 'pcenter', 'bilno', 'id'),)


class ItemCoding(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type_id = models.BigIntegerField()
    type_size = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'item_coding'


class ItemIncomeMapping(models.Model):
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    prodn = models.CharField(max_length=30)
    income_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_income_mapping'
        unique_together = (('pcenter', 'prodn', 'income_code'),)


class ItemProds(models.Model):
    prods = models.BigIntegerField()
    prodn = models.CharField(max_length=30)
    qty = models.FloatField(blank=True, null=True)
    qty1 = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    accno = models.CharField(max_length=14, blank=True, null=True)
    qty2 = models.FloatField(blank=True, null=True)
    first_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    first_avr = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    total_sold = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    last_sold_date = models.DateField(blank=True, null=True)
    deliv_qty_temp = models.BigIntegerField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp_balance = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    prods_unit = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    conv = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    stock_date_qty = models.BigIntegerField(blank=True, null=True)
    stock_date_qty1 = models.BigIntegerField(blank=True, null=True)
    stock_date_qty2 = models.BigIntegerField(blank=True, null=True)
    avr_on = models.NullBooleanField()
    first_qty_valid_payed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    first_qty_valid_notpayed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    first_qty_notvalid_payed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    first_qty_notvalid_notpayed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_valid_payed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_valid_notpayed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_notvalid_payed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_notvalid_notpayed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    stock_date_cost = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    unit_cd = models.IntegerField(blank=True, null=True)
    temp_qty = models.BigIntegerField(blank=True, null=True)
    first_temp_qty = models.BigIntegerField(blank=True, null=True)
    act_temp_qty = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_prods'
        unique_together = (('prods', 'prodn'),)


class ItemProdsDate(models.Model):
    prods = models.ForeignKey('Store', db_column='prods')
    prodn = models.CharField(max_length=30)
    vdate = models.DateField()
    qty = models.FloatField(blank=True, null=True)
    cost = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)
    prods_unit = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    conv = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_prods_date'
        unique_together = (('prods', 'prodn', 'vdate'),)


class ItemProdsLocations(models.Model):
    prods = models.BigIntegerField()
    prodn = models.CharField(max_length=30)
    location_id = models.BigIntegerField()
    qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_prods_locations'
        unique_together = (('prods', 'prodn', 'location_id'),)


class ItemProdsSerialGroups(models.Model):
    prods = models.FloatField()
    prodn = models.CharField(max_length=30)
    id = models.FloatField()
    start_group = models.FloatField()
    end_group = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    qty1 = models.FloatField(blank=True, null=True)
    start_from = models.FloatField(blank=True, null=True)
    end_to = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_prods_serial_groups'
        unique_together = (('prods', 'prodn', 'id', 'start_group'),)


class ItemProdsexpire(models.Model):
    prods = models.BigIntegerField()
    ite_prodn = models.CharField(max_length=30, blank=True, null=True)
    prodn = models.CharField(max_length=30)
    exp_date = models.DateField()
    qty = models.FloatField(blank=True, null=True)
    batchno = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_prodsexpire'
        unique_together = (('prods', 'prodn', 'exp_date'),)


class ItemProdsexpireIni(models.Model):
    prods = models.BigIntegerField()
    prodn = models.CharField(max_length=30)
    exp_date = models.DateField()
    qty = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    batchno = models.CharField(max_length=20, blank=True, null=True)
    conv = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_prodsexpire_ini'
        unique_together = (('prods', 'prodn', 'exp_date'),)


class ItemTaxes(models.Model):
    prodn = models.CharField(max_length=30)
    id = models.ForeignKey('Taxes', db_column='id')
    percent = models.DecimalField(max_digits=5, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'item_taxes'
        unique_together = (('prodn', 'id'),)


class ItemUnitMapping(models.Model):
    prodn = models.CharField(max_length=30)
    id = models.BigIntegerField()
    unit1 = models.BigIntegerField()
    unit2 = models.BigIntegerField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    par_code = models.CharField(max_length=50, blank=True, null=True)
    uprice = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_unit_mapping'
        unique_together = (('prodn', 'id'),)


class Itempriceoncurr(models.Model):
    prodn = models.CharField(max_length=30)
    currid = models.ForeignKey(Currancy, db_column='currid')
    sal_price = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price2 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price3 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price4 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price5 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price6 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itempriceoncurr'
        unique_together = (('prodn', 'currid'),)


class ItemsAddAssem(models.Model):
    prodn = models.ForeignKey('Itemstable', db_column='prodn')
    prodn1 = models.ForeignKey('Itemstable', db_column='prodn1')
    qty = models.FloatField(blank=True, null=True)
    unit = models.BigIntegerField()
    unit1 = models.DecimalField(max_digits=12, decimal_places=6)
    qty1 = models.FloatField()
    price = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    takeaway = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'items_add_assem'
        unique_together = (('prodn', 'prodn1'),)


class ItemsAddDesc(models.Model):
    prodn = models.CharField(primary_key=True, max_length=30)
    f1 = models.CharField(max_length=50, blank=True, null=True)
    f2 = models.CharField(max_length=50, blank=True, null=True)
    f3 = models.CharField(max_length=50, blank=True, null=True)
    f4 = models.CharField(max_length=50, blank=True, null=True)
    f5 = models.CharField(max_length=50, blank=True, null=True)
    f6 = models.CharField(max_length=50, blank=True, null=True)
    f7 = models.CharField(max_length=50, blank=True, null=True)
    f8 = models.CharField(max_length=50, blank=True, null=True)
    f9 = models.CharField(max_length=50, blank=True, null=True)
    f10 = models.CharField(max_length=50, blank=True, null=True)
    f11 = models.CharField(max_length=50, blank=True, null=True)
    f12 = models.CharField(max_length=50, blank=True, null=True)
    f13 = models.CharField(max_length=50, blank=True, null=True)
    f14 = models.CharField(max_length=50, blank=True, null=True)
    f15 = models.CharField(max_length=50, blank=True, null=True)
    f16 = models.CharField(max_length=50, blank=True, null=True)
    f17 = models.CharField(max_length=50, blank=True, null=True)
    f18 = models.CharField(max_length=50, blank=True, null=True)
    f19 = models.CharField(max_length=50, blank=True, null=True)
    f20 = models.CharField(max_length=50, blank=True, null=True)
    f21 = models.CharField(max_length=50, blank=True, null=True)
    f22 = models.CharField(max_length=50, blank=True, null=True)
    f23 = models.CharField(max_length=50, blank=True, null=True)
    f24 = models.CharField(max_length=50, blank=True, null=True)
    f25 = models.CharField(max_length=50, blank=True, null=True)
    f26 = models.CharField(max_length=50, blank=True, null=True)
    f27 = models.CharField(max_length=50, blank=True, null=True)
    f28 = models.CharField(max_length=50, blank=True, null=True)
    f29 = models.CharField(max_length=50, blank=True, null=True)
    f30 = models.CharField(max_length=50, blank=True, null=True)
    f31 = models.CharField(max_length=50, blank=True, null=True)
    f32 = models.CharField(max_length=50, blank=True, null=True)
    f33 = models.CharField(max_length=50, blank=True, null=True)
    f34 = models.CharField(max_length=50, blank=True, null=True)
    f35 = models.CharField(max_length=50, blank=True, null=True)
    f36 = models.CharField(max_length=50, blank=True, null=True)
    f37 = models.CharField(max_length=50, blank=True, null=True)
    f38 = models.CharField(max_length=50, blank=True, null=True)
    f39 = models.CharField(max_length=50, blank=True, null=True)
    f40 = models.CharField(max_length=50, blank=True, null=True)
    f41 = models.CharField(max_length=50, blank=True, null=True)
    f42 = models.CharField(max_length=50, blank=True, null=True)
    f43 = models.CharField(max_length=50, blank=True, null=True)
    f44 = models.CharField(max_length=50, blank=True, null=True)
    f45 = models.CharField(max_length=50, blank=True, null=True)
    f1_e = models.CharField(max_length=50, blank=True, null=True)
    f2_e = models.CharField(max_length=50, blank=True, null=True)
    f3_e = models.CharField(max_length=50, blank=True, null=True)
    f4_e = models.CharField(max_length=50, blank=True, null=True)
    f5_e = models.CharField(max_length=50, blank=True, null=True)
    f6_e = models.CharField(max_length=50, blank=True, null=True)
    f7_e = models.CharField(max_length=50, blank=True, null=True)
    f8_e = models.CharField(max_length=50, blank=True, null=True)
    f9_e = models.CharField(max_length=50, blank=True, null=True)
    f10_e = models.CharField(max_length=50, blank=True, null=True)
    f11_e = models.CharField(max_length=50, blank=True, null=True)
    f12_e = models.CharField(max_length=50, blank=True, null=True)
    f13_e = models.CharField(max_length=50, blank=True, null=True)
    f14_e = models.CharField(max_length=50, blank=True, null=True)
    f15_e = models.CharField(max_length=50, blank=True, null=True)
    f16_e = models.CharField(max_length=50, blank=True, null=True)
    f17_e = models.CharField(max_length=50, blank=True, null=True)
    f18_e = models.CharField(max_length=50, blank=True, null=True)
    f19_e = models.CharField(max_length=50, blank=True, null=True)
    f20_e = models.CharField(max_length=50, blank=True, null=True)
    f21_e = models.CharField(max_length=50, blank=True, null=True)
    f22_e = models.CharField(max_length=50, blank=True, null=True)
    f23_e = models.CharField(max_length=50, blank=True, null=True)
    f24_e = models.CharField(max_length=50, blank=True, null=True)
    f25_e = models.CharField(max_length=50, blank=True, null=True)
    f26_e = models.CharField(max_length=50, blank=True, null=True)
    f27_e = models.CharField(max_length=50, blank=True, null=True)
    f28_e = models.CharField(max_length=50, blank=True, null=True)
    f29_e = models.CharField(max_length=50, blank=True, null=True)
    f30_e = models.CharField(max_length=50, blank=True, null=True)
    f31_e = models.CharField(max_length=50, blank=True, null=True)
    f32_e = models.CharField(max_length=50, blank=True, null=True)
    f33_e = models.CharField(max_length=50, blank=True, null=True)
    f34_e = models.CharField(max_length=50, blank=True, null=True)
    f35_e = models.CharField(max_length=50, blank=True, null=True)
    f36_e = models.CharField(max_length=50, blank=True, null=True)
    f37_e = models.CharField(max_length=50, blank=True, null=True)
    f38_e = models.CharField(max_length=50, blank=True, null=True)
    f39_e = models.CharField(max_length=50, blank=True, null=True)
    f40_e = models.CharField(max_length=50, blank=True, null=True)
    f41_e = models.CharField(max_length=50, blank=True, null=True)
    f42_e = models.CharField(max_length=50, blank=True, null=True)
    f43_e = models.CharField(max_length=50, blank=True, null=True)
    f44_e = models.CharField(max_length=50, blank=True, null=True)
    f45_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_add_desc'


class ItemsAddDesc2(models.Model):
    prodn = models.CharField(primary_key=True, max_length=30)
    item_mode = models.CharField(max_length=50, blank=True, null=True)
    co = models.CharField(max_length=50, blank=True, null=True)
    br = models.CharField(max_length=50, blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    cat = models.CharField(max_length=50, blank=True, null=True)
    td = models.CharField(max_length=50, blank=True, null=True)
    fl = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    l = models.CharField(max_length=50, blank=True, null=True)
    l1 = models.CharField(max_length=50, blank=True, null=True)
    w = models.CharField(max_length=50, blank=True, null=True)
    w1 = models.CharField(max_length=50, blank=True, null=True)
    h = models.CharField(max_length=50, blank=True, null=True)
    h1 = models.CharField(max_length=50, blank=True, null=True)
    h2 = models.CharField(max_length=50, blank=True, null=True)
    fai = models.CharField(max_length=50, blank=True, null=True)
    frame = models.TextField(blank=True, null=True)
    seat = models.TextField(blank=True, null=True)
    head_rest = models.CharField(max_length=50, blank=True, null=True)
    side_cushion = models.CharField(max_length=50, blank=True, null=True)
    arms_back = models.TextField(blank=True, null=True)
    pouf_footboard = models.CharField(max_length=50, blank=True, null=True)
    cover = models.TextField(blank=True, null=True)
    base = models.CharField(max_length=50, blank=True, null=True)
    bed_base = models.CharField(max_length=50, blank=True, null=True)
    feet = models.TextField(blank=True, null=True)
    partition = models.CharField(max_length=50, blank=True, null=True)
    top1 = models.CharField(max_length=50, blank=True, null=True)
    sliding_shutter = models.TextField(blank=True, null=True)
    mattress_bedsofa = models.CharField(max_length=50, blank=True, null=True)
    coffetable = models.CharField(max_length=50, blank=True, null=True)
    fabric = models.CharField(max_length=50, blank=True, null=True)
    patchwork_version = models.CharField(max_length=50, blank=True, null=True)
    optional_1 = models.TextField(blank=True, null=True)
    optional_2 = models.TextField(blank=True, null=True)
    optional_3 = models.TextField(blank=True, null=True)
    optional_4 = models.TextField(blank=True, null=True)
    optional_5 = models.TextField(blank=True, null=True)
    optional_6 = models.TextField(blank=True, null=True)
    accessories = models.CharField(max_length=50, blank=True, null=True)
    backstage_1 = models.CharField(max_length=50, blank=True, null=True)
    backstage_2 = models.CharField(max_length=50, blank=True, null=True)
    curtain = models.CharField(max_length=50, blank=True, null=True)
    glass = models.TextField(blank=True, null=True)
    candle = models.CharField(max_length=50, blank=True, null=True)
    packing = models.CharField(max_length=50, blank=True, null=True)
    optional_saddle = models.CharField(max_length=50, blank=True, null=True)
    drawer = models.CharField(max_length=50, blank=True, null=True)
    console = models.CharField(max_length=50, blank=True, null=True)
    lamp_shade = models.CharField(max_length=50, blank=True, null=True)
    leather_cover = models.CharField(max_length=50, blank=True, null=True)
    headboard = models.CharField(max_length=50, blank=True, null=True)
    footboard = models.CharField(max_length=50, blank=True, null=True)
    structure_base = models.TextField(blank=True, null=True)
    slate = models.CharField(max_length=50, blank=True, null=True)
    kopfteil = models.CharField(max_length=50, blank=True, null=True)
    fur_leather = models.CharField(max_length=50, blank=True, null=True)
    b = models.CharField(max_length=50, blank=True, null=True)
    c = models.CharField(max_length=50, blank=True, null=True)
    d = models.CharField(max_length=50, blank=True, null=True)
    top2 = models.CharField(max_length=50, blank=True, null=True)
    aiace_top = models.CharField(max_length=50, blank=True, null=True)
    democrito_top = models.CharField(max_length=50, blank=True, null=True)
    vip = models.CharField(max_length=50, blank=True, null=True)
    vogue = models.CharField(max_length=50, blank=True, null=True)
    super_vogue = models.CharField(max_length=50, blank=True, null=True)
    lurex = models.CharField(max_length=50, blank=True, null=True)
    velvet = models.CharField(max_length=50, blank=True, null=True)
    satin = models.CharField(max_length=50, blank=True, null=True)
    extra = models.CharField(max_length=50, blank=True, null=True)
    country_extra = models.CharField(max_length=50, blank=True, null=True)
    lux = models.CharField(max_length=50, blank=True, null=True)
    almara_lux = models.CharField(max_length=50, blank=True, null=True)
    chess_lux = models.CharField(max_length=50, blank=True, null=True)
    chamoix_lux = models.CharField(max_length=50, blank=True, null=True)
    sauvage_lux = models.CharField(max_length=50, blank=True, null=True)
    crocodile_super_lux = models.CharField(max_length=50, blank=True, null=True)
    wenge = models.CharField(max_length=50, blank=True, null=True)
    lapin_rex = models.CharField(max_length=50, blank=True, null=True)
    nutria = models.CharField(max_length=50, blank=True, null=True)
    mohair_wool = models.CharField(max_length=50, blank=True, null=True)
    cashmere = models.CharField(max_length=50, blank=True, null=True)
    silk = models.CharField(max_length=50, blank=True, null=True)
    fox = models.CharField(max_length=50, blank=True, null=True)
    organdie = models.CharField(max_length=50, blank=True, null=True)
    fedra = models.CharField(max_length=50, blank=True, null=True)
    elettra = models.CharField(max_length=50, blank=True, null=True)
    cuoietto = models.CharField(max_length=50, blank=True, null=True)
    fashion = models.CharField(max_length=50, blank=True, null=True)
    lame = models.CharField(max_length=50, blank=True, null=True)
    platinum = models.CharField(max_length=50, blank=True, null=True)
    silver = models.CharField(max_length=50, blank=True, null=True)
    golden = models.CharField(max_length=50, blank=True, null=True)
    mother_of_pearl = models.CharField(max_length=50, blank=True, null=True)
    optional_11 = models.CharField(max_length=50, blank=True, null=True)
    optional_22 = models.CharField(max_length=50, blank=True, null=True)
    optional_33 = models.CharField(max_length=50, blank=True, null=True)
    optional_44 = models.CharField(max_length=50, blank=True, null=True)
    optional_55 = models.CharField(max_length=50, blank=True, null=True)
    optional_66 = models.CharField(max_length=50, blank=True, null=True)
    plexiglass = models.CharField(max_length=50, blank=True, null=True)
    backstage = models.CharField(max_length=50, blank=True, null=True)
    bed_without_slate = models.CharField(max_length=50, blank=True, null=True)
    material_used = models.TextField(blank=True, null=True)
    bridge = models.CharField(max_length=100, blank=True, null=True)
    price_inclusive_of = models.CharField(max_length=200, blank=True, null=True)
    cm = models.CharField(max_length=100, blank=True, null=True)
    l2 = models.CharField(max_length=50, blank=True, null=True)
    p = models.CharField(max_length=50, blank=True, null=True)
    p2 = models.CharField(max_length=50, blank=True, null=True)
    p3 = models.CharField(max_length=50, blank=True, null=True)
    a = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_add_desc2'


class ItemsAddNote(models.Model):
    mlang = models.BooleanField(primary_key=True)
    note_1 = models.CharField(max_length=50, blank=True, null=True)
    note_2 = models.CharField(max_length=50, blank=True, null=True)
    note_3 = models.CharField(max_length=50, blank=True, null=True)
    note_4 = models.CharField(max_length=50, blank=True, null=True)
    note_5 = models.CharField(max_length=50, blank=True, null=True)
    note_6 = models.CharField(max_length=50, blank=True, null=True)
    note_7 = models.CharField(max_length=50, blank=True, null=True)
    note_8 = models.CharField(max_length=50, blank=True, null=True)
    note_9 = models.CharField(max_length=50, blank=True, null=True)
    note_10 = models.CharField(max_length=50, blank=True, null=True)
    note_11 = models.CharField(max_length=50, blank=True, null=True)
    note_12 = models.CharField(max_length=50, blank=True, null=True)
    note_13 = models.CharField(max_length=50, blank=True, null=True)
    note_14 = models.CharField(max_length=50, blank=True, null=True)
    note_15 = models.CharField(max_length=50, blank=True, null=True)
    note_16 = models.CharField(max_length=50, blank=True, null=True)
    note_17 = models.CharField(max_length=50, blank=True, null=True)
    note_18 = models.CharField(max_length=50, blank=True, null=True)
    note_19 = models.CharField(max_length=50, blank=True, null=True)
    note_20 = models.CharField(max_length=50, blank=True, null=True)
    note_21 = models.CharField(max_length=50, blank=True, null=True)
    note_22 = models.CharField(max_length=50, blank=True, null=True)
    note_23 = models.CharField(max_length=50, blank=True, null=True)
    note_24 = models.CharField(max_length=50, blank=True, null=True)
    note_25 = models.CharField(max_length=50, blank=True, null=True)
    note_26 = models.CharField(max_length=50, blank=True, null=True)
    note_27 = models.CharField(max_length=50, blank=True, null=True)
    note_28 = models.CharField(max_length=50, blank=True, null=True)
    note_29 = models.CharField(max_length=50, blank=True, null=True)
    note_30 = models.CharField(max_length=50, blank=True, null=True)
    note_31 = models.CharField(max_length=50, blank=True, null=True)
    note_32 = models.CharField(max_length=50, blank=True, null=True)
    note_33 = models.CharField(max_length=50, blank=True, null=True)
    note_34 = models.CharField(max_length=50, blank=True, null=True)
    note_35 = models.CharField(max_length=50, blank=True, null=True)
    note_36 = models.CharField(max_length=50, blank=True, null=True)
    note_37 = models.CharField(max_length=50, blank=True, null=True)
    note_38 = models.CharField(max_length=50, blank=True, null=True)
    note_39 = models.CharField(max_length=50, blank=True, null=True)
    note_40 = models.CharField(max_length=50, blank=True, null=True)
    note_41 = models.CharField(max_length=50, blank=True, null=True)
    note_42 = models.CharField(max_length=50, blank=True, null=True)
    note_43 = models.CharField(max_length=50, blank=True, null=True)
    note_44 = models.CharField(max_length=50, blank=True, null=True)
    note_45 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_add_note'


class ItemsAllAssem(models.Model):
    prodn = models.CharField(max_length=30)
    prodn1 = models.CharField(max_length=30)
    qty = models.FloatField(blank=True, null=True)
    unit = models.BigIntegerField()
    unit1 = models.DecimalField(max_digits=12, decimal_places=6)
    qty1 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'items_all_assem'
        unique_together = (('prodn', 'prodn1'),)


class ItemsAssem(models.Model):
    prodn = models.ForeignKey('Itemstable', db_column='prodn')
    prodn1 = models.ForeignKey('Itemstable', db_column='prodn1')
    qty = models.FloatField(blank=True, null=True)
    unit = models.BigIntegerField()
    unit1 = models.DecimalField(max_digits=12, decimal_places=6)
    qty1 = models.FloatField()
    is_cat = models.BigIntegerField(blank=True, null=True)
    cat = models.BigIntegerField(blank=True, null=True)
    equation_id = models.IntegerField(blank=True, null=True)
    delivery = models.NullBooleanField()
    takeaway = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'items_assem'
        unique_together = (('prodn', 'prodn1'),)


class ItemsWithNoPointsCenters(models.Model):
    id = models.ForeignKey('ItemsWithNoPointsHeader', db_column='id')
    pcenter = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'items_with_no_points_centers'
        unique_together = (('id', 'pcenter'),)


class ItemsWithNoPointsDetail(models.Model):
    id = models.ForeignKey('ItemsWithNoPointsHeader', db_column='id')
    prodn = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'items_with_no_points_detail'
        unique_together = (('id', 'prodn'),)


class ItemsWithNoPointsHeader(models.Model):
    id = models.BigIntegerField(primary_key=True)
    comments_a = models.CharField(max_length=250, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_with_no_points_header'


class Itemsnotes(models.Model):
    notid = models.FloatField(primary_key=True)
    notes = models.CharField(max_length=800, blank=True, null=True)
    prodn = models.CharField(max_length=50, blank=True, null=True)
    value_v = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemsnotes'


class Itemstable(models.Model):
    prodn = models.CharField(primary_key=True, max_length=30)
    prodname = models.CharField(max_length=200, blank=True, null=True)
    prodname_e = models.CharField(max_length=200, blank=True, null=True)
    country = models.BigIntegerField(blank=True, null=True)
    cat1 = models.BigIntegerField(blank=True, null=True)
    cat2 = models.BigIntegerField(blank=True, null=True)
    cat3 = models.BigIntegerField(blank=True, null=True)
    cat4 = models.BigIntegerField(blank=True, null=True)
    unit = models.ForeignKey('MainUnit', db_column='unit', blank=True, null=True)
    vendor_item_no = models.CharField(max_length=40, blank=True, null=True)
    min_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    item_type = models.BigIntegerField(blank=True, null=True)
    sal_price = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price2 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price3 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price4 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    non_inventory_item = models.NullBooleanField()
    last_order_date = models.DateField(blank=True, null=True)
    last_order_price = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    reorder_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    max_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    unit1 = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    par_code = models.CharField(max_length=30, blank=True, null=True)
    item_color = models.CharField(max_length=15, blank=True, null=True)
    item_volume = models.CharField(max_length=15, blank=True, null=True)
    sal_price5 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    last_sal_date = models.DateField(blank=True, null=True)
    last_order_currancy = models.BigIntegerField(blank=True, null=True)
    last_cost = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    last_pur_date = models.DateField(blank=True, null=True)
    last_pur_price = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    last_pur_currancy = models.BigIntegerField(blank=True, null=True)
    item_waight = models.CharField(max_length=30, blank=True, null=True)
    item_size = models.CharField(max_length=15, blank=True, null=True)
    sal_price6 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    vendor = models.BigIntegerField(blank=True, null=True)
    grossweight = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    unit2 = models.BigIntegerField(blank=True, null=True)
    item_pic = models.CharField(max_length=255, blank=True, null=True)
    avr_on = models.NullBooleanField()
    isactive = models.CharField(max_length=1, blank=True, null=True)
    hasexpiarydate = models.CharField(max_length=1, blank=True, null=True)
    expirehandle = models.CharField(max_length=1, blank=True, null=True)
    dispensepolicy = models.CharField(max_length=1, blank=True, null=True)
    rep_item = models.CharField(max_length=30, blank=True, null=True)
    sal_unit = models.ForeignKey('MainUnit', db_column='sal_unit', blank=True, null=True)
    pur_unit = models.ForeignKey('MainUnit', db_column='pur_unit', blank=True, null=True)
    size_code = models.CharField(max_length=30, blank=True, null=True)
    size_group = models.CharField(max_length=30, blank=True, null=True)
    color_code = models.CharField(max_length=30, blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    fabric_no = models.CharField(max_length=30, blank=True, null=True)
    trend = models.CharField(max_length=50, blank=True, null=True)
    article = models.CharField(max_length=50, blank=True, null=True)
    season = models.CharField(max_length=10, blank=True, null=True)
    orginok = models.NullBooleanField()
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    no_in_ballet = models.BigIntegerField(blank=True, null=True)
    prodn_org = models.CharField(max_length=30, blank=True, null=True)
    prodn_alt = models.CharField(max_length=30, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    is_lwh = models.BigIntegerField(blank=True, null=True)
    stop_item = models.NullBooleanField()
    stop_centers = models.CharField(max_length=255, blank=True, null=True)
    item_thickness = models.CharField(max_length=15, blank=True, null=True)
    item_diameter = models.CharField(max_length=15, blank=True, null=True)
    clr_code = models.ForeignKey(Color, db_column='clr_code', blank=True, null=True)
    sz_code = models.IntegerField(blank=True, null=True)
    itmmaincat = models.CharField(max_length=30, blank=True, null=True)
    stop_item_expend = models.NullBooleanField()
    stop_centers_expend = models.CharField(max_length=255, blank=True, null=True)
    di1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    profit_ratio = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pur_price1 = models.DecimalField(max_digits=22, decimal_places=7, blank=True, null=True)
    pur_price2 = models.DecimalField(max_digits=22, decimal_places=7, blank=True, null=True)
    pur_price3 = models.DecimalField(max_digits=22, decimal_places=7, blank=True, null=True)
    idserial_must = models.NullBooleanField()
    prepare_time = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    item_backcolor = models.BigIntegerField(blank=True, null=True)
    max_add_items = models.IntegerField(blank=True, null=True)
    max_add_items_2 = models.IntegerField(blank=True, null=True)
    serv_typ = models.NullBooleanField()
    have_cablesize = models.NullBooleanField()
    size_cat = models.BigIntegerField(blank=True, null=True)
    defalt_price = models.NullBooleanField()
    manf_year = models.IntegerField(blank=True, null=True)
    color_cat = models.BigIntegerField(blank=True, null=True)
    stop_item_transfer = models.BigIntegerField(blank=True, null=True)
    stop_centers_transfer = models.CharField(max_length=200, blank=True, null=True)
    item_serial_digits = models.BigIntegerField(blank=True, null=True)
    item_class_from = models.IntegerField(blank=True, null=True)
    item_class_to = models.IntegerField(blank=True, null=True)
    stagnant_product = models.IntegerField(blank=True, null=True)
    update_name = models.NullBooleanField()
    no_serial = models.NullBooleanField()
    equation_id = models.IntegerField(blank=True, null=True)
    add_user = models.CharField(max_length=50, blank=True, null=True)
    add_dt = models.DateField(blank=True, null=True)
    upd_user = models.CharField(max_length=50, blank=True, null=True)
    upd_dt = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    item_img = models.BinaryField(blank=True, null=True)
    br_id = models.IntegerField(blank=True, null=True)
    barcode2 = models.CharField(max_length=30, blank=True, null=True)
    barcode3 = models.CharField(max_length=30, blank=True, null=True)
    barcode4 = models.CharField(max_length=20, blank=True, null=True)
    barcode5 = models.CharField(max_length=20, blank=True, null=True)
    lookup_no = models.CharField(max_length=50, blank=True, null=True)
    cl_1_id = models.IntegerField(blank=True, null=True)
    cl_2_id = models.IntegerField(blank=True, null=True)
    cl_3_id = models.IntegerField(blank=True, null=True)
    cl_4_id = models.IntegerField(blank=True, null=True)
    cl_5_id = models.IntegerField(blank=True, null=True)
    cl_6_id = models.IntegerField(blank=True, null=True)
    cl_7_id = models.IntegerField(blank=True, null=True)
    cl_8_id = models.IntegerField(blank=True, null=True)
    cl_9_id = models.IntegerField(blank=True, null=True)
    cl_10_id = models.IntegerField(blank=True, null=True)
    description = models.IntegerField(blank=True, null=True)
    cut_type = models.IntegerField(blank=True, null=True)
    ages = models.IntegerField(blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    sup_desc = models.CharField(max_length=150, blank=True, null=True)
    have_target = models.NullBooleanField()
    class_code = models.FloatField(blank=True, null=True)
    spec_code = models.NullBooleanField()
    exp_period = models.BigIntegerField(blank=True, null=True)
    shelf_life = models.BigIntegerField(blank=True, null=True)
    old_prodn = models.CharField(max_length=200, blank=True, null=True)
    isusedinrestauarnt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemstable'


class Itm(models.Model):
    prodn = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itm'


class ItmMaincategory(models.Model):
    prodn = models.CharField(primary_key=True, max_length=30)
    prodname = models.CharField(max_length=60, blank=True, null=True)
    prodname_e = models.CharField(max_length=60, blank=True, null=True)
    country = models.BigIntegerField(blank=True, null=True)
    cat1 = models.BigIntegerField(blank=True, null=True)
    cat2 = models.BigIntegerField(blank=True, null=True)
    cat3 = models.BigIntegerField(blank=True, null=True)
    cat4 = models.BigIntegerField(blank=True, null=True)
    unit = models.ForeignKey('MainUnit', db_column='unit', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    vendor_item_no = models.CharField(max_length=40, blank=True, null=True)
    min_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    item_type = models.BigIntegerField(blank=True, null=True)
    sal_price = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price2 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price3 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    sal_price4 = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    non_inventory_item = models.NullBooleanField()
    last_order_date = models.DateField(blank=True, null=True)
    last_order_price = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    reorder_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    max_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    unit1 = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    par_code = models.CharField(max_length=30, blank=True, null=True)
    item_color = models.CharField(max_length=15, blank=True, null=True)
    item_volume = models.CharField(max_length=15, blank=True, null=True)
    sal_price5 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    last_sal_date = models.DateField(blank=True, null=True)
    last_order_currancy = models.BigIntegerField(blank=True, null=True)
    last_cost = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    last_pur_date = models.DateField(blank=True, null=True)
    last_pur_price = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    last_pur_currancy = models.BigIntegerField(blank=True, null=True)
    item_waight = models.CharField(max_length=30, blank=True, null=True)
    item_size = models.CharField(max_length=15, blank=True, null=True)
    sal_price6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    vendor = models.BigIntegerField(blank=True, null=True)
    grossweight = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    unit2 = models.BigIntegerField(blank=True, null=True)
    item_pic = models.CharField(max_length=255, blank=True, null=True)
    avr_on = models.NullBooleanField()
    isactive = models.CharField(max_length=1, blank=True, null=True)
    hasexpiarydate = models.CharField(max_length=1, blank=True, null=True)
    expirehandle = models.CharField(max_length=1, blank=True, null=True)
    dispensepolicy = models.CharField(max_length=1, blank=True, null=True)
    rep_item = models.CharField(max_length=30, blank=True, null=True)
    sal_unit = models.ForeignKey('MainUnit', db_column='sal_unit', blank=True, null=True)
    pur_unit = models.ForeignKey('MainUnit', db_column='pur_unit', blank=True, null=True)
    size_code = models.CharField(max_length=30, blank=True, null=True)
    size_group = models.CharField(max_length=30, blank=True, null=True)
    color_code = models.CharField(max_length=30, blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    fabric_no = models.CharField(max_length=30, blank=True, null=True)
    trend = models.CharField(max_length=50, blank=True, null=True)
    article = models.CharField(max_length=50, blank=True, null=True)
    season = models.CharField(max_length=10, blank=True, null=True)
    orginok = models.NullBooleanField()
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    no_in_ballet = models.BigIntegerField(blank=True, null=True)
    prodn_org = models.CharField(max_length=30, blank=True, null=True)
    prodn_alt = models.CharField(max_length=30, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    is_lwh = models.BigIntegerField(blank=True, null=True)
    stop_item = models.NullBooleanField()
    stop_centers = models.CharField(max_length=255, blank=True, null=True)
    item_thickness = models.CharField(max_length=15, blank=True, null=True)
    item_diameter = models.CharField(max_length=15, blank=True, null=True)
    di1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    serv_typ = models.NullBooleanField()
    have_cablesize = models.NullBooleanField()
    itmmaincat = models.CharField(max_length=30, blank=True, null=True)
    idserial_must = models.NullBooleanField()
    catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    max_add_items = models.IntegerField(blank=True, null=True)
    max_add_items_2 = models.IntegerField(blank=True, null=True)
    prepare_time = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    item_backcolor = models.BigIntegerField(blank=True, null=True)
    stop_item_expend = models.NullBooleanField()
    stop_centers_expend = models.CharField(max_length=255, blank=True, null=True)
    profit_ratio = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    pur_price1 = models.DecimalField(max_digits=22, decimal_places=7, blank=True, null=True)
    pur_price2 = models.DecimalField(max_digits=22, decimal_places=7, blank=True, null=True)
    pur_price3 = models.DecimalField(max_digits=22, decimal_places=7, blank=True, null=True)
    size_cat = models.BigIntegerField(blank=True, null=True)
    defalt_price = models.NullBooleanField()
    manf_year = models.IntegerField(blank=True, null=True)
    color_cat = models.BigIntegerField(blank=True, null=True)
    stop_item_transfer = models.BigIntegerField(blank=True, null=True)
    stop_centers_transfer = models.CharField(max_length=200, blank=True, null=True)
    item_serial_digits = models.BigIntegerField(blank=True, null=True)
    item_class_from = models.IntegerField(blank=True, null=True)
    item_class_to = models.IntegerField(blank=True, null=True)
    stagnant_product = models.IntegerField(blank=True, null=True)
    update_name = models.NullBooleanField()
    no_serial = models.NullBooleanField()
    equation_id = models.IntegerField(blank=True, null=True)
    add_user = models.CharField(max_length=50, blank=True, null=True)
    add_dt = models.DateField(blank=True, null=True)
    upd_user = models.CharField(max_length=50, blank=True, null=True)
    upd_dt = models.DateField(blank=True, null=True)
    br_id = models.IntegerField(blank=True, null=True)
    item_img = models.BinaryField(blank=True, null=True)
    cl_2_id = models.IntegerField(blank=True, null=True)
    cl_1_id = models.IntegerField(blank=True, null=True)
    cl_3_id = models.IntegerField(blank=True, null=True)
    cl_4_id = models.IntegerField(blank=True, null=True)
    cl_5_id = models.IntegerField(blank=True, null=True)
    cl_6_id = models.IntegerField(blank=True, null=True)
    cl_7_id = models.IntegerField(blank=True, null=True)
    cl_8_id = models.IntegerField(blank=True, null=True)
    cl_9_id = models.IntegerField(blank=True, null=True)
    cl_10_id = models.IntegerField(blank=True, null=True)
    description = models.IntegerField(blank=True, null=True)
    cut_type = models.IntegerField(blank=True, null=True)
    ages = models.IntegerField(blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    sup_desc = models.CharField(max_length=150, blank=True, null=True)
    spec_code = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'itm_maincategory'


class ItmMaincategoryAddDesc(models.Model):
    prodn = models.CharField(primary_key=True, max_length=30)
    f1 = models.CharField(max_length=50, blank=True, null=True)
    f2 = models.CharField(max_length=50, blank=True, null=True)
    f3 = models.CharField(max_length=50, blank=True, null=True)
    f4 = models.CharField(max_length=50, blank=True, null=True)
    f5 = models.CharField(max_length=50, blank=True, null=True)
    f6 = models.CharField(max_length=50, blank=True, null=True)
    f7 = models.CharField(max_length=50, blank=True, null=True)
    f8 = models.CharField(max_length=50, blank=True, null=True)
    f9 = models.CharField(max_length=50, blank=True, null=True)
    f10 = models.CharField(max_length=50, blank=True, null=True)
    f11 = models.CharField(max_length=50, blank=True, null=True)
    f12 = models.CharField(max_length=50, blank=True, null=True)
    f13 = models.CharField(max_length=50, blank=True, null=True)
    f14 = models.CharField(max_length=50, blank=True, null=True)
    f15 = models.CharField(max_length=50, blank=True, null=True)
    f16 = models.CharField(max_length=50, blank=True, null=True)
    f17 = models.CharField(max_length=50, blank=True, null=True)
    f18 = models.CharField(max_length=50, blank=True, null=True)
    f19 = models.CharField(max_length=50, blank=True, null=True)
    f20 = models.CharField(max_length=50, blank=True, null=True)
    f21 = models.CharField(max_length=50, blank=True, null=True)
    f22 = models.CharField(max_length=50, blank=True, null=True)
    f23 = models.CharField(max_length=50, blank=True, null=True)
    f24 = models.CharField(max_length=50, blank=True, null=True)
    f25 = models.CharField(max_length=50, blank=True, null=True)
    f26 = models.CharField(max_length=50, blank=True, null=True)
    f27 = models.CharField(max_length=50, blank=True, null=True)
    f28 = models.CharField(max_length=50, blank=True, null=True)
    f29 = models.CharField(max_length=50, blank=True, null=True)
    f30 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itm_maincategory_add_desc'


class Kamal(models.Model):
    id = models.FloatField(primary_key=True)
    t1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t8 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t9 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t10 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t11 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t12 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t13 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t14 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t15 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t16 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t17 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t18 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t19 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t20 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t21 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t22 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t23 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t24 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    t25 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v1 = models.CharField(max_length=10, blank=True, null=True)
    v2 = models.DateField(blank=True, null=True)
    v3 = models.CharField(max_length=20, blank=True, null=True)
    v4 = models.CharField(max_length=20, blank=True, null=True)
    v5 = models.CharField(max_length=20, blank=True, null=True)
    v6 = models.CharField(max_length=20, blank=True, null=True)
    v7 = models.CharField(max_length=20, blank=True, null=True)
    v8 = models.CharField(max_length=20, blank=True, null=True)
    v9 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kamal'


class KitComp(models.Model):
    pcenter = models.BigIntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)
    kit_no = models.BigIntegerField(blank=True, null=True)
    originparentid = models.BigIntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    disc2 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kit_comp'


class LabelSetup(models.Model):
    id = models.FloatField(primary_key=True)
    l_width = models.BigIntegerField(blank=True, null=True)
    l_height = models.BigIntegerField(blank=True, null=True)
    l_across = models.FloatField(blank=True, null=True)
    l_down = models.FloatField(blank=True, null=True)
    l_marg_column = models.BigIntegerField(blank=True, null=True)
    l_marg_row = models.BigIntegerField(blank=True, null=True)
    l_mar_top = models.BigIntegerField(blank=True, null=True)
    l_mar_bottom = models.BigIntegerField(blank=True, null=True)
    l_mar_left = models.BigIntegerField(blank=True, null=True)
    l_mar_right = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    price_v = models.FloatField(blank=True, null=True)
    prodname_v = models.BigIntegerField(blank=True, null=True)
    prodname_e_v = models.BigIntegerField(blank=True, null=True)
    prodn_v = models.BigIntegerField(blank=True, null=True)
    prodname_y = models.BigIntegerField(blank=True, null=True)
    prodname_e_y = models.BigIntegerField(blank=True, null=True)
    prodn_y = models.BigIntegerField(blank=True, null=True)
    price_y = models.BigIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    r_1_v = models.BigIntegerField(blank=True, null=True)
    l_orientation = models.BigIntegerField(blank=True, null=True)
    l_zoom = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_setup'


class LastSerial(models.Model):
    shipment_no = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'last_serial'


class Lc(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    supno = models.ForeignKey('Suppliers', db_column='supno', blank=True, null=True)
    descreption1 = models.CharField(max_length=150, blank=True, null=True)
    desc2 = models.IntegerField(blank=True, null=True)
    desc3 = models.CharField(max_length=100, blank=True, null=True)
    desc4 = models.CharField(max_length=150, blank=True, null=True)
    amount1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    currancy = models.IntegerField(blank=True, null=True)
    bank = models.BigIntegerField(blank=True, null=True)
    taamen_co = models.CharField(max_length=100, blank=True, null=True)
    datofcredit = models.DateField(blank=True, null=True)
    bolesa = models.CharField(max_length=30, blank=True, null=True)
    policydate = models.DateField(blank=True, null=True)
    tagded1 = models.DateField(blank=True, null=True)
    tagded2 = models.DateField(blank=True, null=True)
    tagded3 = models.DateField(blank=True, null=True)
    ex_rate = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    v1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v5 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v6 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v7 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v8 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v9 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v10 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v11 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    v12 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    vc9 = models.CharField(max_length=100, blank=True, null=True)
    vc10 = models.CharField(max_length=100, blank=True, null=True)
    vc11 = models.CharField(max_length=100, blank=True, null=True)
    vc12 = models.CharField(max_length=100, blank=True, null=True)
    lc_notes = models.CharField(max_length=500, blank=True, null=True)
    conditions = models.CharField(max_length=30, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    v13 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    per = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    invoice_no = models.BigIntegerField(blank=True, null=True)
    lc_status = models.IntegerField(blank=True, null=True)
    itmarrvdate = models.DateField(blank=True, null=True)
    accno = models.BigIntegerField(blank=True, null=True)
    cash_exp = models.FloatField(blank=True, null=True)
    check_exp = models.FloatField(blank=True, null=True)
    lc_addtion_number = models.CharField(max_length=255, blank=True, null=True)
    used_amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)
    bank_old = models.CharField(max_length=40, blank=True, null=True)
    account_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lc'


class Lengthh(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    name_e = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lengthh'


class Location(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name_1 = models.CharField(max_length=50)
    name_2 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'location'


class LocationDetails(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name_1 = models.CharField(max_length=50, blank=True, null=True)
    name_2 = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'location_details'


class LwhEquations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    eq_name = models.CharField(max_length=100, blank=True, null=True)
    eq_name_e = models.CharField(max_length=100, blank=True, null=True)
    col_equation = models.TextField()

    class Meta:
        managed = False
        db_table = 'lwh_equations'


class M(models.Model):
    month_no = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'm'


class MPatient(models.Model):
    branch = models.ForeignKey(Centers, db_column='branch')
    code = models.BigIntegerField()
    pname = models.CharField(max_length=100)
    ptel = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_patient'
        unique_together = (('branch', 'code'),)


class MPatientvisit(models.Model):
    branch = models.BigIntegerField()
    visit_dt = models.DateField()
    visit_id = models.BigIntegerField()
    patient = models.BigIntegerField()
    le_dispd = models.CharField(max_length=20, blank=True, null=True)
    le_dissph = models.CharField(max_length=20, blank=True, null=True)
    le_discly = models.CharField(max_length=20, blank=True, null=True)
    le_disaxs = models.CharField(max_length=20, blank=True, null=True)
    le_redpd = models.CharField(max_length=20, blank=True, null=True)
    le_redsph = models.CharField(max_length=20, blank=True, null=True)
    le_redcly = models.CharField(max_length=20, blank=True, null=True)
    le_redaxs = models.CharField(max_length=20, blank=True, null=True)
    re_dissph = models.CharField(max_length=20, blank=True, null=True)
    re_discly = models.CharField(max_length=20, blank=True, null=True)
    re_disaxs = models.CharField(max_length=20, blank=True, null=True)
    re_redsph = models.CharField(max_length=20, blank=True, null=True)
    re_redcly = models.CharField(max_length=20, blank=True, null=True)
    re_redaxs = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter', blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_patientvisit'
        unique_together = (('branch', 'visit_dt', 'visit_id'),)


class MTaamenat(models.Model):
    emp_code = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    amount = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    file_no = models.CharField(max_length=30, blank=True, null=True)
    falge = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'm_taamenat'


class MUser(models.Model):
    user_name = models.CharField(primary_key=True, max_length=16)
    password = models.CharField(max_length=16, blank=True, null=True)
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    default_language = models.IntegerField(blank=True, null=True)
    blocked = models.CharField(max_length=1, blank=True, null=True)
    user_no = models.IntegerField(blank=True, null=True)
    us_x8 = models.IntegerField(blank=True, null=True)
    ovprtdel = models.IntegerField(blank=True, null=True)
    update_after_post = models.IntegerField(blank=True, null=True)
    apply_acc_for_vouchers = models.IntegerField(blank=True, null=True)
    dispay_pendingvoucher = models.NullBooleanField()
    omit_acc = models.NullBooleanField()
    update_voucher_date = models.NullBooleanField()
    update_voucher_no = models.NullBooleanField()
    show_entry_users = models.NullBooleanField()
    statement_email = models.NullBooleanField()
    supp_pur_freeze = models.NullBooleanField()
    min_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    max_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    cc_status = models.FloatField(blank=True, null=True)
    acc_priv_status = models.NullBooleanField()
    change_accno = models.FloatField(blank=True, null=True)
    trail_balance_spec = models.NullBooleanField()
    enable_close_voucher = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_user'


class MUserBranches(models.Model):
    user_id = models.FloatField()
    branch_id = models.FloatField()
    autorized = models.FloatField()

    class Meta:
        managed = False
        db_table = 'm_user_branches'
        unique_together = (('user_id', 'branch_id'),)


class MVUserBranches(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    branch_id = models.FloatField()
    autorized = models.FloatField()

    class Meta:
        managed = False
        db_table = 'm_v_user_branches'


class MachineKind(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_kind'


class MachineModel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30, blank=True, null=True)
    machine_type = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_model'


class MachineTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_types'


class Machines(models.Model):
    id = models.BigIntegerField(primary_key=True)
    unit_model = models.BigIntegerField(blank=True, null=True)
    unit_type = models.BigIntegerField(blank=True, null=True)
    serial = models.CharField(max_length=30, blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)
    unit_kind = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines'


class MagentoErr(models.Model):
    prodn = models.CharField(max_length=40, blank=True, null=True)
    error_txt = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magento_err'


class MagentoOrdstatusHist(models.Model):
    order_no = models.CharField(max_length=30)
    status_date = models.DateField()
    status = models.CharField(max_length=30)
    status_comment = models.CharField(max_length=255, blank=True, null=True)
    is_sent = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magento_ordstatus_hist'
        unique_together = (('order_no', 'status_date'),)


class MagentoQtyUpdate(models.Model):
    prodn = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'magento_qty_update'


class MagentoSessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'magento_sessions'


class MainUnit(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    main = models.BigIntegerField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    flage = models.NullBooleanField()
    name_e = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_unit'


class Manufacturer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    name_e = models.CharField(max_length=50)
    sort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class MessageText(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    message_text = models.TextField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_text'


class MessageUserRes(models.Model):
    id = models.ForeignKey(MessageText, db_column='id')
    user_no = models.CharField(max_length=16)
    flage = models.NullBooleanField()
    time_stamp = models.DateField(blank=True, null=True)
    temp = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'message_user_res'
        unique_together = (('id', 'user_no'),)


class Mezan(models.Model):
    accno = models.BigIntegerField(primary_key=True)
    first1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    move1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    move2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    end1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    first2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    end2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mezan'


class ModeTransport(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mode_transport'


class ModificationLog(models.Model):
    code = models.IntegerField()
    bilno = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    user_no = models.CharField(max_length=16)
    change_date = models.CharField(max_length=20)
    history_id = models.DecimalField(max_digits=35, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modification_log'
        unique_together = (('code', 'bilno', 'pcenter', 'user_no', 'change_date'),)


class Months(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'months'


class Move(models.Model):
    id = models.BigIntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    cost1 = models.BigIntegerField(blank=True, null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=3)
    credit = models.DecimalField(max_digits=20, decimal_places=3)
    details = models.CharField(max_length=500, blank=True, null=True)
    reset = models.ForeignKey('Move1', db_column='reset')
    reset_0 = models.ForeignKey('Move1', db_column='reset_id')  # Field renamed because of name conflict.
    cost2 = models.BigIntegerField(blank=True, null=True)
    cost3 = models.BigIntegerField(blank=True, null=True)
    cost4 = models.BigIntegerField(blank=True, null=True)
    chek = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.ForeignKey('Move1', db_column='branch')
    flage = models.NullBooleanField()
    payed = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit1 = models.DecimalField(max_digits=20, decimal_places=4)
    debit1 = models.DecimalField(max_digits=20, decimal_places=4)
    currency = models.ForeignKey(Currancy, db_column='currency', blank=True, null=True)
    curr_rate = models.DecimalField(max_digits=20, decimal_places=5)
    invno_e = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    sman_e = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    flage_checked = models.NullBooleanField()
    invoice_checked = models.NullBooleanField()
    bank_flag = models.IntegerField(blank=True, null=True)
    check_book = models.CharField(max_length=35, blank=True, null=True)
    payed_reset = models.IntegerField(blank=True, null=True)
    payed_reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    payed_branch = models.IntegerField(blank=True, null=True)
    ser = models.IntegerField(blank=True, null=True)
    return_no = models.CharField(max_length=30, blank=True, null=True)
    deposit_type = models.ForeignKey(AccMasterDepositType, blank=True, null=True)
    deposit_bank = models.CharField(max_length=100, blank=True, null=True)
    deposit_cheque = models.CharField(max_length=100, blank=True, null=True)
    deposit_date = models.DateField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    company_code = models.FloatField(blank=True, null=True)
    accname = models.CharField(max_length=250, blank=True, null=True)
    accname_e = models.CharField(max_length=250, blank=True, null=True)
    original_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move'
        unique_together = (('id', 'reset', 'reset_id', 'branch'),)


class Move1(models.Model):
    batch = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    reset = models.IntegerField()
    sr = models.NullBooleanField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    name_to = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=500, blank=True, null=True)
    chek = models.BigIntegerField(blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.ForeignKey(Branches, db_column='branch')
    user_no = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    chek_flage = models.NullBooleanField()
    bank = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    details_1 = models.CharField(max_length=500, blank=True, null=True)
    currency_type = models.IntegerField(blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    post_flage = models.NullBooleanField()
    print_usr = models.IntegerField(blank=True, null=True)
    print_dtm = models.DateField(blank=True, null=True)
    print_no = models.IntegerField(blank=True, null=True)
    check_book = models.ForeignKey(Checks, db_column='check_book', blank=True, null=True)
    paid = models.NullBooleanField()
    site_requisition = models.CharField(max_length=20, blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    approved = models.NullBooleanField()
    typ = models.NullBooleanField()
    inter_company = models.NullBooleanField()
    post_date = models.DateField(blank=True, null=True)
    post_user = models.CharField(max_length=16, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_user = models.CharField(max_length=16, blank=True, null=True)
    posted = models.NullBooleanField()
    is_close_voucher = models.FloatField(blank=True, null=True)
    is_close_voucher_before = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move1'
        unique_together = (('reset', 'reset_id', 'branch'),)


class Move1Comp(models.Model):
    batch = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    reset = models.IntegerField()
    sr = models.NullBooleanField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    name_to = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=500, blank=True, null=True)
    chek = models.BigIntegerField(blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.IntegerField()
    user_no = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    chek_flage = models.NullBooleanField()
    bank = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    details_1 = models.CharField(max_length=500, blank=True, null=True)
    currency_type = models.IntegerField(blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    post_flage = models.NullBooleanField()
    print_usr = models.IntegerField(blank=True, null=True)
    print_dtm = models.DateField(blank=True, null=True)
    print_no = models.IntegerField(blank=True, null=True)
    check_book = models.ForeignKey(Checks, db_column='check_book', blank=True, null=True)
    paid = models.NullBooleanField()
    site_requisition = models.CharField(max_length=20, blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    approved = models.NullBooleanField()
    typ = models.NullBooleanField()
    inter_company = models.NullBooleanField()
    post_date = models.DateField(blank=True, null=True)
    post_user = models.CharField(max_length=16, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_user = models.CharField(max_length=16, blank=True, null=True)
    posted = models.NullBooleanField()
    is_close_voucher = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move1_comp'
        unique_together = (('reset', 'reset_id', 'branch'),)


class Move1Trans(models.Model):
    batch = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    reset = models.IntegerField()
    sr = models.NullBooleanField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    name_to = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    chek = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.IntegerField()
    user_no = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    chek_flage = models.NullBooleanField()
    bank = models.CharField(max_length=35, blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move1_trans'
        unique_together = (('reset', 'reset_id', 'branch'),)


class MoveAdd(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    move_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    center = models.ForeignKey('MoveAddCenters', db_column='center', blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_add'


class MoveAddCenters(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    nam = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_add_centers'


class MoveAuto(models.Model):
    id = models.DecimalField(max_digits=20, decimal_places=5)
    accno = models.BigIntegerField(blank=True, null=True)
    cost1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    reset = models.IntegerField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    cost2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    branch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'move_auto'
        unique_together = (('id', 'reset', 'reset_id', 'branch'),)


class MoveComp(models.Model):
    id = models.BigIntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    cost1 = models.BigIntegerField(blank=True, null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=3)
    credit = models.DecimalField(max_digits=20, decimal_places=3)
    details = models.CharField(max_length=500, blank=True, null=True)
    reset = models.ForeignKey(Move1Comp, db_column='reset')
    reset_0 = models.ForeignKey(Move1Comp, db_column='reset_id')  # Field renamed because of name conflict.
    cost2 = models.BigIntegerField(blank=True, null=True)
    cost3 = models.BigIntegerField(blank=True, null=True)
    cost4 = models.BigIntegerField(blank=True, null=True)
    chek = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.ForeignKey(Move1Comp, db_column='branch')
    flage = models.NullBooleanField()
    payed = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    credit1 = models.DecimalField(max_digits=20, decimal_places=4)
    debit1 = models.DecimalField(max_digits=20, decimal_places=4)
    currency = models.ForeignKey(Currancy, db_column='currency', blank=True, null=True)
    curr_rate = models.DecimalField(max_digits=20, decimal_places=5)
    invno_e = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    sman_e = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    flage_checked = models.NullBooleanField()
    invoice_checked = models.NullBooleanField()
    bank_flag = models.IntegerField(blank=True, null=True)
    check_book = models.CharField(max_length=35, blank=True, null=True)
    payed_reset = models.IntegerField(blank=True, null=True)
    payed_reset_id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    payed_branch = models.IntegerField(blank=True, null=True)
    ser = models.IntegerField(blank=True, null=True)
    return_no = models.CharField(max_length=30, blank=True, null=True)
    deposit_type = models.ForeignKey(AccMasterDepositType, blank=True, null=True)
    deposit_bank = models.CharField(max_length=100, blank=True, null=True)
    deposit_cheque = models.CharField(max_length=100, blank=True, null=True)
    deposit_date = models.DateField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    company_code = models.IntegerField(blank=True, null=True)
    accname = models.CharField(max_length=250, blank=True, null=True)
    accname_e = models.CharField(max_length=250, blank=True, null=True)
    original_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_comp'
        unique_together = (('id', 'reset', 'reset_id', 'branch'),)


class MoveCostcenterDistribution(models.Model):
    move_reset = models.BigIntegerField()
    move_reset_id = models.BigIntegerField()
    move_branch = models.BigIntegerField()
    move_id = models.BigIntegerField()
    costcenter_type = models.NullBooleanField()
    costcenter_no = models.BigIntegerField()
    percentage = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_costcenter_distribution'
        unique_together = (('move_reset', 'move_reset_id', 'move_branch', 'move_id', 'costcenter_no'),)


class MoveTrans(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    accno = models.BigIntegerField(blank=True, null=True)
    cost1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    credit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    reset = models.IntegerField()
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    cost2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    chek = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_trans'


class Ms(models.Model):
    field1 = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'ms'


class NonInvItemscode(models.Model):
    non_inv_id = models.BigIntegerField(primary_key=True)
    items_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_inv_itemscode'


class Numbers(models.Model):
    no = models.BigIntegerField()
    location = models.BigIntegerField()
    name = models.CharField(max_length=20)
    nu = models.BigIntegerField(blank=True, null=True)
    name1 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numbers'
        unique_together = (('no', 'location', 'name'),)


class OlAppointment(models.Model):
    task_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)
    task_desc = models.TextField(blank=True, null=True)
    user_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ol_appointment'


class OlCats(models.Model):
    cat_name = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'ol_cats'


class OlDestinations(models.Model):
    dest_id = models.IntegerField(primary_key=True)
    dest_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    work_tel = models.CharField(max_length=20, blank=True, null=True)
    home_tel = models.CharField(max_length=20, blank=True, null=True)
    work_fax = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    work_address = models.CharField(max_length=255, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    email_1 = models.CharField(max_length=100, blank=True, null=True)
    email_2 = models.CharField(max_length=100, blank=True, null=True)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ol_destinations'


class OlMessages(models.Model):
    msg_id = models.IntegerField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    task_desc = models.TextField(blank=True, null=True)
    user_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ol_messages'


class OlTask(models.Model):
    task_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    periority = models.CharField(max_length=1, blank=True, null=True)
    complete_per = models.IntegerField(blank=True, null=True)
    remind = models.CharField(max_length=1, blank=True, null=True)
    remind_date = models.DateField(blank=True, null=True)
    remind_time = models.DateField(blank=True, null=True)
    remind_voice = models.CharField(max_length=200, blank=True, null=True)
    task_desc = models.TextField(blank=True, null=True)
    destinations = models.CharField(max_length=200, blank=True, null=True)
    cats = models.CharField(max_length=200, blank=True, null=True)
    special = models.CharField(max_length=1, blank=True, null=True)
    t_owner = models.IntegerField(blank=True, null=True)
    complete_date = models.DateField(blank=True, null=True)
    work_hours = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    distance = models.CharField(max_length=200, blank=True, null=True)
    act_hours = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    invoie_info = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ol_task'


class OldCustomerLastPrice(models.Model):
    custno = models.FloatField()
    prodn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    prodname = models.CharField(max_length=100, blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    disc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'old_customer_last_price'


class OldDiscountPolicydet(models.Model):
    id = models.FloatField()
    prodn = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'old_discount_policydet'


class Orders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pcenter = models.BigIntegerField()
    orderdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'orders'


class Pay1(models.Model):
    bilno = models.BigIntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    code = models.BigIntegerField()
    vdate = models.DateField(blank=True, null=True)
    custno = models.BigIntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    sman = models.ForeignKey('SalesMen', db_column='sman', blank=True, null=True)
    total1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    custname = models.CharField(max_length=100, blank=True, null=True)
    chk = models.IntegerField(blank=True, null=True)
    bank = models.CharField(max_length=200, blank=True, null=True)
    bnkcomm = models.FloatField(blank=True, null=True)
    payment = models.BigIntegerField(blank=True, null=True)
    workorder_no = models.BigIntegerField(blank=True, null=True)
    cash_custno = models.BigIntegerField(blank=True, null=True)
    note1 = models.CharField(max_length=100, blank=True, null=True)
    note2 = models.CharField(max_length=100, blank=True, null=True)
    note3 = models.CharField(max_length=100, blank=True, null=True)
    note4 = models.CharField(max_length=100, blank=True, null=True)
    note5 = models.CharField(max_length=100, blank=True, null=True)
    note6 = models.CharField(max_length=100, blank=True, null=True)
    note7 = models.CharField(max_length=100, blank=True, null=True)
    note_to = models.CharField(max_length=100, blank=True, null=True)
    contract_area = models.CharField(max_length=100, blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    curr_id = models.BigIntegerField(blank=True, null=True)
    curr_rate = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True)
    cat1 = models.BigIntegerField(blank=True, null=True)
    cat2 = models.BigIntegerField(blank=True, null=True)
    comm_perc = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay1'
        unique_together = (('bilno', 'pcenter', 'code'),)


class Pay1Det(models.Model):
    bilno = models.ForeignKey(Pay1, db_column='bilno')
    pcenter = models.ForeignKey(Pay1, db_column='pcenter')
    code = models.ForeignKey(Pay1, db_column='code')
    id = models.BigIntegerField()
    amount = models.FloatField()
    bnkcomm = models.FloatField(blank=True, null=True)
    credtnotes_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay1_det'
        unique_together = (('bilno', 'pcenter', 'code', 'id'),)


class Pay2(models.Model):
    bilno = models.BigIntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    code = models.BigIntegerField()
    id = models.BigIntegerField()
    invoice_no = models.BigIntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    temp1 = models.FloatField(blank=True, null=True)
    temp2 = models.FloatField(blank=True, null=True)
    issue_code = models.IntegerField()
    issue_pcenter = models.ForeignKey(Centers, db_column='issue_pcenter')
    issue_bilno = models.BigIntegerField()
    payed = models.DecimalField(max_digits=20, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'pay2'
        unique_together = (('bilno', 'pcenter', 'code', 'id'),)


class PayAccCategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    payer_from = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pay_acc_category'


class PayCust(models.Model):
    code = models.BigIntegerField()
    bilno = models.BigIntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    id = models.BigIntegerField()
    custno = models.ForeignKey(Customers, db_column='custno')
    total = models.BigIntegerField(blank=True, null=True)
    temp1 = models.BigIntegerField(blank=True, null=True)
    temp2 = models.BigIntegerField(blank=True, null=True)
    payed = models.DecimalField(max_digits=20, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'pay_cust'
        unique_together = (('code', 'bilno', 'pcenter', 'id', 'custno'),)


class PaymentDeductRatio(models.Model):
    prodn = models.CharField(max_length=20)
    payment_type = models.BigIntegerField()
    deduct_ratio = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'payment_deduct_ratio'
        unique_together = (('prodn', 'payment_type'),)


class PaymentTerms(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_terms'


class PaymentType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    accno = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_type'


class Paymentsforcashinvoice(models.Model):
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    id = models.BigIntegerField()
    vdate = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    credit_noteno = models.BigIntegerField(blank=True, null=True)
    currency = models.BigIntegerField(blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)
    payement = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paymentsforcashinvoice'
        unique_together = (('code', 'pcenter', 'bilno', 'id'),)


class Pbcatcol(models.Model):
    pbc_tnam = models.CharField(max_length=60)
    pbc_tid = models.BigIntegerField(blank=True, null=True)
    pbc_ownr = models.CharField(max_length=60)
    pbc_cnam = models.CharField(max_length=60)
    pbc_cid = models.BigIntegerField(blank=True, null=True)
    pbc_labl = models.CharField(max_length=254, blank=True, null=True)
    pbc_lpos = models.BigIntegerField(blank=True, null=True)
    pbc_hdr = models.CharField(max_length=254, blank=True, null=True)
    pbc_hpos = models.BigIntegerField(blank=True, null=True)
    pbc_jtfy = models.BigIntegerField(blank=True, null=True)
    pbc_mask = models.CharField(max_length=61, blank=True, null=True)
    pbc_case = models.BigIntegerField(blank=True, null=True)
    pbc_hght = models.BigIntegerField(blank=True, null=True)
    pbc_wdth = models.BigIntegerField(blank=True, null=True)
    pbc_ptrn = models.CharField(max_length=61, blank=True, null=True)
    pbc_bmap = models.CharField(max_length=1, blank=True, null=True)
    pbc_init = models.CharField(max_length=254, blank=True, null=True)
    pbc_cmnt = models.CharField(max_length=254, blank=True, null=True)
    pbc_edit = models.CharField(max_length=61, blank=True, null=True)
    pbc_tag = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatcol'


class Pbcatedt(models.Model):
    pbe_name = models.CharField(max_length=60, blank=True, null=True)
    pbe_edit = models.CharField(max_length=254, blank=True, null=True)
    pbe_type = models.BigIntegerField(blank=True, null=True)
    pbe_cntr = models.BigIntegerField(blank=True, null=True)
    pbe_seqn = models.BigIntegerField(blank=True, null=True)
    pbe_flag = models.BigIntegerField(blank=True, null=True)
    pbe_work = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatedt'


class Pbcatfmt(models.Model):
    pbf_name = models.CharField(unique=True, max_length=60, blank=True, null=True)
    pbf_frmt = models.CharField(max_length=254, blank=True, null=True)
    pbf_type = models.BigIntegerField()
    pbf_cntr = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatfmt'


class Pbcattbl(models.Model):
    pbt_tnam = models.CharField(max_length=60)
    pbt_tid = models.BigIntegerField(blank=True, null=True)
    pbt_ownr = models.CharField(max_length=60)
    pbd_fhgt = models.BigIntegerField(blank=True, null=True)
    pbd_fwgt = models.BigIntegerField(blank=True, null=True)
    pbd_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbd_funl = models.CharField(max_length=1, blank=True, null=True)
    pbd_fchr = models.BigIntegerField(blank=True, null=True)
    pbd_fptc = models.BigIntegerField(blank=True, null=True)
    pbd_ffce = models.CharField(max_length=36, blank=True, null=True)
    pbh_fhgt = models.BigIntegerField(blank=True, null=True)
    pbh_fwgt = models.BigIntegerField(blank=True, null=True)
    pbh_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbh_funl = models.CharField(max_length=1, blank=True, null=True)
    pbh_fchr = models.BigIntegerField(blank=True, null=True)
    pbh_fptc = models.BigIntegerField(blank=True, null=True)
    pbh_ffce = models.CharField(max_length=36, blank=True, null=True)
    pbl_fhgt = models.BigIntegerField(blank=True, null=True)
    pbl_fwgt = models.BigIntegerField(blank=True, null=True)
    pbl_fitl = models.CharField(max_length=1, blank=True, null=True)
    pbl_funl = models.CharField(max_length=1, blank=True, null=True)
    pbl_fchr = models.BigIntegerField(blank=True, null=True)
    pbl_fptc = models.BigIntegerField(blank=True, null=True)
    pbl_ffce = models.CharField(max_length=36, blank=True, null=True)
    pbt_cmnt = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcattbl'


class Pbcatvld(models.Model):
    pbv_name = models.CharField(unique=True, max_length=60, blank=True, null=True)
    pbv_vald = models.CharField(max_length=254, blank=True, null=True)
    pbv_type = models.BigIntegerField(blank=True, null=True)
    pbv_cntr = models.BigIntegerField(blank=True, null=True)
    pbv_msg = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pbcatvld'


class PortInvoice(models.Model):
    branch = models.BigIntegerField()
    inv_no = models.BigIntegerField()
    inv_date = models.DateField()
    job_no = models.CharField(max_length=30, blank=True, null=True)
    doc_no = models.CharField(max_length=30, blank=True, null=True)
    jop_type = models.CharField(max_length=200, blank=True, null=True)
    accno_credit = models.BigIntegerField(blank=True, null=True)
    accno_debit = models.BigIntegerField(blank=True, null=True)
    accname_debit = models.CharField(max_length=100, blank=True, null=True)
    vessel_nm = models.CharField(max_length=30, blank=True, null=True)
    cosignee = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    no_packages = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    total_weight = models.CharField(max_length=50, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    advance = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    commodity = models.CharField(max_length=30, blank=True, null=True)
    job_date = models.DateField(blank=True, null=True)
    cost_center = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    deliv_date = models.DateField(blank=True, null=True)
    job_type = models.CharField(max_length=200, blank=True, null=True)
    loading_airport = models.CharField(max_length=50, blank=True, null=True)
    discharge_airport = models.CharField(max_length=50, blank=True, null=True)
    shipper = models.CharField(max_length=100, blank=True, null=True)
    awb = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'port_invoice'
        unique_together = (('branch', 'inv_no'),)


class PortInvoicedet(models.Model):
    branch = models.ForeignKey(PortInvoice, db_column='branch')
    inv_no = models.ForeignKey(PortInvoice, db_column='inv_no')
    serial = models.IntegerField()
    charge = models.ForeignKey(Charges)
    curr1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    rate = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    refrenc = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    totals = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'port_invoicedet'
        unique_together = (('branch', 'inv_no', 'serial', 'charge_id'),)


class PosEditreports(models.Model):
    pcenter = models.IntegerField(primary_key=True)
    rep_syntax = models.BinaryField(blank=True, null=True)
    rep_syntax1 = models.BinaryField(blank=True, null=True)
    rep_syntax2 = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_editreports'


class PosMachines(models.Model):
    machine_no = models.FloatField(primary_key=True)
    machine_name = models.CharField(max_length=4000, blank=True, null=True)
    center_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_machines'


class PosShiftPayment(models.Model):
    payment_id = models.FloatField()
    shift_id = models.FloatField()
    begin_val = models.FloatField(blank=True, null=True)
    end_val = models.FloatField(blank=True, null=True)
    actual_val = models.FloatField(blank=True, null=True)
    invoice_counts = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_shift_payment'
        unique_together = (('payment_id', 'shift_id'),)


class PosShifts(models.Model):
    shift_id = models.FloatField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    total_sales = models.FloatField(blank=True, null=True)
    invoice_counts = models.FloatField(blank=True, null=True)
    cashier_id = models.FloatField(blank=True, null=True)
    min_bilno = models.FloatField(blank=True, null=True)
    max_bilno = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_shifts'


class PosXreport(models.Model):
    report_id = models.FloatField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    actual_val = models.FloatField(blank=True, null=True)
    invoice_counts = models.FloatField(blank=True, null=True)
    cashier_id = models.FloatField(blank=True, null=True)
    min_bilno = models.FloatField(blank=True, null=True)
    max_bilno = models.FloatField(blank=True, null=True)
    ret_val = models.FloatField(blank=True, null=True)
    ret_counts = models.FloatField(blank=True, null=True)
    max_retbilno = models.FloatField(blank=True, null=True)
    min_retbilno = models.FloatField(blank=True, null=True)
    sal_disc = models.FloatField(blank=True, null=True)
    ret_disc = models.FloatField(blank=True, null=True)
    pcenter = models.FloatField(blank=True, null=True)
    user_no = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_xreport'


class PosXreportPayment(models.Model):
    payment_id = models.FloatField()
    report_id = models.FloatField()
    actual_val = models.FloatField(blank=True, null=True)
    invoice_counts = models.FloatField(blank=True, null=True)
    ret_val = models.FloatField(blank=True, null=True)
    ret_counts = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_xreport_payment'
        unique_together = (('payment_id', 'report_id'),)


class PosZPayment(models.Model):
    payment_id = models.FloatField()
    report_id = models.FloatField()
    begin_val = models.FloatField(blank=True, null=True)
    end_val = models.FloatField(blank=True, null=True)
    sal_val = models.FloatField(blank=True, null=True)
    ret_val = models.FloatField(blank=True, null=True)
    invoice_counts = models.FloatField(blank=True, null=True)
    ret_counts = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_z_payment'
        unique_together = (('payment_id', 'report_id'),)


class PosZfreport(models.Model):
    report_id = models.FloatField(primary_key=True)
    report_date = models.DateField(blank=True, null=True)
    sal_val = models.FloatField(blank=True, null=True)
    invoice_counts = models.FloatField(blank=True, null=True)
    cashier_id = models.FloatField(blank=True, null=True)
    min_bilno = models.FloatField(blank=True, null=True)
    max_bilno = models.FloatField(blank=True, null=True)
    ret_val = models.FloatField(blank=True, null=True)
    ret_counts = models.FloatField(blank=True, null=True)
    min_retbilno = models.FloatField(blank=True, null=True)
    max_retbilno = models.FloatField(blank=True, null=True)
    sal_disc = models.FloatField(blank=True, null=True)
    ret_disc = models.FloatField(blank=True, null=True)
    pcenter = models.FloatField(blank=True, null=True)
    user_no = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_zfreport'


class PosZreport(models.Model):
    report_id = models.FloatField()
    shift_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pos_zreport'
        unique_together = (('report_id', 'shift_id'),)


class PostedTrn(models.Model):
    pid = models.ForeignKey('PostingTrn', db_column='pid')
    id = models.IntegerField()
    code = models.IntegerField(blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter', blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)
    reset_id = models.BigIntegerField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True, null=True)
    reset = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posted_trn'
        unique_together = (('pid', 'id'),)


class PostingTrn(models.Model):
    pid = models.BigIntegerField(primary_key=True)
    vdate = models.DateField(blank=True, null=True)
    user_no = models.BigIntegerField(blank=True, null=True)
    cashinv = models.CharField(max_length=1, blank=True, null=True)
    credtinv = models.CharField(max_length=1, blank=True, null=True)
    cashinvret = models.CharField(max_length=1, blank=True, null=True)
    credtinvret = models.CharField(max_length=1, blank=True, null=True)
    invcost = models.CharField(max_length=1, blank=True, null=True)
    retcost = models.CharField(max_length=1, blank=True, null=True)
    pur = models.CharField(max_length=1, blank=True, null=True)
    purret = models.CharField(max_length=1, blank=True, null=True)
    reciveable = models.CharField(max_length=1, blank=True, null=True)
    pay = models.CharField(max_length=1, blank=True, null=True)
    stockv = models.CharField(max_length=1, blank=True, null=True)
    tahweel = models.CharField(max_length=1, blank=True, null=True)
    posted = models.CharField(max_length=1, blank=True, null=True)
    sel_period = models.CharField(max_length=1, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    sel_pcenter = models.CharField(max_length=1, blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter', blank=True, null=True)
    store_rec = models.CharField(max_length=1, blank=True, null=True)
    cash_pay = models.CharField(max_length=1, blank=True, null=True)
    pur_cost = models.CharField(max_length=1, blank=True, null=True)
    pur_ret_cost = models.CharField(max_length=1, blank=True, null=True)
    postcustadj = models.CharField(max_length=1, blank=True, null=True)
    workorder_cost = models.CharField(max_length=1, blank=True, null=True)
    deprtiation = models.CharField(max_length=1, blank=True, null=True)
    cashsales_partialpay = models.CharField(max_length=1, blank=True, null=True)
    costupdate = models.CharField(max_length=1, blank=True, null=True)
    changebalance = models.CharField(max_length=1, blank=True, null=True)
    balance_adjust = models.NullBooleanField()
    production = models.NullBooleanField()
    purchase_return_diff = models.NullBooleanField()
    trans_diff = models.NullBooleanField()
    exchange_voucher = models.CharField(max_length=1, blank=True, null=True)
    invcostcredit = models.CharField(max_length=1, blank=True, null=True)
    retcostcredit = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posting_trn'


class PredectedPurchase(models.Model):
    prodn = models.CharField(max_length=30)
    prods = models.BigIntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    pred_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pred_value = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    expenses_ratio = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predected_purchase'
        unique_together = (('prodn', 'prods', 'year', 'month'),)


class PredectedSales(models.Model):
    prodn = models.CharField(max_length=30)
    prods = models.BigIntegerField()
    customer = models.BigIntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    qty = models.DecimalField(max_digits=20, decimal_places=4)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    collec_month = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predected_sales'
        unique_together = (('prodn', 'prods', 'customer', 'year', 'month'),)


class PredectedStore(models.Model):
    prodn = models.CharField(max_length=30)
    prods = models.BigIntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    obqty = models.DecimalField(max_digits=20, decimal_places=4)
    pred_sales = models.DecimalField(max_digits=20, decimal_places=4)
    pred_stock = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'predected_store'
        unique_together = (('prodn', 'prods', 'year', 'month'),)


class PricingCalcParameetrs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    a = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    b = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    c = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    d = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    e = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    f = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    g = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    h = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    i = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    j = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    calc_equation = models.TextField(blank=True, null=True)
    equ_expresion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pricing_calc_parameetrs'


class ProdnAreaExpenses(models.Model):
    prodn = models.CharField(max_length=30)
    area_code = models.IntegerField()
    area_name = models.CharField(max_length=100, blank=True, null=True)
    expenses1 = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)
    expenses2 = models.DecimalField(max_digits=30, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prodn_area_expenses'
        unique_together = (('prodn', 'area_code'),)


class ProductCat1(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    costcenter_no = models.BigIntegerField(blank=True, null=True)
    is_displayinpos = models.NullBooleanField()
    items_code = models.CharField(max_length=25, blank=True, null=True)
    printer_nm = models.CharField(max_length=200, blank=True, null=True)
    isusedinrestauarnt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cat1'


class ProductCat2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    cat1 = models.FloatField(blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    costcenter_no = models.BigIntegerField(blank=True, null=True)
    printer_nm = models.CharField(max_length=200, blank=True, null=True)
    chek_bdala = models.NullBooleanField()
    items_code = models.CharField(max_length=25, blank=True, null=True)
    isusedinrestauarnt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cat2'


class ProductCat3(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    cat2 = models.BigIntegerField(blank=True, null=True)
    name_e = models.CharField(max_length=40, blank=True, null=True)
    costcenter_no = models.BigIntegerField(blank=True, null=True)
    items_code = models.CharField(max_length=25, blank=True, null=True)
    printer_nm = models.CharField(max_length=200, blank=True, null=True)
    isusedinrestauarnt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cat3'


class ProductCat4(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    cat3 = models.BigIntegerField(blank=True, null=True)
    name_e = models.CharField(max_length=40, blank=True, null=True)
    costcenter_no = models.BigIntegerField(blank=True, null=True)
    items_code = models.CharField(max_length=25, blank=True, null=True)
    printer_nm = models.CharField(max_length=200, blank=True, null=True)
    isusedinrestauarnt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cat4'


class ProductExpenses(models.Model):
    code = models.BigIntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    id = models.BigIntegerField()
    serial = models.BigIntegerField()
    prodn = models.CharField(max_length=30)
    amount = models.FloatField()
    supno = models.ForeignKey('Suppliers', db_column='supno', blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    exp_notes = models.TextField(blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)
    non_invent = models.NullBooleanField()
    exp_code = models.ForeignKey(ExpensesTypes, db_column='exp_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_expenses'
        unique_together = (('code', 'pcenter', 'bilno', 'id', 'serial'),)


class PurOrderPricingColumns(models.Model):
    pur_order_no = models.BigIntegerField()
    branch = models.IntegerField()
    id = models.IntegerField()
    col_equation = models.TextField()
    col_name = models.CharField(max_length=100, blank=True, null=True)
    a = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    b = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    c = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    d = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    e = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    f = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    g = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    h = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    i = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    j = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pur_order_pricing_columns'
        unique_together = (('pur_order_no', 'branch', 'id'),)


class PurOrderPricingParms(models.Model):
    pur_order_no = models.BigIntegerField()
    branch = models.IntegerField()
    no_of_steps = models.BigIntegerField(blank=True, null=True)
    price_changed = models.BigIntegerField(blank=True, null=True)
    expenses1 = models.BigIntegerField(blank=True, null=True)
    expenses2 = models.BigIntegerField(blank=True, null=True)
    expense3 = models.BigIntegerField(blank=True, null=True)
    expenses4 = models.BigIntegerField(blank=True, null=True)
    price_1_col = models.BigIntegerField(blank=True, null=True)
    price_2_col = models.BigIntegerField(blank=True, null=True)
    price_3_col = models.BigIntegerField(blank=True, null=True)
    price_4_col = models.BigIntegerField(blank=True, null=True)
    price_5_col = models.BigIntegerField(blank=True, null=True)
    price_6_col = models.BigIntegerField(blank=True, null=True)
    rep_syntax = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pur_order_pricing_parms'
        unique_together = (('pur_order_no', 'branch'),)


class PurcahseDelivStages(models.Model):
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    deliv_code = models.IntegerField()
    deliv_date = models.DateField(blank=True, null=True)
    deliv_val = models.FloatField(blank=True, null=True)
    deliv_notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purcahse_deliv_stages'
        unique_together = (('code', 'pcenter', 'bilno', 'deliv_code'),)


class PurcahseExpensis(models.Model):
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    exp_code = models.IntegerField()
    exp_name = models.CharField(max_length=50, blank=True, null=True)
    exp_val = models.DecimalField(max_digits=22, decimal_places=3, blank=True, null=True)
    exp_accno = models.BigIntegerField(blank=True, null=True)
    currency_id = models.BigIntegerField(blank=True, null=True)
    currency_rate = models.FloatField(blank=True, null=True)
    exp_accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purcahse_expensis'
        unique_together = (('code', 'pcenter', 'bilno', 'exp_code'),)


class PurchasePayments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    accno = models.CharField(max_length=14, blank=True, null=True)
    name_e = models.CharField(max_length=20, blank=True, null=True)
    bnk_commp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_payments'


class PuritmSerialno(models.Model):
    id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    serial_no = models.CharField(max_length=20)
    isexist = models.NullBooleanField()
    sal_id = models.BigIntegerField(blank=True, null=True)
    sal_pcenter = models.ForeignKey(Centers, db_column='sal_pcenter', blank=True, null=True)
    sal_code = models.BigIntegerField(blank=True, null=True)
    sal_bilno = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    purrtn_id = models.BigIntegerField(blank=True, null=True)
    purrtn_pcenter = models.BigIntegerField(blank=True, null=True)
    purrtn_code = models.BigIntegerField(blank=True, null=True)
    purrtn_bilno = models.BigIntegerField(blank=True, null=True)
    salrtn_id = models.BigIntegerField(blank=True, null=True)
    salrtn_pcenter = models.BigIntegerField(blank=True, null=True)
    salrtn_code = models.BigIntegerField(blank=True, null=True)
    salrtn_bilno = models.BigIntegerField(blank=True, null=True)
    invrtn_id = models.BigIntegerField(blank=True, null=True)
    invrtn_pcenter = models.BigIntegerField(blank=True, null=True)
    invrtn_code = models.BigIntegerField(blank=True, null=True)
    invrtn_bilno = models.BigIntegerField(blank=True, null=True)
    inv_id = models.BigIntegerField(blank=True, null=True)
    inv_pcenter = models.ForeignKey(Centers, db_column='inv_pcenter', blank=True, null=True)
    inv_code = models.BigIntegerField(blank=True, null=True)
    inv_bilno = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puritm_serialno'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'serial_no'),)


class QuestSlTempExplain1(models.Model):
    statement_id = models.CharField(max_length=30)
    plan_id = models.FloatField()
    timestamp = models.DateField()
    remarks = models.CharField(max_length=80, blank=True, null=True)
    operation = models.CharField(max_length=30, blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)
    object_node = models.CharField(max_length=128, blank=True, null=True)
    object_owner = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=30, blank=True, null=True)
    object_alias = models.CharField(max_length=65, blank=True, null=True)
    object_instance = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=30, blank=True, null=True)
    optimizer = models.CharField(max_length=255, blank=True, null=True)
    search_columns = models.FloatField(blank=True, null=True)
    id = models.FloatField(blank=True, null=True)
    parent_id = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    position = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    cardinality = models.FloatField(blank=True, null=True)
    bytes = models.FloatField(blank=True, null=True)
    other_tag = models.CharField(max_length=255, blank=True, null=True)
    partition_start = models.CharField(max_length=255, blank=True, null=True)
    partition_stop = models.CharField(max_length=255, blank=True, null=True)
    partition_id = models.FloatField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)  # This field type is a guess.
    distribution = models.CharField(max_length=30, blank=True, null=True)
    cpu_cost = models.BigIntegerField(blank=True, null=True)
    io_cost = models.BigIntegerField(blank=True, null=True)
    temp_space = models.BigIntegerField(blank=True, null=True)
    access_predicates = models.CharField(max_length=4000, blank=True, null=True)
    filter_predicates = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quest_sl_temp_explain1'
        unique_together = (('statement_id', 'plan_id', 'timestamp'),)


class ReadyDetails(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    details = models.TextField()
    details_e = models.TextField()

    class Meta:
        managed = False
        db_table = 'ready_details'


class ReadyInvoice(models.Model):
    id = models.BigIntegerField()
    id_1 = models.CharField(max_length=50)
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    udisc_p = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    udisc = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    bilno = models.CharField(max_length=20, blank=True, null=True)
    item_cost = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    unit_text = models.BigIntegerField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    non_invent = models.NullBooleanField()
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ready_invoice'
        unique_together = (('id', 'id_1'),)


class RecQ(models.Model):
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'rec_q'
        unique_together = (('code', 'pcenter', 'bilno'),)


class Reciept1(models.Model):
    code = models.IntegerField()
    vdate = models.DateField(blank=True, null=True)
    sbilno = models.CharField(max_length=30, blank=True, null=True)
    pur_order = models.CharField(max_length=30, blank=True, null=True)
    payment = models.BigIntegerField(blank=True, null=True)
    discount = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    currancy = models.BigIntegerField(blank=True, null=True)
    currancy_change = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    user_no = models.BigIntegerField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    notes_print_flage = models.NullBooleanField()
    inv2 = models.BigIntegerField(blank=True, null=True)
    inv1 = models.BigIntegerField(blank=True, null=True)
    templet = models.NullBooleanField()
    supno = models.ForeignKey('Suppliers', db_column='supno', blank=True, null=True)
    lc_id = models.CharField(max_length=30, blank=True, null=True)
    lc_per = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    order_no = models.CharField(max_length=25, blank=True, null=True)
    temp_date = models.DateField(blank=True, null=True)
    delivary_method = models.ForeignKey(DelivaryMethod, blank=True, null=True)
    xpcenter = models.ForeignKey(Centers, db_column='xpcenter', blank=True, null=True)
    sman = models.BigIntegerField(blank=True, null=True)
    job_no = models.BigIntegerField(blank=True, null=True)
    xcode = models.IntegerField(blank=True, null=True)
    d_date = models.DateField(blank=True, null=True)
    d_location = models.CharField(max_length=100, blank=True, null=True)
    gl_to = models.CharField(max_length=1, blank=True, null=True)
    to_accno = models.BigIntegerField(blank=True, null=True)
    custno = models.ForeignKey(Customers, db_column='custno', blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    payment_terms = models.BigIntegerField(blank=True, null=True)
    rcp1_invtransferrqstno = models.BigIntegerField(blank=True, null=True)
    rcp1_modeofshippment = models.CharField(max_length=100, blank=True, null=True)
    rcp1_insuranceby = models.CharField(max_length=100, blank=True, null=True)
    rcp1_freighterm = models.CharField(max_length=100, blank=True, null=True)
    rcp1_approxvol = models.CharField(max_length=100, blank=True, null=True)
    driver_name = models.BigIntegerField(blank=True, null=True)
    plate_no = models.CharField(max_length=100, blank=True, null=True)
    sticker_no = models.CharField(max_length=100, blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_user = models.BigIntegerField(blank=True, null=True)
    prepared_by = models.BigIntegerField(blank=True, null=True)
    add_expenses = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    deliv_note = models.CharField(max_length=200, blank=True, null=True)
    lc_expenses_cash = models.BigIntegerField(blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    reviewed = models.NullBooleanField()
    area_code = models.IntegerField(blank=True, null=True)
    driver_code = models.IntegerField(blank=True, null=True)
    tot_qty = models.IntegerField(blank=True, null=True)
    bottles_damage = models.BigIntegerField(blank=True, null=True)
    halal_certificate = models.BigIntegerField(blank=True, null=True)
    helth_certificate = models.BigIntegerField(blank=True, null=True)
    letter_of_leding = models.BigIntegerField(blank=True, null=True)
    charge_invoice = models.BigIntegerField(blank=True, null=True)
    po_invoice = models.BigIntegerField(blank=True, null=True)
    origin_certificate = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    account_item_code = models.BigIntegerField(blank=True, null=True)
    purchase_order_no = models.BigIntegerField(blank=True, null=True)
    purchase_order_date = models.DateField(blank=True, null=True)
    total_act_catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pricing_factor = models.FloatField(blank=True, null=True)
    vtime = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=999, blank=True, null=True)
    shipment_no = models.CharField(max_length=10, blank=True, null=True)
    price_type = models.IntegerField(blank=True, null=True)
    accepted = models.NullBooleanField()
    sbildate = models.DateField(blank=True, null=True)
    price_code = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    inv_temp = models.FloatField(blank=True, null=True)
    lc_cost_share = models.FloatField(blank=True, null=True)
    posted_to_agility = models.IntegerField(blank=True, null=True)
    posted_from_agility = models.IntegerField(blank=True, null=True)
    to_accno_old = models.CharField(max_length=40, blank=True, null=True)
    lc_expenses_cash_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reciept_1'
        unique_together = (('code', 'pcenter', 'bilno'),)


class Reciept1Hist(models.Model):
    trn_id = models.IntegerField()
    code = models.IntegerField()
    vdate = models.DateField(blank=True, null=True)
    sbilno = models.CharField(max_length=30, blank=True, null=True)
    pur_order = models.CharField(max_length=20, blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    currancy = models.IntegerField(blank=True, null=True)
    currancy_change = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    user_no = models.IntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    pcenter = models.FloatField()
    bilno = models.FloatField()
    notes = models.CharField(max_length=255, blank=True, null=True)
    notes_print_flage = models.NullBooleanField()
    inv2 = models.IntegerField(blank=True, null=True)
    inv1 = models.IntegerField(blank=True, null=True)
    templet = models.NullBooleanField()
    supno = models.FloatField(blank=True, null=True)
    lc_id = models.CharField(max_length=30, blank=True, null=True)
    lc_per = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    order_no = models.CharField(max_length=25, blank=True, null=True)
    temp_date = models.DateField(blank=True, null=True)
    delivary_method_id = models.IntegerField(blank=True, null=True)
    xpcenter = models.FloatField(blank=True, null=True)
    sman = models.FloatField(blank=True, null=True)
    job_no = models.BigIntegerField(blank=True, null=True)
    xcode = models.IntegerField(blank=True, null=True)
    d_date = models.DateField(blank=True, null=True)
    d_location = models.CharField(max_length=100, blank=True, null=True)
    gl_to = models.CharField(max_length=1, blank=True, null=True)
    to_accno = models.CharField(max_length=14, blank=True, null=True)
    custno = models.FloatField(blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    payment_terms = models.IntegerField(blank=True, null=True)
    rcp1_invtransferrqstno = models.FloatField(blank=True, null=True)
    rcp1_modeofshippment = models.CharField(max_length=100, blank=True, null=True)
    rcp1_insuranceby = models.CharField(max_length=100, blank=True, null=True)
    rcp1_freighterm = models.CharField(max_length=100, blank=True, null=True)
    rcp1_approxvol = models.CharField(max_length=100, blank=True, null=True)
    driver_name = models.IntegerField(blank=True, null=True)
    plate_no = models.CharField(max_length=100, blank=True, null=True)
    sticker_no = models.CharField(max_length=100, blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_user = models.IntegerField(blank=True, null=True)
    prepared_by = models.FloatField(blank=True, null=True)
    add_expenses = models.FloatField(blank=True, null=True)
    deliv_note = models.CharField(max_length=200, blank=True, null=True)
    lc_expenses_cash = models.CharField(max_length=14, blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    reviewed = models.NullBooleanField()
    area_code = models.IntegerField(blank=True, null=True)
    driver_code = models.IntegerField(blank=True, null=True)
    tot_qty = models.IntegerField(blank=True, null=True)
    bottles_damage = models.FloatField(blank=True, null=True)
    halal_certificate = models.IntegerField(blank=True, null=True)
    helth_certificate = models.IntegerField(blank=True, null=True)
    letter_of_leding = models.IntegerField(blank=True, null=True)
    charge_invoice = models.IntegerField(blank=True, null=True)
    po_invoice = models.IntegerField(blank=True, null=True)
    origin_certificate = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
    account_item_code = models.BigIntegerField(blank=True, null=True)
    purchase_order_no = models.BigIntegerField(blank=True, null=True)
    purchase_order_date = models.DateField(blank=True, null=True)
    total_act_catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pricing_factor = models.FloatField(blank=True, null=True)
    vtime = models.DateTimeField(blank=True, null=True)
    posted_to_agility = models.IntegerField(blank=True, null=True)
    posted_from_agility = models.IntegerField(blank=True, null=True)
    trn_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reciept_1_hist'
        unique_together = (('trn_id', 'code', 'pcenter', 'bilno'),)


class Reciept2(models.Model):
    id = models.BigIntegerField()
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    qty = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    non_invent = models.NullBooleanField()
    inv2 = models.BigIntegerField(blank=True, null=True)
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    disc2 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    total = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    rec_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp1 = models.FloatField(blank=True, null=True)
    temp2 = models.FloatField(blank=True, null=True)
    di1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    lc_value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    kit_no = models.BigIntegerField(blank=True, null=True)
    kit_qty = models.FloatField(blank=True, null=True)
    inv_no = models.BigIntegerField(blank=True, null=True)
    iss_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    unit = models.BigIntegerField(blank=True, null=True)
    conv2 = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    isnew = models.NullBooleanField()
    related_branch = models.BigIntegerField(blank=True, null=True)
    related_code = models.IntegerField(blank=True, null=True)
    related_billno = models.BigIntegerField(blank=True, null=True)
    related_id = models.BigIntegerField(blank=True, null=True)
    originparentid = models.BigIntegerField(blank=True, null=True)
    batchno = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    ret_qty = models.IntegerField(blank=True, null=True)
    empty_qty = models.IntegerField(blank=True, null=True)
    credit_qty = models.IntegerField(blank=True, null=True)
    cobon_qty = models.IntegerField(blank=True, null=True)
    delivered = models.IntegerField(blank=True, null=True)
    custno = models.ForeignKey(Customers, db_column='custno', blank=True, null=True)
    contract_no = models.BigIntegerField(blank=True, null=True)
    delivary_no = models.BigIntegerField(blank=True, null=True)
    ser = models.BigIntegerField(blank=True, null=True)
    coolers_istalled = models.BigIntegerField(blank=True, null=True)
    bottles_fountain = models.BigIntegerField(blank=True, null=True)
    coolers_return = models.BigIntegerField(blank=True, null=True)
    cups_delivered = models.BigIntegerField(blank=True, null=True)
    empty_bottles_return = models.BigIntegerField(blank=True, null=True)
    payment_method = models.NullBooleanField()
    comm_domestic = models.BigIntegerField(blank=True, null=True)
    contract_code = models.CharField(max_length=50, blank=True, null=True)
    bottles_demo = models.BigIntegerField(blank=True, null=True)
    bottles_release = models.BigIntegerField(blank=True, null=True)
    old_cost = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    old_stock = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    sort_item = models.BigIntegerField(blank=True, null=True)
    discp = models.FloatField(blank=True, null=True)
    qty1 = models.FloatField(blank=True, null=True)
    start_from = models.BigIntegerField(blank=True, null=True)
    end_to = models.BigIntegerField(blank=True, null=True)
    start_group = models.BigIntegerField(blank=True, null=True)
    end_group = models.BigIntegerField(blank=True, null=True)
    ser_qty = models.FloatField(blank=True, null=True)
    model_no = models.BigIntegerField(blank=True, null=True)
    catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    act_catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    calc_again = models.NullBooleanField()
    sman = models.ForeignKey('SalesMen', db_column='sman', blank=True, null=True)
    item_cost = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    inv_temp = models.FloatField(blank=True, null=True)
    avg_cost = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    avg_cost2 = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reciept_2'
        unique_together = (('id', 'code', 'pcenter', 'bilno'),)


class Reciept2Expire(models.Model):
    id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    exp_date = models.DateField()
    qty = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    batchno = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reciept_2_expire'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'exp_date'),)


class Reciept2Hist(models.Model):
    trn_id = models.IntegerField()
    id = models.FloatField()
    prods = models.IntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    non_invent = models.NullBooleanField()
    inv2 = models.IntegerField(blank=True, null=True)
    temp1 = models.FloatField(blank=True, null=True)
    code = models.IntegerField()
    pcenter = models.FloatField()
    bilno = models.FloatField()
    disc2 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    rec_qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp2 = models.FloatField(blank=True, null=True)
    di1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    di3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    temp_qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    kit_no = models.FloatField(blank=True, null=True)
    kit_qty = models.FloatField(blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    inv_no = models.FloatField(blank=True, null=True)
    conv2 = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    isnew = models.NullBooleanField()
    related_branch = models.FloatField(blank=True, null=True)
    related_code = models.IntegerField(blank=True, null=True)
    related_billno = models.FloatField(blank=True, null=True)
    related_id = models.FloatField(blank=True, null=True)
    originparentid = models.FloatField(blank=True, null=True)
    batchno = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    discp = models.FloatField(blank=True, null=True)
    qty1 = models.FloatField(blank=True, null=True)
    start_from = models.FloatField(blank=True, null=True)
    end_to = models.FloatField(blank=True, null=True)
    start_group = models.FloatField(blank=True, null=True)
    end_group = models.FloatField(blank=True, null=True)
    ser_qty = models.FloatField(blank=True, null=True)
    ret_qty = models.IntegerField(blank=True, null=True)
    empty_qty = models.IntegerField(blank=True, null=True)
    credit_qty = models.IntegerField(blank=True, null=True)
    cobon_qty = models.IntegerField(blank=True, null=True)
    delivered = models.IntegerField(blank=True, null=True)
    custno = models.FloatField(blank=True, null=True)
    contract_no = models.FloatField(blank=True, null=True)
    delivary_no = models.FloatField(blank=True, null=True)
    ser = models.FloatField(blank=True, null=True)
    coolers_istalled = models.FloatField(blank=True, null=True)
    bottles_fountain = models.FloatField(blank=True, null=True)
    coolers_return = models.FloatField(blank=True, null=True)
    cups_delivered = models.FloatField(blank=True, null=True)
    empty_bottles_return = models.FloatField(blank=True, null=True)
    payment_method = models.NullBooleanField()
    comm_domestic = models.IntegerField(blank=True, null=True)
    contract_code = models.CharField(max_length=50, blank=True, null=True)
    bottles_demo = models.FloatField(blank=True, null=True)
    bottles_release = models.FloatField(blank=True, null=True)
    old_cost = models.FloatField(blank=True, null=True)
    old_stock = models.FloatField(blank=True, null=True)
    sort_item = models.FloatField(blank=True, null=True)
    model_no = models.FloatField(blank=True, null=True)
    catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    act_catalog_weight = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    calc_again = models.NullBooleanField()
    sman = models.IntegerField(blank=True, null=True)
    trn_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reciept_2_hist'
        unique_together = (('trn_id', 'id', 'code', 'pcenter', 'bilno'),)


class RecieptRealtedVouchers(models.Model):
    id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    related_bilno = models.BigIntegerField(blank=True, null=True)
    related_code = models.IntegerField(blank=True, null=True)
    related_pcenter = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reciept_realted_vouchers'
        unique_together = (('id', 'code', 'pcenter', 'bilno'),)


class RecieptTaxes(models.Model):
    id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    tax = models.ForeignKey('Taxes')
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reciept_taxes'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'tax_id'),)


class Reports(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    cr1 = models.NullBooleanField()
    cr2 = models.NullBooleanField()
    cr3 = models.NullBooleanField()
    cr4 = models.NullBooleanField()
    cr5 = models.NullBooleanField()
    cr6 = models.NullBooleanField()
    cr7 = models.NullBooleanField()
    cr8 = models.NullBooleanField()
    cr9 = models.NullBooleanField()
    cr10 = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'reports'


class Reset(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nam = models.CharField(max_length=100)
    closing_date = models.DateField(blank=True, null=True)
    name_e = models.CharField(max_length=100)
    branch = models.NullBooleanField()
    branch_serial = models.NullBooleanField()
    accno = models.BigIntegerField(blank=True, null=True)
    dc = models.CharField(max_length=1, blank=True, null=True)
    alarm = models.NullBooleanField()
    active = models.NullBooleanField()
    like_reset = models.NullBooleanField()
    module = models.NullBooleanField()
    approve_group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reset'


class ResetType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reset_type'


class Roleusers(models.Model):
    roleid = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    dml = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roleusers'


class Routes(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'


class Rsections(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    floor_id = models.BigIntegerField(blank=True, null=True)
    x_pos = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    y_pos = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    centerid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rsections'


class RstShifts(models.Model):
    id = models.BigIntegerField()
    center_id = models.BigIntegerField()
    open_date = models.DateField()
    close_date = models.DateField(blank=True, null=True)
    open_user_id = models.FloatField()
    close_user_id = models.FloatField(blank=True, null=True)
    machine_id = models.BigIntegerField(blank=True, null=True)
    open_balance = models.DecimalField(max_digits=15, decimal_places=3)
    total_order_sales = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    total_takeaway_sales = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    total_delivery_sales = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    total_cash_delivery = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    state = models.BooleanField()
    shiftname = models.CharField(max_length=50, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    close_balance = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    shiftid = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rst_shifts'
        unique_together = (('id', 'center_id'),)


class RstShiftsLookup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    orderno = models.FloatField(blank=True, null=True)
    center_id = models.FloatField()
    duration = models.FloatField(blank=True, null=True)
    active = models.FloatField(blank=True, null=True)
    nameen = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rst_shifts_lookup'


class SAcctranSetup(models.Model):
    account_tran = models.IntegerField()
    branch = models.IntegerField()
    batch = models.DecimalField(max_digits=20, decimal_places=5)
    reciept_acc = models.CharField(max_length=14, blank=True, null=True)
    rv_cscd = models.IntegerField(blank=True, null=True)
    rv_chcd = models.IntegerField(blank=True, null=True)
    payment_acc = models.CharField(max_length=14, blank=True, null=True)
    pv_cscd = models.IntegerField(blank=True, null=True)
    pv_chcd = models.IntegerField(blank=True, null=True)
    accdsn = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_acctran_setup'
        unique_together = (('account_tran', 'branch', 'batch'),)


class SalesManChangesHistory(models.Model):
    accno = models.CharField(max_length=14)
    vdate = models.DateField()
    account = models.ForeignKey(AccAddDetail, blank=True, null=True)
    old_val = models.IntegerField()
    change_user = models.CharField(max_length=16)
    change_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'sales_man_changes_history'
        unique_together = (('accno', 'vdate'),)


class SalesMen(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter', blank=True, null=True)
    acc_branch = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    commission = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    accno = models.BigIntegerField(blank=True, null=True)
    guardship_accno = models.BigIntegerField(blank=True, null=True)
    sort_id = models.FloatField(blank=True, null=True)
    alt_sman = models.ForeignKey('self', db_column='alt_sman', blank=True, null=True)
    e_mail = models.CharField(max_length=100, blank=True, null=True)
    jop_position = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_men'


class SalesMen2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    pcenter = models.ForeignKey(Centers, db_column='pcenter', blank=True, null=True)
    acc_branch = models.BigIntegerField(blank=True, null=True)
    commission = models.BigIntegerField(blank=True, null=True)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    accno = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_men2'


class SalesMenBillHistory(models.Model):
    accno = models.CharField(max_length=14)
    sales_man = models.BigIntegerField()
    serial = models.BigIntegerField()
    start_dt = models.DateField(blank=True, null=True)
    end_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_men_bill_history'
        unique_together = (('accno', 'sales_man', 'serial'),)


class SalesQtyPrices(models.Model):
    no1 = models.BigIntegerField()
    no2 = models.BigIntegerField()
    price = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_qty_prices'
        unique_together = (('no1', 'no2'),)


class Saleseason(models.Model):
    season_id = models.BigIntegerField(primary_key=True)
    season_desc = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()

    class Meta:
        managed = False
        db_table = 'saleseason'


class SalitmSerialno(models.Model):
    id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    serial_no = models.CharField(max_length=100)
    prodn = models.CharField(max_length=30)
    warenty_st_date = models.DateField(blank=True, null=True)
    warenty_end_date = models.DateField(blank=True, null=True)
    prods = models.IntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    inv2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salitm_serialno'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'serial_no', 'prodn'),)


class SalitmSerialno2(models.Model):
    id = models.FloatField()
    code = models.IntegerField()
    pcenter = models.FloatField()
    bilno = models.FloatField()
    from_serial_no = models.CharField(max_length=100)
    to_serial_no = models.CharField(max_length=100)
    prodn = models.CharField(max_length=30)
    warenty_st_date = models.DateField(blank=True, null=True)
    warenty_end_date = models.DateField(blank=True, null=True)
    vdate = models.DateTimeField(blank=True, null=True)
    prods = models.FloatField(blank=True, null=True)
    inv2 = models.FloatField(blank=True, null=True)
    group_no = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'salitm_serialno2'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'from_serial_no', 'to_serial_no', 'prodn'),)


class SalitmSerialnoNotSold(models.Model):
    id = models.FloatField()
    code = models.IntegerField()
    pcenter = models.FloatField()
    bilno = models.FloatField()
    serial_no = models.CharField(max_length=20)
    prodn = models.CharField(max_length=30)
    warenty_st_date = models.DateField(blank=True, null=True)
    warenty_end_date = models.DateField(blank=True, null=True)
    vdate = models.DateTimeField(blank=True, null=True)
    prods = models.FloatField(blank=True, null=True)
    inv2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salitm_serialno_not_sold'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'serial_no', 'prodn'),)


class SalitmSerialnoTemp(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    pcenter = models.BigIntegerField(blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=100, blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    warenty_st_date = models.DateField(blank=True, null=True)
    warenty_end_date = models.DateField(blank=True, null=True)
    prods = models.IntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    inv2 = models.IntegerField(blank=True, null=True)
    us_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salitm_serialno_temp'


class Sarf(models.Model):
    bilno = models.BigIntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    code = models.BigIntegerField()
    vdate = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    payment_to = models.CharField(max_length=100, blank=True, null=True)
    cheq = models.CharField(max_length=50, blank=True, null=True)
    payment_type = models.BigIntegerField(blank=True, null=True)
    add_voucher_user = models.CharField(max_length=16, blank=True, null=True)
    lupdate_voucher_user = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sarf'
        unique_together = (('bilno', 'pcenter', 'code'),)


class SclIncomesType(models.Model):
    schoolcode = models.IntegerField()
    code = models.IntegerField()
    namear = models.CharField(max_length=100, blank=True, null=True)
    nameen = models.CharField(max_length=100, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scl_incomes_type'
        unique_together = (('schoolcode', 'code'),)


class SclYears(models.Model):
    code = models.IntegerField()
    schoolcode = models.IntegerField()
    namear = models.CharField(max_length=100, blank=True, null=True)
    nameen = models.CharField(max_length=100, blank=True, null=True)
    yrstart = models.DateField(blank=True, null=True)
    yrend = models.DateField(blank=True, null=True)
    entryuser = models.CharField(max_length=20, blank=True, null=True)
    entrydate = models.DateField(blank=True, null=True)
    lastmoduser = models.CharField(max_length=20, blank=True, null=True)
    lastmoddate = models.DateField(blank=True, null=True)
    age_reference_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scl_years'
        unique_together = (('code', 'schoolcode'),)


class Seasons(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasons'


class SeasonsType(models.Model):
    sea_id = models.IntegerField(primary_key=True)
    sea_name = models.CharField(max_length=20, blank=True, null=True)
    sea_name_e = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasons_type'


class Sections(models.Model):
    section_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_e = models.CharField(max_length=80, blank=True, null=True)
    from_revenue = models.BigIntegerField(blank=True, null=True)
    to_revenue = models.BigIntegerField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sections'


class SerialNo(models.Model):
    id = models.IntegerField()
    serial = models.DecimalField(max_digits=20, decimal_places=3)
    n1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    n2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pc_name = models.CharField(max_length=20, blank=True, null=True)
    computer_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serial_no'
        unique_together = (('id', 'serial'),)


class SerialnoTkts(models.Model):
    ticket_no = models.BigIntegerField(primary_key=True)
    group_no = models.BigIntegerField()
    from_serial_no = models.CharField(max_length=100)
    to_serial_no = models.CharField(max_length=100)
    prodn = models.CharField(max_length=30)
    prods = models.FloatField()
    qty = models.BigIntegerField(blank=True, null=True)
    isavailable = models.BooleanField()
    warenty_st_date = models.DateField(blank=True, null=True)
    warenty_end_date = models.DateField(blank=True, null=True)
    vdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serialno_tkts'


class SerialnoTrns(models.Model):
    id = models.FloatField()
    code = models.IntegerField()
    pcenter = models.FloatField()
    bilno = models.FloatField()
    ticket_no = models.ForeignKey(SerialnoTkts, db_column='ticket_no')

    class Meta:
        managed = False
        db_table = 'serialno_trns'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'ticket_no'),)


class SerialsSummery(models.Model):
    serialno = models.CharField(max_length=30)
    prodn = models.CharField(max_length=30)
    prods = models.IntegerField(blank=True, null=True)
    last_code = models.IntegerField(blank=True, null=True)
    last_pcenter = models.BigIntegerField(blank=True, null=True)
    last_bilno = models.BigIntegerField(blank=True, null=True)
    last_id = models.BigIntegerField(blank=True, null=True)
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'serials_summery'
        unique_together = (('serialno', 'prodn'),)


class ServiceItemsFordelivery(models.Model):
    id = models.BigIntegerField()
    prodn = models.CharField(primary_key=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'service_items_fordelivery'


class Settings(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ss_address_e = models.TextField(blank=True, null=True)
    ss_statment_footer = models.TextField(blank=True, null=True)
    ss_tel1 = models.CharField(max_length=20, blank=True, null=True)
    ss_tel2 = models.CharField(max_length=20, blank=True, null=True)
    ss_address = models.TextField(blank=True, null=True)
    ss_invoice_footer = models.TextField(blank=True, null=True)
    ss_item_repeate = models.NullBooleanField()
    ss_sal_serial = models.NullBooleanField()
    ss_serial_issue = models.NullBooleanField()
    ss_serial_rec = models.NullBooleanField()
    ss_negative_balance = models.NullBooleanField()
    ss_add_itemstostores = models.NullBooleanField()
    ss_multiuseralarm = models.NullBooleanField()
    ss_salesqtycash = models.NullBooleanField()
    ss_salesqtycredit = models.NullBooleanField()
    ss_salesissue = models.NullBooleanField()
    ss_salesrqtycash = models.NullBooleanField()
    ss_salesrqtycredit = models.NullBooleanField()
    ss_printsalbutton = models.NullBooleanField()
    ss_printissbutton = models.NullBooleanField()
    ss_printpurbutton = models.NullBooleanField()
    ss_printrecbutton = models.NullBooleanField()
    ss_printtahwelbutton = models.NullBooleanField()
    ss_savesalbutton = models.NullBooleanField()
    ss_saveissbutton = models.NullBooleanField()
    ss_savepurbutton = models.NullBooleanField()
    ss_saverecbutton = models.NullBooleanField()
    ss_savetahwelbutton = models.NullBooleanField()
    ss_mcustname = models.NullBooleanField()
    ss_serial_pur = models.NullBooleanField()
    ss_serial_trans = models.NullBooleanField()
    ss_serial_adjust = models.NullBooleanField()
    companyname = models.CharField(max_length=100, blank=True, null=True)
    ss_x1 = models.IntegerField(blank=True, null=True)
    ss_x2 = models.IntegerField(blank=True, null=True)
    ss_x3 = models.NullBooleanField()
    ss_x4 = models.NullBooleanField()
    ss_x5 = models.NullBooleanField()
    ss_x6 = models.NullBooleanField()
    ss_x7 = models.NullBooleanField()
    ss_x8 = models.NullBooleanField()
    ss_x9 = models.NullBooleanField()
    ss_x10 = models.NullBooleanField()
    ss_x11 = models.NullBooleanField()
    ss_x12 = models.NullBooleanField()
    ss_x13 = models.NullBooleanField()
    ss_x14 = models.NullBooleanField()
    ss_x15 = models.NullBooleanField()
    ss_x16 = models.NullBooleanField()
    ss_x17 = models.NullBooleanField()
    ss_x18 = models.NullBooleanField()
    ss_x19 = models.NullBooleanField()
    ss_x20 = models.NullBooleanField()
    serial = models.BigIntegerField(blank=True, null=True)
    n1 = models.BigIntegerField(blank=True, null=True)
    n2 = models.BigIntegerField(blank=True, null=True)
    ss_x21 = models.NullBooleanField()
    ss_x22 = models.NullBooleanField()
    ss_x23 = models.NullBooleanField()
    ss_x24 = models.NullBooleanField()
    ss_x25 = models.NullBooleanField()
    ss_x26 = models.NullBooleanField()
    ss_x27 = models.NullBooleanField()
    ss_x28 = models.NullBooleanField()
    ss_x29 = models.NullBooleanField()
    ss_x30 = models.NullBooleanField()
    ss_x31 = models.NullBooleanField()
    ss_x32 = models.NullBooleanField()
    ss_x33 = models.NullBooleanField()
    ss_x34 = models.NullBooleanField()
    ss_x35 = models.NullBooleanField()
    ss_x36 = models.NullBooleanField()
    ss_x37 = models.NullBooleanField()
    ss_x38 = models.NullBooleanField()
    ss_x39 = models.NullBooleanField()
    ss_x40 = models.NullBooleanField()
    ss_x41 = models.NullBooleanField()
    ss_x42 = models.NullBooleanField()
    ss_x43 = models.NullBooleanField()
    ss_x44 = models.NullBooleanField()
    ss_x45 = models.NullBooleanField()
    ss_x46 = models.NullBooleanField()
    ss_x47 = models.NullBooleanField()
    ss_x48 = models.NullBooleanField()
    ss_x49 = models.NullBooleanField()
    ss_x50 = models.NullBooleanField()
    showpcsinsals = models.BigIntegerField(blank=True, null=True)
    showpcsinret = models.BigIntegerField(blank=True, null=True)
    companyname_e = models.CharField(max_length=200, blank=True, null=True)
    currency_name = models.CharField(max_length=30, blank=True, null=True)
    expirehandle = models.CharField(max_length=1, blank=True, null=True)
    dispensepolicy = models.CharField(max_length=1, blank=True, null=True)
    open_cashier = models.CharField(max_length=200, blank=True, null=True)
    price_format = models.CharField(max_length=200, blank=True, null=True)
    show_components = models.CharField(max_length=1, blank=True, null=True)
    clothes = models.CharField(max_length=1, blank=True, null=True)
    cash_round_way = models.BigIntegerField(blank=True, null=True)
    credt_round_way = models.BigIntegerField(blank=True, null=True)
    qty_format = models.CharField(max_length=50, blank=True, null=True)
    date_handle = models.NullBooleanField()
    agent_commission_type = models.NullBooleanField()
    itm_srch = models.NullBooleanField()
    get_price = models.NullBooleanField()
    alt_srch = models.NullBooleanField()
    credtlimitsrc = models.CharField(max_length=1, blank=True, null=True)
    edit_itemname = models.NullBooleanField()
    show_compprice = models.NullBooleanField()
    prodn_length = models.BigIntegerField(blank=True, null=True)
    jv_type = models.BigIntegerField(blank=True, null=True)
    jv_other = models.CharField(max_length=64, blank=True, null=True)
    rcv_type = models.BigIntegerField(blank=True, null=True)
    rcv_other = models.CharField(max_length=64, blank=True, null=True)
    csv_type = models.BigIntegerField(blank=True, null=True)
    csv_other = models.CharField(max_length=64, blank=True, null=True)
    ckv_type = models.BigIntegerField(blank=True, null=True)
    ckv_other = models.CharField(max_length=64, blank=True, null=True)
    bkv_type = models.BigIntegerField(blank=True, null=True)
    bkv_other = models.CharField(max_length=64, blank=True, null=True)
    csinv_type = models.BigIntegerField(blank=True, null=True)
    csinv_other = models.CharField(max_length=64, blank=True, null=True)
    crinv_type = models.BigIntegerField(blank=True, null=True)
    crinv_other = models.CharField(max_length=64, blank=True, null=True)
    ot_type = models.BigIntegerField(blank=True, null=True)
    ot_other = models.CharField(max_length=64, blank=True, null=True)
    multi_curr_jv = models.BigIntegerField(blank=True, null=True)
    brna_ar = models.CharField(max_length=100, blank=True, null=True)
    brna_en = models.CharField(max_length=100, blank=True, null=True)
    payinv_insarfcash = models.NullBooleanField()
    assets_acc_type = models.BigIntegerField(blank=True, null=True)
    stock_date = models.DateField(blank=True, null=True)
    equipment_type = models.CharField(max_length=25, blank=True, null=True)
    lwh_value = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    taxable = models.NullBooleanField()
    display_prcqtymsg = models.NullBooleanField()
    conv_format = models.CharField(max_length=30, blank=True, null=True)
    gerate_purinvoice = models.NullBooleanField()
    automatic_purinv = models.NullBooleanField()
    auto_inv_from_voucher = models.NullBooleanField()
    price_in_trans_sanad = models.NullBooleanField()
    rawabet = models.BigIntegerField(blank=True, null=True)
    compact_database = models.NullBooleanField()
    ss_printpaybutton = models.NullBooleanField()
    ss_printvpaybutton = models.NullBooleanField()
    ss_savepaybutton = models.NullBooleanField()
    ss_savevpaybutton = models.NullBooleanField()
    ss_smanconnecttocust = models.NullBooleanField()
    ss_quotanotestoitmnotes = models.NullBooleanField()
    ss_quotaitemspecialdis = models.NullBooleanField()
    display_salprcqtymsg = models.NullBooleanField()
    cost_way = models.NullBooleanField()
    dailydeletelog = models.NullBooleanField()
    ss_salmanpersalitem = models.NullBooleanField()
    ss_custfinansetperbranch = models.NullBooleanField()
    ss_jewellenablecomponentprice = models.NullBooleanField()
    ss_autoissvouprvunmatchitem = models.NullBooleanField()
    ss_purcolumnisrequired = models.NullBooleanField()
    currency_name_e = models.CharField(max_length=30, blank=True, null=True)
    ss_serial_purord = models.NullBooleanField()
    ss_controlpurinvqty = models.NullBooleanField()
    ss_show_serviceitem_cosr = models.NullBooleanField()
    ss_negative_balance_qty = models.NullBooleanField()
    ss_serial_matched = models.NullBooleanField()
    ss_smaninpurcahse = models.NullBooleanField()
    ss_showallunitsinpurchase = models.NullBooleanField()
    ss_devideobbalance = models.NullBooleanField()
    ss_disallowfuturedate = models.NullBooleanField()
    ss_seial_site_requision = models.NullBooleanField()
    ss_cashcust_csales = models.NullBooleanField()
    ss_salrtneffect = models.NullBooleanField()
    ss_sysdatetype = models.NullBooleanField()
    ss_reservation_level = models.NullBooleanField()
    ss_reserve_not_related_items = models.NullBooleanField()
    ss_show_equipment = models.NullBooleanField()
    ss_showitemlist_start = models.NullBooleanField()
    ss_edititmnminpricelist = models.NullBooleanField()
    ss_transfershowcomponent = models.NullBooleanField()
    ss_unitmappingforeachitem = models.NullBooleanField()
    ss_onecustomerperbranch = models.NullBooleanField()
    ss_cashcreditonecustomer = models.NullBooleanField()
    item_add_items = models.NullBooleanField()
    ss_disallowpurordreuse = models.NullBooleanField()
    ss_allowsavenegativeinv = models.NullBooleanField()
    ss_disallowdiscduplic = models.NullBooleanField()
    ss_allowitempriceoncurr = models.NullBooleanField()
    full_prodn = models.CharField(max_length=30, blank=True, null=True)
    empty_prodn = models.CharField(max_length=30, blank=True, null=True)
    from_prods = models.IntegerField(blank=True, null=True)
    printer_each_cat = models.NullBooleanField()
    pic_item_view = models.NullBooleanField()
    ss_default_prepare_time = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    serial_delivery_no = models.BigIntegerField(blank=True, null=True)
    ss_showbranchrelcrnoteonly = models.NullBooleanField()
    ss_serial_costupdate = models.NullBooleanField()
    ss_cablesize = models.NullBooleanField()
    invoice_from_purorder = models.NullBooleanField()
    notify_foriegn_purorder = models.NullBooleanField()
    iss_voucher_restrict = models.BigIntegerField(blank=True, null=True)
    is_textile = models.BigIntegerField(blank=True, null=True)
    return_item_status = models.BigIntegerField(blank=True, null=True)
    cust_phone_mandatory = models.BigIntegerField(blank=True, null=True)
    unuse_transfer_request = models.BigIntegerField(blank=True, null=True)
    continus_serials = models.BigIntegerField(blank=True, null=True)
    show_expirt_notification = models.BigIntegerField(blank=True, null=True)
    show_reorder_notification = models.BigIntegerField(blank=True, null=True)
    expirt_days = models.BigIntegerField(blank=True, null=True)
    eq_type = models.BigIntegerField(blank=True, null=True)
    dimen_def = models.BigIntegerField(blank=True, null=True)
    prvernt_direct_ci_printing = models.BigIntegerField(blank=True, null=True)
    default_payment_type = models.IntegerField(blank=True, null=True)
    use_formated_cr = models.NullBooleanField()
    return_default_payment_type = models.IntegerField(blank=True, null=True)
    reuse_credit_note = models.NullBooleanField()
    cust_phone_mandatory_cr = models.BigIntegerField(blank=True, null=True)
    discount_in_pur = models.NullBooleanField()
    use_account_item = models.NullBooleanField()
    mandatory_cc = models.NullBooleanField()
    pay_type = models.NullBooleanField()
    serial_at_sale = models.NullBooleanField()
    open_cashier_when_save = models.NullBooleanField()
    show_total_disc = models.NullBooleanField()
    can_issue_expired_items = models.NullBooleanField()
    add_sales_man_intrans = models.NullBooleanField()
    show_catalog_weight_alarm = models.NullBooleanField()
    lwh_affect_on_qty = models.NullBooleanField()
    keep_last_sman = models.NullBooleanField()
    use_customer_item_list = models.BigIntegerField(blank=True, null=True)
    school_db_name = models.CharField(max_length=50, blank=True, null=True)
    default_pur_payment_method = models.BigIntegerField(blank=True, null=True)
    use_payment_deduct = models.BigIntegerField(blank=True, null=True)
    use_supplier_sale_ratio = models.BigIntegerField(blank=True, null=True)
    use_supp_barcode_details = models.BigIntegerField(blank=True, null=True)
    lcd_type = models.IntegerField(blank=True, null=True)
    integrated_with_agility = models.IntegerField(blank=True, null=True)
    validate_cust_date_issue = models.IntegerField(blank=True, null=True)
    intgrated_w_balance = models.NullBooleanField()
    price_digits = models.IntegerField(blank=True, null=True)
    price_start_from = models.IntegerField(blank=True, null=True)
    pcode_digits = models.IntegerField(blank=True, null=True)
    pcode_start_from = models.IntegerField(blank=True, null=True)
    comm_itemcode = models.CharField(max_length=30, blank=True, null=True)
    allow_transdoublecheck = models.FloatField(blank=True, null=True)
    disable_triggers = models.IntegerField(blank=True, null=True)
    item_coding = models.IntegerField(blank=True, null=True)
    ss_negative_balance1 = models.FloatField(blank=True, null=True)
    change_itemname_inpurchase = models.IntegerField(blank=True, null=True)
    purchase_for_customer = models.NullBooleanField()
    use_pkt_no = models.NullBooleanField()
    allow_cust_po_exceed = models.FloatField(blank=True, null=True)
    last_ulter_date = models.DateField(blank=True, null=True)
    auto_serials = models.NullBooleanField()
    copy_cust_from_gl = models.NullBooleanField()
    inv_temp_id = models.FloatField(blank=True, null=True)
    tahwel_chng_prods = models.FloatField(blank=True, null=True)
    taw9eel_flg = models.FloatField(blank=True, null=True)
    fromcategory = models.FloatField(blank=True, null=True)
    tocategory = models.FloatField(blank=True, null=True)
    is_usedefaultprinter = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'settings'


class ShPurchases(models.Model):
    pur_id = models.BigIntegerField(primary_key=True)
    pur_date = models.DateField(blank=True, null=True)
    box_no = models.BigIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    kashier = models.CharField(max_length=20, blank=True, null=True)
    pcenter = models.BigIntegerField(blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)
    month = models.FloatField(blank=True, null=True)
    machine_id = models.FloatField(blank=True, null=True)
    sh_id = models.FloatField(blank=True, null=True)
    year_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sh_purchases'


class ShShareholders(models.Model):
    id = models.ForeignKey(Customers, db_column='id', primary_key=True)
    box_no = models.BigIntegerField()
    take_profit = models.CharField(max_length=1, blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    dod = models.DateField(blank=True, null=True)
    account_type = models.CharField(max_length=1, blank=True, null=True)
    bank_id = models.BigIntegerField(blank=True, null=True)
    job_id = models.CharField(max_length=20, blank=True, null=True)
    galsa_id = models.CharField(max_length=20, blank=True, null=True)
    shares = models.BigIntegerField(blank=True, null=True)
    sh_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sh_shareholders'


class ShShcomments(models.Model):
    sh_id = models.FloatField()
    comment_id = models.IntegerField()
    comment_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'sh_shcomments'
        unique_together = (('sh_id', 'comment_id', 'comment_date'),)


class ShTransactions(models.Model):
    tran_id = models.BigIntegerField()
    tran_type = models.CharField(max_length=20)
    tran_date = models.DateField(blank=True, null=True)
    sh_id = models.FloatField(blank=True, null=True)
    to_sh_id = models.FloatField(blank=True, null=True)
    shares = models.BigIntegerField(blank=True, null=True)
    galsa_id = models.CharField(max_length=20, blank=True, null=True)
    requestor = models.CharField(max_length=80, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sh_transactions'
        unique_together = (('tran_id', 'tran_type'),)


class Shifts(models.Model):
    code = models.IntegerField(primary_key=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    from_time = models.DateField(blank=True, null=True)
    to_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shifts'


class ShipmentMast(models.Model):
    shipment_no = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    custno = models.IntegerField(blank=True, null=True)
    open_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    carrier = models.CharField(max_length=20, blank=True, null=True)
    commission = models.FloatField()
    expenses1 = models.FloatField(blank=True, null=True)
    expenses2 = models.FloatField(blank=True, null=True)
    expenses3 = models.FloatField(blank=True, null=True)
    expenses4 = models.FloatField(blank=True, null=True)
    expenses3_detail = models.CharField(max_length=250, blank=True, null=True)
    expenses4_detail = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_mast'


class ShipmentRecieptXref(models.Model):
    shipment_no = models.IntegerField()
    code = models.IntegerField()
    pcenter = models.FloatField()
    bilno = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shipment_reciept_xref'
        unique_together = (('shipment_no', 'code', 'pcenter', 'bilno'),)


class ShmBlocks(models.Model):
    blk_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_e = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shm_blocks'


class ShmComments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    name_e = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shm_comments'


class ShmJobs(models.Model):
    job_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_e = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shm_jobs'


class Size(models.Model):
    sz_id = models.IntegerField(primary_key=True)
    sz_ardesc = models.CharField(max_length=50, blank=True, null=True)
    sz_latindesc = models.CharField(max_length=50, blank=True, null=True)
    sz_useddesc = models.NullBooleanField()
    sz_ardesc1 = models.CharField(max_length=50, blank=True, null=True)
    sz_latindesc1 = models.CharField(max_length=50, blank=True, null=True)
    sz_ardesc2 = models.CharField(max_length=50, blank=True, null=True)
    sz_latindesc2 = models.CharField(max_length=50, blank=True, null=True)
    sz_code = models.CharField(max_length=5, blank=True, null=True)
    size_cat = models.BigIntegerField(blank=True, null=True)
    reqsort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'size'


class SizeCat(models.Model):
    code = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_e = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'size_cat'


class SizeStandard(models.Model):
    ss_id = models.IntegerField(primary_key=True)
    ss_name = models.CharField(max_length=100, blank=True, null=True)
    ss_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'size_standard'


class SizeType(models.Model):
    siz_id = models.IntegerField(primary_key=True)
    siz_name = models.CharField(max_length=100, blank=True, null=True)
    siz_name_e = models.CharField(max_length=100, blank=True, null=True)
    siz_cat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'size_type'


class Sizee(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    name_e = models.CharField(max_length=50)
    sort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sizee'


class Store(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    accno = models.BigIntegerField(blank=True, null=True)
    name_e = models.CharField(max_length=40, blank=True, null=True)
    sales_man = models.ForeignKey('StoreMan', blank=True, null=True)
    address = models.CharField(max_length=90, blank=True, null=True)
    area = models.CharField(max_length=90, blank=True, null=True)
    sal_limit = models.DecimalField(max_digits=22, decimal_places=3, blank=True, null=True)
    trans_profit_accno = models.BigIntegerField(blank=True, null=True)
    cost_diff_accno = models.BigIntegerField(blank=True, null=True)
    store_balance_adjust_accno = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)
    cost_diff_accno_old = models.CharField(max_length=40, blank=True, null=True)
    trans_profit_accno_old = models.CharField(max_length=40, blank=True, null=True)
    store_balance_adjust_accno_old = models.CharField(max_length=40, blank=True, null=True)
    dif_exchange_voucher_accno = models.BigIntegerField(blank=True, null=True)
    dif_exchange_voucher_accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'


class StoreLocations(models.Model):
    prods_id = models.BigIntegerField()
    location_id = models.BigIntegerField()
    location_ar_desc = models.CharField(max_length=150, blank=True, null=True)
    location_en_desc = models.CharField(max_length=150, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_locations'
        unique_together = (('prods_id', 'location_id'),)


class StoreMan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name_ar = models.CharField(max_length=40, blank=True, null=True)
    name_en = models.CharField(max_length=40, blank=True, null=True)
    civil_id = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=90, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_man'


class StyleItemsSerial(models.Model):
    style_prodn = models.CharField(max_length=30)
    itemserial = models.BigIntegerField(blank=True, null=True)
    vendor = models.BigIntegerField()
    season = models.CharField(max_length=10)
    manf_year = models.IntegerField()
    trend = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'style_items_serial'
        unique_together = (('style_prodn', 'vendor', 'season', 'manf_year', 'trend'),)


class SupCat1(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=40)
    name_e = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup_cat1'


class SupCat2(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=40)
    name_e = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup_cat2'


class SupTaxes(models.Model):
    id = models.ForeignKey('Taxes', db_column='id')
    sup = models.ForeignKey('Suppliers')

    class Meta:
        managed = False
        db_table = 'sup_taxes'
        unique_together = (('id', 'sup_id'),)


class SupplierBarcodeSections(models.Model):
    id = models.BigIntegerField()
    supplier = models.ForeignKey('Suppliers')
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    sec_size = models.BigIntegerField(blank=True, null=True)
    sec_options = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_barcode_sections'
        unique_together = (('id', 'supplier_id'),)


class SupplierBarcodeSectionsDeta(models.Model):
    id = models.BigIntegerField()
    header_id = models.BigIntegerField()
    supplier_id = models.BigIntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_barcode_sections_deta'
        unique_together = (('id', 'header_id', 'supplier_id'),)


class SupplierStores(models.Model):
    id = models.BigIntegerField()
    supplier = models.ForeignKey('Suppliers')
    store_id = models.BigIntegerField()
    store_type = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'supplier_stores'
        unique_together = (('id', 'supplier_id', 'store_id'),)


class Suppliers(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    cat1 = models.FloatField(blank=True, null=True)
    cat2 = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    tel1 = models.CharField(max_length=100, blank=True, null=True)
    tel2 = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    credit_days = models.FloatField(blank=True, null=True)
    accno = models.BigIntegerField(blank=True, null=True)
    name_e = models.CharField(max_length=150, blank=True, null=True)
    id = models.FloatField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    home_page = models.CharField(max_length=100, blank=True, null=True)
    temp1 = models.FloatField(blank=True, null=True)
    temp2 = models.FloatField(blank=True, null=True)
    op_balance = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    cost_center = models.FloatField(blank=True, null=True)
    sale_commission_ratio = models.FloatField(blank=True, null=True)
    account_id = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)
    items_code = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class SyApplication(models.Model):
    app_cd = models.CharField(primary_key=True, max_length=20)
    app_name_a = models.CharField(max_length=100, blank=True, null=True)
    app_name_e = models.CharField(max_length=100, blank=True, null=True)
    opt_cnt = models.IntegerField(blank=True, null=True)
    opt1_label = models.CharField(max_length=100, blank=True, null=True)
    opt2_label = models.CharField(max_length=100, blank=True, null=True)
    opt3_label = models.CharField(max_length=100, blank=True, null=True)
    opt4_label = models.CharField(max_length=100, blank=True, null=True)
    opt5_label = models.CharField(max_length=100, blank=True, null=True)
    opt6_label = models.CharField(max_length=100, blank=True, null=True)
    opt7_label = models.CharField(max_length=100, blank=True, null=True)
    opt8_label = models.CharField(max_length=100, blank=True, null=True)
    opt9_label = models.CharField(max_length=100, blank=True, null=True)
    opt10_label = models.CharField(max_length=100, blank=True, null=True)
    opt11_label = models.CharField(max_length=100, blank=True, null=True)
    opt12_label = models.CharField(max_length=100, blank=True, null=True)
    app_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_application'


class SyLog(models.Model):
    trn_code = models.DecimalField(primary_key=True, max_digits=20, decimal_places=5)
    trn_type = models.CharField(max_length=1, blank=True, null=True)
    m_code = models.IntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    menu_objectid = models.ForeignKey('SyObjects', db_column='menu_objectid', blank=True, null=True)
    user_objectid = models.ForeignKey('SyObjects', db_column='user_objectid', blank=True, null=True)
    user_name = models.CharField(max_length=16, blank=True, null=True)
    app_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_log'


class SyLogcolumns(models.Model):
    trn_code = models.DecimalField(max_digits=20, decimal_places=5)
    serial = models.IntegerField()
    column_name = models.CharField(max_length=100, blank=True, null=True)
    db_name = models.CharField(max_length=100, blank=True, null=True)
    column_desc = models.CharField(max_length=100, blank=True, null=True)
    iskey = models.CharField(max_length=1, blank=True, null=True)
    old_value = models.CharField(max_length=100, blank=True, null=True)
    new_value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_logcolumns'
        unique_together = (('trn_code', 'serial'),)


class SyMenu(models.Model):
    app_cd = models.CharField(max_length=20)
    m_code = models.IntegerField()
    m_name_a = models.CharField(max_length=150, blank=True, null=True)
    m_name_e = models.CharField(max_length=150, blank=True, null=True)
    link_name = models.CharField(max_length=150, blank=True, null=True)
    m_type = models.CharField(max_length=1, blank=True, null=True)
    item_level = models.IntegerField(blank=True, null=True)
    item_sort = models.CharField(max_length=100, blank=True, null=True)
    window_name_a = models.CharField(max_length=100, blank=True, null=True)
    window_name_e = models.CharField(max_length=100, blank=True, null=True)
    ret_win_a = models.CharField(max_length=100, blank=True, null=True)
    ret_win_e = models.CharField(max_length=100, blank=True, null=True)
    sel_opt1 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt2 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt3 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt4 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt5 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt6 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt7 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt8 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt9 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt10 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt11 = models.CharField(max_length=1, blank=True, null=True)
    sel_opt12 = models.CharField(max_length=1, blank=True, null=True)
    opt1 = models.CharField(max_length=100, blank=True, null=True)
    opt2 = models.CharField(max_length=100, blank=True, null=True)
    opt3 = models.CharField(max_length=100, blank=True, null=True)
    opt4 = models.CharField(max_length=100, blank=True, null=True)
    opt5 = models.CharField(max_length=100, blank=True, null=True)
    opt6 = models.CharField(max_length=100, blank=True, null=True)
    opt7 = models.CharField(max_length=100, blank=True, null=True)
    opt8 = models.CharField(max_length=100, blank=True, null=True)
    opt9 = models.CharField(max_length=100, blank=True, null=True)
    opt10 = models.CharField(max_length=100, blank=True, null=True)
    opt11 = models.CharField(max_length=100, blank=True, null=True)
    opt12 = models.CharField(max_length=100, blank=True, null=True)
    parent_m_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_menu'
        unique_together = (('app_cd', 'm_code'),)


class SyObType(models.Model):
    id = models.FloatField(primary_key=True)
    parent_ob_type = models.CharField(max_length=150, blank=True, null=True)
    ob_type = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_ob_type'


class SyObTypeRelations(models.Model):
    type1 = models.CharField(max_length=150)
    type2 = models.CharField(max_length=150)
    h_addnew = models.CharField(max_length=1, blank=True, null=True)
    h_del = models.CharField(max_length=1, blank=True, null=True)
    h_print = models.CharField(max_length=1, blank=True, null=True)
    h_retrieve = models.CharField(max_length=1, blank=True, null=True)
    h_save = models.CharField(max_length=1, blank=True, null=True)
    h_opt = models.CharField(max_length=150, blank=True, null=True)
    title_a = models.CharField(max_length=250, blank=True, null=True)
    title_e = models.CharField(max_length=250, blank=True, null=True)
    h_expexcel = models.CharField(max_length=1, blank=True, null=True)
    h_post = models.CharField(max_length=1, blank=True, null=True)
    h_unpost = models.CharField(max_length=1, blank=True, null=True)
    h_filter = models.CharField(max_length=1, blank=True, null=True)
    h_sort = models.CharField(max_length=1, blank=True, null=True)
    h_prop = models.CharField(max_length=1, blank=True, null=True)
    h_chgcurrency = models.CharField(max_length=1, blank=True, null=True)
    h_reportedit = models.CharField(max_length=1, blank=True, null=True)
    h_find = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_ob_type_relations'
        unique_together = (('type1', 'type2'),)


class SyObjects(models.Model):
    objectid = models.CharField(primary_key=True, max_length=100)
    parentobjectid = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    name_a = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    obj_type = models.CharField(max_length=150, blank=True, null=True)
    subtype = models.CharField(max_length=50, blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    isactive = models.CharField(max_length=1, blank=True, null=True)
    item_level = models.BigIntegerField(blank=True, null=True)
    item_sort = models.CharField(max_length=100, blank=True, null=True)
    user_pwd = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    dataobject = models.CharField(max_length=500, blank=True, null=True)
    dataobjecttype = models.CharField(max_length=50, blank=True, null=True)
    pfc_userid = models.CharField(max_length=100, blank=True, null=True)
    ob_type_cd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_objects'


class SyObjectsCopy(models.Model):
    objectid = models.CharField(unique=True, max_length=100)
    parentobjectid = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    name_a = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    obj_type = models.CharField(max_length=150, blank=True, null=True)
    subtype = models.CharField(max_length=50, blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    isactive = models.CharField(max_length=1, blank=True, null=True)
    item_level = models.BigIntegerField(blank=True, null=True)
    item_sort = models.CharField(max_length=100, blank=True, null=True)
    user_pwd = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    dataobject = models.CharField(max_length=500, blank=True, null=True)
    dataobjecttype = models.CharField(max_length=50, blank=True, null=True)
    pfc_userid = models.CharField(max_length=100, blank=True, null=True)
    ob_type_cd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_objects_copy'


class SyRelations(models.Model):
    objectid = models.ForeignKey(SyObjects, db_column='objectid')
    relatedobjectid = models.CharField(max_length=100)
    retrieve = models.CharField(max_length=1, blank=True, null=True)
    addnew = models.CharField(max_length=1, blank=True, null=True)
    save = models.CharField(max_length=1, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=1, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    print_field = models.CharField(db_column='print', max_length=1, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    sel_opt = models.CharField(max_length=1, blank=True, null=True)
    opt = models.CharField(max_length=500, blank=True, null=True)
    temp = models.CharField(max_length=150, blank=True, null=True)
    relatedobjectid2 = models.CharField(max_length=100, blank=True, null=True)
    expexcel = models.CharField(max_length=1, blank=True, null=True)
    post = models.CharField(max_length=1, blank=True, null=True)
    unpost = models.CharField(max_length=1, blank=True, null=True)
    filter = models.CharField(max_length=1, blank=True, null=True)
    sort = models.CharField(max_length=1, blank=True, null=True)
    prop = models.CharField(max_length=1, blank=True, null=True)
    reportedit = models.CharField(max_length=1, blank=True, null=True)
    chgcurrency = models.CharField(max_length=1, blank=True, null=True)
    find = models.CharField(max_length=1, blank=True, null=True)
    properties = models.CharField(max_length=1, blank=True, null=True)
    code = models.CharField(max_length=100)
    parm_value = models.CharField(max_length=100)
    parm_code = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sy_relations'
        unique_together = (('objectid', 'relatedobjectid', 'code', 'parm_value', 'parm_code'),)


class SyRelationsTemp(models.Model):
    objectid = models.CharField(max_length=100, blank=True, null=True)
    relatedobjectid = models.CharField(max_length=100, blank=True, null=True)
    retrieve = models.CharField(max_length=1, blank=True, null=True)
    addnew = models.CharField(max_length=1, blank=True, null=True)
    save = models.CharField(max_length=1, blank=True, null=True)
    del_field = models.CharField(db_column='del', max_length=1, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    print_field = models.CharField(db_column='print', max_length=1, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    sel_opt = models.CharField(max_length=1, blank=True, null=True)
    opt = models.CharField(max_length=500, blank=True, null=True)
    temp = models.CharField(max_length=150, blank=True, null=True)
    relatedobjectid2 = models.CharField(max_length=100, blank=True, null=True)
    expexcel = models.CharField(max_length=1, blank=True, null=True)
    post = models.CharField(max_length=1, blank=True, null=True)
    unpost = models.CharField(max_length=1, blank=True, null=True)
    filter = models.CharField(max_length=1, blank=True, null=True)
    sort = models.CharField(max_length=1, blank=True, null=True)
    prop = models.CharField(max_length=1, blank=True, null=True)
    reportedit = models.CharField(max_length=1, blank=True, null=True)
    chgcurrency = models.CharField(max_length=1, blank=True, null=True)
    find = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_relations_temp'


class SyUserrights(models.Model):
    user_name = models.CharField(max_length=16)
    app_cd = models.CharField(max_length=20)
    m_code = models.IntegerField()
    ret = models.CharField(max_length=1, blank=True, null=True)
    addition = models.CharField(max_length=1, blank=True, null=True)
    saving = models.CharField(max_length=1, blank=True, null=True)
    deletion = models.CharField(max_length=1, blank=True, null=True)
    printing = models.CharField(max_length=1, blank=True, null=True)
    posting = models.CharField(max_length=1, blank=True, null=True)
    unposting = models.CharField(max_length=1, blank=True, null=True)
    check_printing = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sy_userrights'
        unique_together = (('user_name', 'app_cd', 'm_code'),)


class SynchTab(models.Model):
    disable_triggers = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'synch_tab'


class SysDate(models.Model):
    application_date = models.DateField(primary_key=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_date'


class Systable(models.Model):
    table_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'systable'


class TabAccountItem(models.Model):
    account_item_code = models.BigIntegerField(primary_key=True)
    account_item_name = models.CharField(max_length=100, blank=True, null=True)
    account_item_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tab_account_item'


class Table1(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=3)
    co_name = models.CharField(max_length=100, blank=True, null=True)
    connect_string = models.CharField(max_length=100, blank=True, null=True)
    program_id = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dbtype = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table1'


class Table2(models.Model):
    users_cnt = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'table_2'


class Tables(models.Model):
    id = models.BigIntegerField(primary_key=True)
    table_no = models.CharField(max_length=20, blank=True, null=True)
    table_type_id = models.BigIntegerField(blank=True, null=True)
    section_id = models.BigIntegerField(blank=True, null=True)
    x_pos = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    y_pos = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    state = models.NullBooleanField()
    centerid = models.BigIntegerField(blank=True, null=True)
    current_code = models.IntegerField(blank=True, null=True)
    current_pcenter = models.BigIntegerField(blank=True, null=True)
    current_bilno = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tables'


class Taxes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    percent = models.DecimalField(max_digits=5, decimal_places=3)
    accno = models.CharField(max_length=14, blank=True, null=True)
    app_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxes'


class Temp(models.Model):
    prodn = models.CharField(primary_key=True, max_length=25)
    s = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'


class Test(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Themes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    thm_name = models.CharField(max_length=50, blank=True, null=True)
    object = models.CharField(max_length=50, blank=True, null=True)
    property = models.CharField(max_length=50, blank=True, null=True)
    thm_value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'themes'


class Todolist(models.Model):
    id = models.DecimalField(max_digits=20, decimal_places=5)
    nam = models.TextField(blank=True, null=True)
    flage = models.IntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'todolist'
        unique_together = (('id', 'user_id'),)


class Trans1(models.Model):
    batch = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    reset = models.DecimalField(max_digits=20, decimal_places=5)
    sr = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    name_to = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    chek = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.DecimalField(max_digits=20, decimal_places=5)
    user_no = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    chek_flage = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    bank = models.CharField(max_length=35, blank=True, null=True)
    temp1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    temp2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans1'
        unique_together = (('reset', 'reset_id', 'branch'),)


class Trans2(models.Model):
    id = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    accno = models.BigIntegerField()
    cost1 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    credit = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    details = models.CharField(max_length=150, blank=True, null=True)
    reset = models.DecimalField(max_digits=20, decimal_places=5)
    reset_id = models.DecimalField(max_digits=20, decimal_places=5)
    cost2 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost3 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    cost4 = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    chek = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
    chek_date = models.DateField(blank=True, null=True)
    branch = models.DecimalField(max_digits=20, decimal_places=5)
    payed = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans2'
        unique_together = (('reset', 'reset_id', 'branch', 'accno'),)


class TransCableSerials(models.Model):
    prodn = models.CharField(max_length=30)
    id = models.BigIntegerField()
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    batchno = models.CharField(max_length=20)
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    no_of_ctn = models.BigIntegerField(blank=True, null=True)
    no_of_ctn_used = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_cable_serials'
        unique_together = (('prodn', 'id', 'code', 'pcenter', 'bilno', 'batchno'),)


class TransCash(models.Model):
    code = models.IntegerField()
    pcenter = models.IntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    paymnet = models.BigIntegerField()
    cat = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_cash'
        unique_together = (('code', 'pcenter', 'paymnet'),)


class TransCost(models.Model):
    pcenter = models.BigIntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    cost_center = models.BigIntegerField()
    code = models.BigIntegerField()
    cat = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_cost'
        unique_together = (('code', 'pcenter', 'cost_center'),)


class TransDepr(models.Model):
    code = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    stor = models.BigIntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    cat = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_depr'
        unique_together = (('code', 'pcenter', 'stor'),)


class TransOptions(models.Model):
    trans_type = models.BigIntegerField(primary_key=True)
    trans_checked = models.BigIntegerField(blank=True, null=True)
    sales_cost_center = models.BigIntegerField(blank=True, null=True)
    trans_resettype = models.BigIntegerField(blank=True, null=True)
    trans_acc_db = models.CharField(max_length=25, blank=True, null=True)
    trans_cat_level = models.BigIntegerField(blank=True, null=True)
    trans_cost_resettype = models.BigIntegerField(blank=True, null=True)
    brn_sals = models.BigIntegerField(blank=True, null=True)
    post_flage = models.BigIntegerField(blank=True, null=True)
    paytp_cash = models.BigIntegerField(blank=True, null=True)
    paytp_credit = models.BigIntegerField(blank=True, null=True)
    saldicaccno = models.BigIntegerField(blank=True, null=True)
    bnkcommaccno = models.BigIntegerField(blank=True, null=True)
    credtsaldisc = models.BigIntegerField(blank=True, null=True)
    cashbox = models.NullBooleanField()
    custdebt_accno = models.BigIntegerField(blank=True, null=True)
    custcredt_accno = models.BigIntegerField(blank=True, null=True)
    rec_disc = models.BigIntegerField(blank=True, null=True)
    pay_disc = models.BigIntegerField(blank=True, null=True)
    sales_net = models.NullBooleanField()
    post_salescost = models.NullBooleanField()
    post_salescost_level = models.NullBooleanField()
    lc_expenses_cash = models.BigIntegerField(blank=True, null=True)
    sales_status = models.NullBooleanField()
    sales_date = models.NullBooleanField()
    pur_showsuppinv = models.NullBooleanField()
    sal_showsalmanname = models.NullBooleanField()
    add_jop_no = models.CharField(max_length=1, blank=True, null=True)
    add_expenses_cash = models.BigIntegerField(blank=True, null=True)
    lc_expenses_cash_option = models.NullBooleanField()
    cat_posting_detailed_voucher = models.NullBooleanField()
    purchase_expensis = models.BigIntegerField(blank=True, null=True)
    renttanks_accno = models.CharField(max_length=14, blank=True, null=True)
    aqua_tanks_reset_type = models.BigIntegerField(blank=True, null=True)
    to_reservsales_postingway = models.BigIntegerField(blank=True, null=True)
    show_voucher_notes = models.NullBooleanField()
    round_accno = models.BigIntegerField(blank=True, null=True)
    post_pur_by_gross = models.NullBooleanField()
    saldicaccno_old = models.CharField(max_length=40, blank=True, null=True)
    credtsaldisc_old = models.CharField(max_length=40, blank=True, null=True)
    bnkcommaccno_old = models.CharField(max_length=40, blank=True, null=True)
    custdebt_accno_old = models.CharField(max_length=40, blank=True, null=True)
    custcredt_accno_old = models.CharField(max_length=40, blank=True, null=True)
    rec_disc_old = models.CharField(max_length=40, blank=True, null=True)
    pay_disc_old = models.CharField(max_length=40, blank=True, null=True)
    lc_expenses_cash_old = models.CharField(max_length=40, blank=True, null=True)
    add_expenses_cash_old = models.CharField(max_length=40, blank=True, null=True)
    purchase_expensis_old = models.CharField(max_length=40, blank=True, null=True)
    round_accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_options'


class TransSales(models.Model):
    code = models.IntegerField()
    pcenter = models.IntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    paymnet = models.BigIntegerField()
    cat = models.BigIntegerField(blank=True, null=True)
    cost_center = models.BigIntegerField(blank=True, null=True)
    damage_accno = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)
    damage_accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_sales'


class TransSerialno(models.Model):
    id = models.BigIntegerField()
    prodn = models.CharField(max_length=20, blank=True, null=True)
    code = models.IntegerField()
    pcenter = models.ForeignKey(Centers, db_column='pcenter')
    bilno = models.BigIntegerField()
    serial_no = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'trans_serialno'
        unique_together = (('id', 'code', 'pcenter', 'bilno', 'serial_no'),)


class TransSmanaccs(models.Model):
    sman_id = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    accno = models.BigIntegerField(blank=True, null=True)
    accno_old = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_smanaccs'
        unique_together = (('sman_id', 'pcenter'),)


class Trend(models.Model):
    tr_id = models.IntegerField(primary_key=True)
    tr_name = models.CharField(max_length=100, blank=True, null=True)
    tr_name_e = models.CharField(max_length=20, blank=True, null=True)
    br_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trend'


class Trn(models.Model):
    pcenter = models.BigIntegerField(blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    vtime = models.DateTimeField(blank=True, null=True)
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    com_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trn'


class TrnLine(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    pcenter = models.BigIntegerField(blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    vtime = models.DateTimeField(blank=True, null=True)
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    com_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trn_line'


class TrnLine2(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    pcenter = models.BigIntegerField(blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    bilno = models.BigIntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    vtime = models.DateTimeField(blank=True, null=True)
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    com_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trn_line2'


class TtA(models.Model):
    code = models.IntegerField()
    bilno = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    vdate = models.DateField(blank=True, null=True)
    p_vdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_a'


class TtAdavg(models.Model):
    bilno = models.BigIntegerField(blank=True, null=True)
    pcenter = models.BigIntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    price = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    vtime = models.DateField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    move = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    prods = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    temp_price = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    avg_cost = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    avg_cost2 = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    com_qty = models.FloatField(blank=True, null=True)
    sort_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_adavg'


class TtAvgQ(models.Model):
    prods = models.FloatField()
    prodn = models.CharField(max_length=30)
    vdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_avg_q'


class TtB(models.Model):
    code = models.IntegerField()
    bilno = models.BigIntegerField()
    pcenter = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tt_b'


class TtCoupontypes(models.Model):
    type_id = models.FloatField(blank=True, null=True)
    coupon_id = models.FloatField()
    from_no = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    to_no = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    isactive = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_coupontypes'


class TtCoupontypesT(models.Model):
    code = models.IntegerField()
    vdate = models.DateField(blank=True, null=True)
    bilno = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    coupontypes_id = models.FloatField(blank=True, null=True)
    coupontypes_no = models.FloatField(blank=True, null=True)
    discount_c = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_coupontypes_t'


class TtIssueTree(models.Model):
    pcenter = models.BigIntegerField()
    code = models.IntegerField()
    bilno = models.BigIntegerField()
    id = models.BigIntegerField()
    kit_no = models.BigIntegerField(blank=True, null=True)
    originparentid = models.BigIntegerField(blank=True, null=True)
    non_invent = models.NullBooleanField()
    qty = models.FloatField(blank=True, null=True)
    conv = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    conv2 = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    item_cost = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    disc2 = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    item_level = models.IntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    prods = models.BigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    price1 = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    total = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    total1 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    disc21 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    udisc = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    udisc1 = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_issue_tree'


class TtItemsTempQ(models.Model):
    prodn = models.CharField(max_length=30, blank=True, null=True)
    prods = models.IntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    vdate = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_items_temp_q'


class TtPpp(models.Model):
    total = models.FloatField(blank=True, null=True)
    pcenter = models.BigIntegerField()
    bilno = models.BigIntegerField()
    code = models.IntegerField()
    prod_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_ppp'


class TtRec2(models.Model):
    bilno = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    code = models.IntegerField()
    id = models.BigIntegerField()
    qty = models.DecimalField(max_digits=38, decimal_places=18, blank=True, null=True)
    conv = models.FloatField(blank=True, null=True)
    item_cost = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    related_code = models.FloatField(blank=True, null=True)
    related_billno = models.FloatField(blank=True, null=True)
    related_branch = models.FloatField(blank=True, null=True)
    related_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_rec2'


class TtReciept1Lc(models.Model):
    bilno = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    code = models.IntegerField()
    lc_p = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_reciept_1_lc'


class TtReciept2Lc(models.Model):
    prod_cost = models.FloatField(blank=True, null=True)
    code = models.IntegerField()
    bilno = models.BigIntegerField()
    pcenter = models.BigIntegerField()
    id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tt_reciept_2_lc'


class TtT(models.Model):
    prodn = models.CharField(max_length=30, blank=True, null=True)
    prodn1 = models.CharField(max_length=30, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    item_sort = models.CharField(max_length=2000, blank=True, null=True)
    item_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_t'


class TtT1(models.Model):
    objectid = models.CharField(max_length=100, blank=True, null=True)
    parentobjectid = models.CharField(max_length=100, blank=True, null=True)
    name_a = models.CharField(max_length=100, blank=True, null=True)
    name_e = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    parm_code = models.CharField(max_length=100, blank=True, null=True)
    parm_value = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_t1'


class TtT2(models.Model):
    objectid = models.CharField(max_length=100, blank=True, null=True)
    name_a = models.CharField(max_length=100, blank=True, null=True)
    oid = models.CharField(max_length=100)
    code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_t2'


class TtTurnover(models.Model):
    prodn = models.CharField(max_length=30)
    prodname = models.CharField(max_length=200, blank=True, null=True)
    prods = models.BigIntegerField()
    avrg_inv_cost = models.FloatField(blank=True, null=True)
    begin_bal = models.FloatField(blank=True, null=True)
    end_bal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_turnover'


class TtU(models.Model):
    unit1 = models.BigIntegerField()
    unit2 = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField()
    isused = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_u'


class TtUserinfo(models.Model):
    userid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tt_userinfo'


class Types(models.Model):
    ty_id = models.IntegerField(primary_key=True)
    ty_name = models.CharField(max_length=100, blank=True, null=True)
    ty_name_e = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class UnitMapping(models.Model):
    unit1 = models.BigIntegerField()
    unit2 = models.BigIntegerField()
    conv = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unit_mapping'
        unique_together = (('unit1', 'unit2'),)


class UserAccounts(models.Model):
    user_no = models.IntegerField()
    account_no = models.ForeignKey(Guide, db_column='account_no')
    acc_tp = models.CharField(max_length=1, blank=True, null=True)
    acc_lvl = models.IntegerField(blank=True, null=True)
    view_acc = models.NullBooleanField()
    trans_acc = models.NullBooleanField()
    print_acc = models.NullBooleanField()
    edit_acc = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'user_accounts'
        unique_together = (('user_no', 'account_no'),)


class UserAllowedItems(models.Model):
    id = models.IntegerField()
    item_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user_allowed_items'
        unique_together = (('id', 'item_id'),)


class UserBranches(models.Model):
    id = models.ForeignKey('Users', db_column='id')
    cen = models.ForeignKey(Centers)

    class Meta:
        managed = False
        db_table = 'user_branches'
        unique_together = (('id', 'cen_id'),)


class UserCat1Rights(models.Model):
    user_id = models.BigIntegerField()
    cat1_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_cat1_rights'
        unique_together = (('user_id', 'cat1_id'),)


class UserEntity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.CharField(max_length=100, blank=True, null=True)
    entity_type = models.CharField(max_length=100, blank=True, null=True)
    entity_id = models.IntegerField(blank=True, null=True)
    status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'user_entity'


class UserForbidenItems(models.Model):
    id = models.IntegerField()
    item_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user_forbiden_items'
        unique_together = (('id', 'item_id'),)


class UserGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    us_super = models.NullBooleanField()
    us_mod = models.NullBooleanField()
    us_del = models.NullBooleanField()
    us_sup = models.NullBooleanField()
    us_cust = models.NullBooleanField()
    us_prod = models.NullBooleanField()
    us_sman = models.NullBooleanField()
    us_catprod = models.NullBooleanField()
    us_catcust = models.NullBooleanField()
    us_catsup = models.NullBooleanField()
    us_store = models.NullBooleanField()
    us_pcenter = models.ForeignKey(Centers, db_column='us_pcenter', blank=True, null=True)
    us_units = models.NullBooleanField()
    us_cunt = models.NullBooleanField()
    us_paymnet = models.NullBooleanField()
    us_currancy = models.NullBooleanField()
    us_name = models.CharField(max_length=50, blank=True, null=True)
    us_pass = models.CharField(max_length=20, blank=True, null=True)
    us_system1 = models.NullBooleanField()
    us_system2 = models.NullBooleanField()
    us_ystem3 = models.NullBooleanField()
    us_system4 = models.NullBooleanField()
    us_system5 = models.NullBooleanField()
    us_system6 = models.NullBooleanField()
    us_syetem7 = models.NullBooleanField()
    us_system8 = models.NullBooleanField()
    us_system9 = models.NullBooleanField()
    us_system10 = models.NullBooleanField()
    us_cost = models.NullBooleanField()
    us_date_controll = models.NullBooleanField()
    us_w_change_date = models.NullBooleanField()
    us_onlyonecenter = models.NullBooleanField()
    us_centerno = models.BigIntegerField(blank=True, null=True)
    us_salpricecontroll = models.BigIntegerField(blank=True, null=True)
    us_sal = models.NullBooleanField()
    us_salr = models.NullBooleanField()
    us_qua = models.NullBooleanField()
    us_sal_mod = models.NullBooleanField()
    us_salr_mod = models.NullBooleanField()
    us_qua_mod = models.NullBooleanField()
    us_iss = models.NullBooleanField()
    us_issgift = models.NullBooleanField()
    us_dest = models.NullBooleanField()
    us_iss_mod = models.NullBooleanField()
    us_issgift_mod = models.NullBooleanField()
    us_dest_mod = models.NullBooleanField()
    us_creditlimit = models.NullBooleanField()
    us_discperitemcontroll = models.NullBooleanField()
    us_discountcontroll = models.NullBooleanField()
    us_pur = models.NullBooleanField()
    us_pur_mod = models.NullBooleanField()
    us_rec = models.NullBooleanField()
    us_rec_mod = models.NullBooleanField()
    us_purorder = models.NullBooleanField()
    us_pur_order_mod = models.NullBooleanField()
    us_adjust = models.NullBooleanField()
    us_adjust_mod = models.NullBooleanField()
    us_trans = models.NullBooleanField()
    us_trans_mod = models.NullBooleanField()
    us_lc = models.NullBooleanField()
    us_ob = models.NullBooleanField()
    us_x1 = models.NullBooleanField()
    us_x2 = models.NullBooleanField()
    us_x3 = models.NullBooleanField()
    us_x4 = models.NullBooleanField()
    us_x5 = models.NullBooleanField()
    us_x6 = models.NullBooleanField()
    us_x7 = models.NullBooleanField()
    us_x8 = models.NullBooleanField()
    us_x9 = models.NullBooleanField()
    us_x10 = models.NullBooleanField()
    us_x11 = models.NullBooleanField()
    us_x12 = models.NullBooleanField()
    us_x13 = models.NullBooleanField()
    us_x14 = models.NullBooleanField()
    us_x15 = models.NullBooleanField()
    us_x16 = models.NullBooleanField()
    us_x17 = models.NullBooleanField()
    us_x18 = models.NullBooleanField()
    us_x19 = models.NullBooleanField()
    us_x20 = models.NullBooleanField()
    us_x21 = models.NullBooleanField()
    us_x22 = models.NullBooleanField()
    us_x23 = models.NullBooleanField()
    us_x24 = models.NullBooleanField()
    us_x25 = models.NullBooleanField()
    us_x26 = models.NullBooleanField()
    us_x27 = models.NullBooleanField()
    us_x28 = models.NullBooleanField()
    us_x29 = models.NullBooleanField()
    us_x30 = models.NullBooleanField()
    us_x31 = models.NullBooleanField()
    us_x32 = models.NullBooleanField()
    us_x33 = models.NullBooleanField()
    us_x34 = models.NullBooleanField()
    us_x35 = models.NullBooleanField()
    us_x36 = models.NullBooleanField()
    us_x37 = models.NullBooleanField()
    us_x38 = models.NullBooleanField()
    us_x39 = models.NullBooleanField()
    us_x40 = models.NullBooleanField()
    us_x41 = models.NullBooleanField()
    us_x42 = models.NullBooleanField()
    us_x43 = models.NullBooleanField()
    us_x44 = models.NullBooleanField()
    us_x45 = models.NullBooleanField()
    us_x46 = models.NullBooleanField()
    us_x47 = models.NullBooleanField()
    us_x48 = models.NullBooleanField()
    us_x49 = models.NullBooleanField()
    us_x50 = models.NullBooleanField()
    cp_stotrtrans = models.BigIntegerField(blank=True, null=True)
    overrideminprice = models.BigIntegerField(blank=True, null=True)
    ini_screen = models.BigIntegerField(blank=True, null=True)
    ispointofsale = models.CharField(max_length=1, blank=True, null=True)
    voucher_type_d = models.CharField(max_length=1, blank=True, null=True)
    voucher_type_e = models.CharField(max_length=1, blank=True, null=True)
    qutation_no_d = models.CharField(max_length=1, blank=True, null=True)
    qutation_no_e = models.CharField(max_length=1, blank=True, null=True)
    pur_order_d = models.CharField(max_length=1, blank=True, null=True)
    pur_order_e = models.CharField(max_length=1, blank=True, null=True)
    cust_name_e = models.CharField(max_length=1, blank=True, null=True)
    address_d = models.CharField(max_length=1, blank=True, null=True)
    address_e = models.CharField(max_length=1, blank=True, null=True)
    reserv_d = models.CharField(max_length=1, blank=True, null=True)
    reserv_e = models.CharField(max_length=1, blank=True, null=True)
    delivery_date_d = models.CharField(max_length=1, blank=True, null=True)
    delivery_date_e = models.CharField(max_length=1, blank=True, null=True)
    closed_d = models.CharField(max_length=1, blank=True, null=True)
    closed_e = models.CharField(max_length=1, blank=True, null=True)
    payment_d = models.CharField(max_length=1, blank=True, null=True)
    payment_e = models.CharField(max_length=1, blank=True, null=True)
    store_e = models.CharField(max_length=1, blank=True, null=True)
    unit_d = models.CharField(max_length=1, blank=True, null=True)
    unit_e = models.CharField(max_length=1, blank=True, null=True)
    pack_d = models.CharField(max_length=1, blank=True, null=True)
    pack_e = models.CharField(max_length=1, blank=True, null=True)
    qty_e = models.CharField(max_length=1, blank=True, null=True)
    price_e = models.CharField(max_length=1, blank=True, null=True)
    disc_d = models.CharField(max_length=1, blank=True, null=True)
    disc_e = models.CharField(max_length=1, blank=True, null=True)
    discp_d = models.CharField(max_length=1, blank=True, null=True)
    discp_e = models.CharField(max_length=1, blank=True, null=True)
    discountp_d = models.CharField(max_length=1, blank=True, null=True)
    discountf9_d = models.CharField(max_length=1, blank=True, null=True)
    balance_d = models.CharField(max_length=1, blank=True, null=True)
    posttogl = models.CharField(max_length=1, blank=True, null=True)
    itemstrn = models.CharField(max_length=1, blank=True, null=True)
    prodtot_e = models.CharField(max_length=1, blank=True, null=True)
    prodtot_d = models.CharField(max_length=1, blank=True, null=True)
    cash_report = models.NullBooleanField()
    pay_d = models.NullBooleanField()
    pay_e = models.NullBooleanField()
    pay_o_d = models.NullBooleanField()
    pay_o_e = models.NullBooleanField()
    pay_id = models.NullBooleanField()
    pay_o_id = models.NullBooleanField()
    item_discp = models.BigIntegerField(blank=True, null=True)
    inv_discp = models.BigIntegerField(blank=True, null=True)
    style_visible = models.CharField(max_length=1, blank=True, null=True)
    size_visible = models.CharField(max_length=1, blank=True, null=True)
    color_visible = models.CharField(max_length=1, blank=True, null=True)
    move_visible = models.CharField(max_length=1, blank=True, null=True)
    printaftersave = models.NullBooleanField()
    cashpay_add = models.BigIntegerField(blank=True, null=True)
    cashpay_del = models.BigIntegerField(blank=True, null=True)
    cashpay_control = models.BigIntegerField(blank=True, null=True)
    change_items = models.NullBooleanField()
    areas_edit = models.NullBooleanField()
    search_style = models.BigIntegerField(blank=True, null=True)
    show_weight = models.CharField(max_length=1, blank=True, null=True)
    cashinv_add = models.NullBooleanField()
    cashinv_mod = models.NullBooleanField()
    cashinv_bilno = models.NullBooleanField()
    cashret_add = models.NullBooleanField()
    cashret_mod = models.NullBooleanField()
    cashret_bilno = models.NullBooleanField()
    workorder_add = models.NullBooleanField()
    workorder_mod = models.NullBooleanField()
    cashinv_custno = models.NullBooleanField()
    itm_tot_e = models.NullBooleanField()
    num_d = models.NullBooleanField()
    num_e = models.NullBooleanField()
    inv_serial_rep = models.NullBooleanField()
    spec_prices = models.NullBooleanField()
    ss_units_relations = models.NullBooleanField()
    ss_invoices_serial = models.NullBooleanField()
    ss_expenses_types = models.NullBooleanField()
    ss_salesmen_comm = models.NullBooleanField()
    ss_rec_ways = models.NullBooleanField()
    ss_pur_paymethods = models.NullBooleanField()
    ss_banks_data = models.NullBooleanField()
    ss_drivers_data = models.NullBooleanField()
    ss_transfer_rev = models.NullBooleanField()
    ss_gard = models.NullBooleanField()
    ss_cust_openbalance = models.NullBooleanField()
    ss_supplier_payv = models.NullBooleanField()
    ss_supplier_adjustment = models.NullBooleanField()
    ss_tools_postbal = models.NullBooleanField()
    ss_tools_custadj = models.NullBooleanField()
    ss_tools_barcode = models.NullBooleanField()
    ss_tools_labels = models.NullBooleanField()
    ss_tools_alterdb = models.NullBooleanField()
    ss_x27 = models.NullBooleanField()
    item_location_d = models.NullBooleanField()
    brn_stores = models.NullBooleanField()
    cashinv_del = models.NullBooleanField()
    credtinv_del = models.NullBooleanField()
    cashret_del = models.NullBooleanField()
    credtret_del = models.NullBooleanField()
    sup_ob = models.NullBooleanField()
    us_purpaymeth_sav1 = models.NullBooleanField()
    us_purpaymeth_del1 = models.NullBooleanField()
    edit_workorders = models.NullBooleanField()
    us_supsav1 = models.NullBooleanField()
    us_supdel1 = models.NullBooleanField()
    us_custsav1 = models.NullBooleanField()
    us_custdel1 = models.NullBooleanField()
    us_itmsav1 = models.NullBooleanField()
    us_itmdel1 = models.NullBooleanField()
    us_smansav1 = models.NullBooleanField()
    us_smandel1 = models.NullBooleanField()
    us_storsav1 = models.NullBooleanField()
    us_stordel1 = models.NullBooleanField()
    us_pcentsav1 = models.NullBooleanField()
    us_pcentdel1 = models.NullBooleanField()
    us_areasav1 = models.NullBooleanField()
    us_areadel1 = models.NullBooleanField()
    us_recwaysav1 = models.NullBooleanField()
    us_recwaydel1 = models.NullBooleanField()
    us_banksav1 = models.NullBooleanField()
    us_bankdel1 = models.NullBooleanField()
    us_drivsav1 = models.NullBooleanField()
    us_drivdel1 = models.NullBooleanField()
    us_catsupsav1 = models.NullBooleanField()
    us_catsupdel1 = models.NullBooleanField()
    us_catcustsav1 = models.NullBooleanField()
    us_catcustdel1 = models.NullBooleanField()
    us_catitmsav1 = models.NullBooleanField()
    us_catitmdel1 = models.NullBooleanField()
    us_catunitsav1 = models.NullBooleanField()
    us_catunitdel1 = models.NullBooleanField()
    us_cuntsav1 = models.NullBooleanField()
    us_cuntdel1 = models.NullBooleanField()
    us_paysav1 = models.NullBooleanField()
    us_paydel1 = models.NullBooleanField()
    us_currsav1 = models.NullBooleanField()
    us_currdel1 = models.NullBooleanField()
    us_unitrelsav1 = models.NullBooleanField()
    us_unitreldel1 = models.NullBooleanField()
    us_invsersav1 = models.NullBooleanField()
    us_invserdel1 = models.NullBooleanField()
    us_expsav1 = models.NullBooleanField()
    us_expdel1 = models.NullBooleanField()
    cur_v = models.CharField(max_length=1, blank=True, null=True)
    cur_e = models.CharField(max_length=1, blank=True, null=True)
    currate_v = models.CharField(max_length=1, blank=True, null=True)
    currate_e = models.CharField(max_length=1, blank=True, null=True)
    us_x51 = models.NullBooleanField()
    pur_purorder_dependentinv_repo = models.NullBooleanField()
    us_intpurorder = models.NullBooleanField()
    us_salinvstorechng = models.NullBooleanField()
    us_salinvchngstoreno = models.BigIntegerField(blank=True, null=True)
    us_stopsalinvstorechngaftersav = models.NullBooleanField()
    inst_intallment_setting = models.NullBooleanField()
    inst_intallment_payment = models.NullBooleanField()
    inst_invintallment_report = models.NullBooleanField()
    inst_inarrearinvintallment_rep = models.NullBooleanField()
    inst_intallment_addpayment = models.NullBooleanField()
    inst_intallment_deletepayment = models.NullBooleanField()
    inst_customer_setting = models.NullBooleanField()
    us_update_supp_data = models.NullBooleanField()
    us_intpurordereditdelete = models.NullBooleanField()
    pur_order_dependentinv_rep = models.NullBooleanField()
    workorderissuevoucher_rep = models.NullBooleanField()
    us_suppsalpurrep = models.NullBooleanField()
    us_stylesizecolorinpur = models.NullBooleanField()
    us_discpolicy = models.NullBooleanField()
    related_salman = models.BigIntegerField(blank=True, null=True)
    cashinv_print = models.NullBooleanField()
    creditinv_print = models.NullBooleanField()
    cashret_print = models.NullBooleanField()
    creditret_print = models.NullBooleanField()
    change_int_po_status = models.NullBooleanField()
    us_pur_order_del = models.NullBooleanField()
    us_intpurorderdelete = models.NullBooleanField()
    pur_itembaldisplay = models.CharField(max_length=1, blank=True, null=True)
    us_sitereqadd = models.NullBooleanField()
    us_sitereqdel = models.NullBooleanField()
    us_sitereqmod = models.NullBooleanField()
    us_oldvoucherinq = models.NullBooleanField()
    us_detcashdelivrep = models.NullBooleanField()
    us_cashinv_printonce = models.IntegerField(blank=True, null=True)
    us_creditinv_printonce = models.IntegerField(blank=True, null=True)
    us_cashret_printonce = models.IntegerField(blank=True, null=True)
    us_creditret_printonce = models.IntegerField(blank=True, null=True)
    ss_showpriceinpricelist = models.NullBooleanField()
    cat_weight_d = models.NullBooleanField()
    act_cat_weight_d = models.NullBooleanField()
    total_cat_weight_d = models.NullBooleanField()
    show_entry_users = models.NullBooleanField()
    us_tans_req = models.NullBooleanField()
    us_tans_req_moddel = models.NullBooleanField()
    us_tans_req_seq = models.NullBooleanField()
    normal_inv = models.NullBooleanField()
    exchange_inv = models.NullBooleanField()
    exchange_cr_inv = models.NullBooleanField()
    alteration_type = models.NullBooleanField()
    cust_reserved = models.NullBooleanField()
    us_shifts = models.NullBooleanField()
    shift_save = models.NullBooleanField()
    shift_del = models.NullBooleanField()
    us_altration = models.NullBooleanField()
    alt_save = models.NullBooleanField()
    alt_del = models.NullBooleanField()
    import_file = models.NullBooleanField()
    check_filter = models.NullBooleanField()
    tansfer_following = models.NullBooleanField()
    us_qcas = models.NullBooleanField()
    us_r1 = models.NullBooleanField()
    us_r2 = models.NullBooleanField()
    us_r3 = models.NullBooleanField()
    us_r4 = models.NullBooleanField()
    us_r5 = models.NullBooleanField()
    us_r6 = models.NullBooleanField()
    us_r7 = models.NullBooleanField()
    us_r8 = models.NullBooleanField()
    us_r9 = models.NullBooleanField()
    us_export_vou = models.NullBooleanField()
    us_cash_customer_statment = models.NullBooleanField()
    cashinv_creditnote = models.BigIntegerField(blank=True, null=True)
    cashret_creditnote = models.BigIntegerField(blank=True, null=True)
    add_quotation_pricing = models.NullBooleanField()
    add_step_pricing = models.NullBooleanField()
    print_step_pricing = models.NullBooleanField()
    equation_settings_step_pricing = models.NullBooleanField()
    infor_cust = models.NullBooleanField()
    infor_itemcat = models.NullBooleanField()
    infor_item = models.NullBooleanField()
    infor_supplier = models.NullBooleanField()
    infor_cashinv = models.NullBooleanField()
    infor_cashret = models.NullBooleanField()
    infor_credit = models.NullBooleanField()
    infor_creditret = models.NullBooleanField()
    infor_purorder = models.NullBooleanField()
    infor_intpurorder = models.NullBooleanField()
    infor_qua = models.NullBooleanField()
    infor_iss = models.NullBooleanField()
    infor_issgift = models.NullBooleanField()
    infor_dest = models.NullBooleanField()
    infor_pur = models.NullBooleanField()
    infor_rec = models.NullBooleanField()
    infor_adjust = models.NullBooleanField()
    infor_trans = models.NullBooleanField()
    infor_tans_req = models.NullBooleanField()
    infor_ob = models.NullBooleanField()
    infor_lc = models.NullBooleanField()
    infor_iss_ret = models.NullBooleanField()
    infor_produc = models.NullBooleanField()
    infor_workorder_add = models.NullBooleanField()
    infor_pay = models.NullBooleanField()
    infor_cashpay = models.NullBooleanField()
    infor_transfer_rev = models.NullBooleanField()
    infor_gard = models.NullBooleanField()
    infor_cust_openbalance = models.NullBooleanField()
    infor_supplier_payv = models.NullBooleanField()
    infor_supplier_adjustment = models.NullBooleanField()
    infor_tools_custadj = models.NullBooleanField()
    infor_sup_ob = models.NullBooleanField()
    infor_tansfer_following = models.NullBooleanField()
    infor_qcas = models.NullBooleanField()
    infor_export_vou = models.NullBooleanField()
    engineer_add = models.NullBooleanField()
    engineer_del = models.NullBooleanField()
    engineer_save = models.NullBooleanField()
    edit_serial = models.NullBooleanField()
    analysis_pur_order_rep = models.NullBooleanField()
    add_site_req = models.NullBooleanField()
    edit_del_site_req = models.NullBooleanField()
    infor_site_req = models.NullBooleanField()
    add_partai_payment = models.NullBooleanField()
    edit_partai_payment = models.NullBooleanField()
    del_partai_payment = models.NullBooleanField()
    add_cost_update = models.NullBooleanField()
    edit_del_cost_update = models.NullBooleanField()
    infor_cost_update = models.NullBooleanField()
    crnote_followup_rep = models.NullBooleanField()
    add_saleseason = models.NullBooleanField()
    edit_saleseason = models.NullBooleanField()
    del_saleseason = models.NullBooleanField()
    saleseason_rep = models.NullBooleanField()
    us_replenishment_report = models.BigIntegerField(blank=True, null=True)
    us_createfkforinventorytables = models.BigIntegerField(blank=True, null=True)
    us_temcodemodification = models.BigIntegerField(blank=True, null=True)
    infor_reservation_voucher = models.BigIntegerField(blank=True, null=True)
    add_reservation_voucher = models.BigIntegerField(blank=True, null=True)
    edit_del_reservation_voucher = models.BigIntegerField(blank=True, null=True)
    ctn_list = models.BigIntegerField(blank=True, null=True)
    return_store = models.BigIntegerField(blank=True, null=True)
    show_item_component = models.BigIntegerField(blank=True, null=True)
    add_cash_cust = models.BigIntegerField(blank=True, null=True)
    mod_cash_cust = models.BigIntegerField(blank=True, null=True)
    show_cash_cust = models.BigIntegerField(blank=True, null=True)
    credit_min_limit = models.BigIntegerField(blank=True, null=True)
    credit_max_limit = models.BigIntegerField(blank=True, null=True)
    issue_voucher_from_inv = models.BigIntegerField(blank=True, null=True)
    ci_print_check = models.BigIntegerField(blank=True, null=True)
    validate_store_trans = models.BigIntegerField(blank=True, null=True)
    unpost_to_gl = models.CharField(max_length=1, blank=True, null=True)
    us_pur_ret = models.NullBooleanField()
    us_pur_ret_mod = models.NullBooleanField()
    us_x30_ret = models.NullBooleanField()
    infor_pur_ret = models.NullBooleanField()
    branch_sales_reports = models.NullBooleanField()
    print_many_inv = models.NullBooleanField()
    audit_data = models.NullBooleanField()
    store_men = models.NullBooleanField()
    sales_season = models.NullBooleanField()
    cost_center = models.NullBooleanField()
    car_models = models.NullBooleanField()
    store_men_mod = models.NullBooleanField()
    sales_season_mod = models.NullBooleanField()
    cost_center_mod = models.NullBooleanField()
    car_models_mod = models.NullBooleanField()
    store_men_del = models.NullBooleanField()
    sales_season_del = models.NullBooleanField()
    cost_center_del = models.NullBooleanField()
    car_models_del = models.NullBooleanField()
    export_vouchers = models.NullBooleanField()
    post_cost = models.NullBooleanField()
    exp_item_rep = models.NullBooleanField()
    reorder_item_rep = models.NullBooleanField()
    sales_firstcat_rep = models.NullBooleanField()
    sales_comm_rep = models.NullBooleanField()
    deliv_stages_follow_rep = models.NullBooleanField()
    cust_trial_balance = models.NullBooleanField()
    store_by_location_rep = models.NullBooleanField()
    correct_cust_supp_data = models.NullBooleanField()
    us_devide_mod = models.NullBooleanField()
    us_devide_add = models.NullBooleanField()
    infor_devide = models.NullBooleanField()
    datacollector = models.NullBooleanField()
    m_daily = models.NullBooleanField()
    m_monthly = models.NullBooleanField()
    us_forms_mod = models.NullBooleanField()
    us_forms_add = models.NullBooleanField()
    infor_forms = models.NullBooleanField()
    us_reserv_card = models.NullBooleanField()
    us_color_cat_add = models.NullBooleanField()
    us_color_cat_mod = models.NullBooleanField()
    us_color_cat_del = models.NullBooleanField()
    us_color_add = models.NullBooleanField()
    us_color_mod = models.NullBooleanField()
    us_color_del = models.NullBooleanField()
    us_size_cat_add = models.NullBooleanField()
    us_size_cat_mod = models.NullBooleanField()
    us_size_cat_del = models.NullBooleanField()
    us_size_add = models.NullBooleanField()
    us_size_mod = models.NullBooleanField()
    us_size_del = models.NullBooleanField()
    us_dimen_eq_add = models.NullBooleanField()
    us_dimen_eq_mod = models.NullBooleanField()
    us_dimen_eq_del = models.NullBooleanField()
    us_add_sales_ser = models.NullBooleanField()
    us_wo_mod = models.NullBooleanField()
    us_wo_add = models.NullBooleanField()
    infor_wo = models.NullBooleanField()
    us_user_sales = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'user_groups'


class UserOtvoucherwin(models.Model):
    user_no = models.IntegerField()
    reset_no = models.IntegerField()
    previlage = models.IntegerField(blank=True, null=True)
    ret = models.CharField(max_length=1, blank=True, null=True)
    addition = models.CharField(max_length=1, blank=True, null=True)
    saving = models.CharField(max_length=1, blank=True, null=True)
    deletion = models.CharField(max_length=1, blank=True, null=True)
    printing = models.CharField(max_length=1, blank=True, null=True)
    posting = models.CharField(max_length=1, blank=True, null=True)
    unposting = models.CharField(max_length=1, blank=True, null=True)
    check_printing = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_otvoucherwin'
        unique_together = (('user_no', 'reset_no'),)


class UserPrices(models.Model):
    user = models.ForeignKey('Users')
    price_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_prices'
        unique_together = (('user_id', 'price_id'),)


class UserStores(models.Model):
    id = models.IntegerField()
    store_id = models.IntegerField()
    can_del = models.FloatField(blank=True, null=True)
    can_search = models.FloatField(blank=True, null=True)
    can_new = models.FloatField(blank=True, null=True)
    can_save = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_stores'
        unique_together = (('id', 'store_id'),)


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    us_super = models.NullBooleanField()
    us_mod = models.NullBooleanField()
    us_del = models.NullBooleanField()
    us_sup = models.NullBooleanField()
    us_cust = models.NullBooleanField()
    us_prod = models.NullBooleanField()
    us_sman = models.NullBooleanField()
    us_catprod = models.NullBooleanField()
    us_catcust = models.NullBooleanField()
    us_catsup = models.NullBooleanField()
    us_store = models.NullBooleanField()
    us_pcenter = models.ForeignKey(Centers, db_column='us_pcenter', blank=True, null=True)
    us_units = models.NullBooleanField()
    us_cunt = models.NullBooleanField()
    us_paymnet = models.NullBooleanField()
    us_currancy = models.NullBooleanField()
    us_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    us_pass = models.CharField(max_length=50, blank=True, null=True)
    us_system1 = models.NullBooleanField()
    us_system2 = models.NullBooleanField()
    us_ystem3 = models.NullBooleanField()
    us_system4 = models.NullBooleanField()
    us_system5 = models.NullBooleanField()
    us_system6 = models.NullBooleanField()
    us_syetem7 = models.NullBooleanField()
    us_system8 = models.NullBooleanField()
    us_system9 = models.NullBooleanField()
    us_system10 = models.NullBooleanField()
    us_cost = models.NullBooleanField()
    us_date_controll = models.NullBooleanField()
    us_w_change_date = models.NullBooleanField()
    us_onlyonecenter = models.NullBooleanField()
    us_centerno = models.BigIntegerField(blank=True, null=True)
    us_salpricecontroll = models.BigIntegerField(blank=True, null=True)
    us_sal = models.NullBooleanField()
    us_salr = models.NullBooleanField()
    us_qua = models.NullBooleanField()
    us_sal_mod = models.NullBooleanField()
    us_salr_mod = models.NullBooleanField()
    us_qua_mod = models.NullBooleanField()
    us_iss = models.NullBooleanField()
    us_issgift = models.NullBooleanField()
    us_dest = models.NullBooleanField()
    us_iss_mod = models.NullBooleanField()
    us_issgift_mod = models.NullBooleanField()
    us_dest_mod = models.NullBooleanField()
    us_creditlimit = models.NullBooleanField()
    us_discperitemcontroll = models.NullBooleanField()
    us_discountcontroll = models.NullBooleanField()
    us_pur = models.NullBooleanField()
    us_pur_mod = models.NullBooleanField()
    us_rec = models.NullBooleanField()
    us_rec_mod = models.NullBooleanField()
    us_purorder = models.NullBooleanField()
    us_pur_order_mod = models.NullBooleanField()
    us_adjust = models.NullBooleanField()
    us_adjust_mod = models.NullBooleanField()
    us_trans = models.NullBooleanField()
    us_trans_mod = models.NullBooleanField()
    us_lc = models.NullBooleanField()
    us_ob = models.NullBooleanField()
    us_x1 = models.NullBooleanField()
    us_x2 = models.NullBooleanField()
    us_x3 = models.NullBooleanField()
    us_x4 = models.NullBooleanField()
    us_x5 = models.NullBooleanField()
    us_x6 = models.NullBooleanField()
    us_x7 = models.NullBooleanField()
    us_x8 = models.NullBooleanField()
    us_x9 = models.NullBooleanField()
    us_x10 = models.NullBooleanField()
    us_x11 = models.NullBooleanField()
    us_x12 = models.NullBooleanField()
    us_x13 = models.NullBooleanField()
    us_x14 = models.NullBooleanField()
    us_x15 = models.NullBooleanField()
    us_x16 = models.NullBooleanField()
    us_x17 = models.NullBooleanField()
    us_x18 = models.NullBooleanField()
    us_x19 = models.NullBooleanField()
    us_x20 = models.NullBooleanField()
    us_x21 = models.NullBooleanField()
    us_x22 = models.NullBooleanField()
    us_x23 = models.NullBooleanField()
    us_x24 = models.NullBooleanField()
    us_x25 = models.NullBooleanField()
    us_x26 = models.NullBooleanField()
    us_x27 = models.NullBooleanField()
    us_x28 = models.NullBooleanField()
    us_x29 = models.NullBooleanField()
    us_x30 = models.NullBooleanField()
    us_x31 = models.NullBooleanField()
    us_x32 = models.NullBooleanField()
    us_x33 = models.NullBooleanField()
    us_x34 = models.NullBooleanField()
    us_x35 = models.NullBooleanField()
    us_x36 = models.NullBooleanField()
    us_x37 = models.NullBooleanField()
    us_x38 = models.NullBooleanField()
    us_x39 = models.NullBooleanField()
    us_x40 = models.NullBooleanField()
    us_x41 = models.NullBooleanField()
    us_x42 = models.NullBooleanField()
    us_x43 = models.NullBooleanField()
    us_x44 = models.NullBooleanField()
    us_x45 = models.NullBooleanField()
    us_x46 = models.NullBooleanField()
    us_x47 = models.NullBooleanField()
    us_x48 = models.NullBooleanField()
    us_x49 = models.NullBooleanField()
    us_x50 = models.NullBooleanField()
    overrideprice = models.BigIntegerField(blank=True, null=True)
    overrideminprice = models.BigIntegerField(blank=True, null=True)
    cp_stotrtrans = models.BigIntegerField(blank=True, null=True)
    posttogl = models.CharField(max_length=1, blank=True, null=True)
    ispointofsale = models.CharField(max_length=1, blank=True, null=True)
    voucher_type_d = models.CharField(max_length=1, blank=True, null=True)
    voucher_type_e = models.CharField(max_length=1, blank=True, null=True)
    qutation_no_d = models.CharField(max_length=1, blank=True, null=True)
    qutation_no_e = models.CharField(max_length=1, blank=True, null=True)
    pur_order_d = models.CharField(max_length=1, blank=True, null=True)
    pur_order_e = models.CharField(max_length=1, blank=True, null=True)
    cust_name_e = models.CharField(max_length=1, blank=True, null=True)
    address_d = models.CharField(max_length=1, blank=True, null=True)
    address_e = models.CharField(max_length=1, blank=True, null=True)
    reserv_d = models.CharField(max_length=1, blank=True, null=True)
    reserv_e = models.CharField(max_length=1, blank=True, null=True)
    delivery_date_d = models.CharField(max_length=1, blank=True, null=True)
    delivery_date_e = models.CharField(max_length=1, blank=True, null=True)
    closed_d = models.CharField(max_length=1, blank=True, null=True)
    closed_e = models.CharField(max_length=1, blank=True, null=True)
    payment_d = models.CharField(max_length=1, blank=True, null=True)
    payment_e = models.CharField(max_length=1, blank=True, null=True)
    store_e = models.CharField(max_length=1, blank=True, null=True)
    unit_d = models.CharField(max_length=1, blank=True, null=True)
    unit_e = models.CharField(max_length=1, blank=True, null=True)
    pack_d = models.CharField(max_length=1, blank=True, null=True)
    pack_e = models.CharField(max_length=1, blank=True, null=True)
    qty_e = models.CharField(max_length=1, blank=True, null=True)
    price_e = models.CharField(max_length=1, blank=True, null=True)
    disc_d = models.CharField(max_length=1, blank=True, null=True)
    disc_e = models.CharField(max_length=1, blank=True, null=True)
    discp_d = models.CharField(max_length=1, blank=True, null=True)
    discp_e = models.CharField(max_length=1, blank=True, null=True)
    discountp_d = models.CharField(max_length=1, blank=True, null=True)
    discountf9_d = models.CharField(max_length=1, blank=True, null=True)
    balance_d = models.CharField(max_length=1, blank=True, null=True)
    itemstrn = models.CharField(max_length=1, blank=True, null=True)
    ini_screen = models.BigIntegerField(blank=True, null=True)
    prodtot_e = models.CharField(max_length=1, blank=True, null=True)
    prodtot_d = models.CharField(max_length=1, blank=True, null=True)
    cash_report = models.NullBooleanField()
    pay_d = models.NullBooleanField()
    pay_e = models.NullBooleanField()
    pay_o_d = models.NullBooleanField()
    pay_o_e = models.NullBooleanField()
    pay_id = models.NullBooleanField()
    pay_o_id = models.NullBooleanField()
    item_discp = models.BigIntegerField(blank=True, null=True)
    inv_discp = models.BigIntegerField(blank=True, null=True)
    style_visible = models.CharField(max_length=1, blank=True, null=True)
    size_visible = models.CharField(max_length=1, blank=True, null=True)
    color_visible = models.CharField(max_length=1, blank=True, null=True)
    move_visible = models.CharField(max_length=1, blank=True, null=True)
    printaftersave = models.NullBooleanField()
    cashpay_add = models.BigIntegerField(blank=True, null=True)
    cashpay_del = models.BigIntegerField(blank=True, null=True)
    cashpay_control = models.BigIntegerField(blank=True, null=True)
    change_items = models.NullBooleanField()
    areas_edit = models.NullBooleanField()
    search_style = models.BigIntegerField(blank=True, null=True)
    show_weight = models.CharField(max_length=1, blank=True, null=True)
    cashinv_add = models.NullBooleanField()
    cashinv_mod = models.NullBooleanField()
    cashinv_bilno = models.NullBooleanField()
    cashret_add = models.NullBooleanField()
    cashret_mod = models.NullBooleanField()
    cashret_bilno = models.NullBooleanField()
    workorder_add = models.NullBooleanField()
    workorder_mod = models.NullBooleanField()
    cashinv_custno = models.NullBooleanField()
    itm_tot_e = models.NullBooleanField()
    num_d = models.NullBooleanField()
    num_e = models.NullBooleanField()
    inv_serial_rep = models.NullBooleanField()
    spec_prices = models.NullBooleanField()
    ss_units_relations = models.NullBooleanField()
    ss_invoices_serial = models.NullBooleanField()
    ss_expenses_types = models.NullBooleanField()
    ss_salesmen_comm = models.NullBooleanField()
    ss_rec_ways = models.NullBooleanField()
    ss_pur_paymethods = models.NullBooleanField()
    ss_banks_data = models.NullBooleanField()
    ss_drivers_data = models.NullBooleanField()
    ss_transfer_rev = models.NullBooleanField()
    ss_gard = models.NullBooleanField()
    ss_cust_openbalance = models.NullBooleanField()
    ss_supplier_payv = models.NullBooleanField()
    ss_supplier_adjustment = models.NullBooleanField()
    ss_tools_postbal = models.NullBooleanField()
    ss_tools_custadj = models.NullBooleanField()
    ss_tools_barcode = models.NullBooleanField()
    ss_tools_labels = models.NullBooleanField()
    ss_tools_alterdb = models.NullBooleanField()
    ss_x27 = models.NullBooleanField()
    m_daily = models.NullBooleanField()
    m_monthly = models.NullBooleanField()
    item_location_d = models.NullBooleanField()
    brn_stores = models.NullBooleanField()
    cashinv_del = models.NullBooleanField()
    credtinv_del = models.NullBooleanField()
    cashret_del = models.NullBooleanField()
    credtret_del = models.NullBooleanField()
    sup_ob = models.NullBooleanField()
    edit_workorders = models.NullBooleanField()
    us_purpaymeth_sav1 = models.NullBooleanField()
    us_purpaymeth_del1 = models.NullBooleanField()
    us_supsav1 = models.NullBooleanField()
    us_supdel1 = models.NullBooleanField()
    us_custsav1 = models.NullBooleanField()
    us_custdel1 = models.NullBooleanField()
    us_itmsav1 = models.NullBooleanField()
    us_itmdel1 = models.NullBooleanField()
    us_smansav1 = models.NullBooleanField()
    us_smandel1 = models.NullBooleanField()
    us_storsav1 = models.NullBooleanField()
    us_stordel1 = models.NullBooleanField()
    us_pcentsav1 = models.NullBooleanField()
    us_pcentdel1 = models.NullBooleanField()
    us_areasav1 = models.NullBooleanField()
    us_areadel1 = models.NullBooleanField()
    us_recwaysav1 = models.NullBooleanField()
    us_recwaydel1 = models.NullBooleanField()
    us_banksav1 = models.NullBooleanField()
    us_bankdel1 = models.NullBooleanField()
    us_drivsav1 = models.NullBooleanField()
    us_drivdel1 = models.NullBooleanField()
    us_catsupsav1 = models.NullBooleanField()
    us_catsupdel1 = models.NullBooleanField()
    us_catcustsav1 = models.NullBooleanField()
    us_catcustdel1 = models.NullBooleanField()
    us_catitmsav1 = models.NullBooleanField()
    us_catitmdel1 = models.NullBooleanField()
    us_catunitsav1 = models.NullBooleanField()
    us_catunitdel1 = models.NullBooleanField()
    us_cuntsav1 = models.NullBooleanField()
    us_cuntdel1 = models.NullBooleanField()
    us_paysav1 = models.NullBooleanField()
    us_paydel1 = models.NullBooleanField()
    us_currsav1 = models.NullBooleanField()
    us_currdel1 = models.NullBooleanField()
    us_unitrelsav1 = models.NullBooleanField()
    us_unitreldel1 = models.NullBooleanField()
    us_invsersav1 = models.NullBooleanField()
    us_invserdel1 = models.NullBooleanField()
    us_expsav1 = models.NullBooleanField()
    us_expdel1 = models.NullBooleanField()
    cur_v = models.CharField(max_length=1, blank=True, null=True)
    cur_e = models.CharField(max_length=1, blank=True, null=True)
    currate_v = models.CharField(max_length=1, blank=True, null=True)
    currate_e = models.CharField(max_length=1, blank=True, null=True)
    eq_values = models.NullBooleanField()
    equ_displayonly = models.NullBooleanField()
    us_x51 = models.NullBooleanField()
    us_prod_sav = models.NullBooleanField()
    us_prod_del = models.NullBooleanField()
    us_catprod_del = models.NullBooleanField()
    us_catprod_sav = models.NullBooleanField()
    us_currancy_del = models.NullBooleanField()
    us_currancy_sav = models.NullBooleanField()
    ss_rec_ways_del = models.NullBooleanField()
    ss_rec_ways_sav = models.NullBooleanField()
    ss_pur_paymethods_del = models.NullBooleanField()
    ss_pur_paymethods_sav = models.NullBooleanField()
    us_qua_del = models.NullBooleanField()
    us_qua_sav = models.NullBooleanField()
    workorder_add_del = models.NullBooleanField()
    workorder_add_sav = models.NullBooleanField()
    us_lc_del = models.NullBooleanField()
    us_lc_sav = models.NullBooleanField()
    cashpay_add_del = models.NullBooleanField()
    cashpay_add_sav = models.NullBooleanField()
    pay_o_d_del = models.NullBooleanField()
    pay_o_d_sav = models.NullBooleanField()
    pay_d_del = models.NullBooleanField()
    pay_d_sav = models.NullBooleanField()
    us_x24_del = models.NullBooleanField()
    us_x24_sav = models.NullBooleanField()
    pur_purorder_dependentinv_repo = models.NullBooleanField()
    us_intpurorder = models.NullBooleanField()
    pur_order_dependentinv_rep = models.NullBooleanField()
    us_salinvstorechng = models.NullBooleanField()
    us_salinvchngstoreno = models.BigIntegerField(blank=True, null=True)
    us_stopsalinvstorechngaftersav = models.NullBooleanField()
    us_update_supp_data = models.NullBooleanField()
    us_intpurordereditdelete = models.NullBooleanField()
    workorderissuevoucher_rep = models.NullBooleanField()
    us_suppsalpurrep = models.NullBooleanField()
    us_stylesizecolorinpur = models.NullBooleanField()
    us_discpolicy = models.NullBooleanField()
    related_salman = models.ForeignKey(SalesMen, db_column='related_salman', blank=True, null=True)
    cashinv_print = models.NullBooleanField()
    creditinv_print = models.NullBooleanField()
    cashret_print = models.NullBooleanField()
    creditret_print = models.NullBooleanField()
    change_int_po_status = models.NullBooleanField()
    us_pur_order_del = models.NullBooleanField()
    us_intpurorderdelete = models.NullBooleanField()
    pur_itembaldisplay = models.CharField(max_length=1, blank=True, null=True)
    us_sitereqadd = models.NullBooleanField()
    us_sitereqdel = models.NullBooleanField()
    us_sitereqmod = models.NullBooleanField()
    us_oldvoucherinq = models.NullBooleanField()
    us_detcashdelivrep = models.NullBooleanField()
    us_cashinv_printonce = models.IntegerField(blank=True, null=True)
    us_creditinv_printonce = models.IntegerField(blank=True, null=True)
    us_cashret_printonce = models.IntegerField(blank=True, null=True)
    us_creditret_printonce = models.IntegerField(blank=True, null=True)
    ss_showpriceinpricelist = models.NullBooleanField()
    cat_weight_d = models.NullBooleanField()
    act_cat_weight_d = models.NullBooleanField()
    total_cat_weight_d = models.NullBooleanField()
    show_entry_users = models.NullBooleanField()
    us_tans_req = models.NullBooleanField()
    us_tans_req_moddel = models.NullBooleanField()
    us_tans_req_seq = models.NullBooleanField()
    user_group = models.BigIntegerField(blank=True, null=True)
    normal_inv = models.NullBooleanField()
    exchange_inv = models.NullBooleanField()
    exchange_cr_inv = models.NullBooleanField()
    alteration_type = models.NullBooleanField()
    cust_reserved = models.NullBooleanField()
    us_shifts = models.NullBooleanField()
    shift_save = models.NullBooleanField()
    shift_del = models.NullBooleanField()
    us_altration = models.NullBooleanField()
    alt_save = models.NullBooleanField()
    alt_del = models.NullBooleanField()
    import_file = models.NullBooleanField()
    check_filter = models.NullBooleanField()
    tansfer_following = models.NullBooleanField()
    us_qcas = models.NullBooleanField()
    us_r1 = models.NullBooleanField()
    us_r2 = models.NullBooleanField()
    us_r3 = models.NullBooleanField()
    us_r4 = models.NullBooleanField()
    us_r5 = models.NullBooleanField()
    us_r6 = models.NullBooleanField()
    us_r7 = models.NullBooleanField()
    us_r8 = models.NullBooleanField()
    us_r9 = models.NullBooleanField()
    us_export_vou = models.NullBooleanField()
    us_cash_customer_statment = models.NullBooleanField()
    cashinv_creditnote = models.BigIntegerField(blank=True, null=True)
    cashret_creditnote = models.BigIntegerField(blank=True, null=True)
    add_quotation_pricing = models.NullBooleanField()
    add_step_pricing = models.NullBooleanField()
    print_step_pricing = models.NullBooleanField()
    equation_settings_step_pricing = models.NullBooleanField()
    infor_cust = models.NullBooleanField()
    infor_itemcat = models.NullBooleanField()
    infor_item = models.NullBooleanField()
    infor_supplier = models.NullBooleanField()
    infor_cashinv = models.NullBooleanField()
    infor_cashret = models.NullBooleanField()
    infor_credit = models.NullBooleanField()
    infor_creditret = models.NullBooleanField()
    infor_purorder = models.NullBooleanField()
    infor_intpurorder = models.NullBooleanField()
    infor_qua = models.NullBooleanField()
    infor_iss = models.NullBooleanField()
    infor_issgift = models.NullBooleanField()
    infor_dest = models.NullBooleanField()
    infor_pur = models.NullBooleanField()
    infor_rec = models.NullBooleanField()
    infor_adjust = models.NullBooleanField()
    infor_trans = models.NullBooleanField()
    infor_tans_req = models.NullBooleanField()
    infor_ob = models.NullBooleanField()
    infor_lc = models.NullBooleanField()
    infor_iss_ret = models.NullBooleanField()
    infor_produc = models.NullBooleanField()
    infor_workorder_add = models.NullBooleanField()
    infor_pay = models.NullBooleanField()
    infor_cashpay = models.NullBooleanField()
    infor_transfer_rev = models.NullBooleanField()
    infor_gard = models.NullBooleanField()
    infor_cust_openbalance = models.NullBooleanField()
    infor_supplier_payv = models.NullBooleanField()
    infor_supplier_adjustment = models.NullBooleanField()
    infor_tools_custadj = models.NullBooleanField()
    infor_sup_ob = models.NullBooleanField()
    infor_tansfer_following = models.NullBooleanField()
    infor_qcas = models.NullBooleanField()
    infor_export_vou = models.NullBooleanField()
    engineer_add = models.NullBooleanField()
    engineer_del = models.NullBooleanField()
    engineer_save = models.NullBooleanField()
    edit_serial = models.NullBooleanField()
    analysis_pur_order_rep = models.NullBooleanField()
    add_site_req = models.NullBooleanField()
    edit_del_site_req = models.NullBooleanField()
    infor_site_req = models.NullBooleanField()
    add_partai_payment = models.NullBooleanField()
    edit_partai_payment = models.NullBooleanField()
    del_partai_payment = models.NullBooleanField()
    add_cost_update = models.NullBooleanField()
    edit_del_cost_update = models.NullBooleanField()
    infor_cost_update = models.NullBooleanField()
    crnote_followup_rep = models.NullBooleanField()
    add_saleseason = models.NullBooleanField()
    edit_saleseason = models.NullBooleanField()
    del_saleseason = models.NullBooleanField()
    saleseason_rep = models.NullBooleanField()
    return_store = models.BigIntegerField(blank=True, null=True)
    us_replenishment_report = models.BigIntegerField(blank=True, null=True)
    us_createfkforinventorytables = models.BigIntegerField(blank=True, null=True)
    us_temcodemodification = models.BigIntegerField(blank=True, null=True)
    infor_reservation_voucher = models.BigIntegerField(blank=True, null=True)
    add_reservation_voucher = models.BigIntegerField(blank=True, null=True)
    edit_del_reservation_voucher = models.BigIntegerField(blank=True, null=True)
    ctn_list = models.BigIntegerField(blank=True, null=True)
    show_item_component = models.BigIntegerField(blank=True, null=True)
    add_cash_cust = models.BigIntegerField(blank=True, null=True)
    mod_cash_cust = models.BigIntegerField(blank=True, null=True)
    show_cash_cust = models.BigIntegerField(blank=True, null=True)
    credit_min_limit = models.BigIntegerField(blank=True, null=True)
    credit_max_limit = models.BigIntegerField(blank=True, null=True)
    issue_voucher_from_inv = models.BigIntegerField(blank=True, null=True)
    ci_print_check = models.BigIntegerField(blank=True, null=True)
    validate_store_trans = models.BigIntegerField(blank=True, null=True)
    unpost_to_gl = models.CharField(max_length=1, blank=True, null=True)
    us_pur_ret = models.NullBooleanField()
    us_pur_ret_mod = models.NullBooleanField()
    us_x30_ret = models.NullBooleanField()
    infor_pur_ret = models.NullBooleanField()
    branch_sales_reports = models.NullBooleanField()
    print_many_inv = models.NullBooleanField()
    audit_data = models.NullBooleanField()
    store_men = models.NullBooleanField()
    sales_season = models.NullBooleanField()
    cost_center = models.NullBooleanField()
    car_models = models.NullBooleanField()
    store_men_mod = models.NullBooleanField()
    sales_season_mod = models.NullBooleanField()
    cost_center_mod = models.NullBooleanField()
    car_models_mod = models.NullBooleanField()
    store_men_del = models.NullBooleanField()
    sales_season_del = models.NullBooleanField()
    cost_center_del = models.NullBooleanField()
    car_models_del = models.NullBooleanField()
    export_vouchers = models.NullBooleanField()
    post_cost = models.NullBooleanField()
    exp_item_rep = models.NullBooleanField()
    reorder_item_rep = models.NullBooleanField()
    sales_firstcat_rep = models.NullBooleanField()
    sales_comm_rep = models.NullBooleanField()
    deliv_stages_follow_rep = models.NullBooleanField()
    cust_trial_balance = models.NullBooleanField()
    store_by_location_rep = models.NullBooleanField()
    correct_cust_supp_data = models.NullBooleanField()
    us_devide_mod = models.NullBooleanField()
    us_devide_add = models.NullBooleanField()
    infor_devide = models.NullBooleanField()
    datacollector = models.NullBooleanField()
    us_forms_mod = models.NullBooleanField()
    us_forms_add = models.NullBooleanField()
    infor_forms = models.NullBooleanField()
    us_reserv_card = models.NullBooleanField()
    us_color_cat_add = models.NullBooleanField()
    us_color_cat_mod = models.NullBooleanField()
    us_color_cat_del = models.NullBooleanField()
    us_color_add = models.NullBooleanField()
    us_color_mod = models.NullBooleanField()
    us_color_del = models.NullBooleanField()
    us_size_cat_add = models.NullBooleanField()
    us_size_cat_mod = models.NullBooleanField()
    us_size_cat_del = models.NullBooleanField()
    us_size_add = models.NullBooleanField()
    us_size_mod = models.NullBooleanField()
    us_size_del = models.NullBooleanField()
    us_dimen_eq_add = models.NullBooleanField()
    us_dimen_eq_mod = models.NullBooleanField()
    us_dimen_eq_del = models.NullBooleanField()
    us_add_sales_ser = models.NullBooleanField()
    us_wo_mod = models.NullBooleanField()
    us_wo_add = models.NullBooleanField()
    infor_wo = models.NullBooleanField()
    us_user_sales = models.NullBooleanField()
    pos_delitm = models.NullBooleanField()
    pos_qty = models.NullBooleanField()
    pos_cust = models.NullBooleanField()
    post_to_agility = models.FloatField(blank=True, null=True)
    us_rv_comm_rep = models.FloatField(blank=True, null=True)
    track_po = models.FloatField(blank=True, null=True)
    routes = models.FloatField(blank=True, null=True)
    ss_negative_balance = models.FloatField(blank=True, null=True)
    item_coding = models.FloatField(blank=True, null=True)
    show_all_store_bal = models.FloatField(blank=True, null=True)
    show_add_exp = models.FloatField(blank=True, null=True)
    trans_price_type = models.FloatField(blank=True, null=True)
    issue_price_type = models.FloatField(blank=True, null=True)
    trans_price_id = models.FloatField(blank=True, null=True)
    issue_price_id = models.FloatField(blank=True, null=True)
    us_issuevoucher_printonce = models.IntegerField(blank=True, null=True)
    allow_del_store_trans_approved = models.NullBooleanField()
    us_proforma_add = models.NullBooleanField()
    us_proforma_mod = models.NullBooleanField()
    us_proforma_del = models.NullBooleanField()
    us_proforma_bilno = models.NullBooleanField()
    us_proforma_info = models.NullBooleanField()
    pos_z = models.FloatField(blank=True, null=True)
    invoice_print = models.NullBooleanField()
    us_void = models.FloatField(blank=True, null=True)
    us_update_balance = models.FloatField(blank=True, null=True)
    us_cancel_void = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VUserBranches(models.Model):
    id = models.FloatField(blank=True, null=True)
    cen_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'v_user_branches'


class VUserPrices(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    price_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'v_user_prices'


class VUserStores(models.Model):
    id = models.FloatField(blank=True, null=True)
    store_id = models.IntegerField()
    can_del = models.FloatField(blank=True, null=True)
    can_search = models.FloatField(blank=True, null=True)
    can_new = models.FloatField(blank=True, null=True)
    can_save = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_user_stores'


class VarAllocationAccounts(models.Model):
    account_id = models.BigIntegerField()
    all_account_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'var_allocation_accounts'
        unique_together = (('account_id', 'all_account_id'),)


class ViGuide(models.Model):
    account_id = models.BigIntegerField(blank=True, null=True)
    accno = models.CharField(max_length=40, blank=True, null=True)
    account_level = models.BigIntegerField(blank=True, null=True)
    mask_code = models.CharField(max_length=37, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    userno = models.FloatField(blank=True, null=True)
    print_acc = models.FloatField(blank=True, null=True)
    trans_acc = models.FloatField(blank=True, null=True)
    edit_acc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vi_guide'


class ViGuideHc(models.Model):
    account_id = models.BigIntegerField()
    accno = models.CharField(max_length=40, blank=True, null=True)
    account_level = models.BigIntegerField(blank=True, null=True)
    mask_code = models.CharField(max_length=37, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    userno = models.FloatField(blank=True, null=True)
    print_acc = models.FloatField(blank=True, null=True)
    trans_acc = models.FloatField(blank=True, null=True)
    edit_acc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vi_guide_hc'


class ViUserroles(models.Model):
    userid = models.FloatField(blank=True, null=True)
    roleid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vi_userroles'


class VisiteType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visite_type'


class VoucherPrint(models.Model):
    serial = models.IntegerField()
    voucher_tp = models.IntegerField()
    label = models.CharField(max_length=80, blank=True, null=True)
    copies = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher_print'
        unique_together = (('serial', 'voucher_tp'),)


class Vouchers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nam = models.CharField(max_length=30, blank=True, null=True)
    typ = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'vouchers'


class W(models.Model):
    test = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'w'


class WorkOrder(models.Model):
    id = models.BigIntegerField()
    contract_id = models.BigIntegerField()
    service = models.TextField(blank=True, null=True)
    invoice_no = models.BigIntegerField(blank=True, null=True)
    issue_no = models.BigIntegerField(blank=True, null=True)
    vdate = models.DateField(blank=True, null=True)
    tech = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_order'
        unique_together = (('id', 'contract_id'),)


class WorkOrderSparePart(models.Model):
    id = models.BigIntegerField(primary_key=True)
    work_order_no = models.BigIntegerField(blank=True, null=True)
    prodn = models.CharField(max_length=30, blank=True, null=True)
    prods = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_order_spare_part'


class WorkersHours(models.Model):
    prodn = models.CharField(max_length=30)
    code_worker = models.IntegerField()
    price_hour = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workers_hours'
        unique_together = (('prodn', 'code_worker'),)


class WorkersName(models.Model):
    code_worker = models.IntegerField(primary_key=True)
    worker_namear = models.CharField(max_length=100, blank=True, null=True)
    worker_nameen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workers_name'


class WorkorderExpenses(models.Model):
    code = models.ForeignKey(Issue1, db_column='code')
    pcenter = models.ForeignKey(Issue1, db_column='pcenter')
    iss_bilno26 = models.ForeignKey(Issue1, db_column='iss_bilno26')
    iss_bilno25 = models.ForeignKey(Issue1, db_column='iss_bilno25')
    iss_bilno24 = models.ForeignKey(Issue1, db_column='iss_bilno24')
    iss_bilno23 = models.ForeignKey(Issue1, db_column='iss_bilno23')
    iss_bilno22 = models.ForeignKey(Issue1, db_column='iss_bilno22')
    iss_bilno21 = models.ForeignKey(Issue1, db_column='iss_bilno21')
    iss_bilno20 = models.ForeignKey(Issue1, db_column='iss_bilno20')
    iss_bilno19 = models.ForeignKey(Issue1, db_column='iss_bilno19')
    iss_bilno18 = models.ForeignKey(Issue1, db_column='iss_bilno18')
    iss_bilno17 = models.ForeignKey(Issue1, db_column='iss_bilno17')
    iss_bilno16 = models.ForeignKey(Issue1, db_column='iss_bilno16')
    iss_bilno15 = models.ForeignKey(Issue1, db_column='iss_bilno15')
    iss_bilno14 = models.ForeignKey(Issue1, db_column='iss_bilno14')
    iss_bilno13 = models.ForeignKey(Issue1, db_column='iss_bilno13')
    iss_bilno12 = models.ForeignKey(Issue1, db_column='iss_bilno12')
    iss_bilno11 = models.ForeignKey(Issue1, db_column='iss_bilno11')
    iss_bilno10 = models.ForeignKey(Issue1, db_column='iss_bilno10')
    iss_bilno9 = models.ForeignKey(Issue1, db_column='iss_bilno9')
    iss_bilno8 = models.ForeignKey(Issue1, db_column='iss_bilno8')
    iss_bilno7 = models.ForeignKey(Issue1, db_column='iss_bilno7')
    iss_bilno6 = models.ForeignKey(Issue1, db_column='iss_bilno6')
    iss_bilno5 = models.ForeignKey(Issue1, db_column='iss_bilno5')
    iss_bilno4 = models.ForeignKey(Issue1, db_column='iss_bilno4')
    iss_bilno3 = models.ForeignKey(Issue1, db_column='iss_bilno3')
    iss_bilno2 = models.ForeignKey(Issue1, db_column='iss_bilno2')
    iss_bilno = models.ForeignKey(Issue1, db_column='iss_bilno')
    iss_code = models.ForeignKey(Issue1, db_column='iss_code')
    iss_code2 = models.ForeignKey(Issue1, db_column='iss_code2')
    iss_code3 = models.ForeignKey(Issue1, db_column='iss_code3')
    iss_code4 = models.ForeignKey(Issue1, db_column='iss_code4')
    iss_code5 = models.ForeignKey(Issue1, db_column='iss_code5')
    iss_code6 = models.ForeignKey(Issue1, db_column='iss_code6')
    iss_code7 = models.ForeignKey(Issue1, db_column='iss_code7')
    iss_code8 = models.ForeignKey(Issue1, db_column='iss_code8')
    iss_code9 = models.ForeignKey(Issue1, db_column='iss_code9')
    iss_code10 = models.ForeignKey(Issue1, db_column='iss_code10')
    iss_code11 = models.ForeignKey(Issue1, db_column='iss_code11')
    iss_code12 = models.ForeignKey(Issue1, db_column='iss_code12')
    iss_code13 = models.ForeignKey(Issue1, db_column='iss_code13')
    iss_code14 = models.ForeignKey(Issue1, db_column='iss_code14')
    iss_code15 = models.ForeignKey(Issue1, db_column='iss_code15')
    iss_code16 = models.ForeignKey(Issue1, db_column='iss_code16')
    iss_code17 = models.ForeignKey(Issue1, db_column='iss_code17')
    iss_code18 = models.ForeignKey(Issue1, db_column='iss_code18')
    iss_code19 = models.ForeignKey(Issue1, db_column='iss_code19')
    iss_code20 = models.ForeignKey(Issue1, db_column='iss_code20')
    iss_code21 = models.ForeignKey(Issue1, db_column='iss_code21')
    iss_code22 = models.ForeignKey(Issue1, db_column='iss_code22')
    iss_code23 = models.ForeignKey(Issue1, db_column='iss_code23')
    iss_code24 = models.ForeignKey(Issue1, db_column='iss_code24')
    iss_code25 = models.ForeignKey(Issue1, db_column='iss_code25')
    iss_code26 = models.ForeignKey(Issue1, db_column='iss_code26')
    iss_code27 = models.ForeignKey(Issue1, db_column='iss_code27')
    bilno = models.ForeignKey(Issue1, db_column='bilno')
    serial = models.BigIntegerField()
    amount = models.BigIntegerField()
    exp_code = models.ForeignKey(ExpensesTypes, db_column='exp_code')
    supno = models.ForeignKey(Suppliers, db_column='supno', blank=True, null=True)
    exp_comments = models.TextField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workorder_expenses'
        unique_together = (('code', 'pcenter', 'bilno', 'serial'),)


class WorkorderPay(models.Model):
    code = models.ForeignKey(Issue1, db_column='code')
    iss_pcenter79 = models.ForeignKey(Issue1, db_column='iss_pcenter79')
    iss_bilno40 = models.ForeignKey(Issue1, db_column='iss_bilno40')
    iss_pcenter78 = models.ForeignKey(Issue1, db_column='iss_pcenter78')
    iss_bilno39 = models.ForeignKey(Issue1, db_column='iss_bilno39')
    iss_pcenter76 = models.ForeignKey(Issue1, db_column='iss_pcenter76')
    iss_bilno38 = models.ForeignKey(Issue1, db_column='iss_bilno38')
    iss_pcenter74 = models.ForeignKey(Issue1, db_column='iss_pcenter74')
    iss_bilno37 = models.ForeignKey(Issue1, db_column='iss_bilno37')
    iss_pcenter72 = models.ForeignKey(Issue1, db_column='iss_pcenter72')
    iss_bilno36 = models.ForeignKey(Issue1, db_column='iss_bilno36')
    iss_pcenter70 = models.ForeignKey(Issue1, db_column='iss_pcenter70')
    iss_bilno35 = models.ForeignKey(Issue1, db_column='iss_bilno35')
    iss_pcenter68 = models.ForeignKey(Issue1, db_column='iss_pcenter68')
    iss_bilno34 = models.ForeignKey(Issue1, db_column='iss_bilno34')
    iss_pcenter65 = models.ForeignKey(Issue1, db_column='iss_pcenter65')
    iss_bilno33 = models.ForeignKey(Issue1, db_column='iss_bilno33')
    iss_pcenter64 = models.ForeignKey(Issue1, db_column='iss_pcenter64')
    iss_bilno32 = models.ForeignKey(Issue1, db_column='iss_bilno32')
    iss_pcenter62 = models.ForeignKey(Issue1, db_column='iss_pcenter62')
    iss_bilno31 = models.ForeignKey(Issue1, db_column='iss_bilno31')
    iss_pcenter60 = models.ForeignKey(Issue1, db_column='iss_pcenter60')
    iss_bilno30 = models.ForeignKey(Issue1, db_column='iss_bilno30')
    iss_pcenter58 = models.ForeignKey(Issue1, db_column='iss_pcenter58')
    iss_bilno29 = models.ForeignKey(Issue1, db_column='iss_bilno29')
    iss_pcenter56 = models.ForeignKey(Issue1, db_column='iss_pcenter56')
    iss_bilno28 = models.ForeignKey(Issue1, db_column='iss_bilno28')
    iss_pcenter54 = models.ForeignKey(Issue1, db_column='iss_pcenter54')
    iss_bilno27 = models.ForeignKey(Issue1, db_column='iss_bilno27')
    iss_pcenter51 = models.ForeignKey(Issue1, db_column='iss_pcenter51')
    iss_bilno26 = models.ForeignKey(Issue1, db_column='iss_bilno26')
    iss_pcenter50 = models.ForeignKey(Issue1, db_column='iss_pcenter50')
    iss_bilno25 = models.ForeignKey(Issue1, db_column='iss_bilno25')
    iss_pcenter49 = models.ForeignKey(Issue1, db_column='iss_pcenter49')
    iss_bilno24 = models.ForeignKey(Issue1, db_column='iss_bilno24')
    iss_pcenter48 = models.ForeignKey(Issue1, db_column='iss_pcenter48')
    iss_bilno23 = models.ForeignKey(Issue1, db_column='iss_bilno23')
    iss_pcenter46 = models.ForeignKey(Issue1, db_column='iss_pcenter46')
    iss_bilno22 = models.ForeignKey(Issue1, db_column='iss_bilno22')
    iss_pcenter44 = models.ForeignKey(Issue1, db_column='iss_pcenter44')
    iss_bilno21 = models.ForeignKey(Issue1, db_column='iss_bilno21')
    iss_pcenter42 = models.ForeignKey(Issue1, db_column='iss_pcenter42')
    iss_bilno20 = models.ForeignKey(Issue1, db_column='iss_bilno20')
    iss_pcenter40 = models.ForeignKey(Issue1, db_column='iss_pcenter40')
    iss_bilno19 = models.ForeignKey(Issue1, db_column='iss_bilno19')
    iss_pcenter37 = models.ForeignKey(Issue1, db_column='iss_pcenter37')
    iss_bilno18 = models.ForeignKey(Issue1, db_column='iss_bilno18')
    iss_pcenter36 = models.ForeignKey(Issue1, db_column='iss_pcenter36')
    iss_bilno17 = models.ForeignKey(Issue1, db_column='iss_bilno17')
    iss_pcenter32 = models.ForeignKey(Issue1, db_column='iss_pcenter32')
    iss_bilno16 = models.ForeignKey(Issue1, db_column='iss_bilno16')
    iss_pcenter31 = models.ForeignKey(Issue1, db_column='iss_pcenter31')
    iss_bilno15 = models.ForeignKey(Issue1, db_column='iss_bilno15')
    iss_pcenter29 = models.ForeignKey(Issue1, db_column='iss_pcenter29')
    iss_bilno14 = models.ForeignKey(Issue1, db_column='iss_bilno14')
    iss_pcenter27 = models.ForeignKey(Issue1, db_column='iss_pcenter27')
    iss_bilno13 = models.ForeignKey(Issue1, db_column='iss_bilno13')
    iss_pcenter25 = models.ForeignKey(Issue1, db_column='iss_pcenter25')
    iss_bilno12 = models.ForeignKey(Issue1, db_column='iss_bilno12')
    iss_pcenter23 = models.ForeignKey(Issue1, db_column='iss_pcenter23')
    iss_bilno11 = models.ForeignKey(Issue1, db_column='iss_bilno11')
    iss_pcenter21 = models.ForeignKey(Issue1, db_column='iss_pcenter21')
    iss_bilno10 = models.ForeignKey(Issue1, db_column='iss_bilno10')
    iss_pcenter15 = models.ForeignKey(Issue1, db_column='iss_pcenter15')
    iss_bilno9 = models.ForeignKey(Issue1, db_column='iss_bilno9')
    iss_pcenter10 = models.ForeignKey(Issue1, db_column='iss_pcenter10')
    iss_bilno8 = models.ForeignKey(Issue1, db_column='iss_bilno8')
    iss_pcenter9 = models.ForeignKey(Issue1, db_column='iss_pcenter9')
    iss_bilno7 = models.ForeignKey(Issue1, db_column='iss_bilno7')
    iss_pcenter8 = models.ForeignKey(Issue1, db_column='iss_pcenter8')
    iss_bilno6 = models.ForeignKey(Issue1, db_column='iss_bilno6')
    iss_pcenter6 = models.ForeignKey(Issue1, db_column='iss_pcenter6')
    iss_bilno5 = models.ForeignKey(Issue1, db_column='iss_bilno5')
    iss_pcenter5 = models.ForeignKey(Issue1, db_column='iss_pcenter5')
    iss_bilno4 = models.ForeignKey(Issue1, db_column='iss_bilno4')
    iss_pcenter4 = models.ForeignKey(Issue1, db_column='iss_pcenter4')
    iss_bilno3 = models.ForeignKey(Issue1, db_column='iss_bilno3')
    iss_pcenter2 = models.ForeignKey(Issue1, db_column='iss_pcenter2')
    iss_bilno2 = models.ForeignKey(Issue1, db_column='iss_bilno2')
    pcenter = models.ForeignKey(Issue1, db_column='pcenter')
    iss_bilno = models.ForeignKey(Issue1, db_column='iss_bilno')
    iss_code = models.ForeignKey(Issue1, db_column='iss_code')
    iss_pcenter = models.ForeignKey(Issue1, db_column='iss_pcenter')
    iss_code2 = models.ForeignKey(Issue1, db_column='iss_code2')
    iss_pcenter3 = models.ForeignKey(Issue1, db_column='iss_pcenter3')
    iss_code3 = models.ForeignKey(Issue1, db_column='iss_code3')
    iss_pcenter7 = models.ForeignKey(Issue1, db_column='iss_pcenter7')
    iss_code4 = models.ForeignKey(Issue1, db_column='iss_code4')
    iss_pcenter11 = models.ForeignKey(Issue1, db_column='iss_pcenter11')
    iss_code5 = models.ForeignKey(Issue1, db_column='iss_code5')
    iss_pcenter12 = models.ForeignKey(Issue1, db_column='iss_pcenter12')
    iss_code6 = models.ForeignKey(Issue1, db_column='iss_code6')
    iss_pcenter13 = models.ForeignKey(Issue1, db_column='iss_pcenter13')
    iss_code7 = models.ForeignKey(Issue1, db_column='iss_code7')
    iss_pcenter14 = models.ForeignKey(Issue1, db_column='iss_pcenter14')
    iss_code8 = models.ForeignKey(Issue1, db_column='iss_code8')
    iss_pcenter16 = models.ForeignKey(Issue1, db_column='iss_pcenter16')
    iss_code9 = models.ForeignKey(Issue1, db_column='iss_code9')
    iss_pcenter17 = models.ForeignKey(Issue1, db_column='iss_pcenter17')
    iss_code10 = models.ForeignKey(Issue1, db_column='iss_code10')
    iss_pcenter18 = models.ForeignKey(Issue1, db_column='iss_pcenter18')
    iss_code11 = models.ForeignKey(Issue1, db_column='iss_code11')
    iss_pcenter19 = models.ForeignKey(Issue1, db_column='iss_pcenter19')
    iss_code12 = models.ForeignKey(Issue1, db_column='iss_code12')
    iss_pcenter20 = models.ForeignKey(Issue1, db_column='iss_pcenter20')
    iss_code13 = models.ForeignKey(Issue1, db_column='iss_code13')
    iss_pcenter22 = models.ForeignKey(Issue1, db_column='iss_pcenter22')
    iss_code14 = models.ForeignKey(Issue1, db_column='iss_code14')
    iss_pcenter24 = models.ForeignKey(Issue1, db_column='iss_pcenter24')
    iss_code15 = models.ForeignKey(Issue1, db_column='iss_code15')
    iss_pcenter26 = models.ForeignKey(Issue1, db_column='iss_pcenter26')
    iss_code16 = models.ForeignKey(Issue1, db_column='iss_code16')
    iss_pcenter28 = models.ForeignKey(Issue1, db_column='iss_pcenter28')
    iss_code17 = models.ForeignKey(Issue1, db_column='iss_code17')
    iss_pcenter30 = models.ForeignKey(Issue1, db_column='iss_pcenter30')
    iss_code18 = models.ForeignKey(Issue1, db_column='iss_code18')
    iss_pcenter33 = models.ForeignKey(Issue1, db_column='iss_pcenter33')
    iss_code19 = models.ForeignKey(Issue1, db_column='iss_code19')
    iss_pcenter34 = models.ForeignKey(Issue1, db_column='iss_pcenter34')
    iss_code20 = models.ForeignKey(Issue1, db_column='iss_code20')
    iss_pcenter35 = models.ForeignKey(Issue1, db_column='iss_pcenter35')
    iss_code21 = models.ForeignKey(Issue1, db_column='iss_code21')
    iss_pcenter38 = models.ForeignKey(Issue1, db_column='iss_pcenter38')
    iss_code22 = models.ForeignKey(Issue1, db_column='iss_code22')
    iss_pcenter39 = models.ForeignKey(Issue1, db_column='iss_pcenter39')
    iss_code23 = models.ForeignKey(Issue1, db_column='iss_code23')
    iss_pcenter41 = models.ForeignKey(Issue1, db_column='iss_pcenter41')
    iss_code24 = models.ForeignKey(Issue1, db_column='iss_code24')
    iss_pcenter43 = models.ForeignKey(Issue1, db_column='iss_pcenter43')
    iss_code25 = models.ForeignKey(Issue1, db_column='iss_code25')
    iss_pcenter45 = models.ForeignKey(Issue1, db_column='iss_pcenter45')
    iss_code26 = models.ForeignKey(Issue1, db_column='iss_code26')
    iss_pcenter47 = models.ForeignKey(Issue1, db_column='iss_pcenter47')
    iss_code27 = models.ForeignKey(Issue1, db_column='iss_code27')
    iss_pcenter52 = models.ForeignKey(Issue1, db_column='iss_pcenter52')
    iss_code28 = models.ForeignKey(Issue1, db_column='iss_code28')
    iss_pcenter53 = models.ForeignKey(Issue1, db_column='iss_pcenter53')
    iss_code29 = models.ForeignKey(Issue1, db_column='iss_code29')
    iss_pcenter55 = models.ForeignKey(Issue1, db_column='iss_pcenter55')
    iss_code30 = models.ForeignKey(Issue1, db_column='iss_code30')
    iss_pcenter57 = models.ForeignKey(Issue1, db_column='iss_pcenter57')
    iss_code31 = models.ForeignKey(Issue1, db_column='iss_code31')
    iss_pcenter59 = models.ForeignKey(Issue1, db_column='iss_pcenter59')
    iss_code32 = models.ForeignKey(Issue1, db_column='iss_code32')
    iss_pcenter61 = models.ForeignKey(Issue1, db_column='iss_pcenter61')
    iss_code33 = models.ForeignKey(Issue1, db_column='iss_code33')
    iss_pcenter63 = models.ForeignKey(Issue1, db_column='iss_pcenter63')
    iss_code34 = models.ForeignKey(Issue1, db_column='iss_code34')
    iss_pcenter66 = models.ForeignKey(Issue1, db_column='iss_pcenter66')
    iss_code35 = models.ForeignKey(Issue1, db_column='iss_code35')
    iss_pcenter67 = models.ForeignKey(Issue1, db_column='iss_pcenter67')
    iss_code36 = models.ForeignKey(Issue1, db_column='iss_code36')
    iss_pcenter69 = models.ForeignKey(Issue1, db_column='iss_pcenter69')
    iss_code37 = models.ForeignKey(Issue1, db_column='iss_code37')
    iss_pcenter71 = models.ForeignKey(Issue1, db_column='iss_pcenter71')
    iss_code38 = models.ForeignKey(Issue1, db_column='iss_code38')
    iss_pcenter73 = models.ForeignKey(Issue1, db_column='iss_pcenter73')
    iss_code39 = models.ForeignKey(Issue1, db_column='iss_code39')
    iss_pcenter75 = models.ForeignKey(Issue1, db_column='iss_pcenter75')
    iss_code40 = models.ForeignKey(Issue1, db_column='iss_code40')
    iss_pcenter77 = models.ForeignKey(Issue1, db_column='iss_pcenter77')
    bilno = models.ForeignKey(Issue1, db_column='bilno')
    serial = models.BigIntegerField()
    amount = models.BigIntegerField()
    exp_date = models.DateField(blank=True, null=True)
    exp_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workorder_pay'
        unique_together = (('code', 'pcenter', 'bilno', 'serial'),)


class Y(models.Model):
    year_no = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'y'


class YearFinalDevidedStock(models.Model):
    prodn = models.CharField(max_length=30)
    prods = models.BigIntegerField()
    year = models.IntegerField()
    qty = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_valid_payed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_valid_notpayed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_notvalid_payed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    qty_notvalid_notpayed = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'year_final_devided_stock'
        unique_together = (('prodn', 'prods', 'year'),)


class Years(models.Model):
    y_id = models.IntegerField(primary_key=True)
    y_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'years'
