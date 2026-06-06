from pydantic import (
    BaseModel,
    Field,
    AnyUrl,
    field_validator,
    model_validator, 
    computed_field,
    EmailStr
)
from typing import Annotated,Literal,Optional,List
from uuid import UUID 


# create pydantic
class Seller(BaseModel):
    name:Annotated[str,Field(
        min_length=2,
        max_length=60,
        title="seller name",
        description="name of seller",
    ),]
    email:EmailStr

    @field_validator("email",mode="after")
    @classmethod
    def validate_seller_email_domain(cls,value:EmailStr):
        allowed_domain=["mistore.in","example.com"]
        domain=str(value).split("@")[-1].lower()
        if domain not in allowed_domain:
            raise ValueError("seller email domain not allow:{domain}")
        return value

# field valdiator of cheack - and comuted field for calculated coloumn
class Product(BaseModel):
    id: int | None = None
    name: Annotated[str, Field(min_length=3, max_length=50)]
    brand:Annotated[str,Field(description="enter product brand name")]
    price:Annotated[int,Field(ge=0)]
    imageUrl:Annotated[
        List[AnyUrl], Field(max_length=1,description="At least one url")
    ]
    seller:Seller
    @field_validator("name",mode="after")
    @classmethod
    def validate_nameformat(cls, value: str):
        # if "-" not in value:
        #     raise ValueError("name not have -")
        
        return value
    # @model_validator(mode="after")
    # @classmethod
    # def validate_business_rules(cls,model:Product):
    #     if model.stock == 0 and model.is_active is True:
    #         raise ValueError("model error")
    #     return model
    # @computed_field
    # @property
    # def final_price(self)->float:
    #     return round(self.price * 100)


# update pydantic


class SellerUpdate(BaseModel):
    name: Optional[
        Annotated[
            str,
            Field(
                min_length=2,
                max_length=60,
                title="seller name",
                description="name of seller",
            )
        ]
    ] = None

    email: Optional[EmailStr] = None

    @field_validator("email", mode="after")
    @classmethod
    def validate_seller_email_domain(cls, value: EmailStr):
        if value is None:
            return value

        allowed_domain = ["mistore.in", "example.com"]
        domain = str(value).split("@")[-1].lower()

        if domain not in allowed_domain:
            raise ValueError(f"seller email domain not allow: {domain}")

        return value


class ProductUpdate(BaseModel):
   

    name: Optional[
        Annotated[
            str,
            Field(min_length=3, max_length=50)
        ]
    ] = None

    brand: Optional[
        Annotated[
            str,
            Field(description="enter product brand name")
        ]
    ] = None

    price: Optional[
        Annotated[
            int,
            Field(ge=0)
        ]
    ] = None

    imageUrl: Optional[
        Annotated[
            List[AnyUrl],
            Field(max_length=1, description="At least one url")
        ]
    ] = None

    seller: Optional[SellerUpdate] = None

    @field_validator("name", mode="after")
    @classmethod
    def validate_nameformat(cls, value: str):
        if value is None:
            return value

        # if "-" not in value:
        #     raise ValueError("name not have -")

        return value