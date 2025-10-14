from typing import List, Optional
from pydantic import BaseModel, Field

class Comment(BaseModel):
    user: str
    content: str
    replies: Optional[List['Comment']] = None  # Self-referential field

Comment.model_rebuild()  # Required to handle self-referential models
comment = Comment(
    id=1,
    content="This is a  first comment",
    replies=[
        Comment(
            id=2,
            content="This is a reply to the first comment",
            replies=[
                Comment(
                    id=3,
                    content="This is a nested reply"
                )
            ]
        ),
        Comment(
            id=4,
            content="This is another reply to the first comment"
        )
    ]
)
