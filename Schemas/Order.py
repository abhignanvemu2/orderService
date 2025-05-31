from pydantic import BaseModel, Field

class StatusUpdate(BaseModel):
    status: int

class CreateOrder(BaseModel):
    menu_item_id: int = Field(..., gt=0, description="Menu Item should not be Empty")  # Must be greater than 0
    restaurent_id: int = Field(..., gt=0, description="Restaurent should not be Empty")  # Must be greater than 0
    user_id: int = Field(..., gt=0, description="User should not be Empty")  # Must be greater than 0

    class Config:
        min_anystr_length = 1  # Ensures the string fields, if any, are not empty
        anystr_strip_whitespace = True  # Strips extra whitespace from string fields