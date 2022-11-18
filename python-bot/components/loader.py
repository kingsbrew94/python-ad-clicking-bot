from components.navbar import Menu


class Loader(Menu):

    def _set_fields(self, field_name: str):
        props = self.search_mdt(self.loaders(), field_name)
        return self.get_element(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def big(self):
        return self._set_fields('Big')

    def small(self):
        return self._set_fields('Small')