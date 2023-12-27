from pydantic import BaseModel


class HeroesModel(BaseModel):
    id: int
    name: str
    description: str
    image: str

    def __init__(self, **hero_data):
        hero_image = f"{hero_data['thumbnail']['path']}.{hero_data['thumbnail']['extension']}"
        super().__init__(
            id=hero_data["id"],
            name=hero_data["name"],
            description=hero_data["description"],
            image=hero_image
        )


class HeroesResponse(BaseModel):
    total: int
    result: list[HeroesModel]

    def __init__(self, **response_data):
        heroes_list = response_data["data"]["results"]

        super().__init__(total=len(heroes_list), result=heroes_list)
