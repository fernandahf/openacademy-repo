# -*- coding: utf-8 -*-
'''
Global test to openacademy course model.
Test create course and trigger constraints.
'''
from psycopg2.errors import CheckViolation

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger

class GlobalTestOpenAcademyCourse(TransactionCase):

    # Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to test methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']
    
    # Method of class that don't is test
    def create_course(self, name, description, responsible_id):
        # Create a course with parameters received
        course_id = self.course.create({
            'name': name,
            'description': description,
            'responsible_id': responsible_id
        })
        return course_id


    # Method of test startswith 'def test_*(self):'

    # Mute error odoo.sql_db to avoid it in log
    @mute_logger('odoo.sql_db')
    def test_01_same_name_and_description(self):
        '''
        Create a course with same name and description.
        To test constraint of name different to description.
        '''
        # Error raised expected with message
        with self.assertRaisesRegexp(
                CheckViolation,
                'new row for relation "openacademy_course" '
                'violates check constraint '
                '"openacademy_course_name_description_check"'
                ):
            # Create a course with same name and description to raise error    
            self.create_course('Test', 'Test', None)
