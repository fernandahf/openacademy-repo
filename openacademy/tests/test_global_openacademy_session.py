# -*- coding: utf-8 -*-
'''
Global test to openacademy session model.
Test create session and trigger constraints.
'''

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class GlobalTestOpenAcademySession(TransactionCase):
    '''
    This create global test to sessions
    '''

    # Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to test methods
        super().setUp()
        self.session = self.env['openacademy.session']
        self.partner = self.env.ref('base.res_partner_address_7')
        self.course = self.env.ref('openacademy.course1')
        self.partner_attendee = self.env.ref('base.res_partner_address_1')

    # Method of class that don't is test
    # def create_session(self, name, )

    # Method of test startswith 'def test_*(self):'
    def test_10_instructor_is_attendee(self):
        '''
        Check that raise of 'A session's instructor can't be an attendee'
        '''
        with self.assertRaisesRegexp(
                ValidationError,
                "A session's instructor can't be an attendee"):
            self.session.create({
                'name': 'Session test 1',
                'seats': 25,
                'instructor_id': self.partner.id,
                'attendee_ids': [(6, 0, [self.partner.id])],
                'course_id': self.course.id,
                })
