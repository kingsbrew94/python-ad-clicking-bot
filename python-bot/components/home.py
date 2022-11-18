from components.navbar import Menu


class Home(Menu):

    def _set_fields(self, field_name: str, key_field: str = '$BUTTON'):
        props = self.search_mdt(self.home()[key_field], field_name)
        return self.get_element(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def app(self):
        return self._set_fields('App','$APP')

    def facebook_link(self):
        return self._set_fields('Facebook')

    def tiktok_link(self):
        return self._set_fields('TikTok')


