from components.structure import Struct


class LoginForm(Struct):

    def __init__(self, user_id: str):
        super().__init__()
        self.set_accounts(user_id)

    def _set_fields(self, field_name: str):
        props = self.search_mdt(self.login_inputs(), field_name)
        return self.get_element(
            props['$SELECTOR']['$TYPE'], props['$SELECTOR']['$VALUE']) if props is not None else props

    def username_input(self):
        return self._set_fields('Username')

    def password_input(self):
        return self._set_fields('Password')

    def login_button(self):
        return self._set_fields('LoginButton')

    def get(self) -> object:
        return self
