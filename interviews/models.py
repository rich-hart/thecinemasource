from django.db import models
from enum import Enum

from thecinemasource.storage_backends import MediaStorage

class Post(models.Model):
    class Category(Enum):
        Interview = "IN"
        @classmethod
        def get_choices(cls):
            return [(e.value, e.name) for _, e in enumerate(cls)]

#| ID                    | bigint(20) unsigned | NO   | PRI | NULL                | auto_increment |
    deprecated_id = models.IntegerField(null=True)
#| post_author           | bigint(20) unsigned | NO   | MUL | 0                   |                |
    author = models.CharField(max_length = 255)
#| post_date             | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    date = models.DateTimeField()
#| post_date_gmt         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
#| post_content          | longtext            | NO   | MUL | NULL                |                |
    content = models.TextField()
#| post_title            | text                | NO   | MUL | NULL                |                |
    title = models.CharField(max_length = 255)
#| post_category         | int(4)              | NO   |     | 0                   |                |
    category = models.CharField(
        max_length=2,
        choices=Category.get_choices(),
        default=Category.Interview.value,
    )
#| post_excerpt          | text                | NO   |     | NULL                |                |
    excerpt = models.TextField()


#| post_status           | varchar(20)         | NO   |     | publish             |                |
#| comment_status        | varchar(20)         | NO   |     | open                |                |
#| ping_status           | varchar(20)         | NO   |     | open                |                |
#| post_password         | varchar(20)         | NO   |     |                     |                |
#| post_name             | varchar(200)        | NO   | MUL |                     |                |
#    name = models.CharField(max_length = 255)
#| to_ping               | text                | NO   |     | NULL                |                |
#| pinged                | text                | NO   |     | NULL                |                |
#| post_modified         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
#| post_modified_gmt     | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
#| post_content_filtered | longtext            | NO   |     | NULL                |                |
#| post_parent           | bigint(20) unsigned | NO   | MUL | 0                   |                |
#| guid                  | varchar(255)        | NO   |     |                     |                |
#| menu_order            | int(11)             | NO   |     | 0                   |                |
#| post_type             | varchar(20)         | NO   | MUL | post                |                |
#| post_mime_type        | varchar(100)        | NO   |     |                     |                |
#| comment_count         | bigint(20)          | NO   |     | 0                   |                |

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date']

class Photograph(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    upload = models.FileField(storage=MediaStorage()) 
