from DAO.InventoryDAO import InventoryDAO

class InventoryService:
    inventoryDAO = InventoryDAO()

    def get_inventory_by_user_id(self, user_id):
        return self.inventoryDAO.get_inventory_by_user(user_id)
    
    def update_inventory_by_id(self, id, amount):
        return self.inventoryDAO.update_inventory(id, amount)


