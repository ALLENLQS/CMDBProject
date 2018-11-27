# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='接口名称')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='接口描述')),
                ('doc', models.CharField(max_length=32, verbose_name='接口文档')),
            ],
        ),
        migrations.CreateModel(
            name='CMDBUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=32, verbose_name='用户账号')),
                ('password', models.CharField(max_length=32, verbose_name='用户密码')),
                ('nickname', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('phone', models.CharField(max_length=32, verbose_name='用户手机号')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('photo', models.ImageField(verbose_name='用户头像', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('processor', models.CharField(max_length=32, null=True, blank=True)),
                ('vendor_id', models.CharField(max_length=32, null=True, blank=True)),
                ('cpu_family', models.CharField(max_length=32, null=True, blank=True)),
                ('model', models.CharField(max_length=32, null=True, blank=True)),
                ('model_name', models.CharField(max_length=32, null=True, blank=True)),
                ('stepping', models.CharField(max_length=32, null=True, blank=True)),
                ('microcode', models.CharField(max_length=32, null=True, blank=True)),
                ('cpu_MHZ', models.CharField(max_length=32, null=True, blank=True)),
                ('cache_size', models.CharField(max_length=32, null=True, blank=True)),
                ('physical_id', models.CharField(max_length=32, null=True, blank=True)),
                ('siblings', models.CharField(max_length=32, null=True, blank=True)),
                ('core_id', models.CharField(max_length=32, null=True, blank=True)),
                ('cpu_cores', models.CharField(max_length=32, null=True, blank=True)),
                ('apicid', models.CharField(max_length=32, null=True, blank=True)),
                ('initial_apicid', models.CharField(max_length=32, null=True, blank=True)),
                ('fpu', models.CharField(max_length=32, null=True, blank=True)),
                ('fpu_exception', models.CharField(max_length=32, null=True, blank=True)),
                ('cpuid_level', models.CharField(max_length=32, null=True, blank=True)),
                ('wp', models.CharField(max_length=32, null=True, blank=True)),
                ('flags', models.CharField(max_length=32, null=True, blank=True)),
                ('bogomips', models.CharField(max_length=32, null=True, blank=True)),
                ('clfush_size', models.CharField(max_length=32, null=True, blank=True)),
                ('cache_alignment', models.CharField(max_length=32, null=True, blank=True)),
                ('address_sizes', models.CharField(max_length=32, null=True, blank=True)),
                ('power_management', models.CharField(max_length=32, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('MemTota', models.CharField(max_length=32, null=True, blank=True)),
                ('MemFree', models.CharField(max_length=32, null=True, blank=True)),
                ('MemAvailable', models.CharField(max_length=32, null=True, blank=True)),
                ('Buffers', models.CharField(max_length=32, null=True, blank=True)),
                ('Cached', models.CharField(max_length=32, null=True, blank=True)),
                ('SwapCached', models.CharField(max_length=32, null=True, blank=True)),
                ('Active', models.CharField(max_length=32, null=True, blank=True)),
                ('Inactive', models.CharField(max_length=32, null=True, blank=True)),
                ('Active_anon', models.CharField(max_length=32, null=True, blank=True)),
                ('Inactive_anon', models.CharField(max_length=32, null=True, blank=True)),
                ('Active_file', models.CharField(max_length=32, null=True, blank=True)),
                ('Inactive_file', models.CharField(max_length=32, null=True, blank=True)),
                ('Unevictable', models.CharField(max_length=32, null=True, blank=True)),
                ('Mlocked', models.CharField(max_length=32, null=True, blank=True)),
                ('SwapTotal', models.CharField(max_length=32, null=True, blank=True)),
                ('SwapFree', models.CharField(max_length=32, null=True, blank=True)),
                ('Dirty', models.CharField(max_length=32, null=True, blank=True)),
                ('Writeback', models.CharField(max_length=32, null=True, blank=True)),
                ('AnonPages', models.CharField(max_length=32, null=True, blank=True)),
                ('Mapped', models.CharField(max_length=32, null=True, blank=True)),
                ('Shmem', models.CharField(max_length=32, null=True, blank=True)),
                ('Slab', models.CharField(max_length=32, null=True, blank=True)),
                ('SReclaimable', models.CharField(max_length=32, null=True, blank=True)),
                ('SUnreclaim', models.CharField(max_length=32, null=True, blank=True)),
                ('KernelStack', models.CharField(max_length=32, null=True, blank=True)),
                ('PageTables', models.CharField(max_length=32, null=True, blank=True)),
                ('NFS_Unstable', models.CharField(max_length=32, null=True, blank=True)),
                ('Bounce', models.CharField(max_length=32, null=True, blank=True)),
                ('WritebackTmp', models.CharField(max_length=32, null=True, blank=True)),
                ('CommitLimit', models.CharField(max_length=32, null=True, blank=True)),
                ('Committed_AS', models.CharField(max_length=32, null=True, blank=True)),
                ('VmallocTotal', models.CharField(max_length=32, null=True, blank=True)),
                ('VmallocUsed', models.CharField(max_length=32, null=True, blank=True)),
                ('VmallocChunk', models.CharField(max_length=32, null=True, blank=True)),
                ('HardwareCorrupted', models.CharField(max_length=32, null=True, blank=True)),
                ('AnonHugePages', models.CharField(max_length=32, null=True, blank=True)),
                ('HugePages_Total', models.CharField(max_length=32, null=True, blank=True)),
                ('HugePages_Free', models.CharField(max_length=32, null=True, blank=True)),
                ('HugePages_Rsvd', models.CharField(max_length=32, null=True, blank=True)),
                ('HugePages_Surp', models.CharField(max_length=32, null=True, blank=True)),
                ('Hugepagesize', models.CharField(max_length=32, null=True, blank=True)),
                ('DirectMap4k', models.CharField(max_length=32, null=True, blank=True)),
                ('DirectMap2M', models.CharField(max_length=32, null=True, blank=True)),
                ('DirectMap1G', models.CharField(max_length=32, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('ip', models.CharField(max_length=32, verbose_name='服务器ip')),
                ('mac', models.CharField(max_length=32, verbose_name='服务器物理地址')),
                ('cpu', models.CharField(max_length=32, verbose_name='服务器cpu')),
                ('memory', models.CharField(max_length=32, verbose_name='服务器内存')),
                ('disk', models.CharField(max_length=32, verbose_name='服务器磁盘')),
                ('isalive', models.CharField(max_length=32, verbose_name='服务器状态')),
            ],
        ),
        migrations.CreateModel(
            name='Server_Cpu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('server_id', models.IntegerField()),
                ('cpu_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Server_memory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('server_id', models.IntegerField()),
                ('memory_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cmdbuser',
            name='service',
            field=models.ManyToManyField(to='Server.Server'),
        ),
    ]
