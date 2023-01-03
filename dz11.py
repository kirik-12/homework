class Beer:
    def __init__(self, name, volume, ibu) -> None:
        self.name = name
        self.volume = volume
        self.ibu = ibu

    
    def brew_strength(self):
        bitter = self.ibu
        if bitter < 10:
            return 'small beer'
        elif 10 <= bitter < 30:
            return 'average beer'
        else:
            return 'strong beer'
    

    def presentation(self):
        return f'it is beer: {self.name} with volume: {self.volume}.'
    

    def rating(self):
        bitter = self.ibu
        if bitter < 10:
            return 'very sweet beer'
        elif 10 <= bitter < 30:
            return 'Great beer'
        else:
            return 'Very bitter beer'


class Barbie:
    def __init__(self, appearance, mentality, character) -> None:
        self.appearance = appearance
        self.mentality = mentality
        self.character = character

    def Barbie_info(self):
        return f'This doll has the following characteristics \n \
            appearance: {self.appearance} \n \
            mentality: {self.mentality} \n \
            character: {self.character}\n '

    
    def Barbie_change_appearance(self, new_appearance):
        self.appearance = new_appearance

    
    def Barbie_change_mentality(self, new_mentality):
        self.mentality = new_mentality


    def Barbie_change_character(self, new_character):
        self.character = new_character



class BarbieDoll(Barbie):
    def __init__(self, appearance, mentality, character, material, type_of_production, color, additional_attributes) -> None:
        super().__init__(appearance, mentality, character)

        self.material = material
        self.type_of_production = type_of_production
        self.color = color
        self.additional_attributes = additional_attributes


    def Barbie_info(self):
        return super().Barbie_info() + \
                f'\
                material: {self.material} \n \
                type_of_pruduction: {self.type_of_production} \n \
                color: {self.color} \n \
                additional_attributes: {self.additional_attributes} \n'
    

    def Barbie_change_appearance(self, new_appearance):
        return super().Barbie_change_appearance(new_appearance)
    

    def Barbie_change_mentality(self, new_mentality):
        return super().Barbie_change_mentality(new_mentality)

    
    def Barbie_change_character(self, new_character):
        return super().Barbie_change_character(new_character)


    def Barbie_change_material(self, new_material):
        self.material = new_material

    
    def Barbie_change_type_of_production(self, new_type_of_production):
        self.type_of_production = new_type_of_production

    
    def Barbie_change_color(self, new_color):
        self.color = new_color


    def Barbie_change_additional_attributes(self, new_additional_attributes):
        self.additional_attributes = new_additional_attributes
