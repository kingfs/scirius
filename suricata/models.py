"""
Copyright(C) 2014, Stamus Networks
Written by Eric Leblond <eleblond@stamus-networks.com>

This file is part of Scirius.

Scirius is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Scirius is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Scirius.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.db import models

# Create your models here.

from rules.models import Ruleset

class Suricata(models.Model):
    name = models.CharField(max_length=100, unique = True)
    descr = models.CharField(max_length=400)
    output_directory = models.CharField(max_length=400)
    created_date = models.DateTimeField('date created')
    updated_date = models.DateTimeField('date updated', blank = True)
    ruleset = models.ForeignKey(Ruleset, blank = True)

    editable = True

    def __unicode__(self):
        return self.name

    def generate(self):
        # FIXME extract archive file for sources
        # generate rule file
        rules = self.ruleset.generate()
        # write to file
        rfile = open(self.output_directory + "/" + scirius.rules, 'w')
        rfile.write("# Rules file for " + ruleset.name + " generated by Scirius at " + str(datetime.now()) + "\n")
        for rule in rules:
            rfile.write( rule.content + "\n")
