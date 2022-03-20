from uuid import uuid3


class Card(object):
    def __init__(
        self,
        name,
        play_cost,
        cardtype,
        play_ability=None,
        click_ability=None,
        paid_ability=None,
    ) -> None:
        self.name = name
        self.id = uuid3()
        self.cost = play_cost
        self.cardtype = cardtype
        self.play_ability = parse_ability(play_ability)
        self.click_ability = parse_ability(click_ability)
        self.paid_ability = parse_ability(paid_ability)

    def __repr__(self) -> str:
        return f"<Card {self.name}>"


def parse_ability(play_ability):
    pass
