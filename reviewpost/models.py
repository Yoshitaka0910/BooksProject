from django.db import models

CATEGORY = (('one','1F:小説'),('two','2F:物語風ビジネス書'),('three','3F:社会'),('four','4F:自然科学・数学'),('five','5F:テクノロジー'),('six','6F:チーム・コミュニティ'),('seven','7F:クリエイティブ'),('eight','8F:思考法'),('nine','9F:生き方・働き方'),('ten','10F:思想'))

class BooksModel(models.Model):
    category = models.CharField(
        max_length=50,
        choices = CATEGORY
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    images = models.ImageField(upload_to='')