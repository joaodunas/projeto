# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Perguntas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descr = models.CharField(max_length=512, blank=True, null=True)
    aprovado = models.BooleanField(blank=True, null=True)
    anulado = models.BooleanField(blank=True, null=True)
    datacriacao = models.DateField(blank=True, null=True)
    dataalt = models.DateField(blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'perguntas'


class PerguntasTestes(models.Model):
    perguntas = models.OneToOneField(Perguntas, models.DO_NOTHING, primary_key=True)
    testes = models.ForeignKey('Testes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'perguntas_testes'
        unique_together = (('perguntas', 'testes'),)


class Resolucoesresposta(models.Model):
    valor = models.BooleanField()
    resolucoesteste = models.OneToOneField('Resolucoesteste', models.DO_NOTHING, primary_key=True)
    respostas = models.ForeignKey('Respostas', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'resolucoesresposta'
        unique_together = (('resolucoesteste', 'respostas'),)


class Resolucoesteste(models.Model):
    id = models.BigIntegerField(primary_key=True)
    datainicio = models.DateField(blank=True, null=True)
    datafim = models.DateField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    concluido = models.BooleanField(blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    testes = models.ForeignKey('Testes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'resolucoesteste'


class Respostas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descr = models.CharField(max_length=512, blank=True, null=True)
    valor = models.BooleanField()
    justificacao = models.CharField(max_length=512, blank=True, null=True)
    perguntas = models.ForeignKey(Perguntas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'respostas'


class Revisaoperguntas(models.Model):
    perguntavalida = models.BooleanField(blank=True, null=True)
    obs = models.CharField(max_length=512, blank=True, null=True)
    datacriacao = models.DateField(blank=True, null=True)
    dataalt = models.DateField(blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    perguntas = models.ForeignKey(Perguntas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'revisaoperguntas'


class Testes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    aprovado = models.BooleanField(blank=True, null=True)
    descr = models.CharField(max_length=512, blank=True, null=True)
    datacriacao = models.DateField(blank=True, null=True)
    dataalt = models.DateField(blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'testes'


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    podecriarquiz = models.BooleanField(blank=True, null=True)
    podecriarteste = models.BooleanField(blank=True, null=True)
    podereverquiz = models.BooleanField(blank=True, null=True)
    podereverteste = models.BooleanField(blank=True, null=True)
    poderesponderteste = models.BooleanField(blank=True, null=True)
    anulado = models.BooleanField(blank=True, null=True)
    datacriacao = models.DateField(blank=True, null=True)
    avatar = models.BinaryField(blank=True, null=True)
    nr_respostas_corretas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
