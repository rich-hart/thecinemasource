from django.db import models
from enum import Enum

from thecinemasource.storage_backends import MediaStorage

class Choice(Enum):
    @classmethod
    def get_choices(cls):
        return [(e.value, e.name) for _, e in enumerate(cls)]


class Post(models.Model):
    class Category(Choice):
        Interview = "IN"

    class Index(Choice):
        A = "A"
        B = "B"
        C = "C"
        D = "D"
        E = "E"
        F = "F"
        G = "G"
        H = "H"
        I = "I"
        J = "J"
        K = "K"
        L = "L"
        M = "M"
        N = "N"
        O = "O"
        P = "P"
        Q = "Q"
        R = "R"
        S = "S"
        T = "T"
        U = "U"
        V = "V"
        W = "W"
        X = "X"
        Y = "Y"
        Z = "Z"

#| ID                    | bigint(20) unsigned | NO   | PRI | NULL                | auto_increment |
    deprecated_id = models.IntegerField(null=True)
#| post_author           | bigint(20) unsigned | NO   | MUL | 0                   |                |
    author = models.TextField()
#| post_date             | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
    date = models.DateField()
#| post_date_gmt         | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
#| post_content          | longtext            | NO   | MUL | NULL                |                |
    content = models.TextField()
#| post_title            | text                | NO   | MUL | NULL                |                |
    title = models.TextField()
#| post_category         | int(4)              | NO   |     | 0                   |                |
    category = models.CharField(
        max_length=2,
        choices=Category.get_choices(),
        default=Category.Interview.value,
    )
#| post_excerpt          | text                | NO   |     | NULL                |                |
    excerpt = models.TextField()

    index = models.CharField(
        max_length=1,
        choices=Index.get_choices(),
        null = True,
    )

#| post_status           | varchar(20)         | NO   |     | publish             |                |
#| comment_status        | varchar(20)         | NO   |     | open                |                |
#| ping_status           | varchar(20)         | NO   |     | open                |                |
#| post_password         | varchar(20)         | NO   |     |                     |                |
#| post_name             | varchar(200)        | NO   | MUL |                     |                |
    last_name = models.CharField(max_length = 255)
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
        ordering = ['title']

class Photograph(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    upload = models.FileField(storage=MediaStorage())

class Favorite(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    created =  models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']
