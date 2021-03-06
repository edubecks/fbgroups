# coding: utf-8
__author__ = 'edubecks'
from djangoapp.apps.caronasbrasil.main_controller import MainController
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, CaronaModel
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'manually add group'

    def handle(self, *args, **options):

        ## clean
        CaronaGroupModel.objects.all().delete()


        ## Test
        ## https://www.facebook.com/groups/641749869191341/
        # fb_group_id = '641749869191341'
        # city1 = 'sao paulo'
        # city1_state = 'SP'
        # city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        # city2 = 'sao carlos'
        # city2_state = 'SP'
        # city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']

        fb_groups = [
            ## Caronas sao carlos - sao paulo
            ## https://www.facebook.com/groups/caronascsp/
            {
                'fb_group_id': '144978565569620',
                'city1' : 'sao paulo',
                'city1_state' : 'SP',
                'city2' : 'sao carlos',
                'city2_state' : 'SP',
                'city1_list' : [u'Sanpa', u'Sampa', ur'SP', ur'sao\s*paulo\s?(\(.*?\))?',
                              'sao paulo, sp, br', 'spaulo'],
                'city2_list' : [u'Sanca', u'Samca', ur'Sao\s*Carlos', u'SC', 'sao carlos, sp, br',
                              'scarlos']
            },

            ## Caronas sao carlos - rio claro
            ## https://www.facebook.com/groups/134844749969747/
            {
                'fb_group_id': '134844749969747',
                'city1' : 'rio claro',
                'city1_state' : 'SP',
                'city2' : 'sao carlos',
                'city2_state' : 'SP',
                'city1_list' : [ur'RC', ur'rio\s*claro\s?(\(.*?\))?', 'rio claro, sp, br', 'rclaro', 'R\.C.'],
                'city2_list' : [u'Sanca', u'Samca', ur'Sao\s*Carlos', u'SC', 'sao carlos, sp, br',
                              'scarlos']
            },

            ## Caronas sao carlos - campinas
            ## https://www.facebook.com/groups/caronasancacps/
            {
                'fb_group_id': '102514733197800',
                'city1' : 'campinas',
                'city1_state' : 'SP',
                'city2' : 'sao carlos',
                'city2_state' : 'SP',
                'city1_list' : [ur'campinas', 'campinas, sp, br', 'cps', 'camps',
                                ur'campinas\s?(\(.*?\))?',],
                'city2_list' : [u'Sanca', u'Samca', ur'Sao\s*Carlos', u'SC', 'sao carlos, sp, br',
                              'scarlos']
            },



        ]
        
        for group in fb_groups:
            if 'fb_group_id' in group:
                ## saving model
                CaronaGroupModel.objects.create(
                    fb_group_id=group['fb_group_id'],
                    city1=group['city1'],
                    city1_state=group['city1_state'],
                    city1_list=':'.join(group['city1_list']),
                    city2=group['city2'],
                    city2_state=group['city2_state'],
                    city2_list=':'.join(group['city2_list'])
                )

        return

