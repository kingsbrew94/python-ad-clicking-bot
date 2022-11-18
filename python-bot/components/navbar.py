from components.structure import Struct


class Menu(Struct):

    def __init__(self):
        super().__init__()

    def _set_fields(self, field_name: str):
        props = self.search_mdt(self.nav_bar()['$BUTTONS'], field_name)
        return self.get_elements(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def home_link(self):
        return self._set_fields('Home')[0]

    def member_link(self):
        return self._set_fields('Member')[1]

    def task_link(self):
        return self._set_fields('Task')[2]

    def record_link(self):
        return self._set_fields('Record')[3]

    def profile_link(self):
        return self._set_fields('My')[4]