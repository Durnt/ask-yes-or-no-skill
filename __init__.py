from mycroft import MycroftSkill, intent_file_handler


class AskYesOrNo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('no.or.yes.ask.intent')
    def handle_no_or_yes_ask(self, message):
        self.speak_dialog('no.or.yes.ask')


def create_skill():
    return AskYesOrNo()

