from components.navbar import Menu


class Record(Menu):

    def _set_rec_fields(self, field_name: str, field_key: str):
        props = self.search_mdt(self.record()[field_key], field_name)
        return self.get_elements(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def credit(self):
        props = self.record()['$CREDIT']
        return self.get_elements(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE'])[1] if props is not None else props

    def progress_link(self):
        return self._set_rec_fields('Progress', '$MENUS')[0]

    def review_link(self):
        return self._set_rec_fields('Review', '$MENUS')[0]

    def finished_link(self):
        return self._set_rec_fields('Finished', '$MENUS')[0]

    def invalid_link(self):
        return self._set_rec_fields('Invalid', '$MENUS')[0]

    def sample_button(self):
        return self._set_rec_fields('Sample', '$TICKET')[0]

    def cancel_button(self):
        return self._set_rec_fields('Cancel', '$TICKET')[1]

    def wos_button(self):
        return self._set_rec_fields('WoS', '$TICKET')[2]
