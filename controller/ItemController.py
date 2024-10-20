from Service.ItemService import ItemService

class ItemController:
    items = ItemService()

    def getAllItems(self):
        return self.items.get_all_items()