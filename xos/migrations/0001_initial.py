
# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCORDService',
            fields=[
            ],
            options={
                'verbose_name': 'MCORD Service',
                'proxy': True,
            },
            bases=('core.service',),
        ),
        migrations.CreateModel(
            name='VBBUComponent',
            fields=[
            ],
            options={
                'verbose_name': 'VBBU MCORD Service Component',
                'proxy': True,
            },
            bases=('core.tenantwithcontainer',),
        ),
        migrations.CreateModel(
            name='VPGWCComponent',
            fields=[
            ],
            options={
                'verbose_name': 'VPGWC MCORD Service Component',
                'proxy': True,
            },
            bases=('core.tenantwithcontainer',),
        ),
    ]
