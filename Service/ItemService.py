from DAO.ItemDAO import ItemDAO

class ItemService:
    itemDAO = ItemDAO()

    def get_item_by_id(self, id):
        return self.itemDAO.get_item_by_id(id)
    
    def get_all_items(self):
        return self.itemDAO.get_all_items()
    
    def add_item(self, item):
        return self.itemDAO.add_items(item)
    
    def update_item(self, id, item):
        return self.itemDAO.update_item(id=id,item=item)
    
    def delete_item(self, id):
        return self.itemDAO.delete_item(id=id)


