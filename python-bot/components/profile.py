from components.navbar import Menu


class Account(Menu):

    def _set_fields(self, field_name: str):
        props = self.search_mdt(self.profile(), field_name)
        return self.get_elements(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def balance(self):
        props = self.search_mdt(self.profile(), 'Balance')
        return self.get_element(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def logout_link(self):
        return self._set_fields('Logout')[-1]

