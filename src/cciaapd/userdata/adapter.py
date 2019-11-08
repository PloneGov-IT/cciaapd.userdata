# -*- coding: utf-8 -*-
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """

    def get_user_type(self):
        return self.context.getProperty('user_type', '')

    def set_user_type(self, value):
        return self.context.setMemberProperties({'user_type': value})

    user_type = property(get_user_type, set_user_type)

    def get_economic_sector(self):
        return self.context.getProperty('economic_sector', '')

    def set_economic_sector(self, value):
        return self.context.setMemberProperties({'economic_sector': value})

    economic_sector = property(get_economic_sector, set_economic_sector)

    def get_economic_sector_other(self):
        return self.context.getProperty('economic_sector_other', '').decode(
            'utf-8'
        )

    def set_economic_sector_other(self, value):
        return self.context.setMemberProperties(
            {'economic_sector_other': value}
        )

    economic_sector_other = property(
        get_economic_sector_other, set_economic_sector_other
    )

    def get_area_activity(self):
        return self.context.getProperty('area_activity', '').decode('utf-8')

    def set_area_activity(self, value):
        return self.context.setMemberProperties({'area_activity': value})

    area_activity = property(get_area_activity, set_area_activity)
