from DAO.ItemDAO import ItemDAO

class ItemService:
    itemDAO = ItemDAO()

    def get_item_by_id(self, id):
        return self.itemDAO.get_item_by_id(id)
    
    def get_all_items(self):
        return self.itemDAO.get_all_items()


