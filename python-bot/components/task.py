from components.navbar import Menu


class Task(Menu):

    def _set_task_fields(self, field_name: str, field_key: str):
        props = self.search_mdt(self.task()[field_key], field_name)
        return self.get_element(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def facebook_link(self):
        return self._set_task_fields('Facebook', '$HALLS')

    def tiktok_link(self):
        return self._set_task_fields('TikTok', '$HALLS')

    def level0_link(self):
        return self._set_task_fields('Lv.0', '$LEVELS')

    def level1_link(self):
        return self._set_task_fields('Lv.1', '$LEVELS')

    def level2_link(self):
        return self._set_task_fields('Lv.2', '$LEVELS')

    def level3_link(self):
        return self._set_task_fields('Lv.3', '$LEVELS')

    def commissions_link(self):
        return self._set_task_fields('Commission','$COMMISSIONS')
