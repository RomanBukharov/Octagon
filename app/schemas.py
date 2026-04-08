from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: str = ""
    category_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    url: str | None = None
    category_id: int | None = None


class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    title: str


class Category(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CategoryWithBooks(Category):
    books: list[Book] = Field(default_factory=list)
